FROM python:3.10-slim

RUN pip install --no-cache-dir openpyxl pandas

WORKDIR /app

COPY . .

RUN chmod +x verify.sh variant.txt

ENTRYPOINT ["/bin/bash", "./verify.sh"]
