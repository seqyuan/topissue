FROM python:3.9-alpine3.18

MAINTAINER Zan Yuan <seqyuan@gmail.com>
ENV LANG=en_US.UTF-8

RUN pip install PyGithub

WORKDIR /tmp

COPY get_latest_issue.py /get_latest_issue.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

