FROM python:3.12-alpine AS builder
WORKDIR /app

COPY requirements.txt .
COPY requirements-dev.txt .
RUN pip install -r requirements.txt -r requirements-dev.txt

COPY . .
RUN python -m unittest tests/**/test*.py

FROM python:3.12-alpine
WORKDIR /app

EXPOSE 8000

# Copy and install dependencies first, so code changes don't affect their cache
COPY --from=builder /app/requirements.txt .

RUN pip install -r requirements.txt

COPY --from=builder /app .

CMD [ "fastapi", "dev", "infrastructure/fastapi_app.py", "--host", "0.0.0.0" ]