FROM python:3.10-slim

RUN pip install --no-cache-dir openpyxl pandas

WORKDIR /app

COPY . .

RUN sed -i 's/\r//' verify.sh && chmod +x verify.sh variant.txt

ENTRYPOINT ["/bin/bash", "./verify.sh"]
