"""
PySide6 Divider component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtWidgets

from components.style_color import colors

import sys

# -------
# Divider
# -------
class MD3Divider(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Divider

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Divider position
                (x, y) -> x, y: upper left corner
            size: tuple
                Divider size
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
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        if attributes['shape'] == 'horizontal':
            w = attributes['length'] if 'length' in attributes else 32
            h = 1
            self.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        elif attributes['shape'] == 'vertical':
            w = 1
            h = attributes['length'] if 'length' in attributes else 32
            self.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.setGeometry(x, y, w, h)

        self.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)

        self.setThemeStyle(attributes['theme'])


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        
        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        border_color = colors(theme, 'outline')
            
        self.setStyleSheet(f'QFrame#{self.name} {{ '
                f'border: 1px solid {border_color};'
                f'background-color: {background_color};'
                f'}}' )
