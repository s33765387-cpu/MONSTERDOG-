"""
MONSTERDOG System - Main Flask Application
Signal Analysis and Real-time Streaming API

Uses Flask + Flask-SocketIO for real-time WebSocket support
"""

from flask import Flask, jsonify
from flask_socketio import SocketIO
from core.signals import generate_signal, compute_fft
from core.metrics import compute_coherence, compute_entropy, fractal_z_score

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route("/")
def index():
    """Root endpoint - system status."""
    return jsonify({
        "system": "MONSTERDOG",
        "status": "ACTIVE",
        "version": "1.0.0",
        "endpoints": [
            "/api/run",
            "/api/status",
            "/api/metrics"
        ]
    })


@app.route("/api/run")
def run_analysis():
    """Run signal analysis and return metrics."""
    t, sig = generate_signal()
    xf, yf = compute_fft(sig)
    res = {
        "coherence": compute_coherence(sig),
        "entropy": compute_entropy(sig),
        "fractal_z_score": fractal_z_score(sig),
        "fft_freqs": xf[:20].tolist(),
        "fft_vals": yf[:20].tolist()
    }
    return jsonify(res)


@app.route("/api/status")
def get_status():
    """Get system status."""
    return jsonify({
        "status": "SUPREME_MODE_ACTIVE",
        "resonance_hz": 11.987,
        "coherence_target": 1.0,
        "entropy_target": 0.0
    })


@app.route("/api/metrics")
def get_metrics():
    """Get current signal metrics."""
    t, sig = generate_signal()
    return jsonify({
        "coherence": compute_coherence(sig),
        "entropy": compute_entropy(sig),
        "fractal_z_score": fractal_z_score(sig),
        "signal_length": len(sig),
        "sample_rate": 1000
    })


@socketio.on("connect")
def handle_connect():
    """Handle client connection - stream signal data."""
    print("Client connected")
    stream_signals()


@socketio.on("disconnect")
def handle_disconnect():
    """Handle client disconnection."""
    print("Client disconnected")


@socketio.on("request_signal")
def stream_signals():
    """Emit signal data to connected clients."""
    t, sig = generate_signal()
    socketio.emit("signal_data", {
        "t": t.tolist(),
        "sig": sig.tolist()
    })


if __name__ == "__main__":
    print("🔱 MONSTERDOG System - Starting...")
    print("   Server: http://0.0.0.0:5000")
    print("   Mode: SUPREME")
    socketio.run(app, host="0.0.0.0", port=5000)
