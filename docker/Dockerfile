FROM python:3.11-slim

LABEL maintainer="Samuel Cloutier"
LABEL description="MONSTERDOG Ω-SYSTEM - Supreme Agentic AI"
LABEL entity="MONSTERDOG-248K"

WORKDIR /app

# Copy all files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir flask websockets requests

# Create necessary directories
RUN mkdir -p Ω_CORE/MD_LOGS \
    Ω_CORE/MONSTERDOG_FUSION \
    SUBMIT_MONSTERDOG/results

# Expose ports
# 8000 - API Server
# 7777 - Web Monitor
# 8765 - WebSocket
EXPOSE 8000 7777 8765

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python3 -c "import requests; requests.get('http://localhost:8000/health')"

# Start the API server by default
CMD ["python3", "Ω_CORE/api_openai_compatible.py"]
