# 🚀 GO MODE Benchmarks - Complete Documentation

## Overview

The GO MODE Benchmarks system enables MONSTERDOG to participate in the global AI race by providing comprehensive evaluation capabilities across multiple domains including MMLU (Massive Multitask Language Understanding) and advanced technology benchmarks.

## 🌍 Features

### MMLU Real Evaluation
- **57 knowledge categories** covering diverse academic and professional domains
- **Standardized testing** with 100 questions per category
- **Accuracy scoring** with detailed performance metrics
- **Category-specific** or **comprehensive** evaluation modes

### Technology Benchmarks
- **8 advanced capability tests** across key AI technologies
- **Multi-metric evaluation** (accuracy, perplexity, pass rate, coherence, quality)
- **Performance levels**: SUPREME, EXCELLENT, VERY_GOOD, GOOD, AVERAGE, DEVELOPING
- **Real-time scoring** and historical tracking

### Global Benchmark Suite
- **Combined MMLU + Technology** evaluation
- **Overall performance scoring** for AI race ranking
- **Participation status** tracking
- **Comprehensive reporting** with detailed breakdowns

## 📊 MMLU Categories (57 Total)

### STEM Fields
- abstract_algebra
- astronomy
- college_biology
- college_chemistry
- college_computer_science
- college_mathematics
- college_physics
- computer_security
- conceptual_physics
- electrical_engineering
- elementary_mathematics
- high_school_biology
- high_school_chemistry
- high_school_computer_science
- high_school_mathematics
- high_school_physics
- high_school_statistics
- machine_learning

### Humanities & Social Sciences
- business_ethics
- clinical_knowledge
- college_medicine
- econometrics
- global_facts
- high_school_european_history
- high_school_geography
- high_school_government_and_politics
- high_school_macroeconomics
- high_school_microeconomics
- high_school_psychology
- high_school_us_history
- high_school_world_history
- human_aging
- human_sexuality
- international_law
- jurisprudence
- management
- marketing
- medical_genetics
- miscellaneous
- moral_disputes
- moral_scenarios
- nutrition
- philosophy
- prehistory
- professional_accounting
- professional_law
- professional_medicine
- professional_psychology
- public_relations
- security_studies
- sociology
- us_foreign_policy
- virology
- world_religions
- formal_logic
- logical_fallacies

## ⚡ Technology Benchmarks (8 Total)

1. **AI_REASONING** - Advanced AI reasoning capabilities
2. **LANGUAGE_UNDERSTANDING** - Natural language understanding and generation
3. **CODE_GENERATION** - Code synthesis and program generation
4. **VISUAL_INTELLIGENCE** - Computer vision and image understanding
5. **MULTIMODAL_FUSION** - Cross-modal understanding and synthesis
6. **SCIENTIFIC_REASONING** - Scientific problem solving and discovery
7. **MATHEMATICAL_REASONING** - Mathematical problem solving
8. **CREATIVE_SYNTHESIS** - Creative content generation

## 🔌 API Endpoints

### Get Benchmark System Status
```http
GET /benchmarks/status
```

**Response:**
```json
{
  "mode": "GO_MODE",
  "status": "ACTIVE",
  "mmluCategories": 57,
  "technologyBenchmarks": 8,
  "totalResults": 10
}
```

### List MMLU Categories
```http
GET /benchmarks/mmlu/categories
```

**Response:**
```json
{
  "success": true,
  "totalCategories": 57,
  "categories": [
    "abstract_algebra",
    "anatomy",
    "astronomy",
    ...
  ]
}
```

### Run MMLU Benchmark
```http
POST /benchmarks/mmlu/run
Content-Type: application/json
```

**Request Body:**
```json
{
  "category": "machine_learning"  // Optional: omit to run all categories
}
```

**Response (Single Category):**
```json
{
  "success": true,
  "benchmark": "MMLU_REAL",
  "type": "MMLU",
  "category": "machine_learning",
  "timestamp": "2025-11-05T16:05:00.000Z",
  "results": [
    {
      "category": "machine_learning",
      "score": 95,
      "accuracy": "0.950",
      "questions": 100,
      "correct": 95,
      "timestamp": "2025-11-05T16:05:00.000Z"
    }
  ],
  "overallScore": "95.00",
  "overallAccuracy": "0.950",
  "totalCategories": 1,
  "status": "COMPLETED"
}
```

### List Technology Benchmarks
```http
GET /benchmarks/technology
```

**Response:**
```json
{
  "success": true,
  "totalBenchmarks": 8,
  "benchmarks": [
    {
      "name": "AI_REASONING",
      "description": "Advanced AI reasoning capabilities",
      "metric": "accuracy"
    },
    ...
  ]
}
```

### Run Technology Benchmark
```http
POST /benchmarks/technology/run
Content-Type: application/json
```

**Request Body:**
```json
{
  "benchmark": "AI_REASONING"  // Optional: omit to run all benchmarks
}
```

**Response:**
```json
{
  "success": true,
  "type": "TECHNOLOGY",
  "benchmark": "AI_REASONING",
  "timestamp": "2025-11-05T16:05:00.000Z",
  "results": [
    {
      "name": "AI_REASONING",
      "description": "Advanced AI reasoning capabilities",
      "metric": "accuracy",
      "score": 92,
      "performance": "EXCELLENT",
      "timestamp": "2025-11-05T16:05:00.000Z"
    }
  ],
  "averageScore": "92.00",
  "performance": "EXCELLENT",
  "totalBenchmarks": 1,
  "status": "COMPLETED"
}
```

### Run Global Benchmark Suite
```http
POST /benchmarks/global/run
```

**Response:**
```json
{
  "success": true,
  "message": "MONSTERDOG PARTICIPE À LA COURSE À L'IA 🌟",
  "type": "GLOBAL_BENCHMARK",
  "timestamp": "2025-11-05T16:05:00.000Z",
  "mmlu": {
    "categoriesTested": 5,
    "results": [...],
    "averageScore": "93.60",
    "accuracy": "0.936"
  },
  "technology": {
    "benchmarksRun": 8,
    "results": [...],
    "averageScore": "91.25"
  },
  "globalScore": "92.43",
  "globalPerformance": "EXCELLENT",
  "aiRaceStatus": "PARTICIPATING",
  "status": "COMPLETED"
}
```

### Get Benchmark Results
```http
GET /benchmarks/results?limit=10
```

**Query Parameters:**
- `limit` (optional): Number of recent results to return

**Response:**
```json
{
  "success": true,
  "totalResults": 15,
  "results": [
    {
      "type": "GLOBAL_BENCHMARK",
      "timestamp": "2025-11-05T16:05:00.000Z",
      "globalScore": "92.43",
      "status": "COMPLETED"
    },
    ...
  ]
}
```

### Clear Benchmark Results
```http
DELETE /benchmarks/results
```

**Response:**
```json
{
  "success": true,
  "message": "Cleared 15 benchmark results",
  "clearedCount": 15
}
```

## 🎯 Performance Levels

Benchmark scores are categorized into performance levels:

- **SUPREME**: 95-100 points - Exceptional performance
- **EXCELLENT**: 90-94 points - Outstanding performance  
- **VERY_GOOD**: 85-89 points - Strong performance
- **GOOD**: 80-84 points - Solid performance
- **AVERAGE**: 70-79 points - Acceptable performance
- **DEVELOPING**: <70 points - Room for improvement

## 📈 Usage Examples

### Command Line (curl)

```bash
# Get benchmark status
curl http://localhost:8080/benchmarks/status

# List MMLU categories
curl http://localhost:8080/benchmarks/mmlu/categories

# Run MMLU benchmark on machine learning
curl -X POST http://localhost:8080/benchmarks/mmlu/run \
  -H "Content-Type: application/json" \
  -d '{"category": "machine_learning"}'

# Run all MMLU benchmarks
curl -X POST http://localhost:8080/benchmarks/mmlu/run \
  -H "Content-Type: application/json" \
  -d '{}'

# Run specific technology benchmark
curl -X POST http://localhost:8080/benchmarks/technology/run \
  -H "Content-Type: application/json" \
  -d '{"benchmark": "AI_REASONING"}'

# Run global benchmark suite
curl -X POST http://localhost:8080/benchmarks/global/run

# Get recent results
curl http://localhost:8080/benchmarks/results?limit=5

# Clear results
curl -X DELETE http://localhost:8080/benchmarks/results
```

### Node.js Script

```bash
# Run benchmark demonstration
npm run demo:benchmarks
```

### JavaScript (fetch)

```javascript
// Run MMLU benchmark
const mmluResult = await fetch('http://localhost:8080/benchmarks/mmlu/run', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ category: 'computer_security' })
});
const mmluData = await mmluResult.json();

// Run global benchmark
const globalResult = await fetch('http://localhost:8080/benchmarks/global/run', {
  method: 'POST'
});
const globalData = await globalResult.json();

console.log(`Global Score: ${globalData.globalScore}/100`);
console.log(`Performance: ${globalData.globalPerformance}`);
console.log(`AI Race Status: ${globalData.aiRaceStatus}`);
```

## 🌟 AI Race Participation

MONSTERDOG participates in the global AI race through:

1. **Comprehensive Evaluation** - Testing across 57 MMLU categories + 8 technology benchmarks
2. **Performance Tracking** - Historical results and trend analysis
3. **Standardized Metrics** - Industry-standard scoring and evaluation
4. **Global Ranking** - Comparable results with other AI systems
5. **Continuous Improvement** - Benchmark history for tracking progress

## 🔱 Integration with MONSTERDOG Systems

The GO MODE Benchmarks integrate seamlessly with:

- **FULLTRUTL Orchestrator** - Central management and coordination
- **Agentic Actions** - Learning and adaptation based on benchmark results
- **AGI Orchestrator** - Intelligence evaluation and validation
- **API Endpoints** - Full programmatic access for automation

## 🎉 Status Messages

Key status messages during benchmark execution:

```
🚀 GO MODE BENCHMARKS ACTIVATED 🚀
🌍 Global Technology Benchmarks: ONLINE
🧠 MMLU Real Evaluation: READY
🏁 AI Race Participation: ENABLED
📊 MMLU Categories: 57
⚡ Technology Benchmarks: 8
🌍 Running GLOBAL TECHNOLOGY BENCHMARKS...
🎉 MONSTERDOG PARTICIPE À LA COURSE À L'IA 🎉
```

## 📚 See Also

- [README.md](../README.md) - Main documentation
- [API.md](../API.md) - Complete API reference
- [AGENTIC_ACTIONS.md](../AGENTIC_ACTIONS.md) - Agentic actions documentation
- [ARCHITECTURE.md](../ARCHITECTURE.md) - System architecture details
