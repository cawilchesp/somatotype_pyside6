"""
PySide6 Text Field component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

from components.style_color import colors

import sys

# ----------
# Text Field
# ----------
class MD3TextField(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Text Field

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Text field position
                (x, y) -> x, y: upper left corner
            width: int
                Text field width
            type: str (optional, any character allowed if not specified)
                Text field type
                    text: only letters and accents
                    integer: only integer numbers
                    double: allow decimal point
                    weight: double values from 0.00 to 999.99
                    height_si: double values from 0.00 to 2.99
                    height_us: number in format [ft]'[in]" (ex. 5'12")
                    email: text in email format
                    ip: numbers in ip format (0.0.0.0 - 255.255.255.255)
                    password: any character with visible/hidden icon
            size: int
                Text field size
            labels: tuple
                Text field text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            enabled: bool
                Text field enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
            return_pressed: def
                Text field 'return pressed' method name
            text_edited: def
                Text field 'text edited' method name
            text_changed: def
                Text field 'text changed' method name
        
        Returns
        -------
        None
        """
        super(MD3TextField, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 96
        self.setGeometry(x, y, w, 52)

        self.text_field = QtWidgets.QLineEdit(self)
        self.text_field.setGeometry(0, 8, w, 44)
        self.text_field.setClearButtonEnabled(True)

        patterns_dict = {
            'text': r"[\p{L}\s]+",
            'integer': r'[+-]?\d+',
            'double': r'[+-]?\d+\.\d+',
            'weight': r'([0-9]\d{0,2})\.(\d{1,2})',
            'height_si': r'[0-3]\.(\d{1,2})',
            'height_us': r'[0-9]\'([0-9]|10|11|12)\"',
            'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            'ip': r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        }

        if 'type' in attributes:
            if attributes['type'] in patterns_dict:
                pattern = patterns_dict[attributes['type']]
                reg_exp = QRegularExpressionValidator(QRegularExpression(f'{pattern}'))
                self.text_field.setValidator(reg_exp)

            if attributes['type'] == 'password':
                icon_theme = 'L' if attributes['theme'] else 'D'
                current_path = sys.path[0].replace("\\","/")
                images_path = f'{current_path}/icons'
                self.visible_icon = QtGui.QIcon(f'{images_path}/eye_{icon_theme}.png')
                self.hidden_icon = QtGui.QIcon(f'{images_path}/eye_off_{icon_theme}.png')
                                
                self.text_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
                self.toggle_password = self.text_field.addAction(self.visible_icon, QtWidgets.QLineEdit.ActionPosition.TrailingPosition)
                self.toggle_password.triggered.connect(self.password_action)
                self.toggle_password_state = False

        if 'size' in attributes:
            self.text_field.setMaxLength(attributes['size'])

        self.label_field = QtWidgets.QLabel(self)
        self.label_field.setGeometry(8, 0, 16, 16)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])

        if 'return_pressed' in attributes:
            self.text_field.returnPressed.connect(attributes['return_pressed'])
        if 'text_edited' in attributes:
            self.text_field.textEdited.connect(attributes['text_edited'])
        if 'text_changed' in attributes:
            self.text_field.textChanged.connect(attributes['text_changed'])
            

    def password_action(self) -> None:
        if not self.toggle_password_state:
            self.text_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
            self.toggle_password_state = True
            self.toggle_password.setIcon(self.hidden_icon)
        else:
            self.text_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
            self.toggle_password_state = False
            self.toggle_password.setIcon(self.visible_icon)


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_surface')

        disabled_background_color = colors(theme, 'disable')
        disabled_color = colors(theme, 'on_disable')
            
        self.setStyleSheet(f'QFrame {{ '
                f'border: 0px solid; '
                f'border-radius: 4; '
                f'background-color: {background_color} }}'
                f'QFrame:!enabled {{ '
                f'background-color: {disabled_background_color};'
                f'color: {disabled_color}'
                f'}}'

                f'QLineEdit {{ '
                f'border: 1px solid {color}; '
                f'border-radius: 4;'
                f'padding: 0 8 0 8; '
                f'background-color: {background_color}; '
                f'color: {color} }}'
                f'QLineEdit:!enabled {{ '
                f'border: 1px solid {disabled_color}; '
                f'background-color: {disabled_background_color};'
                f'color: {disabled_color}'
                f'}}'

                f'QLabel {{ '
                f'border: 0px solid; '
                f'padding: 0 4 0 4;'
                f'background-color: {background_color}; '
                f'color: {color} }}')


    def setLanguage(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.attributes['labels'][0])
        elif language == 1: self.label_field.setText(self.attributes['labels'][1])
        self.label_field.adjustSize()