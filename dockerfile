FROM python:3.12-slim-bookworm

WORKDIR /currency_converter
COPY . .

RUN pip install pipenv
RUN pipenv install
EXPOSE 8080
CMD ["pipenv","run","gunicorn","-w","4","app:app","-b","0.0.0.0:8080" ]