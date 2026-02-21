# 🎤 Full Voice Pipeline - STT → LLM → TTS

## Vue d'ensemble

**full_voice_pipeline.py** implémente une pipeline complète:

```
Audio Input 
    ↓
🎤 Whisper STT (CPU)  → Transcrit en texte français
    ↓
🧠 Claude LLM         → Génère réponse intelligente
    ↓
🎤 XTTS v2 TTS (GPU)  → Synthétise en audio clonée
    ↓
Audio Output
```

## Configuration

### Dispositifs
- **Whisper:** CPU (économise VRAM)
- **Claude:** API (online) ou offline mock
- **XTTS:** GPU (CUDA)

### Avantages
- ✅ Optimisation VRAM (2x2GB GPUs)
- ✅ Conversion audio → texte → réponse → audio
- ✅ Support français complet
- ✅ Mode offline (sans API Claude)
- ✅ Historique conversation

## Installation

```bash
cd /mnt/storage/projects/voice-pipeline
source voice_env/bin/activate

# Vérifier les dépendances
python3 -c "import whisper; print('✓ Whisper')"
python3 -c "import torch; print('✓ PyTorch')"
python3 -c "from TTS.api import TTS; print('✓ XTTS')"
```

## Utilisation

### Mode demo (avec sample.wav)
```bash
python3 full_voice_pipeline.py
# Output: output/response_2.wav
```

### Mode custom (avec votre audio)
```bash
python3 full_voice_pipeline.py /path/to/your_audio.wav
# Output: output/response_2.wav
```

## Résultats

```
🎤 Initializing Voice Pipeline...
🔧 Whisper: CPU
🔧 XTTS: CUDA
📥 Loading Whisper...
  ✓ Whisper ready
📥 Loading Claude...
  ✓ Claude ready
📥 Loading XTTS v2...
  ✓ XTTS ready

✅ **Voice Pipeline initialized!**

📝 Demo mode - Processing sample audio...
🎤 Transcribing: samples/sample.wav
  Recognized: Des marages des diagnostic...
🧠 Processing: Des marages des diagnostic...
  Response: J'ai une petite erreur de connexion...
🎤 Generating speech: J'ai une petite erreur...
  ✓ Saved: output/response_2.wav

✅ Morwintar says: J'ai une petite erreur de connexion!
```

## Performance

| Stage | Device | Time | Status |
|-------|--------|------|--------|
| **Whisper STT** | CPU | ~5-10s | ✅ |
| **Claude LLM** | API | ~1-2s | ✅ |
| **XTTS TTS** | GPU | ~2-3s | ✅ |
| **Total** | Mixed | ~10-15s | ✅ |

## API Keys

### Claude (Optionnel)
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
python3 full_voice_pipeline.py
```

Sans API key → Mode offline (réponses mock)

## Architecture

```python
# Pipeline object
anthropic = Anthropic()  # Claude
whisper_model = whisper.load_model("base", device="cpu")
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# Functions
def stt(audio_path) → str          # Whisper transcription
def llm(user_text) → str           # Claude response
def tts_generate(text) → wav       # XTTS synthesis
def process_voice_input(audio) → (response, history)  # Full pipeline
```

## Limitations

- **GPU Memory:** 2GB max (OK pour XTTS seul)
- **Audio Format:** WAV 16-bit mono/stéréo recommandé
- **Langue:** Français principalement (configurable)
- **Claude:** Besoin d'API key pour réponses intelligentes

## Optimisations Futures

1. Voice Activity Detection (VAD) - détecter silence
2. Streaming audio processing
3. Multi-language support
4. GPU memory pooling
5. Caching des réponses frecuentes

---

_Morwintar - Listen, Think, Speak_ 🎤🧠🎤

Date: 2026-02-21
