# 🧠 Neurodegenerative Disease Detection Using Spiral Images and Voice Analysis

## 📌 Overview

Neurodegenerative diseases such as Parkinson's Disease can significantly affect motor control, handwriting patterns, and vocal characteristics. Early detection plays a crucial role in improving patient care and treatment outcomes.

This project presents an **AI-powered healthcare diagnostic system** that leverages **Deep Learning and Computer Vision techniques** to detect Parkinson's Disease through:

* ✍️ Spiral Drawing Image Analysis
* 🎙️ Voice Audio Analysis

The system integrates Convolutional Neural Networks (CNNs) with a Flask-based web application to provide automated predictions, confidence scores, and patient report management.

---

## 🎯 Objectives

* Detect Parkinson's Disease using spiral handwriting patterns.
* Analyze voice recordings to identify vocal biomarkers associated with Parkinson's Disease.
* Provide a user-friendly web interface for patients and healthcare professionals.
* Store prediction reports securely for future analysis and monitoring.

---

## 🚀 Key Features

### 👤 User Module

* User Registration & Authentication
* Secure Login System
* Spiral Image Upload
* Voice Sample Upload
* Instant Prediction Results
* Confidence Score Display
* Personal Prediction History

### 👨‍💼 Admin Module

* Admin Dashboard
* User Management
* Prediction Report Monitoring
* Disease Detection Statistics

### 🤖 AI Prediction Engine

* CNN-based Spiral Image Classification
* CNN-based Voice Signal Classification
* Mel-Spectrogram Audio Processing
* Real-time Prediction Generation
* Confidence Score Calculation

### 🗄️ Database Management

* MySQL Integration
* User Data Storage
* Prediction Report Storage
* Historical Result Tracking

---

## 🏗️ System Architecture

```text
User Input
     │
     ├── Spiral Image Upload
     │         │
     │         ▼
     │   CNN Image Model
     │         │
     │         ▼
     │   Prediction Result
     │
     └── Voice Audio Upload
               │
               ▼
      Mel Spectrogram Conversion
               │
               ▼
         CNN Audio Model
               │
               ▼
         Prediction Result

                    ▼
             Flask Backend

                    ▼
              MySQL Database

                    ▼
           Report Generation
```

---

## 💻 Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap
* JavaScript

### Backend

* Python
* Flask Framework

### Database

* MySQL

### Artificial Intelligence & Machine Learning

* TensorFlow
* Keras
* Convolutional Neural Networks (CNN)
* NumPy
* Librosa
* OpenCV

### Development Tools

* PyCharm
* Git
* GitHub

---

## 📂 Dataset Information

### Spiral Image Dataset

The image dataset contains spiral drawings categorized into:

* Healthy Subjects
* Parkinson's Disease Patients

### Voice Audio Dataset

The audio dataset contains voice recordings categorized into:

* Healthy Individuals
* Parkinson's Disease Patients

Audio samples are transformed into **Mel-Spectrograms** before being fed into the CNN model for classification.

---

## 🧠 Deep Learning Models

### Spiral Image Classification Model

* Input Size: 200 × 200 RGB Images
* CNN Architecture
* Batch Normalization
* Max Pooling Layers
* Dropout Regularization
* Softmax Classification

### Voice Analysis Model

* Audio Resampling using Librosa
* Mel-Spectrogram Feature Extraction
* Spectrogram Resizing
* CNN-Based Audio Classification
* Softmax Output Layer

---

## 🔄 Workflow

### Spiral Image Analysis

1. User uploads a spiral drawing image.
2. Image preprocessing is performed.
3. CNN model extracts visual features.
4. Disease prediction is generated.
5. Confidence score is displayed.
6. Result is stored in the database.

### Voice Analysis

1. User uploads a voice recording.
2. Audio is converted into a Mel-Spectrogram.
3. CNN model extracts acoustic features.
4. Prediction is generated.
5. Confidence score is displayed.
6. Result is stored in the database.

---

## 📊 Model Output

The system predicts:

### Image Model

* Healthy
* Parkinson's Disease

### Voice Model

* Healthy
* Parkinson's Disease

Output includes:

* Predicted Class
* Confidence Score (%)
* Date of Prediction
* Prediction Type (Image/Audio)

---

## 📁 Project Structure

```text
Neurodegenerative-Disease-Detection/
│
├── DataSet/
├── Soundset/
├── Model/
│   └── pdmodel.h5
│
├── static/
├── templates/
│
├── App.py
├── CNNPar.py
├── Model.py
├── Predict.py
├── NewsoundPredict.py
│
├── parkinsonspiraldudiodb.sql
└── README.md
```

---

## ⚙️ Installation & Setup

### Clone Repository

```bash
git clone https://github.com/Ranjithapriya14/Multimodal-Approach-Neurodegenerative-diseases.git
```

### Navigate to Project Directory

```bash
cd Ranjithapriya14/Multimodal-Approach-Neurodegenerative-diseases
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Database

1. Open MySQL.
2. Create a database:

```sql
CREATE DATABASE parkinsonspiraldudiodb;
```

3. Import:

```text
parkinsonspiraldudiodb.sql
```

### Run Application

```bash
python App.py
```

Open:

```text
http://127.0.0.1:5000/
```

---

## 🔮 Future Enhancements

* Real-Time Voice Recording
* Explainable AI (XAI)
* Mobile Application Development
* Cloud Deployment (AWS/Azure)
* Doctor Recommendation System
* Medical Report Generation
* Multi-Disease Detection Framework
* REST API Integration

---

## 🌟 Project Highlights

✔ Deep Learning-Based Healthcare Application

✔ Dual-Modal Disease Detection (Image + Audio)

✔ CNN Architecture for Medical Prediction

✔ Flask Web Application Development

✔ MySQL Database Integration

✔ End-to-End AI Deployment Workflow

---

## 👩‍💻 Author

**Ranjithapriya**

B.E. Computer Science and Engineering

Passionate about Artificial Intelligence, Machine Learning, Healthcare Analytics, and Full-Stack Development.

### Connect with Me

* LinkedIn: www.linkedin.com/in/ranjitha-priya-g-071880293
* GitHub: https://github.com/Ranjithapriya14
