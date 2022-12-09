"""
PyQt Slider component adapted to follow Material Design 3 guidelines

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


# ------
# Slider
# ------
class MD3Slider(QtWidgets.QSlider):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Slider

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Slider position and width
            (x, y, w) -> x, y: upper left corner, w: width
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(MD3Slider, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(0)
        self.setMaximum(2)
        self.setSingleStep(1)

        self.apply_styleSheet(attributes['theme'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if theme:
            background_color = light["surface"]
            groove_color = light["on_surface"]
            color = light["primary"]
            disabled_color = light["disable"]
        else:
            background_color = dark["surface"]
            groove_color = dark["on_surface"]
            color = dark["primary"]
            disabled_color = dark["disable"]


        self.setStyleSheet(f'QSlider#{self.name} {{ '
                f'background-color: {background_color} }}'
                
                f'QSlider#{self.name}::groove:horizontal {{ '
                f'background: {groove_color};'
                f'height: 4px;'
                f'}}'
                f'QSlider#{self.name}::handle:horizontal {{'
                f'background-color: {color}; '
                f'width: 20px; '
                f'height: 20px; '
                f'margin: -8px 0;'
                f'border-radius: 10px;' 
                f'}}'
                f'QSlider#{self.name}::handle:disabled {{'
                f'background-color: {disabled_color}'
                f'}}'
                f'QSlider#{self.name}::add-page:horizontal {{'
                f'background: {groove_color};'
                f'}}'
                f'QSlider#{self.name}::sub-page:horizontal {{'
                f'background: {color};'
                f'}}' 
                f'QSlider#{self.name}::sub-page:disabled {{'
                f'background: {disabled_color};'
                f'}}' )
