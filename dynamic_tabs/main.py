import sys
from PyQt5 import QtWidgets
from tab import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #checkboxların durumuna göre signal-slot bağlantısı yapılır. 
        # Bir onay kutusu işaretlendiğinde veya temizlendiğinde, stateChanged() sinyalini yayar
        self.checkBox.stateChanged.connect(self.open_close_tab)
        self.checkBox_2.stateChanged.connect(self.open_close_tab)
        self.checkBox_3.stateChanged.connect(self.open_close_tab)
        self.checkBox_4.stateChanged.connect(self.open_close_tab)
        #tableri görünmez yaptık. Burada setTabEnabled kullanarak tableri gösterebilir ama etkin kılmayabiliriz
        self.tabWidget.setTabVisible(3, False)
        self.tabWidget.setTabVisible(1, False)
        self.tabWidget.setTabVisible(2, False)
        self.tabWidget.setTabVisible(4, False)
        #tablerin arka plan rengini değiştirdik
        self.tab.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.tab_2.setStyleSheet("background-color: rgb(183, 255, 101);")
        self.tab_3.setStyleSheet("background-color: rgb(255, 189, 212);")
        self.tab_4.setStyleSheet("background-color: rgb(168, 106, 255);")
        self.tab_5.setStyleSheet("background-color: rgb(35, 255, 156);")

    #checkbox işaretli mi değil mi sorgusu için isChecked() metodu kullanılabilir  
    def open_close_tab(self):
        if self.checkBox.isChecked():
            self.tabWidget.setTabVisible(3, True)
        else:
            self.tabWidget.setTabVisible(3, False)
        if self.checkBox_2.isChecked():
            self.tabWidget.setTabVisible(2, True)
        else:
            self.tabWidget.setTabVisible(2, False)
        if self.checkBox_3.isChecked():
            self.tabWidget.setTabVisible(1, True)
        else:
            self.tabWidget.setTabVisible(1, False)
        if self.checkBox_4.isChecked():
            self.tabWidget.setTabVisible(4, True)
        else:
            self.tabWidget.setTabVisible(4,False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
