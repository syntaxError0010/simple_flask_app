# ── Stage 1: base image ───────────────────────────────────────────────────────
FROM python:3.12-slim AS base

# Keeps Python from buffering stdout/stderr so logs appear immediately
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# ── Stage 2: install dependencies ─────────────────────────────────────────────
FROM base AS deps

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Stage 3: final image ───────────────────────────────────────────────────────
FROM base AS final

# Copy installed packages from deps stage
COPY --from=deps /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin

# Copy application source
COPY app.py .

# ── Environment variables with defaults (override at runtime) ──────────────────
ENV APP_NAME="MyFlaskApp" \
    APP_ENV="production" \
    APP_VERSION="1.0.0" \
    APP_PORT="5000" \
    APP_AUTHOR="Demo User" \
    SECRET_KEY="change-me-in-production"

# Expose the port the app listens on
EXPOSE 5000

# Create a non-root user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser

# ── Start the app ─────────────────────────────────────────────────────────────
CMD ["python", "app.py"]