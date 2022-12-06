"""
PyQt Menu component adapted to follow Material Design 3 guidelines


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


# ----
# Menú
# ----
class MD3Menu(QtWidgets.QComboBox):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Menu

        Parameters
        ----------
        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            geometry: tuple
                Menu position and width
                (x, y, w) -> x, y: upper left corner, w: width
            max_items: int
                Max visible items in the menu
            max_count: int
                Total Items in the menu
            options_dict: dict
                Menu options with translations
                Format: {0: ('es_1', 'en_1'), 1: ('es_2', 'en_2')}
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
        super(MD3Menu, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (96, 32)
        self.setGeometry(x, y, w, h)

        if 'options' in attributes:
            self.max_items = len(attributes['options']) if len(attributes['options']) < 6 else 10
            self.language_text(attributes['language'])
        else:
            self.max_items = 10

        self.setMaxVisibleItems(self.max_items)
        self.setMaxCount(self.max_items)
        self.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.setCurrentIndex(-1)
        self.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.view().window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.apply_styleSheet(attributes['theme'])


    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
            border_color = light["background"]
            disable_color = light["disable"]
            triangle_image = 'triangle_down_L.png'
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
            border_color = dark["background"]
            disable_color = dark["disable"]
            triangle_image = 'triangle_down_D.png'
        self.setStyleSheet(f'QComboBox#{self.name} {{ border: 1px solid {color};'
                f'border-radius: 4; background-color: {background_color}; color: {color} }}'
                f'QComboBox#{self.name}::drop-down {{ border-color: {border_color} }}'
                f'QComboBox#{self.name}::down-arrow {{ width: 16; height: 16;'
                f'image: url({images_path}/{triangle_image}) }}'
                f'QComboBox#{self.name}:!Enabled {{ background-color: {disable_color} }}'
                f'QComboBox#{self.name} QListView {{ border: 1px solid {color}; border-radius: 4;'
                f'background-color: {background_color}; color: {color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if 'options' in self.attributes:
            for key, value in self.attributes['options'].items():
                self.addItem('')
                if language == 0:   self.setItemText(key, value[0])
                elif language == 1: self.setItemText(key, value[1])