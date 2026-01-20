# Use Python 3.11 base image with development tools
FROM mcr.microsoft.com/devcontainers/python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME=/opt/poetry \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies for multimedia processing
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    ffmpeg \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry

# Verify Poetry installation
RUN poetry --version

# Set working directory
WORKDIR /workspace

# Copy dependency files for caching
COPY pyproject.toml poetry.lock* ./

# Install Python dependencies (this layer will be cached)
RUN poetry install --no-root --no-interaction || true

# Create directories for outputs
RUN mkdir -p outputs/images outputs/videos outputs/audio logs data

# Set proper permissions for vscode user
RUN chown -R vscode:vscode /workspace
