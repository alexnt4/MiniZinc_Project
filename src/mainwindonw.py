import re
import string
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from minizinc import Instance, Model, Solver


class Ui_Dialog(object):
    def __init__(self, parent=None):
        self.mzn_model = Model('./model2.mzn')
        self.solver = Solver.lookup("gecode")
        self.mzn_instance = None
    
    def setupScene(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.pen = QtGui.QPen(QtCore.Qt.gray)
        self.redPen = QtGui.QPen(QtCore.Qt.red)
        self.greenBrush = QtGui.QBrush(QtCore.Qt.green)
        self.redBrush = QtGui.QBrush(QtCore.Qt.red)
        self.graphicsView.setScene(self.scene)
        self.scale = 50 # scale of pixels to draw everything
        self.padding_y = 50 # space to move y pixels


    def drawPlane(self):
        self.scene.clear()
        matriz = self.mzn_instance._data["tamano_matriz"]
        n_ciudades = self.mzn_instance._data["num_posiciones_existentes"]
        ciudades = self.mzn_instance._data["ciudades"]
        self.max_x = matriz*self.scale
        self.max_y = matriz*self.scale

        # draw vertical lines
        for item in range(matriz+1):
            self.scene.addLine(item*self.scale, self.padding_y, item*self.scale, self.max_y+self.padding_y, self.pen)
        # draw horizontal lines
        for item in range(matriz+1):  
            self.scene.addLine(0, item*self.scale+self.padding_y, self.max_x, item*self.scale+self.padding_y, self.pen)
        # draw cities
        for item in range(n_ciudades):
            ciudad_x = ciudades[item][0] * self.scale - 5
            ciudad_y = ciudades[item][1] * self.scale + self.padding_y - 5
            self.scene.addEllipse(QtCore.QRectF(ciudad_x, ciudad_y, 10, 10), self.pen, self.greenBrush)

    def drawSolution(self):
        self.ubicaciones = self.result["ubicaciones"]  # Matriz con las ubicaciones
        matriz = self.mzn_instance._data["tamano_matriz"]

        self.max_x = matriz * self.scale
        self.max_y = matriz * self.scale


        base = self.mzn_instance._data["ciudades"]

        # Limpia la escena antes de dibujar
        self.scene.clear()

        # Dibuja las líneas verticales
        for item in range(matriz + 1):
            self.scene.addLine(
                item * self.scale, self.padding_y, 
                item * self.scale, self.max_y + self.padding_y, 
                self.pen
            )
        # Dibuja las líneas horizontales
        for item in range(matriz + 1):
            self.scene.addLine(
                0, item * self.scale + self.padding_y, 
                self.max_x, item * self.scale + self.padding_y, 
                self.pen
            )

        # Coordenadas excluyendo las de base
        base_coords = [(c[1], c[0]) for c in base]  # Ajusta las coordenadas de 'ciudades' a formato (y, x)
        filtered_coords = []  # Lista para almacenar 

        for y in range(len(self.ubicaciones)):  # Recorre las filas de la matriz
            for x in range(len(self.ubicaciones[y])):  # Recorre las columnas de la fila
                if self.ubicaciones[y][x] == 1:  # Si el valor es 1
                # Corrige la posición sumando 1 para ajustar el desfase
                    corrected_x = x + 1
                    corrected_y = y  + 1

                    if (corrected_y, corrected_x) not in base_coords:
                        filtered_coords.append((corrected_x, corrected_y))

                    #print(f"Encontrado 1 en coordenada: ({corrected_x}, {corrected_y})")

                    # Calcula la posición del círculo rojo en la escena
                    circle_x = corrected_x * self.scale - 5
                    circle_y = corrected_y * self.scale + self.padding_y - 5

                    # Dibuja el círculo rojo en la escena
                    self.scene.addEllipse(
                    QtCore.QRectF(circle_x, circle_y, 10, 10),
                    self.pen,
                    self.redBrush
                )
        #print(f"Coordenadas excluyendo base: {filtered_coords}")

        #labelsResults
        obje = str(self.result.objective)  # Convertir a string
        
        result_str = str(self.result)  # Convierte el objeto a string si no lo es ya
        for line in result_str.split("\n"):  # Divide en líneas
            if "ganancia_ciudades:" in line:  # Busca la línea que contiene "ganancia_ciudades"
                ganancia_ciudades = int(line.split(":")[1].strip())  # Extrae y convierte el valor
                break

        ress = str(ganancia_ciudades)

        
        basss = str(base)

        coor = str(filtered_coords)
        
        text = (f"ganancia sin incluir nuevas localizaciones {ress}\n")
        text += (f"ganancia con nuevas ubicaciones {obje}\n")     # Asignar el texto al QLabel
        text += (f"coordenadas localizaciones predeterminadas {basss}\n")
        text += (f"coordenadas de las nuevas localizaciones {coor}\n")
        self.labelResult.setText(text)





        


        


    def buttonFileClicked(self):
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "Dzn Files (*.dzn)", options=options)
        if filename:
            self.mzn_instance = Instance(self.solver, self.mzn_model)
            self.mzn_instance.add_file(filename, True)
            #print(f"Contenido de mzn_instance después de agregar el archivo: {self.mzn_instance._data["num_posiciones_existentes"]}")
            self.labelFile.setText(filename)
            self.drawPlane()

    def selectSolver(self):
        self.solver = Solver.lookup(self.comboBox.itemText(self.comboBox.currentIndex()))

    def buttonSolverClicked(self):
        if (self.mzn_instance is None):
            return
        self.labelData.setText('Resolviendo el modelo...')
        start_time = time.time()
        self.result = self.mzn_instance.solve()
        #self.solution = self.mzn_instance.result
        duration = time.time() - start_time
        if (self.result):
            self.labelData.setText(f"Modelo Resuleto! Duración: {duration} segundos")
            #print(self.result)
            #print(self.result["gananciaciudades"])
            #objective = self.result.objective
            #print("Objective:", objective)
            #print(self.solution)
            self.drawSolution()
            #print(self.result["gananciatotal"])
            #self.labelResult.setText(res)
        else:
            self.labelData.setText(f"No hay solución para el modelo. Tiempo de ejecución: {duration}")


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 800)
        Dialog.setWindowIcon(QtGui.QIcon("relleno-sanitario.png"))

        # Ajuste principal con margen global
        self.mainLayout = QtWidgets.QVBoxLayout(Dialog)
        self.mainLayout.setContentsMargins(10, 10, 10, 10)  # Márgenes exteriores (izq, sup, der, inf)
        self.mainLayout.setSpacing(15)  # Espaciado entre widgets principales

        # Fila 1: Label Message
        self.labelMessage = QtWidgets.QLabel(Dialog)
        self.labelMessage.setObjectName("labelMessage")
        self.labelMessage.setAlignment(QtCore.Qt.AlignLeft)  # Alinear el texto a la izquierda
        self.mainLayout.addWidget(self.labelMessage)

        # Fila 2: Botones y ComboBox
        self.row2Layout = QtWidgets.QHBoxLayout()
        self.row2Layout.setSpacing(10)  # Espaciado entre widgets en la fila
        self.pushButtonFile = QtWidgets.QPushButton(Dialog)
        self.pushButtonFile.setObjectName("pushButtonFile")
        self.row2Layout.addWidget(self.pushButtonFile)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["gecode", "chuffed", "coin-bc"])
        self.row2Layout.addWidget(self.comboBox)

        self.pushButtonSolver = QtWidgets.QPushButton(Dialog)
        self.pushButtonSolver.setObjectName("pushButtonSolver")
        self.row2Layout.addWidget(self.pushButtonSolver)

        self.mainLayout.addLayout(self.row2Layout)

        # Fila 3: Información del archivo y datos
        self.labelFile = QtWidgets.QLabel(Dialog)
        self.labelFile.setObjectName("labelFile")
        self.mainLayout.addWidget(self.labelFile)

        self.labelData = QtWidgets.QLabel(Dialog)
        self.labelData.setObjectName("labelData")
        self.mainLayout.addWidget(self.labelData)

        self.labelResult = QtWidgets.QLabel(Dialog)
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setWordWrap(True)  # Permitir que el texto sea multilinea
        self.mainLayout.addWidget(self.labelResult)

        # Vista gráfica
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.setMinimumHeight(300)
        self.mainLayout.addWidget(self.graphicsView)

        # Retraducir y conectar
        self.retranslateUi(Dialog)
        self.pushButtonFile.clicked.connect(self.buttonFileClicked)
        self.comboBox.currentIndexChanged.connect(self.selectSolver)
        self.pushButtonSolver.clicked.connect(self.buttonSolverClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.setupScene()

    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sedes Ingenieria"))
        self.pushButtonFile.setText(_translate("Dialog", "Seleccionar archivo dzn"))
        self.pushButtonSolver.setText(_translate("Dialog", "Resolver"))
        self.labelMessage.setText(_translate("Dialog", "Seleccione un archivo de datos para empezar. El solver por defecto es Gecode"))
        self.labelData.setText(_translate("Dialog", "Esperando datos..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
