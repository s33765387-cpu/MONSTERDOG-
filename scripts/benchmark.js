#!/usr/bin/env node

/**
 * MONSTERDOG Supreme - Performance Benchmark
 * Measures system performance across all entities and systems
 */

const MonsterdogEntity = require('../src/entities/monsterdog');
const GeminidogEntity = require('../src/entities/geminidog');
const ExochronosEntity = require('../src/entities/exochronos');
const WebXREngine = require('../src/webxr');
const NFTIntegration = require('../src/nft');
const AGIOrchestrator = require('../src/agi');

// Store original console.log
const originalLog = console.log;

// Quiet mode for benchmarking (suppresses entity console output)
function quietMode(enable) {
  if (enable) {
    console.log = () => {};
  } else {
    console.log = originalLog;
  }
}

originalLog('═══════════════════════════════════════════════════');
originalLog('👾 MONSTERDOG SUPREME - Performance Benchmark 👾');
originalLog('═══════════════════════════════════════════════════');
originalLog('');

const benchmarkResults = [];

/**
 * Benchmark a function and record results
 * @param {string} name - Benchmark name
 * @param {Function} fn - Function to benchmark
 * @param {number} iterations - Number of iterations
 */
function benchmark(name, fn, iterations = 1000) {
  quietMode(true); // Suppress console output during benchmark
  
  // Warm up
  for (let i = 0; i < 10; i++) {
    fn();
  }
  
  // Actual benchmark
  const startTime = process.hrtime.bigint();
  for (let i = 0; i < iterations; i++) {
    fn();
  }
  const endTime = process.hrtime.bigint();
  
  quietMode(false); // Restore console output
  
  const totalTime = Number(endTime - startTime) / 1000000; // Convert to milliseconds
  const avgTime = totalTime / iterations;
  const opsPerSecond = (iterations / (totalTime / 1000)).toFixed(2);
  
  benchmarkResults.push({
    name,
    iterations,
    totalTime: totalTime.toFixed(2),
    avgTime: avgTime.toFixed(4),
    opsPerSecond
  });
  
  originalLog(`📊 ${name}`);
  originalLog(`   Iterations: ${iterations}`);
  originalLog(`   Total time: ${totalTime.toFixed(2)} ms`);
  originalLog(`   Avg time: ${avgTime.toFixed(4)} ms/op`);
  originalLog(`   Ops/sec: ${opsPerSecond}`);
  originalLog('');
}

// Benchmark MONSTERDOG Entity
originalLog('⚡ Benchmarking MONSTERDOG Entity...');
benchmark('MONSTERDOG Entity Creation', () => {
  new MonsterdogEntity();
});

benchmark('MONSTERDOG Entity Activation', () => {
  const monsterdog = new MonsterdogEntity();
  monsterdog.activate();
}, 100);

const monsterdog = new MonsterdogEntity();
monsterdog.activate();
benchmark('MONSTERDOG Entity getStatus()', () => {
  monsterdog.getStatus();
});

benchmark('MONSTERDOG Entity getData()', () => {
  monsterdog.getData();
});

// Benchmark GEMINIDOG Entity
originalLog('⚡ Benchmarking GEMINIDOG Entity...');
benchmark('GEMINIDOG Entity Creation', () => {
  new GeminidogEntity();
});

benchmark('GEMINIDOG Entity Activation', () => {
  const geminidog = new GeminidogEntity();
  geminidog.activate();
}, 100);

const geminidog = new GeminidogEntity();
geminidog.activate();
benchmark('GEMINIDOG Entity getStatus()', () => {
  geminidog.getStatus();
});

benchmark('GEMINIDOG Entity getData()', () => {
  geminidog.getData();
});

// Benchmark EXOCHRONOS Entity
originalLog('⚡ Benchmarking EXOCHRONOS Entity...');
benchmark('EXOCHRONOS Entity Creation', () => {
  new ExochronosEntity();
});

benchmark('EXOCHRONOS Entity Activation', () => {
  const exochronos = new ExochronosEntity();
  exochronos.activate();
}, 100);

const exochronos = new ExochronosEntity();
exochronos.activate();
benchmark('EXOCHRONOS Entity getStatus()', () => {
  exochronos.getStatus();
});

benchmark('EXOCHRONOS Entity getData()', () => {
  exochronos.getData();
});

// Benchmark WebXR Engine
originalLog('⚡ Benchmarking WebXR Engine...');
benchmark('WebXR Engine Creation', () => {
  new WebXREngine();
});

benchmark('WebXR Engine Initialization', () => {
  const webxr = new WebXREngine();
  webxr.initialize();
}, 100);

const webxr = new WebXREngine();
webxr.initialize();
benchmark('WebXR Engine getScene()', () => {
  webxr.getScene();
});

// Benchmark NFT Integration
originalLog('⚡ Benchmarking NFT Integration...');
benchmark('NFT Integration Creation', () => {
  new NFTIntegration();
});

benchmark('NFT Integration Initialization', () => {
  const nft = new NFTIntegration();
  nft.initialize();
}, 100);

const nft = new NFTIntegration();
nft.initialize();
benchmark('NFT Integration getCollection()', () => {
  nft.getCollection();
});

benchmark('NFT Integration mintEntity()', () => {
  nft.mintEntity('MONSTERDOG', '0x123');
});

// Benchmark AGI Orchestrator
originalLog('⚡ Benchmarking AGI Orchestrator...');
benchmark('AGI Orchestrator Creation', () => {
  new AGIOrchestrator();
});

benchmark('AGI Orchestrator Initialization', () => {
  const agi = new AGIOrchestrator();
  agi.initialize();
}, 100);

const agi = new AGIOrchestrator();
agi.initialize();
benchmark('AGI Orchestrator getStatus()', () => {
  agi.getStatus();
});

benchmark('AGI executeCommand()', () => {
  agi.executeCommand({ type: 'TEST_COMMAND' });
});

benchmark('AGI simulateReality()', () => {
  agi.simulateReality({ test: true });
});

// Summary
originalLog('═══════════════════════════════════════════════════');
originalLog('📈 Benchmark Summary:');
originalLog('═══════════════════════════════════════════════════');
originalLog('');

// Group results by component
const components = {
  'MONSTERDOG Entity': [],
  'GEMINIDOG Entity': [],
  'EXOCHRONOS Entity': [],
  'WebXR Engine': [],
  'NFT Integration': [],
  'AGI Orchestrator': []
};

benchmarkResults.forEach(result => {
  if (result.name.startsWith('MONSTERDOG Entity')) {
    components['MONSTERDOG Entity'].push(result);
  } else if (result.name.startsWith('GEMINIDOG Entity')) {
    components['GEMINIDOG Entity'].push(result);
  } else if (result.name.startsWith('EXOCHRONOS Entity')) {
    components['EXOCHRONOS Entity'].push(result);
  } else if (result.name.startsWith('WebXR Engine')) {
    components['WebXR Engine'].push(result);
  } else if (result.name.startsWith('NFT Integration')) {
    components['NFT Integration'].push(result);
  } else if (result.name.startsWith('AGI')) {
    components['AGI Orchestrator'].push(result);
  }
});

Object.entries(components).forEach(([component, results]) => {
  originalLog(`🔱 ${component}:`);
  results.forEach(result => {
    originalLog(`   ${result.name}:`);
    originalLog(`     ${result.opsPerSecond} ops/sec (${result.avgTime} ms/op)`);
  });
  originalLog('');
});

originalLog('═══════════════════════════════════════════════════');
originalLog('🔱 BENCHMARK COMPLETE 🔱');
originalLog(`✴︎ Total tests: ${benchmarkResults.length} ✴︎`);
originalLog('⚛ System Performance: MEASURED ⚛');
originalLog('═══════════════════════════════════════════════════');
