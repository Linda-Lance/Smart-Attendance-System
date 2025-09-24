# 📘 Smart Attendance System  

An AI-powered **face recognition-based attendance system** built using **OpenCV, DeepFace, and Python**.  
The system captures student faces, stores them in a database, marks attendance automatically, and sends attendance reports via **WhatsApp**.  

---

## 🚀 Features  

- ✅ **Face Capture Module** – Collects face images of each student.  
- ✅ **Face Recognition** – Uses **DeepFace (Facenet)** for high accuracy.  
- ✅ **Attendance Logging** – Saves records in a CSV file with timestamp.  
- ✅ **WhatsApp Report** – Sends attendance summary report automatically after camera session ends.    
- ✅ **Lightweight GUI** – Uses OpenCV live camera feed with bounding boxes.  

---

## 🏆 Tech Stack  

- **Python**  
- **OpenCV** – Face detection  
- **DeepFace** – Face recognition (Facenet, VGGFace, ArcFace, etc.)  
- **PyWhatKit** – WhatsApp automation  
- **Pandas** – Attendance logs

---

## 📂 Project Structure  

```
Smart-Attendance-System/
│
├── data/                         # Haarcascade / model files
│   └── deploy.prototxt
│   └── face_embeddings.npz
│   └── res10_300x300_ssd_iter_140000.caffemodel
│
│
├── Attendance/                   # Attendance CSV reports
│   └── attendance_2025-09-24.csv
│   └── attendance_2025-09-23.csv
│
├── add_faces_facenet.py                  # Script to collect new faces
├── test.py                       # Main face recognition + attendance
├── whatsapp_sender.py            # Sends attendance report via WhatsApp
│
├── requirements.txt              # Dependencies
└── README.md                     # Documentation
```

---

## ⚙️ Installation  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/yourusername/Smart-Attendance-System.git
cd Smart-Attendance-System
```

### 2️⃣ Create Virtual Environment  
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

📌 Example `requirements.txt`:
```
opencv-python
deepface
mtcnn
tensorflow
pywhatkit
pandas
```

---

## 🧑‍💻 Usage  

### Step 1: Collect Faces  
Run the following script to capture faces for a new student:  
```bash
python add_faces.py
```
- Enter the student’s name when prompted.  
- The system will capture **50 images** by default.  
- Images will be stored in `known_faces/<name>/`.  

### Step 2: Run Attendance System  
```bash
python test.py
```
- Opens the webcam.  
- Detects and recognizes faces.  
- Marks attendance with timestamp in `Attendance/attendance_<date>.csv`.  

### Step 3: WhatsApp Attendance Report  
- After the camera session ends, the **complete attendance report** is automatically sent via WhatsApp using `whatsapp_sender.py`.  

---

## 🧠 Face Recognition Models  

This project supports multiple backends via **DeepFace**:  
- **VGG-Face** (default)  
- **Facenet**  
- **OpenFace**  
- **DeepFace**  
- **ArcFace**  

👉 You can change the model in `test.py`:  

```python
DeepFace.find(img_path, db_path="known_faces", model_name="Facenet")
```

---

## 📸 Training Images

Here are some sample training images used for face recognition:

- Elon Musk Image Training :
<img width="639" height="505" alt="Elon Musk_Train_Img" src="https://github.com/user-attachments/assets/e0c67d8d-5ff9-4a34-846e-e2ac637c28cf" />

- Bill Gates Image Training:
<img width="640" height="504" alt="Bill Gates_Train_Img" src="https://github.com/user-attachments/assets/49a673c9-00fc-4161-85a7-1285f68bfd7a" />

---

## 🎯 Result

Below is an example of how the system detects and recognizes faces in real time:

- Elon Musk Live Prediction

<img width="1356" height="732" alt="Elon Musk_Live_Prediction" src="https://github.com/user-attachments/assets/e1f0391e-2b43-4b2c-a704-ae6c1171ceac" />

-Bill Gates Live Prediction

<img width="1357" height="734" alt="Bill Gates_Live_Prediction" src="https://github.com/user-attachments/assets/9e0113e7-f641-465c-9b60-f7a630ac802c" /> 

- Attendance file (`CSV`) example:  

<img width="502" height="136" alt="attendance_csv" src="https://github.com/user-attachments/assets/3626fb45-e2d0-4c07-a8b7-19a4635084b6" />

- WhatsApp message example:  

<img width="836" height="561" alt="whatsapp_msg" src="https://github.com/user-attachments/assets/05d5c4d1-b3a5-4815-9446-418caa1813c3" />

---

## 🔧 Troubleshooting  

- **Face not detected properly?**  
  Use **DNN SSD / RetinaFace** instead of Haar cascades.  

- **Numpy / TensorFlow errors?**  
  Downgrade Numpy to `<2.0`:  
  ```bash
  pip install numpy==1.24.4
  ```

- **WhatsApp messages not sending?**  
  - Make sure WhatsApp Web is logged in.  
  - Instead of `pywhatkit`, you can use `pyautogui` to auto-send messages.  

---

## 📌 Future Enhancements  

- 📷 Multiple camera support  
- 📊 Dashboard for real-time attendance  
- 🔔 SMS / Email notification system  
- 🧩 Cloud database (Firebase / MongoDB)  

---

## 👩‍💻 Author  

👤 **Linda Lance**  
- [LinkedIn](https://linkedin.com/)
- [Github](https://github.com/Linda-Lance)
- lindalance2210@gmail.com 

