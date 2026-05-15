FROM python:3.10-alpine

RUN apk add --no-cache bash coreutils

WORKDIR /app

COPY . .

RUN sed -i 's/\r//' verify.sh && chmod +x verify.sh variant.txt

ENTRYPOINT ["/bin/bash", "./verify.sh"]
