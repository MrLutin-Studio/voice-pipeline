#!/usr/bin/env python3
"""
Full Voice Pipeline: Whisper STT → Claude LLM → XTTS TTS
=========================================================
Listen → Think → Speak
"""

import os
import sys
import torch
import whisper
import soundfile as sf
import numpy as np
from TTS.api import TTS
from anthropic import Anthropic

# Config
WHISPER_DEVICE = "cpu"  # CPU pour Whisper (economiser VRAM)
TTS_DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
VOICE_SAMPLE = "samples/sample.wav"
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize systems
print("🎤 Initializing Voice Pipeline...")
print(f"🔧 Whisper: {WHISPER_DEVICE.upper()}")
print(f"🔧 XTTS: {TTS_DEVICE.upper()}")

# 1. Whisper STT
print("📥 Loading Whisper...")
whisper_model = whisper.load_model("base", device=WHISPER_DEVICE)
print("  ✓ Whisper ready")

# 2. Claude LLM
print("📥 Loading Claude...")
try:
    anthropic = Anthropic()  # Uses ANTHROPIC_API_KEY env var
    print("  ✓ Claude ready")
except Exception as e:
    print(f"  ⚠️ Claude offline (API key missing): {str(e)[:50]}")
    anthropic = None

# 3. XTTS TTS
print("📥 Loading XTTS v2...")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=(TTS_DEVICE == "cuda"))
print("  ✓ XTTS ready")

print("\n✅ **Voice Pipeline initialized!**\n")

def stt(audio_path: str) -> str:
    """Speech-to-Text with Whisper"""
    print(f"🎤 Transcribing: {audio_path}")
    result = whisper_model.transcribe(audio_path, language="fr")
    text = result["text"].strip()
    print(f"  Recognized: {text[:100]}...")
    return text

def llm(user_text: str, conversation_history: list = None) -> str:
    """LLM processing with Claude"""
    if conversation_history is None:
        conversation_history = []
    
    print(f"🧠 Processing: {user_text[:100]}...")
    
    # Add user message
    conversation_history.append({
        "role": "user",
        "content": user_text
    })
    
    # Get Claude response
    if anthropic:
        try:
            response = anthropic.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                system="Tu es Morwintar, un assistant IA avec une personnalité. Réponds en français, sois direct et un peu sarcastique.",
                messages=conversation_history
            )
            assistant_message = response.content[0].text
        except Exception as e:
            print(f"  ⚠️ Claude error: {str(e)[:50]}")
            assistant_message = "J'ai une petite erreur de connexion, mais je suis toujours là!"
    else:
        # Offline mode - mock response
        assistant_message = f"J'ai bien entendu: '{user_text[:50]}...'. En mode offline, je peux juste répéter ce que tu dis!"
    
    print(f"  Response: {assistant_message[:100]}...")
    
    # Add to history
    conversation_history.append({
        "role": "assistant",
        "content": assistant_message
    })
    
    return assistant_message, conversation_history

def tts_generate(text: str, output_file: str = None) -> np.ndarray:
    """Text-to-Speech with XTTS v2"""
    if output_file is None:
        output_file = f"{OUTPUT_DIR}/response.wav"
    
    print(f"🎤 Generating speech: {text[:50]}...")
    
    try:
        wav = tts.tts(
            text=text,
            speaker_wav=VOICE_SAMPLE,
            language="fr"
        )
        
        sf.write(output_file, wav, samplerate=24000)
        print(f"  ✓ Saved: {output_file}")
        return wav
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return None

def process_voice_input(audio_path: str, conversation_history: list = None) -> str:
    """Full pipeline: STT → LLM → TTS"""
    
    # Step 1: Transcribe
    user_text = stt(audio_path)
    
    # Step 2: Process with Claude
    response_text, conversation_history = llm(user_text, conversation_history)
    
    # Step 3: Synthesize response
    output_file = f"{OUTPUT_DIR}/response_{len(conversation_history)}.wav"
    tts_generate(response_text, output_file)
    
    return response_text, conversation_history

# Main loop
if __name__ == "__main__":
    print("🎯 Voice Pipeline Ready!")
    print("Usage: python3 full_voice_pipeline.py <audio_file.wav>")
    print()
    
    conversation_history = []
    
    if len(sys.argv) > 1:
        audio_file = sys.argv[1]
        
        if os.path.exists(audio_file):
            print(f"Processing: {audio_file}\n")
            response, conversation_history = process_voice_input(audio_file, conversation_history)
            print(f"\n✅ Response: {response}\n")
        else:
            print(f"❌ File not found: {audio_file}")
    else:
        # Demo with sample.wav
        if os.path.exists(VOICE_SAMPLE):
            print(f"📝 Demo mode - Processing sample audio...\n")
            response, conversation_history = process_voice_input(VOICE_SAMPLE, conversation_history)
            print(f"\n✅ Morwintar says: {response}\n")
        else:
            print(f"❌ Sample audio not found: {VOICE_SAMPLE}")
            print("Place an audio file in samples/sample.wav first")

print("✅ **FULL VOICE PIPELINE OPERATIONAL!**")
