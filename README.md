# Face Recognition Attendance System

📖 **Overview**

This project is a real-time Face Recognition Attendance System built with Python, OpenCV, and Machine Learning (KNN).
It detects faces using a webcam, recognizes registered users, and marks attendance with entry/exit times in CSV files.
The system also provides voice feedback and can send WhatsApp notifications for attendance updates.

✨ **Features**
  - Face detection & recognition using OpenCV Haarcascade and KNN classifier
  - Automatic attendance logging into CSV files with timestamps
  - Text-to-Speech (TTS) feedback for entry/exit
  - WhatsApp integration to send attendance reports using pywhatkit & pyautogui
  - Custom background interface for a clean display

🛠️ **Tech Stack**
  - Python 3.x
  - OpenCV – Face detection & image processing
  - Scikit-learn (KNN) – Face recognition
  - NumPy & Pandas – Data handling
  - PyWhatKit & PyAutoGUI – WhatsApp message automation
  - SAPI.SpVoice (win32com) – Text-to-Speech engine (Windows only)

📂 **Project Structure**
Face-Attendance-System/
│── data/                     # Stores haarcascade and face data
│   ├── haarcascade_frontalface_default.xml
│   ├── names.pkl
│   ├── faces_data.pkl
│
│── Attendance/               # Attendance CSV files saved daily
│   ├── Attendance_18-09-2025.csv
│
│── whatsapp_sender.py        # WhatsApp messaging script
│── test.py                   # Main attendance script
│── collect_faces.py          # (Optional) Script to collect face data
│── background_img.png        # Background UI image
│── README.md                 # Project documentation
│── requirements.txt          # Dependencies


⚙️** Installation & Setup**

1️⃣ Clone the Repository
git clone https://github.com/your-username/Face-Attendance-System.git
cd Face-Attendance-System

2️⃣ Create Virtual Environment (recommended)
python -m venv venv
#Activate it:
#Windows
venv\Scripts\activate
#macOS/Linux
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Face Data Collection (to register a new user)
python collect_faces.py


Enter your name when prompted

The system will capture 100 face samples

5️⃣ Run the Attendance System
python test.py

Look at the camera to get recognized

Attendance will be logged automatically

Exit by pressing q

📜 **Requirements File** (requirements.txt)
opencv-python
scikit-learn
numpy
pandas
pywhatkit
pyautogui
requests
pywin32

🚀 **How It Works**
  - Face Data Collection – Captures & stores user faces in data/.
  - Training – Uses KNN classifier to learn face embeddings.
  - Recognition & Attendance – Detects faces, logs timestamps, provides TTS feedback.
  - WhatsApp Notification – Sends attendance summary via WhatsApp after session ends.

📊 **Sample Attendance CSV**
NAME	ENTRY TIME	EXIT TIME	STATUS
Linda	09:45:12	12:10:35	Exit
Alex	10:00:21	11:59:50	Exit


📢 **Future Enhancements**
  - Cloud database integration (Firebase/MySQL)
  - Web dashboard for real-time monitoring
  - Mobile app integration
  - Improved face recognition using Deep Learning (CNN)
