FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install flask mysql-connector-python

EXPOSE 5000

CMD ["python", "app.py"]
