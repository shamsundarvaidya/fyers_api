import sys

from fyers_api import fyersModel




from PySide2.QtCore import QSize, Qt
from PySide2.QtWidgets import QApplication, QMainWindow,QLabel
from PySide2.QtCore import QTimer, QPoint

client_id = "09PDZZH120-100"

acc_tok = ""

with open('token.txt') as tk:
    acc_tok = tk.read()


fyers = fyersModel.FyersModel(client_id=client_id, token=acc_tok,log_path="./")

data = {"symbols":"NSE:NIFTY50-INDEX"}
    

def get_ltp_data():
    response = fyers.quotes(data)
#print(response)
    if response['s'] == "error":
        return(response['message'])
    else:
        nif_data = response['d'][0]['v']
        nif_ltp = nif_data['lp']
        nif_chg = nif_data['ch']
        #print(fyers.quotes(data)['d'][0]['v']['ch'])
        #print(f'LTP : {nif_ltp}||ch:{nif_chg}')
        return(f'Cpu:{nif_chg}')

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(100, 30)
        self.setStyleSheet("QMainWindow{background-color: darkgray;border: 1px solid black}")
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.move(1450,800)

        self.setWindowTitle("My App")

        self.lab = QLabel("Hello!")
        self.lab.setStyleSheet("QLabel{background-color: rgb(0,0,0); border: 1px solid red; color: rgb(255,255,255); font: bold italic 10pt 'Times New Roman';}")
        self.lab.setGeometry(5, 5, 60, 40)
        # Set the central widget of the Window.
        self.setCentralWidget(self.lab)
        self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.update_data)
        self.timer.start()

    def update_data(self):
        self.lab.setText(get_ltp_data())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        print(self.oldPos.x(),self.oldPos.y())

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()