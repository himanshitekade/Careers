FROM python:3.10.5-slim-buster
ADD requirements.txt /tw_career/requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /tw_career/requirements.txt 

ADD . /tw_career
WORKDIR /tw_career

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "5", "--timeout", "180", "tw_career.wsgi:application"]