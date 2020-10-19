FROM python:3.7
WORKDIR /usr/src/app

ENV POETRY_VERSION=1.0.10 \
    PATH="/root/.poetry/bin:$PATH"
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/${POETRY_VERSION}/get-poetry.py | python && \
    poetry config virtualenvs.create false
COPY ./pyproject.toml /usr/src/app/pyproject.toml
RUN poetry install

CMD tail -f /dev/null
