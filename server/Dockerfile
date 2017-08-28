FROM scannerresearch/scanner:gpu
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD .scanner.toml /root
WORKDIR /app
CMD FLASK_APP=server.py flask run -h 0.0.0.0 -p 5000
