from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QSpinBox, QRadioButton, QGroupBox, QButtonGroup, QHBoxLayout, QVBoxLayout

card_win = QWidget()
card_win.resize(550, 450)

btn_menu = QPushButton("меню")
btn_sleep = QPushButton("відпочинок")

box_min = QSpinBox()
box_min.setValue(30)
lbl_min = QLabel("хвилинка")

rbtn1 = QRadioButton("")
rbtn2 = QRadioButton("")
rbtn3 = QRadioButton("")
rbtn4 = QRadioButton("")

RadioGroupBox = QGroupBox("Варіанти відповіди")
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

AnsGroupBox = QGroupBox("результат тесту")
lbl_result = QLabel("")
lbl_correct = QLabel("")

line_rbtn1 = QHBoxLayout()
line_rbtn2 = QHBoxLayout()
line_main = QVBoxLayout()

line_rbtn1.addWidget(rbtn1)
line_rbtn1.addWidget(rbtn2)
line_rbtn2.addWidget(rbtn3)
line_rbtn2.addWidget(rbtn4)

line_main.addLayout(line_rbtn1)
line_main.addLayout(line_rbtn2)

RadioGroupBox.setLayout(line_main)

line_ans = QVBoxLayout()
line_ans.addWidget(lbl_result, alignment=(Qt.AlignLeft|Qt.AlignTop))
line_ans.addWidget(lbl_correct, alignment=Qt.AlignCenter)

line1 = QHBoxLayout()
line1.addWidget(btn_menu)
line1.addStretch(2)
line1.addWidget(btn_sleep)
line1.addWidget(box_min)
line1.addWidget(lbl_min)

line2 = QHBoxLayout()
line3= QHBoxLayout()
line4 = QHBoxLayout()

lbl_question = QLabel("")

line2.addWidget(lbl_question, alignment=(Qt.AlignHCenter|Qt.AlignVCenter))

line3.addWidget(RadioGroupBox)
line3.addWidget(AnsGroupBox)

btn_ok = QPushButton("Відповісти")

line4.addStretch(1)
line4.addWidget(btn_ok, stretch=2)
line4.addStretch(1)

card_layout = QVBoxLayout()

card_layout.addLayout(line1, stretch=1)
card_layout.addLayout(line2, stretch=4)
card_layout.addLayout(line3, stretch=8)
card_layout.addLayout(line4)



card_win.setLayout(card_layout)