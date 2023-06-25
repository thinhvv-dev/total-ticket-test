FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY /requirements /requirements

RUN apk update && apk upgrade \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev mysql-client libmagic libffi-dev \
    && apk add gettext \
    && python -m pip install --upgrade pip \
    && pip install -r /requirements/local.txt \
    && apk del build-deps

COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN ln -s /usr/local/bin/entrypoint.sh / # backwards compat

COPY wait-for /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for
RUN ln -s /usr/local/bin/wait-for / # backwards compat


WORKDIR /src
ADD . /src/

ENTRYPOINT ["/entrypoint.sh"]
