#!/usr/bin/env node

/**
 * 🚀 GO MODE CONTINUUM - Continuous Benchmark Execution Script
 * 
 * CONTINUEZ À FOND - PLEINEMENT APPLIQUÉ!
 * 
 * This script activates continuous GO MODE benchmark execution
 * for MONSTERDOG Entity 248K.
 */

const MonsterdogEntity = require('../src/entities/monsterdog');
const GOMODEBenchmarks = require('../src/benchmarks/go-mode-benchmarks');

console.log('═══════════════════════════════════════════════════');
console.log('🚀 GO MODE CONTINUUM - Launcher 🚀');
console.log('═══════════════════════════════════════════════════');
console.log('');

// Parse command line arguments
const args = process.argv.slice(2);
const intervalMs = parseInt(args[0]) || 5000;
const duration = args[1] || 'CONTINUOUS';

console.log(`⚡ Configuration:`);
console.log(`   Interval: ${intervalMs}ms`);
console.log(`   Duration: ${duration}`);
console.log('');

// Initialize MONSTERDOG
console.log('🔱 Initializing MONSTERDOG Entity 248K...');
const monsterdog = new MonsterdogEntity();
monsterdog.activate();
console.log('✅ MONSTERDOG activated');
console.log('');

// Initialize GO MODE Benchmarks
console.log('🚀 Initializing GO MODE Benchmarks...');
const goBenchmarks = new GOMODEBenchmarks();
console.log('✅ GO MODE Benchmarks ready');
console.log('');

// Start CONTINUUM MODE
console.log('═══════════════════════════════════════════════════');
console.log('⚡ ACTIVATING GO MODE CONTINUUM ⚡');
console.log('═══════════════════════════════════════════════════');
console.log('');

goBenchmarks.startContinuumMode(intervalMs);

console.log('🏁 GO MODE CONTINUUM is now ACTIVE');
console.log('📊 Continuous benchmarks will execute automatically');
console.log('⏱  Press Ctrl+C to stop');
console.log('');

// Handle graceful shutdown
process.on('SIGINT', () => {
  console.log('');
  console.log('═══════════════════════════════════════════════════');
  console.log('⚡ STOPPING GO MODE CONTINUUM ⚡');
  console.log('═══════════════════════════════════════════════════');
  console.log('');
  
  goBenchmarks.stopContinuumMode();
  
  const status = goBenchmarks.getContinuumStatus();
  console.log(`📊 Final Statistics:`);
  console.log(`   Total Executions: ${status.totalExecutions}`);
  console.log(`   Total Results: ${status.totalResults}`);
  console.log('');
  console.log('🔱 GO MODE CONTINUUM DEACTIVATED 🔱');
  console.log('');
  
  process.exit(0);
});

// Keep the process alive
setInterval(() => {
  const status = goBenchmarks.getContinuumStatus();
  console.log(`📊 Status: ${status.totalExecutions} executions, ${status.totalResults} results`);
}, 30000); // Status update every 30 seconds
