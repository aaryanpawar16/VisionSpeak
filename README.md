# 👁️ VisionSpeak

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1MxlOW3HnhmLQzG0GWJCI7ebk4IwslfrW?usp=sharing)

A multimodal AI application designed to bridge the gap between visual information and audio feedback. This tool intelligently detects text in images (OCR) and reads it aloud. If no text is detected, it automatically switches to a Vision Transformer model to describe the scene visually.

## 📄 Research & Publication

This project is associated with the following research paper published in **Atlantis Press (ICSIAIML-25)**:

🔗 **[Read the Research Paper](https://www.atlantis-press.com/proceedings/icsiaiml-25/126021228)**

## ✨ Features

* **Smart Detection Switch:** Automatically detects if an image contains text or just objects.
* **OCR (Optical Character Recognition):** Uses **PaddleOCR** for high-accuracy text extraction (handwritten & printed).
* **Image Captioning:** Uses the **BLIP (Bootstrapping Language-Image Pre-training)** model to generate descriptive captions for images without text.
* **Text-to-Speech (TTS):** Converts the extracted text or generated description into audio using **gTTS**.
* **Dual Input Modes:** Supports live Webcam capture and static image uploads.

## 🚀 Quick Start (Google Colab)

The easiest way to try this project without installation is via Google Colab. The notebook supports camera capture via the browser.

[**Click here to run in Google Colab**](https://colab.research.google.com/drive/1MxlOW3HnhmLQzG0GWJCI7ebk4IwslfrW?usp=sharing)

## 💻 Local Installation

To run this project on your local machine (Windows, Mac, or Linux), follow these steps:

### Prerequisites
* Python 3.8 or higher
* Webcam (for live capture mode)

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/REPO_NAME.git](https://github.com/YOUR_USERNAME/REPO_NAME.git)
cd REPO_NAME
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```Bash
python main.py
```

## 🛠️ Tech Stack
OCR Engine: PaddleOCR

Vision Model: Hugging Face Transformers (BLIP)

Audio Generation: Google Text-to-Speech (gTTS)

Image Processing: OpenCV & PIL

## 📂 Project Structure
├── main.py              # The main script (Logic for OCR, Captioning, and TTS)
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
└── .gitignore           # Ignored files (images, cache)

## 🤝 Citation
If you use this code or methodology in your research, please consider citing our paper:

Proceedings of the International Conference on Smart Innovations in Artificial Intelligence and Machine Learning (ICSIAIML-25) > Atlantis Press, 2025.

Available at: https://www.atlantis-press.com/proceedings/icsiaiml-25/126021228


