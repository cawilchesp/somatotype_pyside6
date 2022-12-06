"""
PyQt Card component adapted to follow Material Design 3 guidelines

"""

from PyQt6 import QtGui, QtWidgets

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
            theme: bool
                App theme
                True: Light theme, False: Dark theme
            language: int
                App language (Optional if no labels)
                0: Spanish, 1: English
        
        Returns
        -------
        None
        """
        super(MD3Card, self).__init__(parent)

        self.attributes = attributes

        self.name = attributes['name']
        self.setObjectName(self.name)

        x, y = attributes['position'] if 'position' in attributes else (8,8)
        w, h = attributes['size'] if 'size' in attributes else (96, 96)
        self.setGeometry(x, y, w, h)

        self.apply_styleSheet(attributes['theme'])

        if 'labels' in attributes:
            self.title = QtWidgets.QLabel(self)
            self.title.setGeometry(8, 8, w-16, 32)
            self.title.setFont(QtGui.QFont('Segoe UI', 14))

            self.language_text(attributes['language'])
    

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
        self.setStyleSheet(f'QFrame#{self.name} {{ border-radius: 12px;'
                f'background-color: {background_color} }}'
                f'QLabel {{ background-color: {background_color}; color: {color} }}')


    def language_text(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.title.setText(self.attributes['labels'][0])
            elif language == 1: self.title.setText(self.attributes['labels'][1])