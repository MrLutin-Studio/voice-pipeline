# Voice Pipeline - Setup Complet

## 🎤 Vue d'ensemble

Voice Pipeline est un système de synthèse vocale clonée utilisant:
- **XTTS v2** (Text-to-Speech avec clonage de voix)
- **OpenAI Whisper** (Speech-to-Text)
- **Claude API** (Traitement du langage naturel)

L'assistant **Morwintar** utilise ce système pour avoir une vraie voix synthétisée.

---

## 📋 Prérequis Système

### Python
- Python 3.11+ requis (3.12+ a des incompatibilités)
- Recommandé: Python 3.11

### GPU (Optionnel)
- **Détecté:** GTX 750 Ti (Compute Capability 5.0) + GTX 1050 (Compute Capability 6.1)
- **Limitation:** PyTorch 2.10 ne supporte que CC 7.0+ (RTX 20+)
- **Workaround:** Fonctionne en CPU, mais plus lent

### Dépendances Système
```bash
sudo apt-get install -y python3.11-venv libavutil-dev libavcodec-dev libavformat-dev libswscale-dev
```

---

## 🔧 Installation

### 1. Cloner le repo
```bash
cd /mnt/storage/projects
gh repo clone MrLutin-Studio/voice-pipeline
cd voice-pipeline
```

### 2. Créer l'environnement virtuel
```bash
python3.11 -m venv voice_env
source voice_env/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Installer PyTorch compatible
```bash
# PyTorch avec CUDA 12.1 (recommandé)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 5. Installer coqui-tts et dépendances
```bash
pip install coqui-tts>=0.27.0 torchaudio
```

### 6. Appliquer les patches (IMPORTANT!)

Ces patches corrigent les incompatibilités entre coqui-tts et transformers:

**Patch 1:** `TTS/tts/layers/tortoise/autoregressive.py`
```python
# Remplacer:
# from transformers.pytorch_utils import isin_mps_friendly as isin
# Par:
try:
    from transformers.pytorch_utils import isin_mps_friendly as isin
except ImportError:
    import torch
    def isin(elements, test_elements):
        return torch.isin(elements, test_elements)
```

Les patches sont appliqués automatiquement par:
```bash
python3 apply_patches.py
```

---

## 🎤 Configuration

### Fichiers Requis

**samples/sample.wav** - Votre sample audio pour le clonage de voix
- Durée recommandée: 10-30 secondes
- Format: WAV 16-bit mono/stéréo
- La voix doit être claire et distincte

### Vérifier la config

```bash
python3 -c "from TTS.api import TTS; print('✓ TTS importé avec succès')"
```

---

## ▶️ Utilisation

### 1. Génération Simple

```bash
source voice_env/bin/activate
python3 generate_presentation.py
```

Cela génère `output/presentation_smooth.wav` avec 7 phrases de présentation.

### 2. Synthèse Personnalisée

```bash
python3 -c "
from TTS.api import TTS
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
tts = TTS('tts_models/multilingual/multi-dataset/xtts_v2').to(device)

text = 'Votre texte ici'
tts.tts_to_file(
    text=text,
    speaker_wav='samples/sample.wav',
    language='fr',
    file_path='output/custom.wav'
)
"
```

### 3. Options de Performance

```bash
# Utiliser CPU (plus lent)
python3 generate_presentation.py --device cpu

# Utiliser GPU (plus rapide, si compatible)
python3 generate_presentation.py --device cuda
```

---

## 🐛 Troubleshooting

### ImportError: cannot import name 'isin_mps_friendly'

**Cause:** Incompatibilité transformers/coqui-tts

**Fix:**
```bash
pip install transformers==4.35.0
# Puis appliquer les patches
```

### CUDA out of memory

```bash
# Utiliser CPU
export CUDA_VISIBLE_DEVICES=""
python3 generate_presentation.py
```

### GPU non détecté

```bash
# Vérifier les drivers
nvidia-smi

# Charger les modules
sudo modprobe nvidia
nvidia-smi
```

---

## 🎯 GPU Information

### Détecté sur ce Host

| GPU | Compute Capability | Memory | Status |
|-----|-------------------|--------|--------|
| GTX 750 Ti | 5.0 | 2GB | ✅ Drivers OK |
| GTX 1050 | 6.1 | 2GB | ✅ Drivers OK |

**Note:** Ces GPUs sont trop vieux pour PyTorch 2.10 (qui supporte CC 7.0+).

### Pour utiliser les GPUs

Installer une ancienne version de PyTorch:
```bash
pip install torch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 --index-url https://download.pytorch.org/whl/cu116
```

---

## 📁 Fichiers Importants

```
voice-pipeline/
├── generate_presentation.py   # Script principal
├── voice_pipeline.py          # Pipeline complet
├── simple_tts.py              # TTS simple
├── requirements.txt           # Dépendances
├── config.json                # Configuration
├── samples/
│   └── sample.wav             # Votre voix
├── output/                    # Résultats générés
└── voice_env/                 # Environnement virtuel
```

---

## 🔑 Commandes Utiles

```bash
# Activer l'env
source voice_env/bin/activate

# Tester l'installation
python3 -c "from TTS.api import TTS; print('OK')"

# Vérifier les GPUs
nvidia-smi
python3 -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# Générer la présentation
python3 generate_presentation.py

# Envoyer sur Telegram
cp output/presentation_smooth.wav /tmp/ && python3 send_telegram.py
```

---

## 📝 Notes

- ✅ Voice Pipeline fonctionne entièrement en CPU
- ✅ Les GPUs sont détectés mais compatibilité PyTorch limitée
- ✅ Génération audio de haute qualité (~3 min pour 7 phrases sur CPU)
- ✅ Support multilingue (FR, EN, ES, etc.)

---

## 🎤 Morwintar Voice Stats

- **Voice Model:** XTTS v2 (Coqui)
- **Language:** French (FR)
- **Quality:** 24kHz, 16-bit
- **Generation Time:** ~30sec par phrase (CPU)
- **Status:** ✅ FULLY OPERATIONAL

---

_Dernière mise à jour: 2026-02-21_
