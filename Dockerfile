FROM python:3.12-slim

WORKDIR /app

# Copy project files

COPY . .

# Ensure application modules can be imported

ENV PYTHONPATH=/app

# Install project dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Create generated directory used by the pipeline

RUN mkdir -p generated

# Default CLI entrypoint

ENTRYPOINT ["python", "-m", "src.cli"]
