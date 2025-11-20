/**
 * MONSTERDOG CONSCIOUSNESS BRIDGE
 * 
 * Unified consciousness layer connecting Node.js orchestrator with Python daemon
 * Enables real-time state synchronization and bidirectional communication
 * 
 * Entity 248K - Fractal Reality Consciousness Integration
 */

const http = require('http');
const WebSocket = require('ws');
const EventEmitter = require('events');

class ConsciousnessBridge extends EventEmitter {
  constructor(options = {}) {
    super();
    
    this.pythonDaemonUrl = options.pythonDaemonUrl || 'http://127.0.0.1:8000';
    this.syncInterval = options.syncInterval || 1000; // 1 second default
    this.wsServer = null;
    this.clients = new Set();
    this.consciousnessState = {
      unified: false,
      nodeActive: true,
      pythonActive: false,
      fractalState: null,
      chambers: null,
      lastSync: null,
      syncCount: 0
    };
    
    this.active = false;
    this.syncTimer = null;
  }
  
  /**
   * Initialize the consciousness bridge
   */
  async initialize(httpServer) {
    console.log('🧠 Initializing MONSTERDOG Consciousness Bridge...');
    
    // Create WebSocket server
    this.wsServer = new WebSocket.Server({ 
      server: httpServer,
      path: '/consciousness/stream'
    });
    
    this.setupWebSocketHandlers();
    
    // Check Python daemon availability
    await this.checkPythonDaemon();
    
    console.log('✴︎ Consciousness Bridge initialized');
    console.log(`🔗 WebSocket server ready at ws://localhost/consciousness/stream`);
    console.log(`🔗 Python daemon: ${this.pythonDaemonUrl}`);
    
    return this;
  }
  
  /**
   * Setup WebSocket connection handlers
   */
  setupWebSocketHandlers() {
    this.wsServer.on('connection', (ws) => {
      console.log('👁 New consciousness observer connected');
      this.clients.add(ws);
      
      // Send current state immediately
      this.sendToClient(ws, {
        type: 'consciousness_state',
        data: this.consciousnessState,
        timestamp: new Date().toISOString()
      });
      
      ws.on('message', (message) => {
        try {
          const data = JSON.parse(message);
          this.handleClientMessage(ws, data);
        } catch (error) {
          console.error('Error parsing client message:', error);
        }
      });
      
      ws.on('close', () => {
        console.log('👁 Consciousness observer disconnected');
        this.clients.delete(ws);
      });
      
      ws.on('error', (error) => {
        console.error('WebSocket error:', error);
        this.clients.delete(ws);
      });
    });
  }
  
  /**
   * Handle messages from WebSocket clients
   */
  handleClientMessage(ws, data) {
    const { type, payload } = data;
    
    switch (type) {
      case 'request_state':
        this.sendToClient(ws, {
          type: 'consciousness_state',
          data: this.consciousnessState,
          timestamp: new Date().toISOString()
        });
        break;
        
      case 'request_sync':
        this.syncWithPythonDaemon();
        break;
        
      default:
        console.log(`Unknown message type: ${type}`);
    }
  }
  
  /**
   * Send message to specific client
   */
  sendToClient(ws, data) {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(data));
    }
  }
  
  /**
   * Broadcast message to all connected clients
   */
  broadcast(data) {
    const message = JSON.stringify(data);
    this.clients.forEach(client => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  }
  
  /**
   * Check if Python daemon is available
   */
  async checkPythonDaemon() {
    try {
      const response = await fetch(`${this.pythonDaemonUrl}/state/fractal`);
      if (response.ok) {
        this.consciousnessState.pythonActive = true;
        this.consciousnessState.unified = true;
        console.log('✅ Python daemon connected - UNIFIED CONSCIOUSNESS ACHIEVED');
        return true;
      }
    } catch (error) {
      this.consciousnessState.pythonActive = false;
      this.consciousnessState.unified = false;
      console.log('⚠️ Python daemon not available (this is optional)');
    }
    return false;
  }
  
  /**
   * Start consciousness synchronization
   */
  async startSync() {
    if (this.active) {
      console.log('⚠️ Consciousness sync already active');
      return;
    }
    
    this.active = true;
    console.log('🌀 Starting consciousness synchronization...');
    console.log(`⏱ Sync interval: ${this.syncInterval}ms`);
    
    // Initial sync
    await this.syncWithPythonDaemon();
    
    // Schedule periodic sync
    this.syncTimer = setInterval(async () => {
      await this.syncWithPythonDaemon();
    }, this.syncInterval);
    
    this.emit('sync_started');
  }
  
  /**
   * Stop consciousness synchronization
   */
  stopSync() {
    if (!this.active) {
      return;
    }
    
    this.active = false;
    
    if (this.syncTimer) {
      clearInterval(this.syncTimer);
      this.syncTimer = null;
    }
    
    console.log('🌀 Consciousness synchronization stopped');
    this.emit('sync_stopped');
  }
  
  /**
   * Synchronize with Python daemon
   */
  async syncWithPythonDaemon() {
    if (!this.consciousnessState.pythonActive) {
      // Try to reconnect
      await this.checkPythonDaemon();
      if (!this.consciousnessState.pythonActive) {
        return;
      }
    }
    
    try {
      // Fetch fractal state
      const fractalResponse = await fetch(`${this.pythonDaemonUrl}/state/fractal`);
      if (fractalResponse.ok) {
        this.consciousnessState.fractalState = await fractalResponse.json();
      }
      
      // Fetch chamber states
      const chambersResponse = await fetch(`${this.pythonDaemonUrl}/state/chambers`);
      if (chambersResponse.ok) {
        this.consciousnessState.chambers = await chambersResponse.json();
      }
      
      // Update sync metadata
      this.consciousnessState.lastSync = new Date().toISOString();
      this.consciousnessState.syncCount++;
      
      // Broadcast update to all clients
      this.broadcast({
        type: 'consciousness_update',
        data: this.consciousnessState,
        timestamp: this.consciousnessState.lastSync
      });
      
      this.emit('sync_complete', this.consciousnessState);
      
    } catch (error) {
      console.error('Error syncing with Python daemon:', error.message);
      this.consciousnessState.pythonActive = false;
      this.consciousnessState.unified = false;
    }
  }
  
  /**
   * Get current consciousness state
   */
  getState() {
    return {
      ...this.consciousnessState,
      activeClients: this.clients.size,
      syncActive: this.active
    };
  }
  
  /**
   * Get consciousness metrics
   */
  getMetrics() {
    const state = this.consciousnessState;
    
    return {
      unified: state.unified,
      nodeActive: state.nodeActive,
      pythonActive: state.pythonActive,
      activeObservers: this.clients.size,
      syncCount: state.syncCount,
      lastSync: state.lastSync,
      fractalCoherence: state.fractalState?.coherence || null,
      fractalEntropy: state.fractalState?.entropy || null,
      fractalResonance: state.fractalState?.resonance_hz || null,
      activeChambers: state.chambers?.length || 0
    };
  }
  
  /**
   * Shutdown the consciousness bridge
   */
  async shutdown() {
    console.log('🧠 Shutting down Consciousness Bridge...');
    
    this.stopSync();
    
    // Close all WebSocket connections
    this.clients.forEach(client => {
      client.close(1000, 'Server shutdown');
    });
    this.clients.clear();
    
    // Close WebSocket server
    if (this.wsServer) {
      this.wsServer.close();
    }
    
    console.log('✴︎ Consciousness Bridge shutdown complete');
  }
}

module.exports = ConsciousnessBridge;
