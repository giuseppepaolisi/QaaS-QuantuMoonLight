import os
import pathlib
import pandas as pd
from flask import request, Response

from src import app
from src.source.preprocessingDataset import (
    callPS,
    aggId,
    featureExtraction_Selection,
)
from src.source.utils import utils

"""
handles the preprocessing process of the dataset
"""
class PreprocessingControl:
    @app.route("/preprocessingControl", methods=["POST"])
    # @login_required
    def preprocessingControl():
        userpath = request.form.get("userpath")
        userpathToPredict = request.form.get("userpathToPredict")
        prototypeSelection = request.form.get("prototypeSelection")
        featureExtraction = request.form.get("featureExtraction")
        featureSelection = request.form.get("featureSelection")
        numRawsPS = request.form.get("numRawsPS", type=int)
        numColsFE = request.form.get("numColsFE", type=int)
        numColsFS = request.form.get("numColsFS", type=int)
        model = request.form.get("model")
        if model == None or model == "None":
            classification = False
        else:
            classification = True

        # Cartella dell'utente dove scrivere tutti i risultati
        pathPC = pathlib.Path(userpath).parents[0]
        print("path in PC: ", pathPC)
        if not featureExtraction and not prototypeSelection and not featureSelection and model == "QSVM":
            # Se l'utente non vuole preprocessare il dataset ma vuole fare QSVM,
            # allora qui creo i dataset da classificare aggiungendo la colonna ID
            aggId.addId(
                pathPC / "Data_training.csv",
                pathPC / "DataSetTrainPreprocessato.csv",
            )
            aggId.addId(
                pathPC / "Data_testing.csv",
                pathPC / "DataSetTestPreprocessato.csv",
            )
            print("Exiting from preprocessingControl with NoPS and NoFE")
            return Response(status=200)

        numRaws = utils.numberOfRows(userpath)
        numCols = utils.numberOfColumns(userpath)
        if featureExtraction == True or featureExtraction == "True":
            if numColsFE > numCols:
                numColsFE=numCols
        if featureSelection == True or featureSelection == "True":
            print("++++" + featureSelection)
            if numColsFS > numCols:
                numColsFS = numCols
        if prototypeSelection == True or prototypeSelection == "True":
            if numRawsPS > numRaws:
                numRawsPS=numRaws

        print("\n\n\t\t\t\tControllo Valoti")
        print(userpath)
        print(userpathToPredict)
        #print(prototypeSelection)
        print(featureExtraction)
        print(featureSelection)
        print(numRawsPS)
        print(numColsFE)
        print(numColsFS)
        print(model)

        PreprocessingControl.preprocessing(
            userpath,
            userpathToPredict,
            prototypeSelection,
            featureExtraction,
            featureSelection,
            numRawsPS,
            numColsFE,
            numColsFS,
            classification,
        )

        # Cancello i file di supporto al preprocessing
        if os.path.exists(pathPC / "IdPCADataset.csv"):
            os.remove(pathPC / "IdPCADataset.csv")
        if os.path.exists(pathPC / "IdPCADatasetTrain.csv"):
            os.remove(pathPC / "IdPCADatasetTrain.csv")

        print("Exiting from preprocessingControl")
        return Response(status=200)

    def preprocessing(
            userpath: str,
            userpathToPredict: str,
            prototypeSelection: bool,
            featureExtraction: bool,
            featureSelection: bool,
            numRowsPS: int,
            numColsFE: int,
            numColsFS: int,
            classification: bool,
    ):
        """
        This function is going to preprocess a given Dataset with prototypeSelection or featureExtraction

        :param userpath: string that points to the location of the dataset to be preprocessed
        :param prototypeSelection: boolean flag that indicated whether the user wants to execute a prototypeSelection or not
        :param userpathToPredict: string that points to the location of the dataset to be predicted
        :param featureExtraction: boolean flag that indicated whether the user wants to execute a feature Extraction or not
        :param numRowsPS: number of rows the prototype selection should reduce the dataset to
        :param numColsFE: number of columns the feature extraction should reduce the dataset to
        :param classification: boolean flag that indicated whether the user wants to execute classification or not
        :return: two preprocessed dataset: 'DataSetTrainPreprocessato.csv', 'DataSetTestPreprocessato.csv'
        :rtype: (str, str)
        """

        pathPC = pathlib.Path(userpath).parents[0]

        pathTrain = pathPC / "Data_training.csv"
        pathTest = pathPC / "Data_testing.csv"

        #print(f"prototypeSelection è {'uguale a' if prototypeSelection else 'diverso da'} True")
        #print("Sono una prototype? " + str(prototypeSelection))

        if prototypeSelection == True or prototypeSelection == "True":
            print("\n\n\t\tsono nell'if della prototype selection")
            pathTrain = callPS.callPrototypeSelection(
                pathTrain,
                numRowsPS,
            )  # create 'reducedTrainingPS.csv'

        if featureExtraction == True or featureSelection == True  or featureExtraction == "True" or featureSelection == "True":
            pathTrain, pathTest = featureExtraction_Selection.callFeatureExtraction_Selection(
                featureSelection,
                featureExtraction,
                pathTrain,
                pathTest,
                userpathToPredict,
                classification,
                numColsFE,
                numColsFS
            )  # create 'yourPCA_Train', 'yourPCA_Test' and, in case classification=True, 'doPredictionFE.csv'

        aggId.addId(
            pathTrain,
            pathPC / "DataSetTrainPreprocessato.csv",
        )  # create 'DataSetTrainPreprocessato.csv'
        aggId.addId(
            pathTest,
            pathPC / "DataSetTestPreprocessato.csv",
        )  # create 'DataSetTestPreprocessato.csv'

        return (
            pathPC / "DataSetTrainPreprocessato.csv",
            pathPC / "DataSetTestPreprocessato.csv",
        )
