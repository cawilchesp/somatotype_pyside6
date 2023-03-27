"""
PySide6 Slider component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtWidgets
from PySide6.QtCore import Qt

from components.style_color import colors

# ------
# Slider
# ------
class MD3Slider(QtWidgets.QSlider):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Slider

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Button position
                (x, y) -> x, y: upper left corner
            width: int
                Button width
            range: tuple
                Slider range (min, step, max)
            value: int
                Slider current value
            enabled: bool
                Slider enabled / disabled
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            slider_moved: def
                Slider 'moved' method name
            slider_released: def
                Slider 'released' method name
        
        Returns
        -------
        None
        """
        super(MD3Slider, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w = attributes['width'] if 'width' in attributes else 32
        self.setGeometry(x, y, w, 32)

        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(attributes['range'][0])
        self.setSingleStep(attributes['range'][1])
        self.setMaximum(attributes['range'][2])

        self.setValue(attributes['value'])
        self.setEnabled(attributes['enabled']) if 'enabled' in attributes else True
        
        self.setThemeStyle(attributes['theme'])

        if 'slider_moved' in attributes:
            self.sliderMoved.connect(attributes['slider_moved'])
        if 'slider_released' in attributes:
            self.sliderReleased.connect(attributes['slider_released'])


    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        color = colors(theme, 'primary')
        disabled_color = colors(theme, 'on_disable')
        groove_color = '#494949'

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
