FROM python:3.10.5


COPY . /python-api-testing

WORKDIR /python-api-testing

RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "--html=./report/report.html", "--self-contained-html"]

CMD tail -f /dev/null