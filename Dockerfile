FROM python:3.

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update \
	&& apt-get upgrade -y \
	&& apt-get install -y --no-install-recommends \
		libsqlite3-dev libpq-dev libxml2-dev libxslt1-dev zlib1g-dev \
		libsasl2-dev libldap2-dev build-essential libssl-dev libffi-dev \
		libjpeg-dev liblcms2-dev libblas-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip setuptools

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r /code/requirements.txt

ADD . /code/
EXPOSE 8000