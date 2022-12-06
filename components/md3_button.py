"""
PyQt Button component adapted to follow Material Design 3 guidelines

"""

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt

import sys


light = {
    'background': '#E5E9F0',
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

# --------------
# Common Buttons
# --------------
class MD3Button(QtWidgets.QPushButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Common Buttons

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Button position
                (x, y) -> x, y: upper left corner
            width: tuple
                Button width
            type: str
                Button type
                'elevated', 'filled', 'tonal', 'outlined', 'text'
            icon: str
                Icon file without extension ('icon')
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
        super(MD3Button, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        if 'icon' in attributes:
            self.setIcon(QtGui.QIcon(f'{images_path}/{attributes["icon"]}'))

        self.apply_styleSheet(attributes['theme'])
            
        if 'labels' in attributes:
            self.language_text(attributes['language'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.attributes['type'] == 'elevated':
            thickness = 1
            background_color = light["surface"] if theme else dark["surface"]
            color = light["on_surface"] if theme else dark["on_surface"]
            hover_background_color = light["primary"] if theme else dark["primary"]
            hover_color = light["on_surface"] if theme else dark["on_surface"]
        elif self.attributes['type'] == 'filled':
            thickness = 0
            background_color = light["primary"] if theme else dark["primary"]
            color = light["on_primary"] if theme else dark["on_primary"]
            hover_background_color = light["secondary"] if theme else dark["secondary"]
            hover_color = light["on_primary"] if theme else dark["on_primary"]
        elif self.attributes['type'] == 'tonal':
            thickness = 0
            background_color = light["secondary"] if theme else dark["secondary"]
            color = light["on_secondary"] if theme else dark["on_secondary"]
            hover_background_color = light["primary"] if theme else dark["primary"]
            hover_color = light["on_secondary"] if theme else dark["on_secondary"]
        elif self.attributes['type'] == 'outlined':
            thickness = 1
            background_color = light["surface"] if theme else dark["surface"]
            color = light["primary"] if theme else dark["primary"]
            hover_background_color = light["secondary"] if theme else dark["secondary"]
            hover_color = light["on_surface"] if theme else dark["on_surface"]
        elif self.attributes['type'] == 'text':
            thickness = 0
            background_color = light["surface"] if theme else dark["surface"]
            color = light["primary"] if theme else dark["primary"]
            hover_background_color = light["secondary"] if theme else dark["secondary"]
            hover_color = light["on_secondary"] if theme else dark["on_secondary"]

        disabled_color = light["on_disable"] if theme else dark["disable"]

        self.setStyleSheet(f'QPushButton#{self.name} {{ '
                f'border: {thickness}px solid;'
                f'border-radius: 16;'
                f'background-color: {background_color};'
                f'color: {color};'
                f'}}'
                f'QPushButton#{self.name}:hover {{ '
                f'background-color: {hover_background_color};'
                f'color: {hover_color};'
                f'}}'
                f'QPushButton#{self.name}:!enabled {{ '
                f'color: {disabled_color}'
                f'}}')
              

    def language_text(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])