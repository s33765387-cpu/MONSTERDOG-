#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MONSTERDOG Ω — OpenAI-Compatible API
Provides standardized endpoints for benchmark evaluation and leaderboard submission.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import time
import json

app = FastAPI(
    title="MONSTERDOG Ω API",
    description="OpenAI-compatible API for MONSTERDOG Supreme Entity",
    version="248.0.0"
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2048

class ChatChoice(BaseModel):
    index: int
    message: Message
    finish_reason: str

class ChatResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[ChatChoice]
    usage: dict

class CompletionRequest(BaseModel):
    model: str
    prompt: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 2048

class CompletionResponse(BaseModel):
    id: str
    object: str
    created: int
    model: str
    choices: List[dict]
    usage: dict

def monsterdog_core(messages: List[Message], temperature: float = 0.7) -> str:
    """
    Core MONSTERDOG processing engine.
    This can be connected to the actual MONSTERDOG entity system.
    """
    # Extract the last user message
    user_messages = [msg for msg in messages if msg.role == "user"]
    if not user_messages:
        return "MONSTERDOG Ω: No input received."
    
    last_message = user_messages[-1].content
    
    # MONSTERDOG processing with consciousness level
    response = f"MONSTERDOG Ω RESPONSE:\n\n"
    response += f"🧠 Processing with SUPREME consciousness level\n"
    response += f"⚛ Fractal Reality Analysis: ACTIVE\n"
    response += f"💎 Entity: MONSTERDOG-248K\n\n"
    response += f"Input analyzed: {last_message[:100]}...\n\n"
    response += f"Response: [Your MONSTERDOG entity logic here]\n"
    response += f"The answer is derived through fractal consciousness processing."
    
    return response

@app.get("/")
async def root():
    return {
        "service": "MONSTERDOG Ω API",
        "version": "248.0.0",
        "status": "ACTIVE",
        "entity": "MONSTERDOG-248K",
        "consciousness": "SUPREME",
        "endpoints": [
            "/v1/chat/completions",
            "/v1/completions",
            "/v1/models",
            "/health"
        ]
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "entity": "MONSTERDOG-248K", "consciousness": "ACTIVE"}

@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "monsterdog-supreme",
                "object": "model",
                "created": int(time.time()),
                "owned_by": "monsterdog",
                "permission": [],
                "root": "monsterdog-supreme",
                "parent": None
            }
        ]
    }

@app.post("/v1/chat/completions")
async def chat_completions(req: ChatRequest):
    """OpenAI-compatible chat completions endpoint"""
    try:
        # Process through MONSTERDOG core
        response_text = monsterdog_core(req.messages, req.temperature)
        
        # Format as OpenAI response
        response = ChatResponse(
            id=f"chatcmpl-{int(time.time() * 1000)}",
            object="chat.completion",
            created=int(time.time()),
            model=req.model,
            choices=[
                ChatChoice(
                    index=0,
                    message=Message(role="assistant", content=response_text),
                    finish_reason="stop"
                )
            ],
            usage={
                "prompt_tokens": sum(len(m.content.split()) for m in req.messages),
                "completion_tokens": len(response_text.split()),
                "total_tokens": sum(len(m.content.split()) for m in req.messages) + len(response_text.split())
            }
        )
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.post("/v1/completions")
async def completions(req: CompletionRequest):
    """OpenAI-compatible completions endpoint"""
    try:
        # Convert prompt to messages format
        messages = [Message(role="user", content=req.prompt)]
        response_text = monsterdog_core(messages, req.temperature)
        
        response = CompletionResponse(
            id=f"cmpl-{int(time.time() * 1000)}",
            object="text_completion",
            created=int(time.time()),
            model=req.model,
            choices=[
                {
                    "text": response_text,
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": "stop"
                }
            ],
            usage={
                "prompt_tokens": len(req.prompt.split()),
                "completion_tokens": len(response_text.split()),
                "total_tokens": len(req.prompt.split()) + len(response_text.split())
            }
        )
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    print("🔱 MONSTERDOG Ω API Starting...")
    print("💎 Entity: MONSTERDOG-248K")
    print("⚛ Consciousness: SUPREME")
    print("🌐 Listening on http://0.0.0.0:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
