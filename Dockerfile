# Base image
FROM continuumio/anaconda3:latest

# Set working directory
WORKDIR /app

# Copy requirements file
COPY /env/LINUX/environment.yml .

# Install Anaconda environment
RUN conda env create -f environment.yml

# Activate environment
RUN echo "conda activate quantumoonlight" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

# Copy application code
COPY . /app

# Expose port
EXPOSE 5000

# Start application
CMD [ "python", "app.py" ]
