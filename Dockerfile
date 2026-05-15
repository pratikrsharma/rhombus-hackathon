FROM python:3.10-slim-bookworm

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

RUN useradd -m myappuser
USER myappuser

EXPOSE 8000

CMD ["python3", "app.py"]

