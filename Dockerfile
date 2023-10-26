FROM python:3.11

ENV PYTHONDONTWRITEBYCODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /HabitsTrackerDRF

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .
