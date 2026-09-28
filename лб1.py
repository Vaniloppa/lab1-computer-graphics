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
    path, _ = QFileDialog.getSaveFileName(None, "Сохранить", "result.png", "*.png",)
    if path:
        img.save(path)

def save2():
    global img
    if img is None: return
    path, _ = QFileDialog.getSaveFileName(None, "Сохранить", "result.pbm", "*.pbm",)
    if path:
        mono_img = img.convertToFormat(QImage.Format.Format_Mono)
        w, h = mono_img.width(), mono_img.height()

        with open(path, 'w', encoding='ascii') as f:
            f.write("P1\n")
            f.write(f"{w} {h}\n")
            for y in range(h):
                row_values = []
                for x in range(w):
                    color = mono_img.pixelColor(x, y)
                    if color.red() < 128: 
                        row_values.append("1")
                    else:
                        row_values.append("0")
                f.write(" ".join(row_values) + "\n")

app = QApplication(sys.argv)
win = QWidget()
win.label = QLabel()
win.label.setMinimumSize(400, 400)
win.label.setStyleSheet("border: 1px solid gray;")
b1 = QPushButton("Открыть");   b1.clicked.connect(open_img)
b2 = QPushButton("Обработать");b2.clicked.connect(process)
b3 = QPushButton("Сохранить"); b3.clicked.connect(save)
b4 = QPushButton("Сохранить в формате pbm"); b4.clicked.connect(save2)
lay = QVBoxLayout(win)
lay.addWidget(b1); lay.addWidget(b2); lay.addWidget(b3); lay.addWidget(b4); lay.addWidget(win.label)
win.show()
sys.exit(app.exec())