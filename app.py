import os
from flask import Flask, render_template_string

app = Flask(__name__)

# ── Configuration from environment variables ──────────────────────────────────
APP_NAME = os.environ.get("APP_NAME",    "MyFlaskApp")
APP_ENV = os.environ.get("APP_ENV",     "development")
APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")
APP_PORT = int(os.environ.get("APP_PORT", "5000"))
APP_AUTHOR = os.environ.get("APP_AUTHOR",  "Demo User")
SECRET_KEY = os.environ.get("SECRET_KEY",  "change-me-in-production")

app.secret_key = SECRET_KEY

# ── HTML template ─────────────────────────────────────────────────────────────
TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{{ app_name }}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:        #0a0e17;
      --surface:   #111827;
      --border:    #1e2d40;
      --accent:    #00e5ff;
      --accent2:   #7c3aed;
      --text:      #e2e8f0;
      --muted:     #64748b;
      --ok:        #22d3a5;
      --warn:      #f59e0b;
      --radius:    12px;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Syne', sans-serif;
      min-height: 100vh;
      display: grid;
      place-items: center;
      padding: 2rem;
      background-image:
        radial-gradient(ellipse 60% 40% at 20% 10%, rgba(0,229,255,.06) 0%, transparent 60%),
        radial-gradient(ellipse 50% 40% at 80% 80%, rgba(124,58,237,.07) 0%, transparent 60%);
    }

    .card {
      width: 100%;
      max-width: 680px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: 0 24px 64px rgba(0,0,0,.5);
      animation: fadeUp .5s ease both;
    }

    @keyframes fadeUp {
      from { opacity:0; transform: translateY(20px); }
      to   { opacity:1; transform: translateY(0); }
    }

    .card-header {
      padding: 2rem 2rem 1.5rem;
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .logo {
      width: 44px; height: 44px;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      border-radius: 10px;
      display: grid;
      place-items: center;
      font-size: 1.3rem;
      flex-shrink: 0;
    }

    h1 {
      font-size: 1.5rem;
      font-weight: 800;
      letter-spacing: -.02em;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: .35rem;
      font-size: .7rem;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: .08em;
      padding: .25rem .65rem;
      border-radius: 999px;
      margin-left: .5rem;
    }

    .badge.production { background: rgba(34,211,165,.12); color: var(--ok);  border: 1px solid rgba(34,211,165,.3); }
    .badge.development{ background: rgba(245,158,11,.12); color: var(--warn); border: 1px solid rgba(245,158,11,.3); }

    .badge::before { content: '●'; font-size: .5rem; }

    .card-body { padding: 2rem; display: flex; flex-direction: column; gap: 1rem; }

    .row {
      display: grid;
      grid-template-columns: 180px 1fr;
      align-items: center;
      gap: 1rem;
      padding: .85rem 1rem;
      background: rgba(255,255,255,.02);
      border: 1px solid var(--border);
      border-radius: 8px;
      transition: background .2s;
    }
    .row:hover { background: rgba(255,255,255,.04); }

    .label {
      font-size: .7rem;
      font-family: 'JetBrains Mono', monospace;
      text-transform: uppercase;
      letter-spacing: .1em;
      color: var(--muted);
    }

    .value {
      font-family: 'JetBrains Mono', monospace;
      font-size: .9rem;
      color: var(--accent);
      word-break: break-all;
    }

    .value.masked { color: var(--muted); filter: blur(4px); transition: filter .2s; cursor: pointer; }
    .value.masked:hover { filter: none; }

    .card-footer {
      padding: 1.25rem 2rem;
      border-top: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: .75rem;
      color: var(--muted);
      font-family: 'JetBrains Mono', monospace;
    }

    .status-dot {
      display: inline-flex; align-items: center; gap: .4rem;
    }
    .dot {
      width: 8px; height: 8px; border-radius: 50%;
      background: var(--ok);
      box-shadow: 0 0 8px var(--ok);
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%,100% { opacity:1; }
      50%      { opacity:.4; }
    }
  </style>
</head>
<body>
  <div class="card">
    <div class="card-header">
      <div class="logo">🐍</div>
      <div>
        <h1>
          {{ app_name }}
          <span class="badge {{ app_env }}">{{ app_env }}</span>
        </h1>
        <p style="font-size:.85rem; color:var(--muted); margin-top:.25rem;">
          Dockerized Python · Flask · Environment Config Demo
        </p>
      </div>
    </div>

    <div class="card-body">
      <div class="row">
        <span class="label">APP_NAME</span>
        <span class="value">{{ app_name }}</span>
      </div>
      <div class="row">
        <span class="label">APP_VERSION</span>
        <span class="value">{{ app_version }}</span>
      </div>
      <div class="row">
        <span class="label">APP_ENV</span>
        <span class="value">{{ app_env }}</span>
      </div>
      <div class="row">
        <span class="label">APP_PORT</span>
        <span class="value">{{ app_port }}</span>
      </div>
      <div class="row">
        <span class="label">APP_AUTHOR</span>
        <span class="value">{{ app_author }}</span>
      </div>
      <div class="row">
        <span class="label">SECRET_KEY</span>
        <span class="value masked" title="hover to reveal">{{ secret_key }}</span>
      </div>
    </div>

    <div class="card-footer">
      <span class="status-dot"><span class="dot"></span> Running on port {{ app_port }}</span>
      <span>v{{ app_version }}</span>
    </div>
  </div>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(
        TEMPLATE,
        app_name=APP_NAME,
        app_env=APP_ENV,
        app_version=APP_VERSION,
        app_port=APP_PORT,
        app_author=APP_AUTHOR,
        secret_key=SECRET_KEY,
    )


@app.route("/health")
def health():
    return {"status": "ok", "app": APP_NAME, "version": APP_VERSION}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT, debug=(APP_ENV == "development"))
