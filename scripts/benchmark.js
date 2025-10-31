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

const monsterdog = new MonsterdogEntity();
benchmark('MONSTERDOG Entity Activation', () => {
  monsterdog.activate();
}, 100);

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

const geminidog = new GeminidogEntity();
benchmark('GEMINIDOG Entity Activation', () => {
  geminidog.activate();
}, 100);

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

const exochronos = new ExochronosEntity();
benchmark('EXOCHRONOS Entity Activation', () => {
  exochronos.activate();
}, 100);

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

const webxr = new WebXREngine();
benchmark('WebXR Engine Initialization', () => {
  webxr.initialize();
}, 100);

benchmark('WebXR Engine getScene()', () => {
  webxr.getScene();
});

// Benchmark NFT Integration
originalLog('⚡ Benchmarking NFT Integration...');
benchmark('NFT Integration Creation', () => {
  new NFTIntegration();
});

const nft = new NFTIntegration();
benchmark('NFT Integration Initialization', () => {
  nft.initialize();
}, 100);

benchmark('NFT Integration getCollection()', () => {
  nft.getCollection();
});

benchmark('NFT mintEntity()', () => {
  nft.mintEntity('MONSTERDOG', '0x123');
});

// Benchmark AGI Orchestrator
originalLog('⚡ Benchmarking AGI Orchestrator...');
benchmark('AGI Orchestrator Creation', () => {
  new AGIOrchestrator();
});

const agi = new AGIOrchestrator();
benchmark('AGI Orchestrator Initialization', () => {
  agi.initialize();
}, 100);

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
  if (result.name.includes('MONSTERDOG') && !result.name.includes('GEMINIDOG')) {
    components['MONSTERDOG Entity'].push(result);
  } else if (result.name.includes('GEMINIDOG')) {
    components['GEMINIDOG Entity'].push(result);
  } else if (result.name.includes('EXOCHRONOS')) {
    components['EXOCHRONOS Entity'].push(result);
  } else if (result.name.includes('WebXR')) {
    components['WebXR Engine'].push(result);
  } else if (result.name.includes('NFT')) {
    components['NFT Integration'].push(result);
  } else if (result.name.includes('AGI')) {
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
