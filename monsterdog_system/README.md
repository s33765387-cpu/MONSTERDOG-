# MONSTERDOG System

🔱 **A comprehensive signal processing and visualization system with WebXR, Dash, and Streamlit dashboards.**

## 📦 Project Structure

```
monsterdog_system/
├── app.py                 # Flask + SocketIO main application
├── dockerfile             # Docker container configuration
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── core/                  # Core processing modules
│   ├── signals.py         # Signal generation and FFT
│   ├── metrics.py         # Coherence, entropy, fractal metrics
│   ├── viz.py             # Visualization for diagrams
│   └── fractal.py         # Fractal reality engine
├── webxr/                 # WebXR 3D visualization
│   ├── index.html         # A-Frame WebXR scene
│   └── xr_app.js          # WebXR socket integration
├── dashboard/             # Interactive dashboards
│   ├── dash_app.py        # Plotly Dash dashboard
│   └── streamlit_app.py   # Streamlit dashboard
├── pdf/                   # PDF report generation
│   ├── pdf_gen.py         # PDF generator script
│   └── diagrams/          # Generated diagrams
├── tests/                 # Unit tests
│   ├── test_signals.py    # Signal processing tests
│   └── test_metrics.py    # Metrics computation tests
├── infra/                 # Kubernetes deployment
│   ├── k8s_deploy.yaml    # Deployment manifest
│   ├── k8s_service.yaml   # Service and config
│   └── grafana_datasource.yaml
└── monitoring/            # Monitoring configuration
    ├── prometheus.yml     # Prometheus scrape config
    └── grafana_dashboards.json
```

## 🚀 Quick Start

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
# Server: http://0.0.0.0:5000
```

### Run Dash Dashboard

```bash
python dashboard/dash_app.py
# Dashboard: http://127.0.0.1:8050
```

### Run Streamlit Dashboard

```bash
streamlit run dashboard/streamlit_app.py
# Dashboard: http://localhost:8501
```

### Generate PDF Report

```bash
python pdf/pdf_gen.py
# Output: monsterdog_report.pdf
```

### Run Tests

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=core --cov-report=html
```

## 🐳 Docker

### Build Image

```bash
docker build -t monsterdog-system .
```

### Run Container

```bash
docker run -p 5000:5000 -p 8050:8050 monsterdog-system
```

## ☸️ Kubernetes Deployment

```bash
kubectl apply -f infra/k8s_deploy.yaml
kubectl apply -f infra/k8s_service.yaml
```

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | System status |
| `/api/run` | GET | Run signal analysis |
| `/api/status` | GET | Get system status |
| `/api/metrics` | GET | Get current metrics |

### WebSocket Events

- `connect` - Client connected, receives signal data
- `request_signal` - Request new signal data
- `signal_data` - Emitted signal data

## 🧮 Core Metrics

| Metric | Symbol | Target | Description |
|--------|--------|--------|-------------|
| Coherence | ψ | 1.0 | Signal stability measure |
| Entropy | S | 0.0 | Signal disorder measure |
| Resonance | Hz | 11.987 | Fundamental frequency |
| Drift | Δ | 0.0 | Deviation from target |

## 🗄️ Database Schema (TimescaleDB)

```sql
CREATE TABLE signals (
  id SERIAL PRIMARY KEY,
  ts timestamptz DEFAULT now(),
  freq float,
  amplitude float,
  coherence float,
  entropy float,
  meta jsonb
);

-- Enable TimescaleDB
SELECT create_hypertable('signals', 'ts');
```

## 📈 Grafana Queries

### Coherence Over Time
```sql
SELECT ts, coherence FROM signals WHERE $__timeFilter(ts)
```

### Signal Amplitude
```sql
SELECT ts, amplitude FROM signals WHERE $__timeFilter(ts)
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_signals.py -v

# Run with coverage
pip install coverage
coverage run -m pytest tests/
coverage report
coverage html  # Generate HTML report
```

## 🔧 Configuration

Environment variables:
- `FLASK_ENV` - Flask environment (production/development)
- `SUPREME_MODE` - Enable supreme mode (active/disabled)
- `RESONANCE_HZ` - Target resonance frequency (default: 11.987)

## 📋 Requirements

- Python 3.8+
- Node.js 18+ (for WebXR development)
- Docker (optional)
- Kubernetes (for deployment)

## 📄 License

MIT License

---

✴︎ **MONSTERDOG ENTITY 248K - SUPREME MODE ACTIVE** ✴︎
