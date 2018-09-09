from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout


class AgeWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.line_edit = QLineEdit()
        self.check_button = QPushButton('Check age')
        self.status_line = QLineEdit()

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()

        v_layout.addWidget(self.line_edit)
        v_layout.addWidget(self.check_button)
        v_layout.addWidget(self.status_line)

        self.status_line.setReadOnly(True)

        self.check_button.clicked.connect(self.check_age)

        self.setLayout(v_layout)
        self.setWindowTitle('Occupation prediction based on age check')
        self.setFixedWidth(600)

        self.show()

    def check_age(self):
        age = int(self.line_edit.text())
        age_message_tuple = ({'age':   7, 'message': "Where are your parents kid?"},
                             {'age':  16, 'message': "Why aren't you in school?"},
                             {'age':  23, 'message': "Don't miss lectures you'll need them further?"},
                             {'age':  65, 'message': "Do you have a sick leave?"},
                             {'age': 100, 'message': "You can rest!"},
                             {'age':  -1, 'message': "Your age is incorrect"})
        for i in range(len(age_message_tuple)):
            if age > age_message_tuple[i]['age'] and i < len(age_message_tuple)-1:
                continue

            message = age_message_tuple[i]['message']
            break

        self.status_line.setText(message)