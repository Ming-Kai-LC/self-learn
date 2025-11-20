# Multi-stage build for efficient container size
FROM python:3.9-slim as builder

# Set working directory
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    make \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# ==================== Final Stage ====================
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MODEL_PATH=/opt/ml/model \
    PYTHONPATH=/app

# Create non-root user for security
RUN useradd -m -u 1000 sagemaker && \
    mkdir -p /opt/ml/model /opt/ml/input /opt/ml/output && \
    chown -R sagemaker:sagemaker /opt/ml

# Set working directory
WORKDIR /app

# Copy Python packages from builder
COPY --from=builder /root/.local /home/sagemaker/.local

# Copy application code
COPY --chown=sagemaker:sagemaker src/ /app/

# Install nginx for SageMaker serving
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy nginx configuration
COPY docker/nginx.conf /etc/nginx/nginx.conf

# Create startup script
COPY docker/serve.sh /app/serve.sh
RUN chmod +x /app/serve.sh

# Switch to non-root user
USER sagemaker

# Make sure scripts are executable and in PATH
ENV PATH=/home/sagemaker/.local/bin:$PATH

# Expose port for SageMaker
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:8080/ping || exit 1

# Entry point
ENTRYPOINT ["/app/serve.sh"]
