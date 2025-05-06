
---

````markdown
# Sign Language Recognition using CNN

A machine learning project that uses a Convolutional Neural Network (CNN) to recognize American Sign Language (ASL) hand gestures. This project aims to bridge communication gaps for people who are hard of hearing or mute by converting ASL into readable text.

---

## 🚀 Features

- Classifies ASL gestures from images
- Built with Keras + TensorFlow
- Real-time predictions using a Streamlit web interface
- Visualized training process with TensorBoard

---

## 📂 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/sign-language-recognition.git
   cd sign-language-recognition
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

---

## 🧠 Model Details

* **Input**: Grayscale images resized to 48x48 pixels
* **CNN Architecture**:

  * Convolutional Layers (ReLU activation)
  * MaxPooling
  * Dropout for regularization
  * Fully connected Dense layers
  * Softmax output for multi-class classification

---

## 📊 Dataset

* The dataset consists of labeled ASL hand gesture images.
* Preprocessing: resized, normalized.
* Data augmentation is applied using Keras `ImageDataGenerator` to improve model generalization.

---

## ✅ Usage

1. Upload or show a hand gesture in the app interface.
2. The model will predict the ASL sign.
3. The predicted label is displayed on the web interface.

---

## 🛠 Troubleshooting

* **Streamlit not opening**: Ensure that your environment is set up correctly. Run `streamlit run app.py` again.
* **GPU issues**: If you're experiencing issues with TensorFlow, consider switching to CPU training in Google Colab or update TensorFlow.
* **Accuracy is low**: Ensure the dataset is balanced and preprocessed properly. If necessary, augment the dataset further.

---

## 📌 Future Work

* Add real-time video feed recognition.
* Expand model to recognize full ASL sentences.
* Include a wider variety of hand gestures.

---

## 📚 Technologies

* **Python**, **TensorFlow**, **Keras**, **OpenCV**
* **Streamlit** (for web interface)
* **Google Colab** (for model training)

---

## 📸 Demo

![Demo Screenshot](diagrams/demo.png)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE] file for details.

---
