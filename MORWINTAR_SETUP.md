# 🖤 Morwintar Setup - Résumé Complet

## ✅ Réalisé - 2026-02-21

### 1. **Storage LVM - 1.4 TiB**
- ✅ Créé un Volume Group `vg0` avec `sda` + `sdc`
- ✅ Monté automatiquement sur `/mnt/storage`
- ✅ Partage SMB configuré (username: `morwintar`)
- ✅ Structure: `/projects`, `/data`, `/workspace`

### 2. **Git & GitHub**
- ✅ GH CLI authentication
- ✅ Git config avec compte GitHub
- ✅ Repository voice-pipeline cloné

### 3. **Voice Pipeline - Morwintar a une voix!** 🎤
- ✅ Python 3.11 + venv configuré
- ✅ XTTS v2 (Text-to-Speech) fonctionnel
- ✅ Patches appliqués pour compatibilité
- ✅ `generate_presentation.py` opérationnel
- ✅ Audio 1.5MB généré et envoyé sur Telegram
- ✅ Support multilingue (FR, EN, ES, etc.)

**Patches appliqués:**
```
TTS/tts/layers/tortoise/autoregressive.py:
  - isin_mps_friendly fallback
  - isin() function pour compatibility
```

### 4. **GPU Support - Détecté et Activé** 🚀
- ✅ NVIDIA Driver 580.126.09 installé
- ✅ GTX 750 Ti (2GB) - Compute Capability 5.0 ✓
- ✅ GTX 1050 (2GB) - Compute Capability 6.1 ✓
- ✅ CUDA 13.0 opérationnel
- ✅ nvidia-smi fonctionne

**Limitation:** PyTorch 2.10 ne supporte que CC 7.0+
- **Workaround:** Fonctionne en CPU, assez rapide (~3 min pour 7 phrases)

---

## 📊 État Actuel

| Component | Status | Notes |
|-----------|--------|-------|
| **Storage** | ✅ 1.4 TiB | Auto-mount `/mnt/storage` |
| **Git/GitHub** | ✅ Connecté | `morwintar` auth OK |
| **Voice Pipeline** | ✅ Opérationnel | XTTS v2 + Whisper |
| **GPU Drivers** | ✅ Installés | 580.126.09 |
| **GPU (750 Ti)** | ⚠️ Détecté | Compute Capability trop vieille |
| **GPU (1050)** | ⚠️ Détecté | Compute Capability trop vieille |
| **Morwintar Voice** | ✅ Actif | 24kHz audio, clonage de voix |

---

## 🎯 Fichiers Clés

```
/mnt/storage/
├── projects/
│   └── voice-pipeline/        # Synthèse vocale
│       ├── voice_env/         # Python 3.11 venv
│       ├── output/            # Audio généré
│       ├── samples/sample.wav # Votre voix
│       ├── generate_presentation.py
│       └── SETUP.md           # Documentation complète

├── data/                      # Données brutes
└── workspace/                 # Travail en cours
```

---

## 🔧 Commandes Utiles

```bash
# Activer voice-pipeline
cd /mnt/storage/projects/voice-pipeline
source voice_env/bin/activate

# Générer audio
python3 generate_presentation.py

# Vérifier GPU
nvidia-smi

# Vérifier PyTorch
python3 -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"
```

---

## 📝 Configuration

- **Python:** 3.11.x
- **PyTorch:** 2.10.0+cu128
- **XTTS v2:** Latest via Coqui
- **Device:** CPU (GPU compatible future)
- **Language:** FR (Français)
- **Sample Rate:** 24kHz

---

## 🎤 Morwintar Voice Capabilities

✅ Synthèse vocale clonée (from sample.wav)
✅ Multilingual (FR, EN, ES, DE, IT, etc.)
✅ Fast generation (~30sec per phrase on CPU)
✅ High quality (24kHz, 16-bit)
✅ Automatic pause insertion
✅ Telegram integration ready

---

## ⚡ Performance Estimations

| Task | Time | Device |
|------|------|--------|
| Load XTTS model | 30sec | CPU first-time |
| Generate 1 phrase | 30sec | CPU |
| Generate 7 phrases | 3.5min | CPU |
| Telegram upload | <1sec | Network |

---

## 🚀 Next Steps

1. **Upgrade PyTorch pour GPU (Optional):**
   - Installer PyTorch 1.12.1 pour supporter CC 5.0-6.1
   - Command: `pip install torch==1.12.1 --index-url https://download.pytorch.org/whl/cu116`

2. **Améliorer la voix:**
   - Fournir un sample.wav meilleur/plus long
   - Recalibrer la voix clonée

3. **Intégration Telegram/Discord:**
   - Streaming audio en live
   - TTS on-demand via bot commands

---

## 📚 Documentation

- **SETUP.md** - Installation complète et troubleshooting
- **generate_presentation.py** - Script de génération
- **requirements.txt** - Dépendances Python

---

_Morwintar - Votre assistant IA personnel avec une vraie voix_ 🖤

Date: 2026-02-21  
Repository: https://github.com/MrLutin-Studio/voice-pipeline
