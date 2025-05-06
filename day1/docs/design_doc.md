
---

## 📄 Design Document: Real-Time Sign Language Recognition System

### 🧩 Problem Statement

Millions of people with hearing and speech disabilities rely on sign language, yet real-time interpretation is still inaccessible in many settings. A system that can recognize hand gestures and convert them into text can bridge this gap and enhance inclusivity.

---

### 🎯 Goals

* Build a robust image classification system to recognize ASL gestures.
* Enable real-time gesture recognition through live camera input.
* Provide an intuitive interface to display the translated text.

---

### 🚫 Non-Goals

* Sentence-level ASL interpretation or grammar parsing.
* Video sequence classification (focus is on static gestures only).
* Integration with third-party translation services or speech synthesis.

---

### 💡 Design Options

| Option                                  | Description                                                             | Pros                                       | Cons                                                 |
| --------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------- |
| **Custom CNN**                          | Build a CNN from scratch using Keras on grayscale 48x48 gesture images. | Lightweight, faster training, full control | May require tuning to reach high accuracy            |
| **Pretrained Models (e.g., MobileNet)** | Use transfer learning to classify gestures.                             | High accuracy, less data needed            | Overkill for simple classification, slower inference |
| **Color Image Input**                   | Train using RGB images for better clarity.                              | Richer features                            | More memory and compute needed                       |

---

### 🧠 Decision

We chose a **custom CNN** with grayscale image input. It ensures a balance between **model accuracy**, **real-time performance**, and **simplicity**—ideal for deployment in lightweight environments like Streamlit.

---

### ⚠️ Risks & Mitigations

| Risk                                        | Mitigation                                                     |
| ------------------------------------------- | -------------------------------------------------------------- |
| Overfitting on small dataset                | Use data augmentation, dropout layers, and batch normalization |
| Real-time performance issues                | Optimize image size, limit model depth, run on GPU             |
| Inconsistent gesture detection in low light | Normalize input, use thresholding, enhance preprocessing       |

---

### 🚀 Outcome

This system empowers communication by translating ASL gestures into readable text through a real-time, browser-based interface—demonstrating the potential of machine learning in accessibility technology.

---

