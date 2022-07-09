FROM python:3.10.5

ARG ARG_ENV=dev
ARG TAG=all
ENV ENV=$ARG_ENV

COPY . /python-api-testing

WORKDIR /python-api-testing

RUN pip install --no-cache-dir -r requirements.txt

RUN if [ "$TAG" == "all" ] ; then pytest -s -v --html=./report/report.html --self-contained-html ; else pytest -s -v -m "$TAG" --html=./report/report.html --self-contained-html; fi ; exit 0

CMD tail -f /dev/null