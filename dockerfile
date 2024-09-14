FROM python:3-alpine

WORKDIR /currency_converter
COPY . .

RUN pip install pipenv
RUN pipenv install
EXPOSE 8080
CMD [ "pipenv","run","flask","run","--host=0.0.0.0","--port=8080" ]