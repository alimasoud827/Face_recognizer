### Face Detectior with OpenCV & Node.js

This project detects faces in images using OpenCV and Python, integrated with a Node.js backend.

### 🚀 Features

Upload an image via a URL.

Detect faces using OpenCV's Haar Cascade.

Display the processed image with detected faces.

Uses Express.js for the backend.

## 🛠️ Setup Instructions

## 1️⃣ Clone the Repository

git clone https://github.com/alimasoud827/face-detection.git

cd face-detection

## 2️⃣ Install Dependencies

Backend (Node.js)

npm install

Python Dependencies

pip install opencv-python requests numpy

## 3️⃣ Run the Server

node server.mjs

## 🖼️ Usage

Start the Node.js server.

Open http://localhost:5000/ in your browser.

Enter an image URL and submit.

The detected faces will be displayed on the page.

## 📜 File Structure

├── public/                  # Stores processed images

│   ├── detected_faces.jpg   # Output image

├── views/                   # Frontend templates (EJS)

│   ├── index.ejs

├── face_det.py              # Python script for face detection

├── server.mjs               # Express.js backend

├── package.json             # Node.js dependencies

└── README.md                # Project documentation

## 🧑‍💻 API Endpoint

POST /detect

Request Body: { "image_url": "<URL_TO_IMAGE>" }

Response: Processed image with detected faces

## 🛠️ Troubleshooting

UnicodeEncodeError on Windows

If you get an error related to ✅ emoji:

print("Face detection complete. Saved to", output_path.encode("utf-8", "ignore").decode("utf-8"))

Or run in CMD before starting Python:

chcp 65001

## 📜 License

This project is open-source under the MIT License.

Developed by Ali Masoud 🚀

