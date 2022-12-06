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
            icons: tuple
                Icon files with extension.
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
        super(MD3Switch, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (0, 0)
        self.setGeometry(x, y, 26, 32)

        self.side = attributes['side']

        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setCheckable(True)

        self.icon_on, self.icon_off = attributes['icons']

        self.state = attributes['state']

        self.set_state(self.state)
        self.apply_styleSheet(attributes['theme'])


    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        if state:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_on}'))
            self.setChecked(True)
        else:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_off}'))
            self.setChecked(False)
        self.setIconSize(QtCore.QSize(16,16))


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        border_position = f'border-top-{self.side}-radius: 16; border-bottom-{self.side}-radius: 16'

        if theme:
            background_color = light["primary"]
            color = light["on_primary"]
        else:
            background_color = dark["primary"]
            color = dark["on_primary"]
        
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 0px solid; {border_position};'
                f'padding: 0 0 0 0;'
                f'background-color: {background_color}; color: {color} }}'
                f'QToolButton#{self.name}:checked {{ background-color: {background_color};'
                f'color: {color} }}'
                )


    def language_text(self, language: int) -> None:
        """ Change language of switch text """
        return 0