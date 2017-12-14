FROM scannerresearch/scanner-base:ubuntu16.04-cpu
ARG cores=1

WORKDIR /opt
RUN git clone https://github.com/scanner-research/storehouse/ && \
    cd storehouse && \
    cd thirdparty && mkdir build && cd build && cmake .. && make -j${cores} && cd ../../ && \
    mkdir build && cd build && cmake .. && make -j${cores} && cd .. && \
    cd python && python setup.py bdist_wheel && \
    cd .. && pip install python/dist/*
RUN git clone https://github.com/google/googletest && \
    cd googletest && mkdir build && cd build && cmake .. && make -j${cores} && make install && cd .. && \
    cd .. && rm -rf googletest
RUN git clone https://github.com/scanner-research/hwang && \
    cd hwang && \
    mkdir build && cd build && cmake .. && make -j${cores} && cd .. && \
    cd python && python setup.py bdist_wheel && \
    cd .. && pip install python/dist/*
RUN pip install flask gunicorn

WORKDIR /app
ENV PORT=7500
CMD gunicorn -c gunicorn_conf.py server:app
