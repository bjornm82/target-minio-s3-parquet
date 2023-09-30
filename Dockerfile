FROM python:3.11.5-slim-bullseye

COPY . /usr/app/

WORKDIR /usr/app/

RUN pip install poetry
RUN poetry install

CMD [ "poetry", "run", "pytest" ]