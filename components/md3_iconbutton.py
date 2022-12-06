"""
PyQt Icon Button component adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt

import sys


light = {
    'background': '#3785F5',
    'on_background': '#000000',
    'surface': '#FFFFFF',
    'on_surface': '#000000',
    'primary': '#3785F5',
    'on_primary': '#000000',
    'secondary': '#7FB0F5',
    'on_secondary': '#000000',
    'disable': '#B2B2B2',
    'on_disable': '#000000',
    'error': '#B3261E',
    'on_error': '#FFB4AB'
}

dark = {
    'background': '#3B4253',
    'on_background': '#E5E9F0',
    'surface': '#2E3441',
    'on_surface': '#E5E9F0',
    'primary': '#7FB0F5',
    'on_primary': '#000000',
    'secondary': '#3785F5',
    'on_secondary': '#000000',
    'disable': '#B2B2B2',
    'on_disable': '#000000',
    'error': 'B3261E',
    'on_error': '#FFB4AB'
}

current_path = sys.path[0].replace("\\","/")
images_path = f'{current_path}/icons'


# -----------
# Icon Button
# -----------
class MD3IconButton(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Icon Button

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Card position
                (x, y) -> x, y: upper left corner
            width: tuple
                Card width
            type: str
                Label type
                'standard', 'filled', 'tonal', 'outlined'
            icon: str
                Icon file without extension ('icon')
            border: str
                Border color ('value')
            labels: tuple
                Item label text ('item', 'field')
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            theme: bool
                App theme ('item', 'value', 'icon', 'field')
                True: Light theme, False: Dark theme
            language: int
                App language ('item', 'field')
                0: Spanish, 1: English
        
        Returns
        -------
        None
        """
        super(MD3IconButton, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (32, 32)
        self.setGeometry(x, y, w, h)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setAutoRaise(True)
        
        self.apply_styleSheet(attributes['theme'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if self.attributes['type'] == 'standard':
            thickness = 0
            border_color = None
            if theme:
                background_color = light["surface"]
                hover_background_color = light["secondary"]
                self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_L.png'))
            else:
                background_color = dark["surface"]
                hover_background_color = dark["secondary"]
                self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_D.png'))
        elif self.attributes['type'] == 'filled':
            thickness = 0
            border_color = None
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_L.png'))
            background_color = light["primary"] if theme else dark["primary"]
            hover_background_color = light["secondary"] if theme else dark["secondary"]
        elif self.attributes['type'] == 'tonal':
            thickness = 0
            border_color = None
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_L.png'))
            background_color = light["secondary"] if theme else dark["secondary"]
            hover_background_color = light["primary"] if theme else dark["primary"]
        elif self.attributes['type'] == 'outlined':
            thickness = 2
            border_color = light["on_surface"] if theme else dark["on_surface"]
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_L.png'))
            background_color = light["surface"] if theme else dark["surface"]
            hover_background_color = light["secondary"] if theme else dark["secondary"]
            
        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                f'border: {thickness}px solid {border_color};'
                f'border-radius: 16;'
                f'background-color: {background_color};'
                f'}}'
                f'QToolButton#{self.name}:hover {{ '
                f'background-color: {hover_background_color};'
                f'}}')

              
    def language_text(self, language: int) -> None:
        """ Change language of title text """
        return 0
        