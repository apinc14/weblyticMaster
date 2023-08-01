FROM python:3.9


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .



# Expose the required port (if your application runs on port 5005)
EXPOSE 8080
EXPOSE 5005 

CMD ["waitress-serve", "--call", "CoreApi:app"]
