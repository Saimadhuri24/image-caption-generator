# 🖼️ Image Caption Generator

This project is a Deep Learning–based Image Caption Generator built using TensorFlow, VGG16, LSTM, and Flask.

The application automatically generates descriptive captions for uploaded images by combining Computer Vision and Natural Language Processing techniques.

---

## 🎥 Preview

A quick preview of the AI Image Caption Generator:

* Home Page
* <img width="1920" height="1020" alt="Screenshot 2026-06-15 223304" src="https://github.com/user-attachments/assets/3e6afa34-649f-4277-bd5c-438b92b41fab" />

* Generated Caption Result Page
* <img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/de353540-aba4-4d47-844e-7cd52cb72101" />


---

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.

It really helps and motivates further improvements!

---

## 📌 Project Features

* 🖼️ Upload any image and generate captions instantly
* 🤖 Deep Learning-based image understanding
* 🧠 VGG16 feature extraction
* 🔤 LSTM-based caption generation
* 🌐 Flask web application
* 🎨 Responsive UI using HTML & CSS
* 📋 Copy generated captions with one click
* 💾 Pre-trained model and tokenizer support

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* VGG16
* LSTM
* NumPy
* Flask
* HTML
* CSS
* Pickle

---

## 📂 Project Structure

image-caption-generator/

│

├── app.py                     # Flask backend

├── predict.py                 # Caption generation logic

├── tokenizer.pkl              # Saved tokenizer

├── caption_model.keras        # Trained caption model

├── image-captioner.ipynb      # Training notebook

│

├── static/

│   ├── style.css

│   └── uploads/

│

├── templates/

│   ├── index.html

│   └── result.html

│

└── README.md

---

## 🧠 Deep Learning Workflow

### 1️⃣ Image Feature Extraction

* Load image
* Resize to 224×224
* Extract features using VGG16
* Generate 4096-dimensional feature vector

### 2️⃣ Caption Generation

* Tokenize captions
* Pass image features to LSTM model
* Predict next word sequentially
* Generate complete caption until end token

### 3️⃣ Output

* Display uploaded image
* Generate descriptive caption
* Allow user to copy caption

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Flask Application

```bash
python app.py
```

### 3️⃣ Open Browser

```text
http://127.0.0.1:5000/
or
Running on http://10.94.85.86:5000
```

---

## 🖥️ Application Flow

1. User uploads an image
2. VGG16 extracts image features
3. LSTM model generates caption
4. Caption is displayed on the result page
5. User can copy the generated caption

---

## 📊 Model Architecture

* VGG16 Feature Extractor
* Embedding Layer
* LSTM Layer
* Dense Layers
* Softmax Output Layer

---

## 🚀 Future Enhancements

* 📱 Mobile Responsive UI
* 🌍 Multi-language Caption Generation
* 🎤 Voice Caption Output
* 🔍 Beam Search Captioning
* 🤖 BLIP / Transformer-based Caption Models
* ☁️ Cloud Deployment

---

## 👩‍💻 Author

**Sai Madhuri**

AI Image Caption Generator using Deep Learning, TensorFlow, VGG16, LSTM, and Flask.

---

## 📄 License

This project is intended for educational and learning purposes.
