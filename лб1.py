import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QPixmap, QImage, QColor
from PyQt6.QtCore import Qt

img = None

def open_img():
    global img
    path, _ = QFileDialog.getOpenFileName(None, "Открыть", "", "*.png *.jpg *.bmp")
    if path:
        img = QImage(path).convertToFormat(QImage.Format.Format_RGB888)
        win.label.setPixmap(QPixmap.fromImage(img).scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio))

def process():
    global img
    if img is None: return
    w, h = img.width(), img.height()
    img.setPixelColor(0,      0,     QColor(255, 255, 127))
    img.setPixelColor(w // 2, 0,     QColor(255, 127, 255))
    img.setPixelColor(w // 2, h - 1, QColor(127, 255, 255))
    win.label.setPixmap(QPixmap.fromImage(img).scaled(400, 400, Qt.AspectRatioMode.KeepAspectRatio))

def save():
    global img
    if img is None: return
    path, _ = QFileDialog.getSaveFileName(None, "Сохранить", "result.png", "*.png")
    if path:
        img.save(path)

app = QApplication(sys.argv)
win = QWidget()
win.label = QLabel()
win.label.setMinimumSize(400, 400)
win.label.setStyleSheet("border: 1px solid gray;")
b1 = QPushButton("Открыть");   b1.clicked.connect(open_img)
b2 = QPushButton("Обработать");b2.clicked.connect(process)
b3 = QPushButton("Сохранить"); b3.clicked.connect(save)
lay = QVBoxLayout(win)
lay.addWidget(b1); lay.addWidget(b2); lay.addWidget(b3); lay.addWidget(win.label)
win.show()
sys.exit(app.exec())