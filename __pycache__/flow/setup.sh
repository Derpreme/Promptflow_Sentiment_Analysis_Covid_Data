FROM mcr.microsoft.com/azureml/base:latest

# Install dependencies
RUN apt-get update && apt-get install -y curl apt-transport-https gnupg

# Import the public repository GPG keys
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Register the Microsoft SQL Server Ubuntu repository
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

# Install the ODBC driver
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18

# Install unixODBC development headers
RUN apt-get install -y unixodbc-dev

# Install Python packages
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Define the entry point
ENTRYPOINT ["python", "script.py"]
