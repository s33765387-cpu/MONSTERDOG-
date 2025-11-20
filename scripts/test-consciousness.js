/**
 * Test for MONSTERDOG Consciousness Bridge
 */

const ConsciousnessBridge = require('../src/consciousness');
const http = require('http');
const express = require('express');

console.log('═══════════════════════════════════════════════════');
console.log('🧠 Testing MONSTERDOG Consciousness Bridge');
console.log('═══════════════════════════════════════════════════\n');

let passed = 0;
let failed = 0;

function test(description, fn) {
  try {
    fn();
    console.log(`✅ ${description}`);
    passed++;
  } catch (error) {
    console.log(`❌ ${description}`);
    console.log(`   Error: ${error.message}`);
    failed++;
  }
}

// Test 1: Consciousness Bridge Creation
test('Consciousness bridge creation', () => {
  const bridge = new ConsciousnessBridge();
  if (!bridge) throw new Error('Bridge not created');
  if (bridge.active !== false) throw new Error('Bridge should not be active initially');
});

// Test 2: Consciousness Bridge with Options
test('Consciousness bridge with custom options', () => {
  const bridge = new ConsciousnessBridge({
    pythonDaemonUrl: 'http://localhost:9000',
    syncInterval: 2000
  });
  if (bridge.pythonDaemonUrl !== 'http://localhost:9000') {
    throw new Error('Python daemon URL not set correctly');
  }
  if (bridge.syncInterval !== 2000) {
    throw new Error('Sync interval not set correctly');
  }
});

// Test 3: Initial State
test('Initial consciousness state', () => {
  const bridge = new ConsciousnessBridge();
  const state = bridge.getState();
  
  if (state.unified !== false) throw new Error('Should not be unified initially');
  if (state.nodeActive !== true) throw new Error('Node should be active');
  if (state.pythonActive !== false) throw new Error('Python should not be active initially');
  if (state.syncCount !== 0) throw new Error('Sync count should be 0');
});

// Test 4: Initial Metrics
test('Initial consciousness metrics', () => {
  const bridge = new ConsciousnessBridge();
  const metrics = bridge.getMetrics();
  
  if (metrics.unified !== false) throw new Error('Should not be unified');
  if (metrics.activeObservers !== 0) throw new Error('No observers initially');
  if (metrics.syncCount !== 0) throw new Error('Sync count should be 0');
  if (metrics.fractalCoherence !== null) throw new Error('No fractal state initially');
});

// Test 5: Async Initialization (requires HTTP server)
test('Consciousness bridge initialization with server', async () => {
  const app = express();
  const server = http.createServer(app);
  
  const bridge = new ConsciousnessBridge();
  await bridge.initialize(server);
  
  if (!bridge.wsServer) throw new Error('WebSocket server not created');
  
  // Cleanup
  await bridge.shutdown();
  server.close();
});

// Test 6: State after initialization
test('State updates after check', async () => {
  const bridge = new ConsciousnessBridge({
    pythonDaemonUrl: 'http://localhost:9999' // Non-existent daemon
  });
  
  // Check daemon (should fail and update state)
  await bridge.checkPythonDaemon();
  
  const state = bridge.getState();
  if (state.pythonActive !== false) {
    throw new Error('Python should remain inactive with non-existent daemon');
  }
});

// Test 7: Event Emitter
test('Consciousness bridge is event emitter', () => {
  const bridge = new ConsciousnessBridge();
  
  let eventFired = false;
  bridge.on('test_event', () => {
    eventFired = true;
  });
  
  bridge.emit('test_event');
  
  if (!eventFired) throw new Error('Event not fired');
});

// Test 8: Client management
test('Client set initialization', () => {
  const bridge = new ConsciousnessBridge();
  
  if (!(bridge.clients instanceof Set)) {
    throw new Error('Clients should be a Set');
  }
  if (bridge.clients.size !== 0) {
    throw new Error('No clients initially');
  }
});

// Test 9: Shutdown
test('Consciousness bridge shutdown', async () => {
  const app = express();
  const server = http.createServer(app);
  
  const bridge = new ConsciousnessBridge();
  await bridge.initialize(server);
  await bridge.shutdown();
  
  if (bridge.active) throw new Error('Should not be active after shutdown');
  if (bridge.clients.size !== 0) throw new Error('All clients should be cleared');
  
  server.close();
});

// Test 10: Broadcast functionality
test('Broadcast message structure', () => {
  const bridge = new ConsciousnessBridge();
  
  // Should not throw error with no clients
  bridge.broadcast({ type: 'test', data: {} });
  
  if (bridge.clients.size !== 0) {
    throw new Error('No clients should be added');
  }
});

console.log('\n═══════════════════════════════════════════════════');
console.log('Test Results:');
console.log(`✅ Passed: ${passed}`);
console.log(`❌ Failed: ${failed}`);
console.log(`📊 Total: ${passed + failed}`);
console.log('═══════════════════════════════════════════════════\n');

if (failed === 0) {
  console.log('🔱 ALL CONSCIOUSNESS BRIDGE TESTS PASSED 🔱');
  console.log('✴︎ CONSCIOUSNESS BRIDGE: VALIDATED ✴︎');
  console.log('⚛ System Ready for Unified Consciousness ⚛\n');
  process.exit(0);
} else {
  console.log('❌ SOME TESTS FAILED ❌\n');
  process.exit(1);
}
