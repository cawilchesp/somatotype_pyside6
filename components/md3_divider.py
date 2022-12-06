"""
PyQt Divider component adapted to follow Material Design 3 guidelines

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

# -------
# Divider
# -------
class MD3Divider(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Common Buttons

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Card position
                (x, y) -> x, y: upper left corner
            size: tuple
                Card size
                (w, h) -> w: width, h: height
            theme: bool
                App theme
                True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(MD3Divider, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        if attributes['shape'] == 'horizontal':
            w = attributes['length'] if 'length' in attributes else 32
            h = 8
            self.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        elif attributes['shape'] == 'vertical':
            w = 8
            h = attributes['length'] if 'length' in attributes else 32
            self.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.setGeometry(x, y, w, h)

        self.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.apply_styleSheet(attributes['theme'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
        else:
            background_color = dark["surface"]
            
        self.setStyleSheet(f'QFrame#{self.name} {{ '
                f'background-color: {background_color};'
                f'}}' )


    def language_text(self, language: int) -> None:
        return 0
