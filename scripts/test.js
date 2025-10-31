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
