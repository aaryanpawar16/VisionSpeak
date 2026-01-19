# 👁️ AI Vision & Reader Assistant

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
