/**
 * MONSTERDOG XR Application
 * Real-time signal visualization in WebXR
 */

// Connect to the Flask-SocketIO server
const SOCKET_URL = window.location.origin || 'http://localhost:5000';
let socket = null;

// State
let signalData = {
    t: [],
    sig: []
};
let coherence = 0.99995;
let isConnected = false;

// Initialize socket connection
function initSocket() {
    try {
        socket = io(SOCKET_URL);
        
        socket.on('connect', () => {
            console.log('🔗 Connected to MONSTERDOG server');
            isConnected = true;
            updateStatus('Connected');
            requestSignalData();
        });
        
        socket.on('disconnect', () => {
            console.log('❌ Disconnected from server');
            isConnected = false;
            updateStatus('Disconnected');
        });
        
        socket.on('signal_data', (data) => {
            console.log('📊 Received signal data:', data.sig.length, 'points');
            signalData = data;
            updateVisualization(data);
            updateMetrics(data);
        });
        
        socket.on('connect_error', (error) => {
            console.warn('⚠️ Connection error:', error.message);
            updateStatus('Connection error');
        });
        
    } catch (error) {
        console.error('Failed to initialize socket:', error);
        updateStatus('Socket init failed');
    }
}

// Request signal data from server
function requestSignalData() {
    if (socket && isConnected) {
        socket.emit('request_signal');
    }
}

// Update status display
function updateStatus(status) {
    const statusEl = document.getElementById('status');
    if (statusEl) {
        statusEl.textContent = status;
        statusEl.style.color = status === 'Connected' ? '#0f0' : '#f00';
    }
}

// Update metrics display
function updateMetrics(data) {
    const pointsEl = document.getElementById('points');
    if (pointsEl && data.sig) {
        pointsEl.textContent = data.sig.length;
    }
    
    // Calculate approximate coherence from signal variance
    if (data.sig && data.sig.length > 0) {
        const mean = data.sig.reduce((a, b) => a + b, 0) / data.sig.length;
        const variance = data.sig.reduce((a, b) => a + Math.pow(b - mean, 2), 0) / data.sig.length;
        const maxVal = Math.max(...data.sig.map(Math.abs));
        coherence = maxVal > 0 ? 1 - (variance / Math.pow(maxVal, 2)) : 1;
        coherence = Math.max(0, Math.min(1, coherence));
        
        const coherenceEl = document.getElementById('coherence');
        if (coherenceEl) {
            coherenceEl.textContent = coherence.toFixed(6);
        }
    }
}

// Update the 3D visualization
function updateVisualization(data) {
    const signalWave = document.querySelector('#signalWave');
    if (!signalWave || !data.sig || data.sig.length === 0) return;
    
    // Clear existing visualization
    while (signalWave.firstChild) {
        signalWave.removeChild(signalWave.firstChild);
    }
    
    // Create line visualization using boxes
    const step = Math.max(1, Math.floor(data.sig.length / 200)); // Limit points for performance
    
    for (let i = 0; i < data.sig.length; i += step) {
        const box = document.createElement('a-box');
        const x = (i / data.sig.length) * 10 - 5;
        const y = data.sig[i] * 0.5;
        const z = 0;
        
        box.setAttribute('position', `${x} ${y} ${z}`);
        box.setAttribute('width', '0.05');
        box.setAttribute('height', '0.05');
        box.setAttribute('depth', '0.05');
        
        // Color based on amplitude
        const hue = 180 + data.sig[i] * 60; // Cyan to magenta
        box.setAttribute('color', `hsl(${hue}, 100%, 50%)`);
        
        signalWave.appendChild(box);
    }
    
    // Update fractal boxes
    updateFractalBoxes(data);
}

// Update fractal visualization boxes
function updateFractalBoxes(data) {
    const fractalBoxes = document.querySelector('#fractal-boxes');
    if (!fractalBoxes) return;
    
    // Clear existing
    while (fractalBoxes.firstChild) {
        fractalBoxes.removeChild(fractalBoxes.firstChild);
    }
    
    // Create fractal pattern based on FFT (simulated here)
    const numBoxes = 20;
    const radius = 2;
    
    for (let i = 0; i < numBoxes; i++) {
        const angle = (i / numBoxes) * Math.PI * 2;
        const box = document.createElement('a-box');
        
        const x = Math.cos(angle) * radius;
        const z = Math.sin(angle) * radius;
        const y = Math.sin(angle * 3 + Date.now() / 1000) * 0.5;
        
        box.setAttribute('position', `${x} ${y} ${z}`);
        box.setAttribute('width', '0.2');
        box.setAttribute('height', '0.2');
        box.setAttribute('depth', '0.2');
        box.setAttribute('color', `hsl(${i * 18}, 100%, 50%)`);
        box.setAttribute('opacity', '0.7');
        
        fractalBoxes.appendChild(box);
    }
}

// Animation loop
function animate() {
    // Update core entity based on coherence
    const core = document.querySelector('#monsterdog-core');
    if (core) {
        const scale = 1 + (coherence - 0.5) * 0.1;
        core.setAttribute('scale', `${scale} ${scale} ${scale}`);
    }
    
    requestAnimationFrame(animate);
}

// Periodic data request
function startDataLoop() {
    setInterval(() => {
        if (isConnected) {
            requestSignalData();
        }
    }, 1000); // Request new data every second
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
    console.log('🔱 MONSTERDOG XR Initializing...');
    initSocket();
    startDataLoop();
    animate();
});

// Fallback if socket not available - generate demo data
setTimeout(() => {
    if (!isConnected) {
        console.log('📡 Using demo mode (no server connection)');
        updateStatus('Demo Mode');
        
        // Generate demo signal
        const t = [];
        const sig = [];
        for (let i = 0; i < 2000; i++) {
            t.push(i / 1000);
            sig.push(Math.sin(2 * Math.PI * 11.987 * i / 1000));
        }
        
        updateVisualization({ t, sig });
        updateMetrics({ t, sig });
    }
}, 3000);
