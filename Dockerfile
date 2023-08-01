
FROM debian:latest
RUN apt update
RUN apt list --upgradable 

FROM python:3.11
# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY . /app/


# Install application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000 

# Command to start the application
CMD ["python", "run.py"]