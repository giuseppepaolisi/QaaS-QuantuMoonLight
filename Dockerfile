# Base image
FROM ubuntu:20.04

ENV PATH /opt/conda/bin:$PATH

# Update these args to match the latest Miniconda3 version
ARG CONDA_VERSION=py39_23.1.0-1

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates bash gnupg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Miniconda
RUN curl -L -O https://repo.anaconda.com/miniconda/Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh && \
    /bin/bash Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh -b -p /opt/conda && \
    rm Miniconda3-${CONDA_VERSION}-Linux-x86_64.sh

# Add Microsoft repository key and repository
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install ODBC Driver 18 for SQL Server
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

ENV PATH /opt/mssql-tools18/bin:$PATH

# Set working directory
WORKDIR /app

# Copy environment file
COPY env/LINUX/environment.yml .

# Set shell to bash
SHELL ["/bin/bash", "--login", "-c"]

# Create Anaconda environment
RUN conda env create -f environment.yml && conda clean --all --yes

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