import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

#Create an empty app
app = QApplication([])


window = QWidget()
window.setWindowTitle("App")
window.setGeometry(500, 500, 500, 100)





window.show()
sys.exit(app.exec())