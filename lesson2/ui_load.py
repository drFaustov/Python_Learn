from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QGroupBox
import winsound

class AgeWidget(QWidget):

    def __init__(self):
        super().__init__()

        # initialisation of PyQt objects
        self.string1_line_edit = QLineEdit('')
        self.string2_line_edit = QLineEdit('')
        self.age_check_button = QPushButton('Check age')
        self.string_check_button = QPushButton('Check strings')
        self.status_age_line = QLineEdit('')
        self.status_strings_line = QLineEdit('')
        self.if_clause_task_group = QGroupBox('if clause home work')

        self.chat_line_edit = QLineEdit('')
        self.chat_button = QPushButton('Send your phrase')
        self.chat_text_edit = QTextEdit()
        self.chat_group = QGroupBox('chat task')

        # Chat setting for hello
        self.chat_hello = False

        # calling a function for setting properties of the layouts
        self.init_ui()

    def init_ui(self):

        # main layout
        v1_layout = QVBoxLayout()
        v2_layout = QVBoxLayout()
        v3_layout = QVBoxLayout()

        # three horizontal layouts
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h3_layout = QHBoxLayout()

        # setting the if clause task layout
        h1_layout.addWidget(self.string1_line_edit)
        h1_layout.addWidget(self.string2_line_edit)

        h2_layout.addWidget(self.age_check_button)
        h2_layout.addWidget(self.string_check_button)

        h3_layout.addWidget(self.status_age_line)
        h3_layout.addWidget(self.status_strings_line)

        v2_layout.addLayout(h1_layout)
        v2_layout.addLayout(h2_layout)
        v2_layout.addLayout(h3_layout)

        self.status_age_line.setReadOnly(True)
        self.string1_line_edit.setPlaceholderText('Enter your age or a string to check')
        self.string2_line_edit.setPlaceholderText('Enter a second string to check')
        self.status_age_line.setPlaceholderText('Result of the age estimation')
        self.status_strings_line.setPlaceholderText('Result of string comparison')

        self.age_check_button.clicked.connect(self.check_age)
        self.string_check_button.clicked.connect(self.strings_check)

        # Setting the chat task layout
        v3_layout.addWidget(self.chat_line_edit)
        v3_layout.addWidget(self.chat_button)
        v3_layout.addWidget(self.chat_text_edit)

        self.chat_line_edit.setPlaceholderText('Enter something to chat')

        # Adding layouts to groups
        self.if_clause_task_group.setLayout(v2_layout)
        self.chat_group.setLayout(v3_layout)

        # Main widget layout
        v1_layout.addWidget(self.if_clause_task_group)
        v1_layout.addWidget(self.chat_group)

        self.chat_button.clicked.connect(self.chat_button_pressed)

        # Setting the main layout
        self.setLayout(v1_layout)
        self.setWindowTitle('Lesson 2 homework')
        self.setFixedWidth(600)

        self.show()

    def chat_button_pressed(self):
        phrase = self.chat_line_edit.text()
        self.chat_line_edit.setText(None)
        self.chat_text_edit.append('User: ' + phrase)
        phrase_dict = dict({'Hello'    : 'Hello, let\'s talk!',
                            'Sure'     : 'Great, how r u doing?',
                            'All good' : 'Great, I am doing good as well!',
                            'Buy'      : 'It was nice to talk to you! See you!'})

        error_phrase_dict = dict({'0'   : 'I would\'ve say hello first!',
                                  '-1'  : 'Wrong answer, beep, beep ... '})

        if not self.chat_hello and phrase != 'Hello':
            self.chat_text_edit.append('Computer: ' + error_phrase_dict['0'])
        elif phrase in phrase_dict:
            self.chat_text_edit.append('Computer: ' + phrase_dict[phrase])
            if phrase == 'Hello': self.chat_hello = True
        else:
            self.chat_text_edit.append('Computer: ' + error_phrase_dict['-1'])
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)

    def strings_check(self):
        string1 = self.string1_line_edit.text()
        string2 = self.string2_line_edit.text()

        if not isinstance(string1, str) and not isinstance(string2, str):
            # actually this will never happen with the outcome from LineEdit
            self.status_strings_line.setText('This will never happen!')
        elif string1 == string2:
            self.status_strings_line.setText('your strings are equal, so it\'s 2')
        elif string2 == 'learn':
            self.status_strings_line.setText('learn is the second word, so it\'s 3')

    def check_age(self):
        # TODO: Make a check for a number
        age = int(self.string1_line_edit.text())
        age_message_tuple = ({'age':   7, 'message': 'Where are your parents kid?'},
                             {'age':  16, 'message': 'Why aren\'t you in school?'},
                             {'age':  23, 'message': 'Don\'t miss lectures you\'ll need them further?'},
                             {'age':  65, 'message': 'Do you have a sick leave?'},
                             {'age': 100, 'message': 'You can rest!'},
                             {'age':  -1, 'message': 'Your age is incorrect'})

        for age_from_tuple in age_message_tuple:
            if age_from_tuple['age'] < age and age_from_tuple['age'] != -1:
                continue

            message = age_from_tuple['message']
            break

        self.status_age_line.setText(message)