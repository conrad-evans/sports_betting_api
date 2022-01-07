FROM python:3.7.6-alpine3.10 as base

WORKDIR /app

ENV VIRTUAL_ENV="/opt/venv"
RUN python3 -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:${PATH}"

RUN python3 -m pip install --upgrade pip setuptools wheel

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN pytest

FROM base as prod

ENV FLASK_ENV=development

CMD [ "pytest", "/app/app.py" ]