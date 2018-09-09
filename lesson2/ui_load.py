from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout


class AgeWidget(QWidget):

    def __init__(self):
        super().__init__()

        # initialisation of PyQt objects
        self.string1_line_edit = QLineEdit()
        self.string2_line_edit = QLineEdit()
        self.age_check_button = QPushButton('Check age')
        self.string_check_button = QPushButton('Check strings')
        self.status_age_line = QLineEdit()
        self.status_strings_line = QLineEdit()

        # calling a function for setting properties of the layouts
        self.init_ui()

    def init_ui(self):
        # main layout
        v_layout = QVBoxLayout()

        # three horizontal layouts
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h3_layout = QHBoxLayout()

        # setting layouts
        h1_layout.addWidget(self.string1_line_edit)
        h1_layout.addWidget(self.string2_line_edit)

        h2_layout.addWidget(self.age_check_button)
        h2_layout.addWidget(self.string_check_button)

        h3_layout.addWidget(self.status_age_line)
        h3_layout.addWidget(self.status_strings_line)

        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        v_layout.addLayout(h3_layout)

        self.status_age_line.setReadOnly(True)

        self.age_check_button.clicked.connect(self.check_age)
        self.string_check_button.clicked.connect(self.strings_check)

        self.setLayout(v_layout)
        self.setWindowTitle('Occupation prediction based on age check')
        self.setFixedWidth(600)

        self.show()


    def strings_check(self):
        string1 = self.string1_line_edit.text()
        string2 = self.string2_line_edit.text()

        if not isinstance(string1, str) and not isinstance(string2, str):
            # actually this will never happen with the outcome from LineEdit
            self.status_strings_line.setText('This will never happen!')
        elif string1 == string2:
            self.status_strings_line.setText('your strings are equal, so it\'s 2' )
        elif string2 == 'learn':
            self.status_strings_line.setText('learn is the second word, so it\'s 3')


    def check_age(self):
        age = int(self.string1_line_edit.text())
        age_message_tuple = ({'age':   7, 'message': 'Where are your parents kid?'},
                             {'age':  16, 'message': 'Why aren\'t you in school?'},
                             {'age':  23, 'message': 'Don\'t miss lectures you\'ll need them further?'},
                             {'age':  65, 'message': 'Do you have a sick leave?'},
                             {'age': 100, 'message': 'You can rest!'},
                             {'age':  -1, 'message': 'Your age is incorrect'})
        for i in range(len(age_message_tuple)):
            if age > age_message_tuple[i]['age'] and i < len(age_message_tuple)-1:
                continue

            message = age_message_tuple[i]['message']
            break

        self.status_age_line.setText(message)