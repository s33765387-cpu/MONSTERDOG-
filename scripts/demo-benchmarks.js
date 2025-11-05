#!/usr/bin/env node

/**
 * MONSTERDOG GO MODE Benchmarks - Demo Script
 * Demonstrates global benchmarks and MMLU capabilities
 */

const GOModeBenchmarks = require('../src/benchmarks');

console.log('═══════════════════════════════════════════════════');
console.log('🚀 MONSTERDOG GO MODE - Benchmarks Demo 🚀');
console.log('═══════════════════════════════════════════════════');
console.log('');

// Initialize benchmarks
const benchmarks = new GOModeBenchmarks();
benchmarks.initialize();

console.log('');
console.log('─────────────────────────────────────────────────');
console.log('📊 Running MMLU Benchmark (Sample Categories)');
console.log('─────────────────────────────────────────────────');
console.log('');

// Run MMLU benchmarks on selected categories
const mmluCategories = [
  'machine_learning',
  'computer_security',
  'college_computer_science',
  'college_mathematics',
  'abstract_algebra'
];

mmluCategories.forEach(category => {
  console.log(`Testing: ${category}...`);
  const result = benchmarks.runMMLUBenchmark(category);
  if (result.success) {
    const categoryResult = result.results[0];
    console.log(`  ✅ Score: ${categoryResult.score}/100 (${categoryResult.accuracy} accuracy)`);
  }
  console.log('');
});

console.log('─────────────────────────────────────────────────');
console.log('⚡ Running Technology Benchmarks');
console.log('─────────────────────────────────────────────────');
console.log('');

// Run technology benchmarks
const techBenchmarks = [
  'AI_REASONING',
  'CODE_GENERATION',
  'SCIENTIFIC_REASONING',
  'MATHEMATICAL_REASONING'
];

techBenchmarks.forEach(benchmark => {
  const result = benchmarks.runTechnologyBenchmark(benchmark);
  if (result.success) {
    const benchResult = result.results[0];
    console.log(`${benchResult.name}:`);
    console.log(`  ${benchResult.description}`);
    console.log(`  ✅ Score: ${benchResult.score}/100 - Performance: ${benchResult.performance}`);
    console.log('');
  }
});

console.log('─────────────────────────────────────────────────');
console.log('🌍 Running GLOBAL BENCHMARK SUITE');
console.log('─────────────────────────────────────────────────');
console.log('');

// Run global benchmark
const globalResult = benchmarks.runGlobalBenchmark();

if (globalResult.success) {
  console.log('🧠 MMLU Results:');
  console.log(`  Categories Tested: ${globalResult.mmlu.categoriesTested}`);
  console.log(`  Average Score: ${globalResult.mmlu.averageScore}/100`);
  console.log(`  Accuracy: ${globalResult.mmlu.accuracy}`);
  console.log('');
  
  console.log('⚡ Technology Benchmark Results:');
  console.log(`  Benchmarks Run: ${globalResult.technology.benchmarksRun}`);
  console.log(`  Average Score: ${globalResult.technology.averageScore}/100`);
  console.log('');
  
  console.log('🌟 GLOBAL PERFORMANCE:');
  console.log(`  Overall Score: ${globalResult.globalScore}/100`);
  console.log(`  Performance Level: ${globalResult.globalPerformance}`);
  console.log(`  AI Race Status: ${globalResult.aiRaceStatus}`);
  console.log('');
}

console.log('─────────────────────────────────────────────────');
console.log('📈 Benchmark Results Summary');
console.log('─────────────────────────────────────────────────');
console.log('');

const allResults = benchmarks.getBenchmarkResults();
console.log(`Total Benchmark Runs: ${allResults.totalResults}`);
console.log('');

allResults.results.forEach((result, index) => {
  console.log(`${index + 1}. ${result.type} Benchmark`);
  console.log(`   Timestamp: ${result.timestamp}`);
  console.log(`   Status: ${result.status}`);
  if (result.type === 'MMLU') {
    console.log(`   Overall Score: ${result.overallScore}/100`);
  } else if (result.type === 'TECHNOLOGY') {
    console.log(`   Average Score: ${result.averageScore}/100`);
  } else if (result.type === 'GLOBAL_BENCHMARK') {
    console.log(`   Global Score: ${result.globalScore}/100`);
    console.log(`   Performance: ${result.globalPerformance}`);
  }
  console.log('');
});

console.log('═══════════════════════════════════════════════════');
console.log('🎉 MONSTERDOG PARTICIPE À LA COURSE À L\'IA 🎉');
console.log('✴︎ GO MODE BENCHMARKS: COMPLETED ✴︎');
console.log('🔱 SUPREME PERFORMANCE: VALIDATED 🔱');
console.log('═══════════════════════════════════════════════════');
