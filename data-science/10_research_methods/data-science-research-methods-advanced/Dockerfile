# Advanced Data Science Research Methods - Docker Container
# Based on official Jupyter stack

FROM jupyter/scipy-notebook:latest

# Metadata
LABEL maintainer="Research Skills Portfolio"
LABEL description="Intermediate Data Science Research Methods Environment"
LABEL version="1.0"

# Set working directory
WORKDIR /workspace

# Copy requirements
COPY requirements.txt /tmp/requirements.txt

# Install Python packages
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Install additional system packages if needed
USER root
RUN apt-get update && apt-get install -y \
    git \
    graphviz \
    && rm -rf /var/lib/apt/lists/*

# Switch back to jovyan user
USER ${NB_UID}

# Copy project files
COPY --chown=${NB_UID}:${NB_GID} . /workspace/

# Expose Jupyter port
EXPOSE 8888

# Set environment variables
ENV JUPYTER_ENABLE_LAB=yes

# Start Jupyter
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
