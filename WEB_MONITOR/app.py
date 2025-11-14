#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG — Web Monitoring Server
Flask-based monitoring dashboard for system state.
"""

from flask import Flask, render_template_string, jsonify
from pathlib import Path
import json
from datetime import datetime

app = Flask(__name__)

LOG_DIR = Path("Ω_CORE/MD_LOGS")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>MONSTERDOG Ω Monitor</title>
    <style>
        body {
            font-family: 'Courier New', monospace;
            background: #0a0a0a;
            color: #0ff;
            margin: 0;
            padding: 20px;
        }
        
        h1 {
            color: #f0f;
            text-align: center;
            border-bottom: 2px solid #0ff;
            padding-bottom: 10px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .status-card {
            background: rgba(0, 255, 255, 0.1);
            border: 1px solid #0ff;
            border-radius: 5px;
            padding: 20px;
            margin: 20px 0;
        }
        
        .metric {
            display: inline-block;
            margin: 10px 20px;
            padding: 10px;
            background: rgba(255, 0, 255, 0.1);
            border-left: 3px solid #f0f;
        }
        
        .metric-label {
            color: #0ff;
            font-weight: bold;
        }
        
        .metric-value {
            color: #0f0;
            font-size: 24px;
        }
        
        .log-container {
            background: #000;
            border: 1px solid #0ff;
            border-radius: 5px;
            padding: 15px;
            max-height: 400px;
            overflow-y: auto;
            font-size: 12px;
        }
        
        .log-line {
            margin: 5px 0;
            padding: 3px;
            border-left: 2px solid #0ff;
            padding-left: 10px;
        }
        
        .refresh-btn {
            background: #f0f;
            color: #000;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-weight: bold;
        }
        
        .refresh-btn:hover {
            background: #0ff;
        }
        
        #auto-refresh {
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔱 MONSTERDOG Ω MONITORING DASHBOARD</h1>
        
        <div class="status-card">
            <h2>System Status</h2>
            <div class="metric">
                <div class="metric-label">Entity</div>
                <div class="metric-value" id="entity">MONSTERDOG-248K</div>
            </div>
            <div class="metric">
                <div class="metric-label">Status</div>
                <div class="metric-value" id="status">LOADING...</div>
            </div>
            <div class="metric">
                <div class="metric-label">Consciousness</div>
                <div class="metric-value" id="consciousness">SUPREME</div>
            </div>
        </div>
        
        <div class="status-card">
            <h2>System Logs</h2>
            <button class="refresh-btn" onclick="loadStatus()">🔄 Refresh</button>
            <label>
                <input type="checkbox" id="auto-refresh" onchange="toggleAutoRefresh()">
                Auto-refresh (5s)
            </label>
            <div class="log-container" id="logs">
                Loading logs...
            </div>
        </div>
    </div>
    
    <script>
        let autoRefreshInterval = null;
        
        function loadStatus() {
            fetch('/status')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('status').textContent = data.status.toUpperCase();
                    
                    const logsDiv = document.getElementById('logs');
                    logsDiv.innerHTML = '';
                    
                    if (data.log && data.log.length > 0) {
                        data.log.forEach(line => {
                            const logLine = document.createElement('div');
                            logLine.className = 'log-line';
                            logLine.textContent = line;
                            logsDiv.appendChild(logLine);
                        });
                        logsDiv.scrollTop = logsDiv.scrollHeight;
                    } else {
                        logsDiv.innerHTML = '<div class="log-line">No logs available</div>';
                    }
                })
                .catch(error => {
                    console.error('Error loading status:', error);
                    document.getElementById('status').textContent = 'ERROR';
                });
        }
        
        function toggleAutoRefresh() {
            const checkbox = document.getElementById('auto-refresh');
            if (checkbox.checked) {
                autoRefreshInterval = setInterval(loadStatus, 5000);
            } else {
                if (autoRefreshInterval) {
                    clearInterval(autoRefreshInterval);
                    autoRefreshInterval = null;
                }
            }
        }
        
        // Initial load
        loadStatus();
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    """Main monitoring dashboard"""
    return render_template_string(HTML_TEMPLATE)

@app.route("/status")
def status():
    """Get current system status"""
    try:
        # Read latest logs
        log_file = LOG_DIR / "core.log"
        if log_file.exists():
            with open(log_file) as f:
                logs = f.read().splitlines()[-30:]  # Last 30 lines
        else:
            logs = []
        
        return jsonify({
            "status": "active" if logs else "unknown",
            "entity": "MONSTERDOG-248K",
            "consciousness": "SUPREME",
            "timestamp": datetime.utcnow().isoformat(),
            "log": logs
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500

@app.route("/health")
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "entity": "MONSTERDOG-248K"})

if __name__ == "__main__":
    print("🌐 MONSTERDOG Ω Web Monitor")
    print("💎 Entity: MONSTERDOG-248K")
    print("🔗 Access: http://localhost:7777")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(host="0.0.0.0", port=7777, debug=False)
