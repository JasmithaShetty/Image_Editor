#import modules
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

#




#settings
app = QApplication([])
main_window=QWidget()
main_window.setWindowTitle('PhotoQt')
main_window.resize(950,750)

#widgets
btn_folder = QPushButton('Folder')
file_list = QListWidget()

btn_left = QPushButton('Left')
btn_right = QPushButton('Right')
mirror = QPushButton('Mirror')
sharpness = QPushButton('Sharpness')
gray = QPushButton('B/W')
saturation = QPushButton('Saturation')
contrast = QPushButton('Contrast')
blur = QPushButton('Blur')

#Box
filter_box = QComboBox()
filter_box.addItem('Original')
filter_box.addItem('Left')
filter_box.addItem('Right')
filter_box.addItem('Mirror')
filter_box.addItem('Sharpness')
filter_box.addItem('B/W')
filter_box.addItem('Saturation')
filter_box.addItem('Contrast')
filter_box.addItem('Blur')

picture_box = QLabel("Image Apperas here")

#design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

col2.addWidget(picture_box)

master_layout.addLayout(col1)#, 30)
master_layout.addLayout(col2)#,90)

main_window.setLayout(master_layout)


main_window.show()
app.exec_() #or app.exec()