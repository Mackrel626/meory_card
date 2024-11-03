from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

main_win = QWidget()

lbl_quest = QLabel('Введіть запитання')
lbl_right_ans = QLabel('Введіть правильну відповідь')
lbl_wrong_ans1 = QLabel('Введіть першу хибну відповідь')
lbl_wrong_ans2 = QLabel('Введіть другу хибну відповідь')
lbl_wrong_ans3 = QLabel('Введіть трету хибну відповідь')


le_quest = QLineEdit()
le_ringht_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

btn_add_quest = QPushButton("Додати запитання")
btn_clear = QPushButton("Очистити")

lbl_statistics = QLabel("Статистика")
lbl_statistics.setStyleSheet('font-size: 20px; font-weight: bold;')

lbl_stat = QLabel()

btn_back = QPushButton("Назад")

v1 = QVBoxLayout()
v2 = QVBoxLayout()

v1.addWidget(lbl_quest)
v1.addWidget(lbl_right_ans)
v1.addWidget(lbl_wrong_ans1)
v1.addWidget(lbl_wrong_ans2)
v1.addWidget(lbl_wrong_ans3)

v2.addWidget(le_quest)
v2.addWidget(le_ringht_ans)
v2.addWidget(le_wrong_ans1)
v2.addWidget(le_wrong_ans2)
v2.addWidget(le_wrong_ans3)

h1 = QHBoxLayout()
h1.addLayout(v1)
h1.addLayout(v2)

h2 = QHBoxLayout()
h2.addWidget(btn_add_quest)
h2.addWidget(btn_clear)

main_lain = QVBoxLayout()
main_lain.addLayout(h1)
main_lain.addLayout(h2)
main_lain.addWidget(lbl_statistics)
main_lain.addWidget(lbl_stat)
main_lain.addWidget(btn_back)

main_win.setLayout(main_lain)
main_win.resize(400, 300)
