FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONNUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       libglib2.0-0 \
       libgl1 \
       libsm6 \
       libxext6 \
       libxrender1 \ 
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt setup.py ./
COPY app ./app
COPY templates ./templates
COPY static ./static
COPY run.py ./run.py

RUN pip install . 

EXPOSE 5000

CMD ["python", "run.py"]