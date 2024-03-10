FROM python:3.10.13-slim
ENV PYTHONBUFFERED=1
WORKDIR /flaskapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["sh", "-c", "sleep 10s && flask db seed && flask run --host 0.0.0.0"]