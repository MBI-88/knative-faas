FROM python:3.12-slim 

ENV PYTHONUNBUFFERED True

WORKDIR /app 

COPY . . 

RUN  pip install -r ./requirements.txt
ENV PORT=8000

EXPOSE ${PORT}

CMD exec gunicorn --bind "0.0.0.0:${PORT}" --workers 1 --threads 8 --timeout 0 main:app
