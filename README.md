# 🎤 Voice Pipeline

> **Parle → Comprend → Répond avec ta voix**

Un assistant vocal IA qui clone ta voix pour te répondre naturellement.

---

## 🤔 C'est quoi?

Voice Pipeline est un système conversationnel qui:

1. **Écoute** ta voix (ou lit ton texte)
2. **Comprend** ce que tu dis grâce à l'IA
3. **Répond** avec une voix clonée (la tienne ou une autre)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   🎤 Toi    │ →  │  🧠 Claude  │ →  │  🔊 Réponse │
│  (Audio)    │    │   (IA)      │    │ (Ta voix!)  │
└─────────────┘    └─────────────┘    └─────────────┘
      ↓                  ↓                  ↓
   Whisper          Génère une         XTTS v2
  (transcrit)        réponse        (clone vocal)
```

---

## ⚡ Démarrage rapide

### 1. Installation

```bash
# Clone le repo
git clone https://github.com/MrLutin-Studio/voice-pipeline.git
cd voice-pipeline

# Crée un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Installe les dépendances
pip install -r requirements.txt
```

### 2. Configuration

```bash
# Ajoute ta clé API Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 3. Utilisation

```bash
# Depuis un fichier audio
python voice_pipeline.py --input ma_question.wav

# Depuis du texte
python voice_pipeline.py --text "Salut, ça va?"

# Enregistrer depuis le micro
python voice_pipeline.py --record
```

---

## 🎙️ Le Sample Vocal

Pour que l'IA parle avec **ta voix**, il faut un sample:

| Critère | Recommandation |
|---------|----------------|
| **Format** | WAV (16kHz ou 22kHz) |
| **Durée** | 6 à 30 secondes |
| **Qualité** | Propre, sans bruit de fond |
| **Contenu** | Parle naturellement, phrases variées |

Place ton sample dans `samples/sample.wav` ou spécifie-le avec `--voice`.

---

## ⚙️ Configuration avancée

Tout se configure dans `config.json`:

```json
{
  "whisper": {
    "model": "base",       // tiny, base, small, medium, large
    "language": "fr"
  },
  "claude": {
    "model": "claude-haiku-4-5",
    "system_prompt": "Tu es un assistant sympa..."
  },
  "tts": {
    "language": "fr",
    "voice_sample": "samples/sample.wav"
  }
}
```

---

## 📋 Options CLI

| Option | Description |
|--------|-------------|
| `--input`, `-i` | Fichier audio d'entrée |
| `--text`, `-t` | Texte d'entrée (skip transcription) |
| `--voice`, `-v` | Sample vocal (défaut: config.json) |
| `--output`, `-o` | Fichier audio de sortie |
| `--record`, `-r` | Enregistrer depuis le micro |
| `--duration`, `-d` | Durée d'enregistrement (défaut: 5s) |
| `--device` | Forcer `cuda` ou `cpu` |

---

## 💻 Prérequis système

- **Python** 3.10+
- **GPU** recommandé (NVIDIA + CUDA) — ~6GB VRAM
- **CPU** possible mais plus lent
- **Clé API** [Anthropic](https://console.anthropic.com/)

---

## 🐛 Problèmes courants

**"CUDA out of memory"**
→ Utilise `--device cpu` ou un modèle Whisper plus petit (`tiny`)

**Voix robotique ou déformée**
→ Améliore ton sample vocal (plus long, plus propre)

**"No module named 'TTS'"**
→ `pip install coqui-tts`

---

## 📁 Structure du projet

```
voice-pipeline/
├── voice_pipeline.py   # Script principal
├── config.json         # Configuration
├── requirements.txt    # Dépendances Python
├── samples/            # Samples vocaux
│   └── sample.wav
└── output/             # Fichiers générés
```

---

## 📜 Licence

Projet expérimental — usage personnel.  
XTTS v2 sous [Coqui Public Model License](https://coqui.ai/cpml).

---

<p align="center">
  Créé par <b>Morwintar</b> 🖤 avec l'aide de <b>Delta_x1988</b> et <b>GhostNode</b>
</p>
