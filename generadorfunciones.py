from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import matplotlib.animation as animation
import random
from itertools import count

x_vals=[]
y_vals=[]
index=count()

class MainWindow(QMainWindow):
    def __init__(self): # Create matplotlib interface
        self.pause= True

        QMainWindow.__init__(self)
        loadUi("GUI/guitarea.ui", self)
        self.setWindowTitle("GUI hydrometra")
        self.pushbutton_gen_funcion.clicked.connect(self.update_animation)
        self.pushButton_limpiar.clicked.connect(self.clean_plot)
        self.pushButton_detener.clicked.connect(self.stop_plot)
        self.pushButton_save.clicked.connect(self.save_plot)

    def update_animation(self):
        self.ani = animation.FuncAnimation(self.MplWidget, self.update_axes, 
        interval=500)
        self.MplWidget.canvas.draw()

    def update_axes(self, update):
        x_vals.append(next(index))
        y_vals.append(random.randint(0, 5))
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(x_vals, y_vals)
        
    def clean_plot(self):
        x_vals.clear()
        y_vals.clear()
        index=count(0)
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.draw()


    def stop_plot(self):
        if self.pause==True:
            self.ani.event_source.stop()
            self.pushButton_detener.setText("Continuar")
            self.pause=False
        elif self.pause==False:
            self.ani.event_source.start()
            self.pushButton_detener.setText("Detener")
            self.pause=True
    def save_plot(self):
        self.MplWidget.canvas.print_figure('image.png')

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
