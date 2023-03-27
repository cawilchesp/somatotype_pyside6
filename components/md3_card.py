"""
PySide6 Card component adapted to follow Material Design 3 guidelines

"""

from PySide6 import QtGui, QtWidgets

from components.style_color import colors

# ----
# Card
# ----
class MD3Card(QtWidgets.QFrame):
    def __init__(self, parent, attributes: dict) -> None:
        """ Material Design 3 Component: Card

        Parameters
        ----------
        attributes: dict
            name: str
                Widget name
            position: tuple
                Card position
                (x, y) -> x, y: upper left corner
            size: tuple
                Card size
                (w, h) -> w: width, h: height
            labels: tuple
                Card title text (Optional)
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
            type: str
                Card type
                'filled', 'outlined'
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
        super(MD3Card, self).__init__(parent)

        self.attributes = attributes
        self.parent = parent

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (96, 96)
        self.setGeometry(x, y, w, h)

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(8, 8, 32, 32)
        self.title.setFont(QtGui.QFont('Segoe UI', 14))

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])
    

    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """

        if self.attributes['type'] == 'filled':
            thickness = 0
            border_color = None
            background_color = colors(theme, 'surface_tint')
        elif self.attributes['type'] == 'outlined':
            thickness = 2
            border_color = colors(theme, 'outline')
            background_color = colors(theme, 'background')
        color = colors(theme, 'on_surface')
                    
        self.setStyleSheet(f'QFrame#{self.name} {{ '
                f'border: {thickness}px solid {border_color};'
                f'border-radius: 12px;'
                f'background-color: {background_color} }}'
                f'QLabel {{ background-color: {background_color}; '
                f'color: {color} }}')


    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.title.setText(self.attributes['labels'][0])
            elif language == 1: self.title.setText(self.attributes['labels'][1])
            self.title.adjustSize()