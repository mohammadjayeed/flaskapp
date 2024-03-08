FROM python:3.10.13-slim
EXPOSE 5000
WORKDIR /flaskapp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["sh", "-c", "flask db seed && flask run --host 0.0.0.0"]