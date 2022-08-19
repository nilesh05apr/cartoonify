FROM python:3

ENV PYTHONBUFFERED 1

WORKDIR /webapp

ADD . /webapp/

COPY ./requirements.txt /webapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /webapp

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]