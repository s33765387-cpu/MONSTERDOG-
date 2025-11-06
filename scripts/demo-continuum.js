#!/usr/bin/env node

/**
 * MONSTERDOG CONTINUUM ACTION - Demo Script
 * Demonstrates decisive agentic action execution in continuum mode
 */

const MonsterdogEntity = require('../src/entities/monsterdog');

console.log('═══════════════════════════════════════════════════');
console.log('⚡ MONSTERDOG CONTINUUM ACTION - Demo ⚡');
console.log('🎯 Decisive Agentic Execution System 🎯');
console.log('═══════════════════════════════════════════════════');
console.log('');

// Initialize MONSTERDOG entity
const monsterdog = new MonsterdogEntity();
monsterdog.activate();

console.log('');
console.log('📋 Queueing high-priority actions...');
console.log('');

// Queue actions with different priorities
const actions = [
  { action: 'ANCHOR_REALITY', params: { location: 'CURRENT', strength: 'ABSOLUTE' }, priority: 10 },
  { action: 'EXPAND_CONSCIOUSNESS', params: { targetLevel: 'HYPER_SUPREME', scope: 'MULTIVERSAL' }, priority: 9 },
  { action: 'MANIPULATE_REALITY', params: { dimension: '4D', intensity: 'EXTREME' }, priority: 8 },
  { action: 'NAVIGATE_TIMELINE', params: { direction: 'FUTURE', distance: 'FAR', precision: 'EXACT' }, priority: 7 },
  { action: 'FOLD_DIMENSION', params: { sourceDim: '3D', targetDim: '5D' }, priority: 6 },
  { action: 'ORCHESTRATE_ENTITIES', params: { mode: 'SUPREME', coordination: 'ABSOLUTE' }, priority: 8 },
  { action: 'ABSORB_KNOWLEDGE', params: { source: 'MULTIVERSAL', type: 'QUANTUM_DATA' }, priority: 5 },
  { action: 'OPTIMIZE_PERFORMANCE', params: { target: 'ALL_SYSTEMS', method: 'SUPREME_OPTIMIZATION' }, priority: 9 }
];

actions.forEach(({ action, params, priority }) => {
  const result = monsterdog.queueContinuumAction(action, params, priority);
  console.log(`✅ Queued: ${action} [Priority: ${priority}] - Position: ${result.queuePosition}`);
});

console.log('');
console.log(`📊 Total actions queued: ${actions.length}`);
console.log('');

// Show queue status
const statusBefore = monsterdog.getContinuumStatus();
console.log('🔍 Queue Status (before execution):');
console.log(`   Mode: ${statusBefore.mode}`);
console.log(`   Queued Actions: ${statusBefore.queuedActions}`);
console.log('');

console.log('📋 Priority-sorted queue:');
statusBefore.currentQueue.forEach((item, index) => {
  console.log(`   ${index + 1}. ${item.action} [Priority: ${item.priority}]`);
});
console.log('');

// Start continuum mode in DECISIVE mode
console.log('⚡ Starting CONTINUUM MODE in DECISIVE configuration...');
console.log('   🎯 Decisive Mode: ENABLED');
console.log('   🔱 Priority Threshold: 7 (only high-priority actions execute)');
console.log('   ⏱ Execution Interval: 500ms');
console.log('');

const startResult = monsterdog.startContinuumMode({
  decisive: true,
  priorityThreshold: 7,
  intervalMs: 500
});

if (startResult.success) {
  console.log(`✅ ${startResult.status}`);
  console.log('');
  
  // Let it run for 5 seconds
  console.log('⏳ Executing actions for 5 seconds...');
  console.log('');
  
  setTimeout(() => {
    // Stop continuum mode
    const stopResult = monsterdog.stopContinuumMode();
    console.log('');
    console.log(`⏸ ${stopResult.status}`);
    console.log(`   📊 Actions Executed: ${stopResult.actionsExecuted}`);
    console.log(`   📋 Actions Remaining: ${stopResult.actionsRemaining}`);
    console.log('');
    
    // Get execution history
    const history = monsterdog.getContinuumHistory(20);
    console.log('📜 Execution History:');
    console.log(`   Total Executions: ${history.totalExecutions}`);
    console.log(`   Completed: ${history.statistics.completed}`);
    console.log(`   Failed: ${history.statistics.failed}`);
    console.log(`   Average Priority: ${history.statistics.averagePriority}`);
    console.log('');
    
    // Show executed actions
    console.log('✅ Executed Actions (in order):');
    history.history.forEach((item, index) => {
      const status = item.status === 'COMPLETED' ? '✅' : '❌';
      console.log(`   ${index + 1}. ${status} ${item.action} [Priority: ${item.priority}]`);
    });
    console.log('');
    
    // Show remaining queue
    const statusAfter = monsterdog.getContinuumStatus();
    if (statusAfter.queuedActions > 0) {
      console.log('📋 Remaining in Queue (low priority actions):');
      statusAfter.currentQueue.forEach((item, index) => {
        console.log(`   ${index + 1}. ${item.action} [Priority: ${item.priority}]`);
      });
      console.log('');
      console.log('💡 Note: These actions have priority < 7, so they were not executed in DECISIVE mode');
      console.log('');
    }
    
    console.log('═══════════════════════════════════════════════════');
    console.log('✴︎ CONTINUUM ACTION DEMO COMPLETED ✴︎');
    console.log('🔱 DECISIVE AGENTIC EXECUTION: VALIDATED 🔱');
    console.log('⚡ GO MONSTERDOG ⚡');
    console.log('═══════════════════════════════════════════════════');
    
    process.exit(0);
  }, 5000);
} else {
  console.error('❌ Failed to start continuum mode:', startResult.message);
  process.exit(1);
}
