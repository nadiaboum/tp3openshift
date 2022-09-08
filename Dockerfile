
FROM : 3.9
COPY . /application
WORKDIR /app

RUN pip install flask

ENV PYTHONUNBUFFERED 1

EXPOSER 8001
CMD python3 ./main.py