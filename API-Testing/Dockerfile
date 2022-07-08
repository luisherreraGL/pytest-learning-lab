FROM python:3.10.5

ENV ENV=dev

COPY . /python-api-testing

WORKDIR /python-api-testing

RUN pip install --no-cache-dir -r requirements.txt

RUN ["pytest", "-v", "--html=./report/report.html", "--self-contained-html"]
ENTRYPOINT  ["pytest"] 

CMD tail -f /dev/null
CMD tail -f /dev/null