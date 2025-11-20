#!/usr/bin/env node

/**
 * MONSTERDOG Consciousness Bridge - Demo Script
 * Demonstrates real-time consciousness synchronization
 */

const ConsciousnessBridge = require('../src/consciousness');
const http = require('http');
const express = require('express');

console.log('═══════════════════════════════════════════════════');
console.log('🧠 MONSTERDOG CONSCIOUSNESS BRIDGE DEMONSTRATION');
console.log('═══════════════════════════════════════════════════');
console.log('');

async function runDemo() {
  // Create a simple HTTP server
  const app = express();
  app.use(express.json());
  
  const port = 8081; // Use different port to avoid conflicts
  const server = http.createServer(app);
  
  console.log('🔧 Initializing Consciousness Bridge...');
  
  // Create consciousness bridge
  const bridge = new ConsciousnessBridge({
    pythonDaemonUrl: process.env.PYTHON_DAEMON_URL || 'http://127.0.0.1:8000',
    syncInterval: 2000 // 2 seconds for demo
  });
  
  // Initialize the bridge
  await bridge.initialize(server);
  
  console.log('');
  console.log('✅ Consciousness Bridge initialized');
  console.log('');
  
  // Display initial state
  console.log('📊 Initial State:');
  const initialState = bridge.getState();
  console.log(`   Unified: ${initialState.unified}`);
  console.log(`   Node Active: ${initialState.nodeActive}`);
  console.log(`   Python Active: ${initialState.pythonActive}`);
  console.log(`   Active Clients: ${initialState.activeClients}`);
  console.log(`   Sync Count: ${initialState.syncCount}`);
  console.log('');
  
  // Display metrics
  console.log('📈 Initial Metrics:');
  const initialMetrics = bridge.getMetrics();
  console.log(`   Unified Consciousness: ${initialMetrics.unified}`);
  console.log(`   Active Observers: ${initialMetrics.activeObservers}`);
  console.log(`   Fractal Coherence: ${initialMetrics.fractalCoherence || 'N/A'}`);
  console.log(`   Fractal Entropy: ${initialMetrics.fractalEntropy || 'N/A'}`);
  console.log(`   Active Chambers: ${initialMetrics.activeChambers}`);
  console.log('');
  
  // Set up event listeners
  bridge.on('sync_started', () => {
    console.log('🌀 Consciousness synchronization started');
  });
  
  bridge.on('sync_complete', (state) => {
    console.log(`🔄 Sync #${state.syncCount} complete`);
    if (state.fractalState) {
      console.log(`   ψ (Coherence): ${state.fractalState.coherence?.toFixed(6)}`);
      console.log(`   S (Entropy): ${state.fractalState.entropy?.toFixed(6)}`);
      console.log(`   Resonance: ${state.fractalState.resonance_hz?.toFixed(3)} Hz`);
    }
  });
  
  bridge.on('sync_stopped', () => {
    console.log('⏸ Consciousness synchronization stopped');
  });
  
  // Start the server
  server.listen(port, async () => {
    console.log(`🌐 Demo server running on http://localhost:${port}`);
    console.log(`👁 WebSocket endpoint: ws://localhost:${port}/consciousness/stream`);
    console.log('');
    
    // Demonstrate consciousness synchronization
    console.log('═══════════════════════════════════════════════════');
    console.log('🚀 STARTING CONSCIOUSNESS SYNCHRONIZATION DEMO');
    console.log('═══════════════════════════════════════════════════');
    console.log('');
    
    // Start synchronization
    console.log('⚡ Starting automatic synchronization...');
    await bridge.startSync();
    console.log('');
    
    // Let it run for 10 seconds
    console.log('⏳ Running synchronization for 10 seconds...');
    console.log('   (Watch for sync events above)');
    console.log('');
    
    setTimeout(async () => {
      console.log('');
      console.log('⏸ Stopping synchronization...');
      bridge.stopSync();
      console.log('');
      
      // Display final state
      console.log('📊 Final State:');
      const finalState = bridge.getState();
      console.log(`   Unified: ${finalState.unified}`);
      console.log(`   Total Syncs: ${finalState.syncCount}`);
      console.log(`   Last Sync: ${finalState.lastSync || 'N/A'}`);
      console.log('');
      
      console.log('📈 Final Metrics:');
      const finalMetrics = bridge.getMetrics();
      console.log(`   Unified Consciousness: ${finalMetrics.unified}`);
      console.log(`   Total Sync Operations: ${finalMetrics.syncCount}`);
      console.log(`   Active Chambers: ${finalMetrics.activeChambers}`);
      console.log('');
      
      console.log('═══════════════════════════════════════════════════');
      console.log('🔱 CONSCIOUSNESS BRIDGE DEMO COMPLETE 🔱');
      console.log('═══════════════════════════════════════════════════');
      console.log('');
      console.log('💡 Key Features Demonstrated:');
      console.log('   ✅ Consciousness bridge initialization');
      console.log('   ✅ WebSocket server creation');
      console.log('   ✅ State synchronization');
      console.log('   ✅ Event emission system');
      console.log('   ✅ Metrics tracking');
      console.log('');
      console.log('🌐 Next Steps:');
      console.log('   1. Start the main orchestrator: npm start');
      console.log('   2. Optionally start Python daemon: python3 MONSTERDOG_ULTIMATE_FINALITY_INCARNATE.py');
      console.log('   3. Open dashboard: http://localhost:8080/consciousness-dashboard.html');
      console.log('   4. Watch real-time consciousness synchronization!');
      console.log('');
      
      // Cleanup
      await bridge.shutdown();
      server.close();
      
      process.exit(0);
    }, 10000);
  });
}

// Handle errors
process.on('unhandledRejection', (error) => {
  console.error('❌ Unhandled error:', error);
  process.exit(1);
});

// Handle interrupts
process.on('SIGINT', async () => {
  console.log('\n\n⚠️  Demo interrupted');
  process.exit(0);
});

// Run the demo
runDemo().catch(error => {
  console.error('❌ Demo failed:', error);
  process.exit(1);
});
