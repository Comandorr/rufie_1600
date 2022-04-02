# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit
from time import *
from instr import *

app = QApplication([])
window = QWidget()
window.show()

# ВИДЖЕТЫ ПЕРВОГО ЭКРАНА
label_start_1 = QLabel('Добро пожаловать!')
label_start_2 = QLabel(start_instr)
knopka_start = QPushButton('Начать тест')
ekran_1 = [label_start_1, label_start_2, knopka_start]

# ВИДЖЕТЫ ВТОРОГО ЭКРАНА
label_info_1 = QLabel('Введите возраст:')
edit_age = QLineEdit()

label_info_2 = QLabel('Лягте и замерьте пульс за 15 секунд. После введите результат')
knopka_timer_1 = QPushButton('Запустить таймер (15 сек)')
edit_pulse_1 = QLineEdit()

label_info_3 = QLabel('Выполните 30 приседаний за 45 секунд')
knopka_timer_2 = QPushButton('Запустить таймер (45 сек)')

label_info_4 = QLabel(final_instr)
knopka_timer_3 = QPushButton('Запустить таймер (1 мин)')
edit_pulse_2 = QLineEdit()
edit_pulse_3 = QLineEdit()

knopka_finish = QPushButton('Отправить результаты')
ekran_2 = [label_info_1, edit_age,
label_info_2, knopka_timer_1, edit_pulse_1,
label_info_3, knopka_timer_2,
label_info_4, knopka_timer_3, edit_pulse_2, edit_pulse_3,
knopka_finish]

line_1 = QVBoxLayout()
line_1.addWidget(label_start_1)
line_1.addWidget(label_start_2)
line_1.addWidget(knopka_start)
for w in ekran_2:
    line_1.addWidget(w)
    w.hide()

def start():
    for w in ekran_1:
        w.hide()
    for w in ekran_2:
        w.show()
knopka_start.clicked.connect(start)

window.setLayout(line_1)
app.exec_()