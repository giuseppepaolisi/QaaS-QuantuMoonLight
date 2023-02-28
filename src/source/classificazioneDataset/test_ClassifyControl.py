import os
import pathlib
import unittest
from os.path import exists

import flask

from src import app
from src.source.classificazioneDataset.ClassifyControl import ClassificazioneControl
from src.source.utils import utils


class TestClassifyControl(unittest.TestCase):

    def test_classify_control(self):
        """
        Test the input coming from the form and the status code returned, and check if the classification result
        file is created
        """
        path_train = "/src/source/classificazioneDataset/testingFiles/DataSetTrainPreprocessato.csv"
        path_test = "/src/source/classificazioneDataset/testingFiles/doPrediction.csv"
        path_prediction = "/src/source/classificazioneDataset/testingFiles/DataSetTestPreprocessato.csv"
        features = utils.createFeatureList(2)
        token = "43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe5196" \
                "91a7ad17643eecbe13d1c8c4adccd2"
        backend = "aer_simulator"
        email = "quantumoonlight@gmail.com"

        response = app.test_client(self).post(
            "/classify_control",
            data=dict(
                pathTrain=path_train,
                pathTest=path_test,
                email=email,
                userpathToPredict=path_prediction,
                features=features,
                token=token,
                backend=backend,
            ),
        )
        thread = flask.g
        thread.join()
        statuscode = response.status_code
        self.assertEqual(200, statuscode)

    def test_classification_thread(self):
        """
        Test if thread that calls the classify and QSVM works properly
        """
        path_train = "/src/source/classificazioneDataset/testingFiles/DataSetTrainPreprocessato.csv"
        path_test = "/src/source/classificazioneDataset/testingFiles/DataSetTestPreprocessato.csv"
        path_prediction = "/src/source/classificazioneDataset/testingFiles/doPrediction.csv"

        features = utils.createFeatureList(2)
        token = "43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe5196" \
                "91a7ad17643eecbe13d1c8c4adccd2"
        backend_selected = "aer_simulator"
        email = "quantumoonlight@gmail.com"
        model = "QSVC"
        C = 1000
        tau = 100
        optimizer = "SLSQP"
        loss = "squared_error"
        max_iter = 100
        kernelSVR = "rbf"
        kernelSVC = "rbf"
        C_SVC = 1
        C_SVR = 1
        id_dataset = 1
        user_id = email
        result = ClassificazioneControl().classification_thread(path_train,
                                                                path_test,
                                                                path_prediction,
                                                                features,
                                                                token,
                                                                backend_selected,
                                                                email,
                                                                model,
                                                                C,
                                                                tau,
                                                                optimizer,
                                                                loss,
                                                                max_iter,
                                                                kernelSVR,
                                                                kernelSVC,
                                                                C_SVC,
                                                                C_SVR,
                                                                id_dataset,
                                                                user_id)

        self.assertNotEqual(result, 1)

        self.assertTrue(
            exists("/src/source/classificazioneDataset/testingFiles/classifiedFile.csv")
        )

    def test_classify(self):
        """
        Test the classify function with correct parameters and input files, and check if the classification result
        file is created
        """
        path_train = "/src/source/classificazioneDataset/testingFiles/DataSetTrainPreprocessato.csv"
        path_test = "/src/source/classificazioneDataset/testingFiles/DataSetTestPreprocessato.csv"
        path_prediction = "/src/source/classificazioneDataset/testingFiles/doPrediction.csv"

        features = utils.createFeatureList(2)
        token = "43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519" \
                "691a7ad17643eecbe13d1c8c4adccd2"
        backend_selected = "aer_simulator"
        model = "QSVC"
        C = 1000
        tau = 100
        optimizer = "SLSQP"
        loss = "squared_error"
        max_iter = 100
        kernelSVR = "rbf"
        kernelSVC = "rbf"
        C_SVC = 1
        C_SVR = 1
        id_dataset = 1
        user_id = "quantumoonlight@gmail.com"

        result = ClassificazioneControl().classify(
            path_train,
            path_test,
            path_prediction,
            features,
            token,
            backend_selected,
            model,
            C,
            tau,
            optimizer,
            loss,
            max_iter,
            kernelSVR,
            kernelSVC,
            C_SVC,
            C_SVR,
            id_dataset,
            user_id
        )

        self.assertNotEqual(result, 1)

        self.assertTrue(
            exists("/src/source/classificazioneDataset/testingFiles/classifiedFile.csv")
        )

    def test_getClassifiedDataset(self):
        """
        Test the function that send the email, with fixed parameters as input
        """
        file_path = "/src/source/classificazioneDataset/testingFiles/classifiedFile.csv"
        result1 = {
            "testing_accuracy": 0.55687446747,
            "test_success_ratio": 0.4765984595,
            "total_time": str(90.7),
            "no_backend": True
        }
        open(file_path,
            "w",
        )

        user_path_to_predict = "/src/source/classificazioneDataset/testingFiles/doPrediction.csv"

        backend_selected = "aer_simulator"
        model = "QSVC"

        value = ClassificazioneControl().get_classified_dataset(
            result1, user_path_to_predict, "quantumoonlight@gmail.com", model, backend_selected
        )
        self.assertEqual(value, 1)

    def tearDown(self):
        file_path = "/src/source/classificazioneDataset/testingFiles/classifiedFile.csv"
        if os.path.exists(file_path):
            os.remove(file_path)


class TestIbmFail(unittest.TestCase):

    def setUp(self):
        file_path = "/src/source/classificazioneDataset/testingFiles/classifiedFile.csv"
        file_path1 = "/src/source/classificazioneDataset/testingFiles/testingFiles"/"emptyFile.csv"
        if os.path.exists(file_path):
            os.remove(file_path)
        open(file_path1, "w",
        ).write("1234567890987654321")

    def test_classify_ibmFail(self):
        """
        Test the classify function with not valid train and test datasets, to make the IBM backend fail on purpose
        """
        path_train = "/src/source/classificazioneDataset/testingFiles/DataSetTrainPreprocessato.csv"
        path_test = "/src/source/classificazioneDataset/testingFiles/DataSetTestPreprocessato.csv"
        path_prediction = "/src/source/classificazioneDataset/testingFiles/emptyFile.csv"

        features = utils.createFeatureList(2)
        token = "43a75c20e78cef978267a3bdcdb0207dab62575c3c9da494a1cd344022abc8a326ca1a9b7ee3f533bb7ead73a5f9fe519691" \
                "a7ad17643eecbe13d1c8c4adccd2"
        backend_selected = "aer_simulator"
        model = "QSVC"
        C = 1000
        tau = 100
        optimizer = "SLSQP"
        loss = "squared_error"
        max_iter = 100
        kernelSVR = "rbf"
        kernelSVC = "rbf"
        C_SVC = 1
        C_SVR = 1
        id_dataset = 1
        user_id = "quantumoonlight@gmail.com"

        result = ClassificazioneControl().classify(
            path_train,
            path_test,
            path_prediction,
            features,
            token,
            backend_selected,
            model,
            C,
            tau,
            optimizer,
            loss,
            max_iter,
            kernelSVR,
            kernelSVC,
            C_SVC,
            C_SVR,
            id_dataset,
            user_id
        )
        self.assertEqual(result["error"], 1)
        self.assertFalse(
            exists("/src/source/classificazioneDataset/testingFiles/classifiedFile.csv")
        )

    def tearDown(self) -> None:
        file_path = "/src/source/classificazioneDataset/testingFiles/classifiedFile.csv"
        if os.path.exists(file_path ):
            os.remove(file_path)
