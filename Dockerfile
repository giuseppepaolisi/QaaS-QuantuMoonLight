# Base image
FROM continuumio/anaconda3:latest

# Set working directory
WORKDIR /app

# Copy environment file
COPY env/LINUX/environment.yml .

# Create Anaconda environment
RUN conda env create -f environment.yml && conda clean -afy

# Set shell to bash
SHELL ["/bin/bash", "--login", "-c"]

# Activate environment
ENV PATH /opt/conda/envs/quantumoonlight/bin:$PATH

# copy library
COPY env/base.py ../opt/conda/envs/quantumoonlight/lib/python3.9/site-packages/deap/

# Copy application code
COPY . /app

# Expose port
EXPOSE 5000

# Start application
CMD [ "python", "app.py" ]
