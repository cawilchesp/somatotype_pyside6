"""
PyQt Label component adapted to follow Material Design 3 guidelines


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
# Labels
# ------
class MD3Label(QtWidgets.QLabel):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Label

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
                For text: 'subtitle', 'value'
                For indicators: 'icon', 'color'
            align: str 
                Text align ('item', 'value', 'field')
                'center', 'left', 'right'
            icon: str
                Icon file without extension ('icon')
            color: str
                Label color ('color')
                Format: 'R, G, B'
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
        super(MD3Label, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        h = 16 if attributes['type'] == 'subtitle' else 32
        self.setGeometry(x, y, w, h)

        if 'align' in attributes: 
            if attributes['align'] == 'center': self.setAlignment(Qt.AlignmentFlag.AlignCenter)
            elif attributes['align'] == 'left': self.setAlignment(Qt.AlignmentFlag.AlignLeft)
            elif attributes['align'] == 'right': self.setAlignment(Qt.AlignmentFlag.AlignRight)
        else: self.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self.apply_styleSheet(attributes['theme'])
        if 'labels' in attributes:
            self.language_text(attributes['language'])
        

    def set_icon(self, icon: str, theme: bool) -> None:
        """ Apply icon corresponding to the theme """
        self.attributes['icon'] = icon
        if theme: self.setPixmap(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_L.png').pixmap(24))
        else: self.setPixmap(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_D.png').pixmap(24))
        

    def set_color(self, color: str) -> None:
        """ Apply custom color to component """
        self.setStyleSheet(f'QLabel#{self.name} {{ border: 2px solid {light["secondary"]};'
            f'border-radius: 16px; background-color: rgb({color}) }}')


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if 'icon' in self.attributes:
            if theme: self.setPixmap(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_L.png').pixmap(24))
            else: self.setPixmap(QtGui.QIcon(f'{images_path}/{self.attributes["icon"]}_D.png').pixmap(24))

        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
            
        # Specific theme by type
        if self.attributes['type'] == 'subtitle':
            thickness = 0
            border_color = None
            padding = '0px'
        elif self.attributes['type'] == 'value':
            thickness = 2
            border_color = self.attributes['color']
            padding = '0px'
        elif self.attributes['type'] == 'icon':
            thickness = 0
            border_color = None
            padding = '4px'
        elif self.attributes['type'] == 'color':
            thickness = 2
            border_color = light["secondary"]
            background_color = self.attributes['color']
            padding = '0px'

        self.setStyleSheet(f'QLabel#{self.name} {{ '
                f'border: {thickness}px solid rgb({border_color});'
                f'border-radius: 16px;'
                f'background-color: {background_color};'
                f'color: {color};'
                f'padding: {padding} }}' )


    def language_text(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.setText(self.attributes['labels'][0])
            elif language == 1: self.setText(self.attributes['labels'][1])