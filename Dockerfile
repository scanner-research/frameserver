FROM scannerresearch/scanner-base:ubuntu16.04-cpu
ARG cores=1

WORKDIR /opt
RUN pip3 install flask gunicorn

WORKDIR /opt/frameserver
COPY src .
ENV PORT 7500
ENV LD_LIBRARY_PATH /usr/local/lib:$LD_LIBRARY_PATH
CMD gunicorn -c gunicorn_conf.py server:app
