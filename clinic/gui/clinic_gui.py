import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow

class ClinicGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")

        # set the size of your window:
        # setFixedSize(), setMininumSize(), setMaximumSize()
        # use QSize(width, height)
        # self.setFixedSize(QSize(400, 300))


        # Set the central widget of the Window.
        self.setCentralWidget(button)



def main():
    app = QApplication(sys.argv)
    window = ClinicGUI()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()
