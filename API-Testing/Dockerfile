FROM python:3.10.5

ARG ARG_ENV=dev
ENV ENV=$ARG_ENV

COPY . /python-api-testing

WORKDIR /python-api-testing

RUN pip install --no-cache-dir -r requirements.txt

CMD tail -f /dev/null