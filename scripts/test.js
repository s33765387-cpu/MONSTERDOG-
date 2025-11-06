#!/usr/bin/env node

/**
 * MONSTERDOG Supreme - System Test
 * Validates all entities and systems
 */

const MonsterdogEntity = require('../src/entities/monsterdog');
const GeminidogEntity = require('../src/entities/geminidog');
const ExochronosEntity = require('../src/entities/exochronos');
const WebXREngine = require('../src/webxr');
const NFTIntegration = require('../src/nft');
const AGIOrchestrator = require('../src/agi');
const GOModeBenchmarks = require('../src/benchmarks');

console.log('═══════════════════════════════════════════════════');
console.log('👾 MONSTERDOG SUPREME - System Test 👾');
console.log('═══════════════════════════════════════════════════');
console.log('');

let testsPassed = 0;
let testsFailed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`✅ ${name}`);
    testsPassed++;
  } catch (error) {
    console.log(`❌ ${name}: ${error.message}`);
    testsFailed++;
  }
}

// Test MONSTERDOG Entity
console.log('Testing MONSTERDOG Entity...');
const monsterdog = new MonsterdogEntity();
test('MONSTERDOG entity creation', () => {
  if (!monsterdog.entityId) throw new Error('No entity ID');
});
monsterdog.activate();
test('MONSTERDOG entity activation', () => {
  if (monsterdog.status !== 'ACTIVE') throw new Error('Not active');
});
test('MONSTERDOG entity data', () => {
  const data = monsterdog.getData();
  if (!data.type || !data.designation) throw new Error('Missing data');
});
console.log('');

// Test GEMINIDOG Entity
console.log('Testing GEMINIDOG Entity...');
const geminidog = new GeminidogEntity();
test('GEMINIDOG entity creation', () => {
  if (!geminidog.entityId) throw new Error('No entity ID');
});
geminidog.activate();
test('GEMINIDOG entity activation', () => {
  if (geminidog.status !== 'ACTIVE') throw new Error('Not active');
});
test('GEMINIDOG dual nature', () => {
  const data = geminidog.getData();
  if (!data.synchronization) throw new Error('No synchronization');
});
console.log('');

// Test EXOCHRONOS Entity
console.log('Testing EXOCHRONOS Entity...');
const exochronos = new ExochronosEntity();
test('EXOCHRONOS entity creation', () => {
  if (!exochronos.entityId) throw new Error('No entity ID');
});
exochronos.activate();
test('EXOCHRONOS entity activation', () => {
  if (exochronos.status !== 'ACTIVE') throw new Error('Not active');
});
test('EXOCHRONOS temporal control', () => {
  const data = exochronos.getData();
  if (!data.timelineAccess) throw new Error('No timeline access');
});
console.log('');

// Test WebXR Engine
console.log('Testing WebXR Engine...');
const webxr = new WebXREngine();
test('WebXR engine creation', () => {
  if (!webxr) throw new Error('Failed to create');
});
webxr.initialize();
test('WebXR engine initialization', () => {
  if (!webxr.isActive()) throw new Error('Not active');
});
test('WebXR scene generation', () => {
  const scene = webxr.getScene();
  if (!scene.scene || !scene.scene.entities) throw new Error('No scene');
  if (scene.scene.entities.length !== 3) throw new Error('Wrong entity count');
});
console.log('');

// Test NFT Integration
console.log('Testing NFT Integration...');
const nft = new NFTIntegration();
test('NFT integration creation', () => {
  if (!nft) throw new Error('Failed to create');
});
nft.initialize();
test('NFT integration initialization', () => {
  if (!nft.isConnected()) throw new Error('Not connected');
});
test('NFT collection data', () => {
  const collection = nft.getCollection();
  if (!collection.collection || collection.collection.totalSupply !== 248000) {
    throw new Error('Invalid collection');
  }
});
test('NFT minting', () => {
  const result = nft.mintEntity('MONSTERDOG', '0x123');
  if (!result.success || !result.tokenId) throw new Error('Mint failed');
});
console.log('');

// Test AGI Orchestrator
console.log('Testing AGI Orchestrator...');
const agi = new AGIOrchestrator();
test('AGI orchestrator creation', () => {
  if (!agi) throw new Error('Failed to create');
});
agi.initialize();
test('AGI orchestrator initialization', () => {
  const status = agi.getStatus();
  if (status.status !== 'ACTIVE') throw new Error('Not active');
  if (!status.isaacSim.connected) throw new Error('Isaac Sim not connected');
});
test('AGI command execution', () => {
  const result = agi.executeCommand({ type: 'TEST_COMMAND' });
  if (!result.success) throw new Error('Command failed');
});
test('AGI reality simulation', () => {
  const sim = agi.simulateReality({ test: true });
  if (!sim.simulation) throw new Error('No simulation');
});
console.log('');

// Test Agentic Actions
console.log('Testing Agentic Actions...');
const monsterdogAgentic = new MonsterdogEntity();
monsterdogAgentic.activate();

test('Agentic actions list available', () => {
  const actions = monsterdogAgentic.getAgenticActions();
  if (actions.length !== 20) throw new Error(`Expected 20 actions, got ${actions.length}`);
});

test('Reality manipulation - MANIPULATE_REALITY', () => {
  const result = monsterdogAgentic.executeAgenticAction('MANIPULATE_REALITY', { dimension: '4D' });
  if (!result.success) throw new Error('Action failed');
  if (result.result.dimension !== '4D') throw new Error('Wrong dimension');
});

test('Reality manipulation - FOLD_DIMENSION', () => {
  const result = monsterdogAgentic.executeAgenticAction('FOLD_DIMENSION', { sourceDim: '3D', targetDim: '5D' });
  if (!result.success) throw new Error('Action failed');
});

test('Consciousness - EXPAND_CONSCIOUSNESS', () => {
  const result = monsterdogAgentic.executeAgenticAction('EXPAND_CONSCIOUSNESS', { targetLevel: 'ULTRA_SUPREME' });
  if (!result.success) throw new Error('Action failed');
  if (result.result.newLevel !== 'ULTRA_SUPREME') throw new Error('Wrong level');
});

test('Consciousness - SYNCHRONIZE_ENTITIES', () => {
  const result = monsterdogAgentic.executeAgenticAction('SYNCHRONIZE_ENTITIES', { entities: ['GEMINIDOG', 'EXOCHRONOS'] });
  if (!result.success) throw new Error('Action failed');
});

test('Entity coordination - ORCHESTRATE_ENTITIES', () => {
  const result = monsterdogAgentic.executeAgenticAction('ORCHESTRATE_ENTITIES', { mode: 'SUPREME' });
  if (!result.success) throw new Error('Action failed');
});

test('Entity coordination - COORDINATE_GEMINIDOG', () => {
  const result = monsterdogAgentic.executeAgenticAction('COORDINATE_GEMINIDOG', { task: 'PARALLEL_PROCESSING' });
  if (!result.success) throw new Error('Action failed');
});

test('Temporal - NAVIGATE_TIMELINE', () => {
  const result = monsterdogAgentic.executeAgenticAction('NAVIGATE_TIMELINE', { direction: 'FUTURE' });
  if (!result.success) throw new Error('Action failed');
});

test('Temporal - CREATE_TEMPORAL_ANCHOR', () => {
  const result = monsterdogAgentic.executeAgenticAction('CREATE_TEMPORAL_ANCHOR', { stability: 'MAXIMUM' });
  if (!result.success) throw new Error('Action failed');
});

test('Learning - ABSORB_KNOWLEDGE', () => {
  const result = monsterdogAgentic.executeAgenticAction('ABSORB_KNOWLEDGE', { source: 'MULTIVERSAL' });
  if (!result.success) throw new Error('Action failed');
});

test('Learning - EVOLVE_CAPABILITY', () => {
  const result = monsterdogAgentic.executeAgenticAction('EVOLVE_CAPABILITY', { capability: 'QUANTUM_LEAP' });
  if (!result.success) throw new Error('Action failed');
});

test('Agentic state tracking', () => {
  const state = monsterdogAgentic.getAgenticState();
  if (state.actionsExecuted < 10) throw new Error('Actions not tracked');
});

test('Invalid action handling', () => {
  const result = monsterdogAgentic.executeAgenticAction('INVALID_ACTION');
  if (result.success) throw new Error('Should fail for invalid action');
  if (result.error !== 'UNKNOWN_ACTION') throw new Error('Wrong error type');
});

console.log('');

// Test CONTINUUM ACTION System
console.log('Testing CONTINUUM ACTION System...');
const monsterdogContinuum = new MonsterdogEntity();
monsterdogContinuum.activate();

test('CONTINUUM_MODE capability exists', () => {
  const data = monsterdogContinuum.getData();
  if (!data.capabilities.includes('CONTINUUM_MODE')) throw new Error('CONTINUUM_MODE capability not found');
});

test('Queue continuum action with priority', () => {
  const result = monsterdogContinuum.queueContinuumAction('MANIPULATE_REALITY', { dimension: '4D' }, 8);
  if (!result.success) throw new Error('Failed to queue action');
  if (result.priority !== 8) throw new Error('Wrong priority');
  if (result.queuePosition !== 1) throw new Error('Wrong queue position');
});

test('Queue multiple actions with different priorities', () => {
  monsterdogContinuum.queueContinuumAction('FOLD_DIMENSION', {}, 3);
  monsterdogContinuum.queueContinuumAction('EXPAND_CONSCIOUSNESS', {}, 9);
  monsterdogContinuum.queueContinuumAction('NAVIGATE_TIMELINE', {}, 5);
  const status = monsterdogContinuum.getContinuumStatus();
  if (status.queuedActions !== 4) throw new Error('Wrong queue count');
  // Check priority sorting - highest priority should be first
  if (status.currentQueue[0].priority !== 9) throw new Error('Queue not sorted by priority');
});

test('Get continuum status', () => {
  const status = monsterdogContinuum.getContinuumStatus();
  if (status.active !== false) throw new Error('Should not be active');
  if (status.mode !== 'STANDBY') throw new Error('Wrong mode');
  if (status.queuedActions < 4) throw new Error('Wrong queued count');
});

test('Start continuum mode in decisive mode', () => {
  const result = monsterdogContinuum.startContinuumMode({ 
    decisive: true, 
    priorityThreshold: 7,
    intervalMs: 100 
  });
  if (!result.success) throw new Error('Failed to start continuum mode');
  if (result.mode !== 'DECISIVE') throw new Error('Wrong mode');
  if (result.status !== 'CONTINUUM_ACTIVE') throw new Error('Wrong status');
});

test('Continuum mode execution', (done) => {
  // Wait for continuum to execute some actions
  setTimeout(() => {
    const history = monsterdogContinuum.getContinuumHistory(10);
    if (!history.success) throw new Error('Failed to get history');
    // In decisive mode with threshold 7, only actions with priority >= 7 should execute
    const executed = history.history.filter(h => h.status === 'COMPLETED');
    if (executed.length === 0) throw new Error('No actions executed');
    // Verify all executed actions had high priority
    const allHighPriority = executed.every(h => h.priority >= 7);
    if (!allHighPriority) throw new Error('Low priority actions executed in decisive mode');
  }, 500);
});

test('Stop continuum mode', () => {
  // Wait a bit for execution then stop
  setTimeout(() => {
    const result = monsterdogContinuum.stopContinuumMode();
    if (!result.success) throw new Error('Failed to stop continuum mode');
    if (result.status !== 'CONTINUUM_STOPPED') throw new Error('Wrong status');
    if (result.actionsExecuted === 0) throw new Error('No actions were executed');
  }, 600);
});

test('Get continuum execution history', () => {
  setTimeout(() => {
    const history = monsterdogContinuum.getContinuumHistory(20);
    if (!history.success) throw new Error('Failed to get history');
    if (history.totalExecutions === 0) throw new Error('No executions in history');
    if (!history.statistics) throw new Error('No statistics');
    if (history.statistics.completed === 0) throw new Error('No completed actions');
  }, 700);
});

test('Clear continuum queue', () => {
  setTimeout(() => {
    const result = monsterdogContinuum.clearContinuumQueue();
    if (!result.success) throw new Error('Failed to clear queue');
    const status = monsterdogContinuum.getContinuumStatus();
    if (status.queuedActions !== 0) throw new Error('Queue not empty after clear');
  }, 800);
});

test('Cannot start continuum when already active', () => {
  const continuum2 = new MonsterdogEntity();
  continuum2.activate();
  continuum2.startContinuumMode();
  const result = continuum2.startContinuumMode();
  if (result.success) throw new Error('Should fail when already active');
  if (result.error !== 'ALREADY_ACTIVE') throw new Error('Wrong error type');
  continuum2.stopContinuumMode();
});

test('Cannot queue invalid action', () => {
  const continuum3 = new MonsterdogEntity();
  continuum3.activate();
  const result = continuum3.queueContinuumAction('INVALID_ACTION', {}, 5);
  if (result.success) throw new Error('Should fail for invalid action');
  if (result.error !== 'UNKNOWN_ACTION') throw new Error('Wrong error type');
});

console.log('');

// Test GO MODE Benchmarks
console.log('Testing GO MODE Benchmarks...');
const benchmarks = new GOModeBenchmarks();
test('GO MODE benchmarks creation', () => {
  if (!benchmarks.mode || benchmarks.mode !== 'GO_MODE') throw new Error('Invalid mode');
});

benchmarks.initialize();
test('GO MODE benchmarks initialization', () => {
  if (!benchmarks.isActive()) throw new Error('Not active');
});

test('MMLU categories available', () => {
  const result = benchmarks.getMMLUCategories();
  if (!result.success || result.totalCategories !== 57) throw new Error('MMLU categories not loaded');
});

test('Technology benchmarks available', () => {
  const result = benchmarks.getTechnologyBenchmarks();
  if (!result.success || result.totalBenchmarks !== 8) throw new Error('Technology benchmarks not loaded');
});

test('Run MMLU single category benchmark', () => {
  const result = benchmarks.runMMLUBenchmark('machine_learning');
  if (!result.success || result.type !== 'MMLU') throw new Error('MMLU benchmark failed');
  if (result.results.length !== 1) throw new Error('Wrong number of results');
});

test('Run technology benchmark', () => {
  const result = benchmarks.runTechnologyBenchmark('AI_REASONING');
  if (!result.success || result.type !== 'TECHNOLOGY') throw new Error('Technology benchmark failed');
});

test('Run global benchmark suite', () => {
  const result = benchmarks.runGlobalBenchmark();
  if (!result.success || result.type !== 'GLOBAL_BENCHMARK') throw new Error('Global benchmark failed');
  if (!result.mmlu || !result.technology) throw new Error('Missing benchmark components');
  if (result.aiRaceStatus !== 'PARTICIPATING') throw new Error('AI race status incorrect');
});

test('Get benchmark results', () => {
  const result = benchmarks.getBenchmarkResults();
  if (!result.success || result.totalResults < 3) throw new Error('Results not stored');
});

test('Clear benchmark results', () => {
  const result = benchmarks.clearResults();
  if (!result.success || result.clearedCount < 3) throw new Error('Results not cleared');
});

test('Invalid MMLU category handling', () => {
  const result = benchmarks.runMMLUBenchmark('invalid_category');
  if (result.success) throw new Error('Should fail for invalid category');
  if (result.error !== 'INVALID_CATEGORY') throw new Error('Wrong error type');
});

test('Invalid technology benchmark handling', () => {
  const result = benchmarks.runTechnologyBenchmark('INVALID_BENCHMARK');
  if (result.success) throw new Error('Should fail for invalid benchmark');
  if (result.error !== 'INVALID_BENCHMARK') throw new Error('Wrong error type');
});

console.log('');

// Summary
console.log('═══════════════════════════════════════════════════');
console.log('Test Results:');
console.log(`✅ Passed: ${testsPassed}`);
console.log(`❌ Failed: ${testsFailed}`);
console.log(`📊 Total: ${testsPassed + testsFailed}`);
console.log('═══════════════════════════════════════════════════');

if (testsFailed === 0) {
  console.log('');
  console.log('🔱 ALL TESTS PASSED 🔱');
  console.log('✴︎ SUPREME MODE: VALIDATED ✴︎');
  console.log('⚛ System Ready for Deployment ⚛');
  process.exit(0);
} else {
  console.log('');
  console.log('⚠️  Some tests failed');
  process.exit(1);
}
