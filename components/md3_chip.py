"""
PyQt Chip component adapted to follow Material Design 3 guidelines

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


# ----
# Chip
# ----
class MD3Chip(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Chip
        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            geometry: tuple
                Chip button position and width
                (x, y, w) -> x, y: upper left corner, w: width
            labels: tuple
                Chip button text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            icons: tuple
                Icon files with extension. Off state icon is a blank icon.
                (icon_on, icon_off) -> icon_on: On state icon, icon_off: Off state icon
            state: bool
                State of activation
                True: On, False: Off
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
        
        Returns
        -------
        None
        """
        super(MD3Chip, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.chip_icon = attributes['icon'] if 'icon' in self.attributes else 'none'

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)

        self.set_state(attributes['state'], attributes['theme'])
        self.apply_styleSheet(attributes['theme'])

        if 'labels' in attributes:
            self.language_text(attributes['language'])

        
    def set_state(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """
        if state:
            if 'labels' in self.attributes: self.setIcon(QtGui.QIcon(f'{images_path}/done_L.png'))
            else: self.setIcon(QtGui.QIcon(f'{images_path}/{self.chip_icon}_L.png'))
            self.setChecked(True)
        else:
            if theme: self.setIcon(QtGui.QIcon(f'{images_path}/{self.chip_icon}_L.png'))
            else: self.setIcon(QtGui.QIcon(f'{images_path}/{self.chip_icon}_D.png'))
            self.setChecked(False)


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if self.isChecked():
            if 'labels' in self.attributes: self.setIcon(QtGui.QIcon(f'{images_path}/done_L.png'))
            else: self.setIcon(QtGui.QIcon(f'{images_path}/{self.chip_icon}_L.png'))
        else:
            if theme: self.setIcon(QtGui.QIcon(f'{images_path}/{self.chip_icon}_L.png'))
            else: self.setIcon(QtGui.QIcon(f'{images_path}/{self.chip_icon}_D.png'))

        if theme:
            border_color = light["on_surface"]
            background_color = light["surface"]
            color = light["on_surface"]
            checked_background_color = light["primary"]
            checked_color = light["on_primary"]
        else:
            border_color = dark["on_surface"]
            background_color = dark["surface"]
            color = dark["on_surface"]
            checked_background_color = dark["primary"]
            checked_color = dark["on_primary"]

        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                f'border: 1px solid {border_color};'
                f'border-radius: 8;'
                f'padding: 0 4 0 4;'
                f'background-color: {background_color}; '
                f'color: {color} }}'
                f'QToolButton#{self.name}:checked {{ '
                f'background-color: {checked_background_color};'
                f'color: {checked_color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])