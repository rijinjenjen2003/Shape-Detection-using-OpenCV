# 🔷 Shape Detection using OpenCV

## 📌 Overview

This project uses **OpenCV** to detect and classify basic shapes such as **Triangle, Rectangle, and Circle** from images or live webcam feed.

It works by processing the image, detecting contours, and analyzing the number of vertices in each shape.

---

## 🧠 How It Works

1. Convert image to **grayscale**
2. Apply **Gaussian Blur** to remove noise
3. Perform **edge detection (Canny)**
4. Detect **contours**
5. Approximate contour to polygon using `approxPolyDP`
6. Count vertices to classify shapes:

   * 3 → Triangle
   * 4 → Rectangle
   * > 4 → Circle
7. Draw contours and label shapes

---

## 🛠️ Technologies Used

* Python 🐍
* OpenCV

---

## 📂 Project Structure

```
shape-detection/
│── main.py
│── shapes.png
│── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install opencv-python
```

### 2. Run the program

```bash
python main.py
```

---

## 📸 Output

* Detects shapes in image
* Draws green boundaries
* Labels each shape

---

## 🎥 Live Detection (Optional)

* Uses webcam to detect shapes in real-time
* Press **ESC** to exit

---

## ⚠️ Notes

* Works best with **clear shapes on plain background**
* Small contours are ignored to reduce noise

---

## 🚀 Future Improvements

* Detect more shapes (pentagon, hexagon)
* Add color detection
* Improve accuracy using Machine Learning

---

## 🎯 Learning Outcomes

* Image processing basics
* Edge detection & contours
* Shape classification
* Real-time computer vision

---

## 🙌 Acknowledgment

This project was built as part of a structured learning journey using:

**SkillForge Mentor Framework — Designed by Aditya Ajith**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
