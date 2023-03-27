"""
PySide6 Chip component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtGui, QtWidgets
from PySide6.QtCore import Qt

from components.style_color import colors

import sys

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
            position: tuple
                Chip position
                (x, y) -> x, y: upper left corner
            width: int
                Chip width
            labels: tuple
                Chip text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            icon: str (Optional)
                Icon file without extension ('icon')
            state: bool
                State of activation
                True: On, False: Off
            enabled: bool
                Chip enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language
                0: Spanish, 1: English
            clicked: def
                Chip 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3Chip, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)

        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setThemeStyle(attributes['theme'])
        self.setState(attributes['state'], attributes['theme'])
        self.setLanguage(attributes['language'])

        self.clicked.connect(attributes['clicked'])

        
    def setState(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """
        
        icon_theme = 'L' if theme else 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'

        if 'icon' in self.attributes:
            icon_image = self.attributes['icon']
        else:
            icon_image = 'none'
        if state:
            icon_image = 'done'
        self.setChecked(state)
        self.setIcon(QtGui.QIcon(f'{images_path}/{icon_image}_{icon_theme}.png'))


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_secondary')
        border_color = colors(theme, 'outline')
        
        checked_background_color = colors(theme, 'secondary')
        checked_color = colors(theme, 'on_secondary')
        hover_background_color = colors(theme, 'hover')
        hover_color = colors(theme, 'on_primary')
        disabled_background_color = colors(theme, 'disable')
        disabled_color = colors(theme, 'on_disable')

        icon_theme = 'L' if theme else 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        if 'icon' in self.attributes:
            icon_image = self.attributes['icon']
        else:
            icon_image = 'none'
        if self.isChecked():
            icon_image = 'done'
        self.setIcon(QtGui.QIcon(f'{images_path}/{icon_image}_{icon_theme}.png'))
        
        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                f'border: 1px solid {border_color};'
                f'border-radius: 8;'
                f'padding: 0 8 0 8;'
                f'background-color: {background_color}; '
                f'color: {color} '
                f'}}'
                f'QToolButton#{self.name}:checked {{ '
                f'background-color: {checked_background_color};'
                f'color: {checked_color}'
                f'}}'
                f'QToolButton#{self.name}:hover {{ '
                f'background-color: {hover_background_color};'
                f'color: {hover_color};'
                f'}}'
                f'QToolButton#{self.name}:!enabled {{ '
                f'background-color: {disabled_background_color};'
                f'color: {disabled_color}'
                f'}}')


    def setLanguage(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.setText(self.attributes['labels'][0])
        elif language == 1: self.setText(self.attributes['labels'][1])