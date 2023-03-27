"""
PySide6 Video label component adapted to follow Material Design 3 guidelines


"""

from PySide6 import QtWidgets

from components.style_color import colors

# -----------
# Image Label
# -----------
class MD3ImageLabel(QtWidgets.QLabel):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Image Label

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Label position
                (x, y) -> x, y: upper left corner
            size: tuple
                Label size
                (w, h) -> w: width, h: height
            theme: bool
                App theme
                True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(MD3ImageLabel, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (96, 96)
        self.setGeometry(x, y, w, h)
        
        self.setFrameStyle(QtWidgets.QFrame.Shape.Box)

        self.setThemeStyle(attributes['theme'])
    

    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        
        if self.parent.attributes['type'] == 'filled':
            background_color = colors(theme, 'surface_tint')
        elif self.parent.attributes['type'] == 'outlined':
            background_color = colors(theme, 'background')
        border_color = colors(theme, 'outline')
        
        self.setStyleSheet(f'QLabel#{self.name} {{ '
                f'border: 1px solid {border_color};'
                f'border-radius: 12px;'
                f'background-color: {background_color};'
                f'}}' )
