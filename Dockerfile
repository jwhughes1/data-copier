FROM python:3.7

#Install OS Modules
RUN apt update -y && \
    apt install telnet -y && \
    rm -rf /var/lib/apt/lists/*

#Copy Source Code
RUN mkdir -p /data-copier
COPY code_folder /data-copier/code_folder
COPY requirements.txt /data-copier

#Install App Dependencies
RUN pip install -r /data-copier/requirements.txt