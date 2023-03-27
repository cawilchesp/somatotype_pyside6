"""
PySide6 Icon Button component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtCore import Qt

from components.style_color import colors

import sys

# ------
# Switch
# ------
class MD3Switch(QtWidgets.QToolButton):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Switch

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Switch position
                (x, y) -> x, y: upper left corner
            side: str
                Switch button side
                'left', 'right'
            state: bool
                State of activation
                True: On, False: Off
            enabled: bool
                Switch enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            clicked: def
                Switch 'clicked' method name
        
        Returns
        -------
        None
        """
        super(MD3Switch, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (0, 0)
        self.setGeometry(x, y, 26, 32)

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setCheckable(True)
        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True

        self.setThemeStyle(attributes['theme'])
        self.setState(attributes['state'], attributes['theme'])

        self.clicked.connect(attributes['clicked'])
        

    def setState(self, state: bool, theme: bool) -> None:
        """ Set button state and corresponding icon """

        icon_theme = 'L' if theme else 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'

        if state:
            if self.attributes['side'] == 'left':
                icon_image = 'none'
            else:
                icon_image = 'circle_checked'
        else:
            if self.attributes['side'] == 'left':
                icon_image = 'circle'
            else:
                icon_image = 'none'
        self.setChecked(state)
        self.setIcon(QtGui.QIcon(f'{images_path}/{icon_image}_{icon_theme}.png'))
        self.setIconSize(QtCore.QSize(16,16))


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        
        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        border_color = colors(theme, 'outline')
        
        checked_background_color = colors(theme, 'secondary')
        disabled_background_color = colors(theme, 'disable')

        if theme: icon_theme = 'L'
        else: icon_theme = 'D'
        current_path = sys.path[0].replace("\\","/")
        images_path = f'{current_path}/icons'
        if self.isChecked():
            if self.attributes['side'] == 'left':
                icon_image = 'none'
            else:
                icon_image = 'circle_checked'
        else:
            if self.attributes['side'] == 'left':
                icon_image = 'circle'
            else:
                icon_image = 'none'
        self.setIcon(QtGui.QIcon(f'{images_path}/{icon_image}_{icon_theme}.png'))
        self.setIconSize(QtCore.QSize(16,16))

        border_outline = (f'border-top: 2px solid {border_color}; '
                          f'border-{self.attributes["side"]}: 2px solid {border_color}; '
                          f'border-bottom: 2px solid {border_color}')
        border_position = (f'border-top-{self.attributes["side"]}-radius: 16; '
                           f'border-bottom-{self.attributes["side"]}-radius: 16')
        
        self.setStyleSheet(f'QToolButton#{self.name} {{ '
                f'{border_outline}; '
                f'{border_position};'
                f'background-color: {background_color}; '
                f'}}'
                f'QToolButton#{self.name}:checked {{ '
                f'border: 0px solid; '
                f'{border_position};'
                f'background-color: {checked_background_color};'
                f'}}'
                f'QToolButton#{self.name}:!enabled {{ '
                f'background-color: {disabled_background_color};'
                f'}}')
