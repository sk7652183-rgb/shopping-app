# ---------- Build stage ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build deps only in this stage (kept out of final image)
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# ---------- Final stage ----------
FROM python:3.12-slim

WORKDIR /app

# Patch OS packages and strip unneeded ones (perl-base accounts for
# most current CVE findings and isn't needed by a Python app)
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get purge -y --auto-remove perl-base 2>/dev/null || true \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy installed Python packages from the build stage
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY . .

# Run as non-root
RUN useradd --create-home --shell /bin/bash appuser \
    && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
