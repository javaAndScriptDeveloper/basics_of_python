FROM python:3.10-alpine

RUN apk add --no-cache bash coreutils

WORKDIR /app

COPY . .

RUN chmod +x verify.sh variant.txt

ENTRYPOINT ["/bin/bash", "./verify.sh"]
