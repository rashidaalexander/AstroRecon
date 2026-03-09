FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install .
CMD ["python", "-m", "astrorecon.cli", "catalog", "data/sample_catalog.json"]
