FROM odoo:15.0

USER root

RUN apt-get update && apt-get install -y git python3-pip xmlsec1 && pip3 install --upgrade pip