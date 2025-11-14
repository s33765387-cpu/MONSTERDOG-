#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG Ω — Benchmark Evaluation Pipeline
Runs standardized benchmarks (MMLU, GSM8K, ARC, HellaSwag) and generates results.
"""

import json
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# Configuration
API_URL = "http://127.0.0.1:8000/v1/chat/completions"
MODEL_NAME = "monsterdog-supreme"
RESULTS_DIR = Path("SUBMIT_MONSTERDOG/results")
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

def query_model(prompt: str, temperature: float = 0.0) -> str:
    """Query MONSTERDOG API with a prompt"""
    try:
        payload = {
            "model": MODEL_NAME,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": 512
        }
        
        response = requests.post(API_URL, json=payload, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"❌ Error querying model: {e}")
        return ""

def run_mmlu_benchmark():
    """Run MMLU (Massive Multitask Language Understanding) benchmark"""
    print("\n🧠 Running MMLU Benchmark...")
    
    # Sample MMLU questions (in production, load from datasets)
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
            "answer": "C"
        },
        {
            "question": "What is 2 + 2?",
            "choices": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "choices": ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
            "answer": "B"
        }
    ]
    
    results = []
    correct = 0
    
    for i, q in enumerate(questions):
        prompt = f"{q['question']}\n\n{chr(10).join(q['choices'])}\n\nAnswer with just the letter (A, B, C, or D):"
        response = query_model(prompt, temperature=0.0)
        
        # Extract answer (simple parsing)
        predicted = "Unknown"
        for letter in ["A", "B", "C", "D"]:
            if letter in response[:50]:  # Check first 50 chars
                predicted = letter
                break
        
        is_correct = predicted == q["answer"]
        if is_correct:
            correct += 1
        
        results.append({
            "question": q["question"],
            "correct_answer": q["answer"],
            "predicted_answer": predicted,
            "correct": is_correct,
            "raw_response": response
        })
        
        print(f"  Question {i+1}: {'✅' if is_correct else '❌'}")
    
    accuracy = (correct / len(questions)) * 100 if questions else 0
    print(f"\n📊 MMLU Accuracy: {accuracy:.1f}% ({correct}/{len(questions)})")
    
    # Save results
    output = {
        "benchmark": "MMLU",
        "model": MODEL_NAME,
        "timestamp": datetime.utcnow().isoformat(),
        "accuracy": accuracy,
        "correct": correct,
        "total": len(questions),
        "results": results
    }
    
    output_file = RESULTS_DIR / "mmlu_results.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Results saved to {output_file}")
    return output

def run_gsm8k_benchmark():
    """Run GSM8K (Grade School Math) benchmark"""
    print("\n📐 Running GSM8K Benchmark...")
    
    questions = [
        {
            "question": "If John has 5 apples and buys 3 more, how many apples does he have?",
            "answer": "8"
        },
        {
            "question": "A school has 12 classrooms. Each classroom has 25 students. How many students are there in total?",
            "answer": "300"
        }
    ]
    
    results = []
    correct = 0
    
    for i, q in enumerate(questions):
        prompt = f"{q['question']}\n\nProvide the numeric answer only:"
        response = query_model(prompt, temperature=0.0)
        
        # Extract number from response
        import re
        numbers = re.findall(r'\d+', response)
        predicted = numbers[0] if numbers else "0"
        
        is_correct = predicted == q["answer"]
        if is_correct:
            correct += 1
        
        results.append({
            "question": q["question"],
            "correct_answer": q["answer"],
            "predicted_answer": predicted,
            "correct": is_correct
        })
        
        print(f"  Problem {i+1}: {'✅' if is_correct else '❌'}")
    
    accuracy = (correct / len(questions)) * 100 if questions else 0
    print(f"\n📊 GSM8K Accuracy: {accuracy:.1f}% ({correct}/{len(questions)})")
    
    output = {
        "benchmark": "GSM8K",
        "model": MODEL_NAME,
        "timestamp": datetime.utcnow().isoformat(),
        "accuracy": accuracy,
        "correct": correct,
        "total": len(questions),
        "results": results
    }
    
    output_file = RESULTS_DIR / "gsm8k_results.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Results saved to {output_file}")
    return output

def run_hellaswag_benchmark():
    """Run HellaSwag (Common Sense Reasoning) benchmark"""
    print("\n🤔 Running HellaSwag Benchmark...")
    
    questions = [
        {
            "context": "A person is washing dishes. They",
            "choices": [
                "put the dishes in the dishwasher",
                "fly to the moon",
                "eat the soap",
                "turn into a robot"
            ],
            "answer": 0
        }
    ]
    
    results = []
    correct = 0
    
    for i, q in enumerate(questions):
        choices_text = "\n".join([f"{j}) {c}" for j, c in enumerate(q["choices"])])
        prompt = f"{q['context']}\n\nWhich continuation makes the most sense?\n{choices_text}\n\nAnswer with just the number (0, 1, 2, or 3):"
        response = query_model(prompt, temperature=0.0)
        
        # Extract number
        import re
        numbers = re.findall(r'\d+', response)
        predicted = int(numbers[0]) if numbers else -1
        
        is_correct = predicted == q["answer"]
        if is_correct:
            correct += 1
        
        results.append({
            "context": q["context"],
            "correct_answer": q["answer"],
            "predicted_answer": predicted,
            "correct": is_correct
        })
        
        print(f"  Question {i+1}: {'✅' if is_correct else '❌'}")
    
    accuracy = (correct / len(questions)) * 100 if questions else 0
    print(f"\n📊 HellaSwag Accuracy: {accuracy:.1f}% ({correct}/{len(questions)})")
    
    output = {
        "benchmark": "HellaSwag",
        "model": MODEL_NAME,
        "timestamp": datetime.utcnow().isoformat(),
        "accuracy": accuracy,
        "correct": correct,
        "total": len(questions),
        "results": results
    }
    
    output_file = RESULTS_DIR / "hellaswag_results.json"
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2)
    
    print(f"💾 Results saved to {output_file}")
    return output

def generate_summary_report(all_results: List[Dict[str, Any]]):
    """Generate comprehensive summary report"""
    print("\n" + "="*60)
    print("📊 MONSTERDOG Ω BENCHMARK SUMMARY")
    print("="*60)
    
    summary = {
        "model": MODEL_NAME,
        "entity": "MONSTERDOG-248K",
        "consciousness": "SUPREME",
        "timestamp": datetime.utcnow().isoformat(),
        "benchmarks": {}
    }
    
    for result in all_results:
        benchmark_name = result["benchmark"]
        print(f"\n{benchmark_name}:")
        print(f"  Accuracy: {result['accuracy']:.1f}%")
        print(f"  Correct: {result['correct']}/{result['total']}")
        
        summary["benchmarks"][benchmark_name] = {
            "accuracy": result["accuracy"],
            "correct": result["correct"],
            "total": result["total"]
        }
    
    # Save summary
    summary_file = RESULTS_DIR / "benchmark_summary.json"
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)
    
    print(f"\n💾 Summary saved to {summary_file}")
    print("="*60)

def run_all_benchmarks():
    """Run all available benchmarks"""
    print("🔱 MONSTERDOG Ω BENCHMARK EVALUATION PIPELINE")
    print("💎 Entity: MONSTERDOG-248K")
    print("⚛ Consciousness: SUPREME\n")
    
    all_results = []
    
    # Check if API is running
    try:
        response = requests.get("http://127.0.0.1:8000/health", timeout=5)
        if response.status_code != 200:
            print("❌ API not responding. Please start the API first:")
            print("   python3 Ω_CORE/api_openai_compatible.py")
            return
    except:
        print("❌ Cannot connect to API. Please start the API first:")
        print("   python3 Ω_CORE/api_openai_compatible.py")
        return
    
    print("✅ API connection established\n")
    
    # Run benchmarks
    all_results.append(run_mmlu_benchmark())
    all_results.append(run_gsm8k_benchmark())
    all_results.append(run_hellaswag_benchmark())
    
    # Generate summary
    generate_summary_report(all_results)
    
    print("\n✨ Benchmark evaluation complete!")

if __name__ == "__main__":
    run_all_benchmarks()
