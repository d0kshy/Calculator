import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QMainWindow, QPushButton

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Graphs Calculator")
        self.setGeometry(500, 500, 500, 700)

        self.greetMsg = QLabel(self)
        self.greetMsg.setText("Push the button below")
        self.greetMsg.move(100, 100)
        self.greetMsg.adjustSize()

        
        self.text = QLabel(self)
        
        self.btn = QPushButton("Button",parent=self)
        self.btn.move(200, 200)
        self.btn.clicked.connect(self.printText)

    def printText(self):
        self.text.setText("Text")
        self.text.move(300, 300)
        self.text.adjustSize()


def application():
    #Create an empty app
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()