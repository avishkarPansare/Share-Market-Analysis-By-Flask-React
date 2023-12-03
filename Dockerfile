FROM python:3.10-slim

# ========== Defining the working dir --------
WORKDIR /code

# --------- copying the requirements file ------
COPY ./requirements.txt /code/requirements.txt

# --------- install all the dependencies --------
RUN pip install -r /code/requirements.txt

COPY . /code



CMD ["python3", "main.py"]