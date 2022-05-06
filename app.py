from math import cos,sin,acos,asin,pi
from PyQt5 import QtCore, QtGui, QtWidgets
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
import os,sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

l=c=w=ucm=ulm=um=urm=z=r=p=delta=im=None
def impedance():
    global l,c,w,z,r,um,im,delta
    if all(i is not None for i in(um,im)):
        z=um/im
    elif all(i is not None for i in{r,delta}):
        z= r/cos(abs(delta))
    elif all(i is not None for i in{r,l,w,c}):
        z= (r**2+(l*w-(1/(c*w)))**2)**0.5
def restot():
    global z,l,w,c,delta,r,urm,im
    if all(i is not None for i in{z,delta}):
        r= z*cos(abs(delta))
    elif all(i is not None for i in{urm,im}):
        r=urm/im
    elif all(i is not None for i in{z,l,w,c}):
        r= (z**2-(l*w-1/(c*w))**2)**0.5
def inductance():
    global z,r,w,c,ulm,w,im,l
    if all(i is not None for i in{z,r,w,c}):
        l= max((1/w)*((z**2-r**2)**0.5+1/(c*w)),(1/w)*((r**2-z**2)**0.5+1/(c*w)))
    elif all(i is not None for i in{ulm,w,im}):
        l= ulm/(w*im)
def omega():
    global r,z,l,c,w,ulm,im,ucm
    """if all({r,l,z,c}) is not None:
        w= "eq deuxieme degrée" """
    if all(i is not None for i in{ulm,l,im}):
        w= ulm/(l*im)
    elif all(i is not None for i in{ucm,im,c}):
        w=im/(c*ucm)
def capacite():
    global z,r,w,c,l,ulm,im
    if all(i is not None for i in{z,r,w,l}):
        c= max(1/((l*(w**2))-w*((z**2-r**2)**0.5)),1/((l*(w**2))+w*((z**2-r**2)**0.5)))
    elif all(i is not None for i in{ucm,w,im}):
        c= im/(w*ucm)
def puissance():
    global p,um,im,delta
    if all(i is not None for i in{um,im,delta}):
        p= 0.5*um*im*cos(abs(delta))
def tension():
    global p,um,im,delta,z,im,ucm,ulm,urm
    if all(i is not None for i in{im,z}):
        um= im*z
    elif all(i is not None for i in{delta,urm}):
        um= urm/cos(abs(delta))
    elif all(i is not None for i in{p,im,delta}):
        um= (2*p)/(im*cos(abs(delta)))
    elif all(i is not None for i in{ucm,ulm,delta}):
        um= (ucm-ulm)/sin(abs(delta))
def intensite():
    global im,um,z,p,delta,ulm,ucm,w,c,l,r
    if all(i is not None for i in{urm,r}):
        im= urm/r
    elif all(i is not None for i in{p,um,delta}):
        im= (2*p)/(um*cos(abs(delta)))
    elif all(i is not None for i in{um,z}):
        im= um/z
    elif all(i is not None for i in{ucm,c,w}):
        im= ucm*c*w
    elif all(i is not None for i in{l,w,ulm}):
        im= ulm/(w*l)
def deltafind():
    global p,um,im,delta,ulm,ucm,r,z,urm
    if all(i is not None for i in{urm,um}):
        delta= acos(urm/um)
    elif all(i is not None for i in{r,z}):
        delta= acos(r/z)
    elif all(i is not None for i in{ulm,ucm,um}):
        delta= asin((ucm-ulm)/um)
    elif all(i is not None for i in{p,um,im}):
        delta= acos((2*p)/(um*im))
def tension_bobine():
    global um,ucm,ulm,l,w,im,delta
    if all(i is not None for i in{l,w,im}):
        ulm= l*w*im
    elif all(i is not None for i in{delta,ucm,um}):
        ulm= ucm-sin(delta)*um
def tension_con():
    global im,c,w,delta,ulm,um,ucm
    if all(i is not None for i in{im,c,w}):
        ucm= im/(c*w)
    elif all(i is not None for i in{delta,um,ulm}):
        ucm= sin(delta)*um+ulm
def tension_res():
    global delta,um,r,im,urm
    if all(i is not None for i in{delta,um}):
        urm= um*cos(abs(delta))
    elif all(i is not None for i in{r,im}):
        urm= r*im
        
        

class Ui_MainWindow(object):
    photos={"g":resource_path("tesla.jpg"),
            "c":resource_path("light.jpg"),
            "b":resource_path("coil3.jpg"),
            "r":resource_path("red2.jpg"),
            "cir":resource_path("large.jpeg"),
            "sub":resource_path("one.jpg")}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1536,864)
        MainWindow.setStyleSheet("background-color: rgb(17, 99, 118);")
        MainWindow.setWindowIcon(QtGui.QIcon(resource_path('l.ico')))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei Light")
        font.setPointSize(18)        
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        font3 = QtGui.QFont()
        font3.setFamily("Microsoft JhengHei Light")
        font3.setPointSize(8) 
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backphoto = QtWidgets.QLabel(self.centralwidget)
        self.backphoto.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.backphoto.setMouseTracking(False)
        self.backphoto.setText("")
        #self.backphoto.autoFillBackground()
        #self.backphoto.setWindowFlag(Qt.Window,True)
        
        
        self.watermark = QtWidgets.QLabel(MainWindow)
        self.watermark.setGeometry(QtCore.QRect(1300, 800, 300, 70))
        self.watermark.setFont(font3)
        self.watermark.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.watermark.setText("Mahmoud Nefzi")
        
        self.button_gene = QtWidgets.QPushButton(self.centralwidget)
        self.button_gene.setGeometry(QtCore.QRect(50, 20, 161, 61))
        self.button_gene.setFont(font)
        self.button_gene.setStyleSheet("background-color: rgb(170, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_res = QtWidgets.QPushButton(self.centralwidget)
        self.button_res.setGeometry(QtCore.QRect(50, 70, 111, 61))
        self.button_res.setFont(font)
        self.button_res.setStyleSheet("background-color: rgb(170, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_res.setObjectName("button_res")
        self.button_res.clicked.connect(lambda:self.cluck(self.button_res,"r"))
        
        self.button_con = QtWidgets.QPushButton(self.centralwidget)
        self.button_con.setGeometry(QtCore.QRect(50, 120, 191, 61))
        self.button_con.setFont(font)
        self.button_con.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_con.setObjectName("button_con")
        self.button_con.clicked.connect(lambda:self.cluck(self.button_con,"c"))
        
        self.button_circuit = QtWidgets.QPushButton(self.centralwidget)
        self.button_circuit.setGeometry(QtCore.QRect(50, 220, 91, 61))
        self.button_circuit.setFont(font)
        self.button_circuit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.button_circuit.setObjectName("button_circuit")
        self.button_circuit.clicked.connect(lambda:self.cluck(self.button_circuit,"cir"))
        self.button_bob = QtWidgets.QPushButton(self.centralwidget)
        self.button_bob.setGeometry(QtCore.QRect(50, 170, 101, 61))
        self.button_bob.setFont(font)
        self.button_bob.setStyleSheet("background-color: rgb(170, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_bob.setObjectName("button_bob")
        self.button_bob.clicked.connect(lambda:self.cluck(self.button_bob,"b"))
        
        self.button_submit = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit.setGeometry(QtCore.QRect(50, 700, 171, 61))
        self.button_submit.setFont(font)
        self.button_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_submit.setObjectName("button_submit")
        self.button_submit.clicked.connect(lambda:self.cluck(self.button_submit,"sub"))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.button_gene.clicked.connect(lambda:self.cluck(self.button_gene,"g"))
        
        self.button_clr = QtWidgets.QPushButton(self.centralwidget)
        self.button_clr.setGeometry(QtCore.QRect(20, 300, 161, 61))
        self.button_clr.setFont(font)
        self.button_clr.setStyleSheet("background-color: rgb(170, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_clr.clicked.connect(self.clear)

        
        #resistor
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(700, 100, 260, 181))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget.setHidden(True)
        self.res_input = QtWidgets.QLineEdit(self.widget)
        self.res_input.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.res_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.res_input.setObjectName("r")
        self.urm_input = QtWidgets.QLineEdit(self.widget)
        self.urm_input.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.urm_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.urm_input.setObjectName("urm")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 41, 20))
        self.label.setFont(font2)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 20))
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setGeometry(QtCore.QRect(220, 30, 41, 20))
        self.label1.setFont(font2)
        self.label1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.label_21 = QtWidgets.QLabel(self.widget)
        self.label_21.setGeometry(QtCore.QRect(220, 70, 71, 20))
        self.label_21.setFont(font2)
        self.label_21.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        
        #generateur        
        self.widget_2 = QtWidgets.QWidget(MainWindow)
        self.widget_2.setGeometry(QtCore.QRect(600, 100, 280, 181))
        self.widget_2.setObjectName("widget")
        self.widget_2.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget_2.setHidden(True)
        self.um_input = QtWidgets.QLineEdit(self.widget_2)
        self.um_input.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.um_input.setStyleSheet("background-color: rgb(0,0,0);color:rgb(255,255,255);")
        self.um_input.setObjectName("um")
        self.n_input = QtWidgets.QLineEdit(self.widget_2)
        self.n_input.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.n_input.setStyleSheet("background-color: rgb(0,0,0);color:rgb(255,255,255);")
        self.n_input.setObjectName("n")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 41, 20))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0,0,0);")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(45, 70, 41, 20))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0,0,0);")
        self.label_31 = QtWidgets.QLabel(self.widget_2)
        self.label_31.setGeometry(QtCore.QRect(220, 30, 41, 20))
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0,0,0);")
        self.label_41 = QtWidgets.QLabel(self.widget_2)
        self.label_41.setGeometry(QtCore.QRect(220, 70, 41, 20))
        self.label_41.setFont(font2)
        self.label_41.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0,0,0);")
        self.fiu = QtWidgets.QLineEdit(self.widget_2)
        self.fiu.setGeometry(QtCore.QRect(90, 110, 113, 22))
        self.fiu.setStyleSheet("background-color: rgb(0,0,0);color:rgb(255,255,255);")
        self.fiu.setObjectName("n")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(32, 110, 40, 20))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0,0,0);")
        self.label_51 = QtWidgets.QLabel(self.widget_2)
        self.label_51.setGeometry(QtCore.QRect(220, 110, 41, 20))
        self.label_51.setFont(font2)
        self.label_51.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0,0,0);")
        
        #condensateur       
        self.widget_3 = QtWidgets.QWidget(MainWindow)
        self.widget_3.setGeometry(QtCore.QRect(550, 100, 280, 181))
        self.widget_3.setObjectName("widget")
        self.widget_3.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget_3.setHidden(True)
        self.ucm_input = QtWidgets.QLineEdit(self.widget_3)
        self.ucm_input.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.ucm_input.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.c_input = QtWidgets.QLineEdit(self.widget_3)
        self.c_input.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.c_input.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.fiuc = QtWidgets.QLineEdit(self.widget_3)
        self.fiuc.setGeometry(QtCore.QRect(90, 110, 113, 22))
        self.fiuc.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(40, 30, 41, 20))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(50, 70, 41, 20))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 50, 20))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_61 = QtWidgets.QLabel(self.widget_3)
        self.label_61.setGeometry(QtCore.QRect(220, 30, 41, 20))
        self.label_61.setFont(font2)
        self.label_61.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_71 = QtWidgets.QLabel(self.widget_3)
        self.label_71.setGeometry(QtCore.QRect(220, 70, 41, 20))
        self.label_71.setFont(font2)
        self.label_71.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_81 = QtWidgets.QLabel(self.widget_3)
        self.label_81.setGeometry(QtCore.QRect(220, 110, 41, 20))
        self.label_81.setFont(font2)
        self.label_81.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        
        #bobine       
        self.widget_4 = QtWidgets.QWidget(MainWindow)
        self.widget_4.setGeometry(QtCore.QRect(550, 100, 280, 181))
        self.widget_4.setObjectName("widget")
        self.widget_4.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget_4.setHidden(True)
        self.ulm_input = QtWidgets.QLineEdit(self.widget_4)
        self.ulm_input.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.ulm_input.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.l_input = QtWidgets.QLineEdit(self.widget_4)
        self.l_input.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.l_input.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.fiul = QtWidgets.QLineEdit(self.widget_4)
        self.fiul.setGeometry(QtCore.QRect(90, 110, 113, 22))
        self.fiul.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.label_9 = QtWidgets.QLabel(self.widget_4)
        self.label_9.setGeometry(QtCore.QRect(40, 30, 41, 20))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setGeometry(QtCore.QRect(50, 70, 41, 20))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_25 = QtWidgets.QLabel(self.widget_4)
        self.label_25.setGeometry(QtCore.QRect(30, 110, 50, 20))
        self.label_25.setFont(font2)
        self.label_25.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_35 = QtWidgets.QLabel(self.widget_4)
        self.label_35.setGeometry(QtCore.QRect(220, 30, 41, 20))
        self.label_35.setFont(font2)
        self.label_35.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_45 = QtWidgets.QLabel(self.widget_4)
        self.label_45.setGeometry(QtCore.QRect(220, 70, 41, 20))
        self.label_45.setFont(font2)
        self.label_45.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_55 = QtWidgets.QLabel(self.widget_4)
        self.label_55.setGeometry(QtCore.QRect(220, 110, 41, 20))
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        
        #circuit     
        self.widget_5 = QtWidgets.QWidget(MainWindow)
        self.widget_5.setGeometry(QtCore.QRect(550, 100, 280, 181))
        self.widget_5.setObjectName("widget")
        self.widget_5.setStyleSheet("background-color: rgba(255, 255, 255,0);")
        self.widget_5.setHidden(True)
        self.z_input = QtWidgets.QLineEdit(self.widget_5)
        self.z_input.setGeometry(QtCore.QRect(90, 30, 113, 22))
        self.z_input.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.im_input = QtWidgets.QLineEdit(self.widget_5)
        self.im_input.setGeometry(QtCore.QRect(90, 70, 113, 22))
        self.im_input.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.fii = QtWidgets.QLineEdit(self.widget_5)
        self.fii.setGeometry(QtCore.QRect(90, 110, 113, 22))
        self.fii.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.p = QtWidgets.QLineEdit(self.widget_5)
        self.p.setGeometry(QtCore.QRect(90, 150, 113, 22))
        self.p.setStyleSheet("background-color: rgba(255,255,255,0);\n"
                                     "color:rgb(255,255,255);")
        self.label_122 = QtWidgets.QLabel(self.widget_5)
        self.label_122.setGeometry(QtCore.QRect(55, 30, 41, 20))
        self.label_122.setFont(font2)
        self.label_122.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_133 = QtWidgets.QLabel(self.widget_5)
        self.label_133.setGeometry(QtCore.QRect(50, 70, 41, 20))
        self.label_133.setFont(font2)
        self.label_133.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_144 = QtWidgets.QLabel(self.widget_5)
        self.label_144.setGeometry(QtCore.QRect(45, 110, 50, 20))
        self.label_144.setFont(font2)
        self.label_144.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_155 = QtWidgets.QLabel(self.widget_5)
        self.label_155.setGeometry(QtCore.QRect(220, 30, 41, 20))
        self.label_155.setFont(font2)
        self.label_155.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_166 = QtWidgets.QLabel(self.widget_5)
        self.label_166.setGeometry(QtCore.QRect(220, 70, 41, 20))
        self.label_166.setFont(font2)
        self.label_166.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_177 = QtWidgets.QLabel(self.widget_5)
        self.label_177.setGeometry(QtCore.QRect(220, 110, 41, 20))
        self.label_177.setFont(font2)
        self.label_177.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_188 = QtWidgets.QLabel(self.widget_5)
        self.label_188.setGeometry(QtCore.QRect(55, 150, 41, 20))
        self.label_188.setFont(font2)
        self.label_188.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        self.label_199 = QtWidgets.QLabel(self.widget_5)
        self.label_199.setGeometry(QtCore.QRect(220, 150, 41, 20))
        self.label_199.setFont(font2)
        self.label_199.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);")
        
        
        self.textBrowser = QtWidgets.QTextBrowser(MainWindow)
        self.textBrowser.setGeometry(QtCore.QRect(700, 300, 450, 500))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255,255,255);border-color:rgba(255,255,255,0);")
        self.textBrowser.setFont(font)
        
        self.textBrowser.setHidden(True)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        text1="Générateur"
        text2="Résistor"
        self.button_gene.setText(_translate("MainWindow", text1))
        self.button_res.setText(text2)
        self.button_con.setText("Condensateur")
        self.button_circuit.setText(_translate("MainWindow", "Circuit"))
        self.button_bob.setText(_translate("MainWindow", "Bobine"))
        self.button_submit.setText(_translate("MainWindow", "Soummettre"))
        self.button_clr.setText("Effacer")
        
        text3="Ω"
        self.label.setText("R+r")
        self.label_2.setText("(R+r)Im")
        self.label1.setText(text3)
        self.label_21.setText("V")
        
        self.label_3.setText("Um")
        self.label_4.setText("N")
        self.label_5.setText("phi U")
        self.label_31.setText("V")
        self.label_41.setText("Hz")
        self.label_51.setText("rad")
        
        self.label_6.setText("UCm")
        self.label_7.setText("C")
        self.label_8.setText("phi UC")
        self.label_61.setText("V")
        self.label_71.setText("µF")
        self.label_81.setText("rad")
        
        self.label_9.setText("ULm")
        self.label_15.setText("L")
        self.label_25.setText("phi UL")
        self.label_35.setText("V")
        self.label_45.setText("H")
        self.label_55.setText("rad")
        
        self.label_122.setText("Z")
        self.label_133.setText("Im")
        self.label_144.setText("phi i")
        self.label_155.setText("Ω")
        self.label_166.setText("A")
        self.label_177.setText("rad")
        self.label_188.setText("P")
        self.label_199.setText("W")

    def cluck(self,instance,name):
        img=Ui_MainWindow.photos[name]
        self.backphoto.setPixmap(QtGui.QPixmap(img))
        self.backphoto.setScaledContents(True)
        self.backphoto.autoFillBackground()
        instance.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "color: rgb(255, 198, 24);")
        if name == "r":
            self.widget.setHidden(False)
            self.widget_2.setHidden(True)
            self.widget_3.setHidden(True)
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)
            self.textBrowser.setHidden(True)
            
            self.button_con.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_gene.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_bob.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_circuit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        if name == "g":
            self.widget.setHidden(True)
            self.widget_2.setHidden(False)
            self.widget_3.setHidden(True)
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)
            self.textBrowser.setHidden(True)
            
            self.button_con.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_res.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_bob.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_circuit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        if name == "c":
            self.widget.setHidden(True)
            self.widget_2.setHidden(True)
            self.widget_3.setHidden(False)
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)
            self.textBrowser.setHidden(True)
            
            self.button_gene.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_res.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_bob.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_circuit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        if name == "b":
            self.widget.setHidden(True)
            self.widget_2.setHidden(True)
            self.widget_3.setHidden(True)
            self.widget_4.setHidden(False)
            self.widget_5.setHidden(True)
            self.textBrowser.setHidden(True)
            
            self.button_gene.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_res.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_con.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_circuit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        if name == "cir":
            self.widget.setHidden(True)
            self.widget_2.setHidden(True)
            self.widget_3.setHidden(True)
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(False)
            self.textBrowser.setHidden(True)
            
            self.button_gene.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_res.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_con.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_bob.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        
        if name == "sub":
            self.widget.setHidden(True)
            self.widget_2.setHidden(True)
            self.widget_3.setHidden(True)
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)
            self.textBrowser.setHidden(False)
            
            self.button_gene.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_res.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_con.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_bob.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            self.button_circuit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
            
            self.brain()
            
    def brain(self):
            global z,r,l,w,c,p,um,im,delta,ulm,ucm,urm
            tempfii=None
            if self.fiuc.text() != "":
                tempfii=float(self.fiuc.text())+pi/2
            if self.fiul.text() != "":
                tempfii=float(self.fiul.text())-pi/2
            if self.fii.text() != "":
                tempfii=float(self.fii.text())
            if tempfii is not None and self.fiu.text() != "":
                delta = tempfii - float(self.fiu.text())
            if self.z_input.text() != "":
                z=float(self.z_input.text())
            if self.z_input.text() != "":
                z=float(self.z_input.text())
            if self.res_input.text() != "":
                r=float(self.res_input.text())
            if self.l_input.text() != "":
                l=float(self.l_input.text())
            if self.n_input.text() != "":
                w=2*pi*float(self.n_input.text())
            if self.c_input.text() != "":
                c=float(self.c_input.text())*10**-6
            if self.p.text() != "":
                p=float(self.p.text())
            if self.um_input.text() != "":
                um=float(self.um_input.text())
            if self.im_input.text() != "":
                im=float(self.im_input.text())
            if self.ulm_input.text() != "":
                ulm=float(self.ulm_input.text())
            if self.ucm_input.text() != "":
                ucm=float(self.ucm_input.text())
            if self.urm_input.text() != "":
                urm=float(self.urm_input.text())
            
            #╥print(z,r,l,w,c,p,um,im,delta,ulm,ucm,urm)
            
            x=0
            while x<10:
                if z is None : impedance()
                if r is None : restot()
                if l is None : inductance()
                if w is None : omega()
                if c is None : capacite()
                if p is None : puissance()
                if um is None : tension()
                if im is None : intensite()
                if delta is None : deltafind()
                if ulm is None : tension_bobine()
                if ucm is None : tension_con()
                if urm is None : tension_res()
                x+=1
        
    
            broken=any(i is None for i in [z,r,l,w,c,p,um,im,delta,ulm,ucm,urm])

            rads={pi/3:"π/3",
                  pi/4:"π/4",
                  pi/5:"π/5",
                  2*pi/5:"2π/5",
                  pi/6:"π/6",
                  pi/7:"π/7",
                  2*pi/7:"2π/7",
                  3*pi/7:"3π/7",
                  pi/8:"π/8",
                  3*pi/8:"3π/8",
                  pi/10:"π/10",
                  3*pi/10:"3π/10",
                  pi/12:"π/12",
                  5*pi/12:"5π/12",}
            
            if not broken :
                rawdelta=min(rads, key=lambda x:abs(x-delta))
                if rawdelta-delta>0.01:
                    formatteddelta=str(delta)
                else:
                    formatteddelta = rads[rawdelta]
                if ucm<ulm:
                    formatteddelta ="- "+formatteddelta
                self.textBrowser.setText(f"Z = {z} Ω\nR+r = {r} Ω\nL = {l} H\nw = {w}\nC = {c*10**6} µF\nP = {p} W\nUm = {um} V\nIm = {im} A\nphi i - phi u = {formatteddelta} rad\nULm = {ulm} V\nUCm = {ucm} V\n(R+r)Im = {urm} V")
            else:
                self.textBrowser.setText("insufficient information")
            
    def clear(self):
        self.z_input.setText("")
        self.res_input.setText("")
        self.l_input.setText("")
        self.n_input.setText("")
        self.c_input.setText("")
        self.p.setText("")
        self.um_input.setText("")
        self.im_input.setText("")
        self.ulm_input.setText("")
        self.ucm_input.setText("")
        self.urm_input.setText("")
        self.fii.setText("")
        self.fiul.setText("")
        self.fiuc.setText("")
        self.fiu.setText("")
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
