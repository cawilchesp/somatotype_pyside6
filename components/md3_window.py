"""
PySide6 Main Window

"""

from components.style_color import colors

# ------
# Window
# ------
class MD3Window:
    def __init__(self, attributes):
        """ Main Window

        Parameters
        ----------
        attributes: dict
            parent:
                UI Parent object 
            size: tuple
                Window width and height
                (width, height)
            position: tuple (Optional)
                Window position, centered by default
                (x, y) -> x, y: upper left corner
            labels: tuple
                Window title text
                (label_es, label_en) -> label_es: label in spanish, label_en: label in english
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
        self.parent = attributes['parent']
        self.attributes = attributes

        w, h = attributes['size'] if 'size' in attributes else (1300, 700)
        screen_x = int(self.parent.screen().availableGeometry().width() / 2 - (w / 2))
        screen_y = int(self.parent.screen().availableGeometry().height() / 2 - (h / 2))
        x, y = attributes['position'] if 'position' in attributes else (screen_x,screen_y)
        self.parent.setGeometry(x, y, w, h)

        if 'minimum_size' in attributes:
            w_min, h_min = attributes['minimum_size']
            self.parent.setMinimumSize(w_min, h_min)

        if 'maximum_size' in attributes:
            w_max, h_max = attributes['maximum_size']
            self.parent.setMaximumSize(w_max, h_max)

        self.setThemeStyle(attributes['theme'])
        self.setLanguage(attributes['language'])
            

    def setThemeStyle(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        
        background_color = colors(theme, 'background')
        color = colors(theme, 'on_background')
        menu_color = colors(theme, 'on_surface')
        menu_border_color = colors(theme, 'on_background')
        menu_background_color = colors(theme, 'surface')

        self.parent.setStyleSheet(f'QWidget {{ '
                f'background-color: {background_color};'
                f'color: {color} }}'
                f'QComboBox QListView {{ '
                f'border: 1px solid {menu_border_color}; '
                f'border-radius: 4;'
                f'background-color: {menu_background_color}; '
                f'color: {menu_color} }}')


    def setLanguage(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.parent.setWindowTitle(self.attributes['labels'][0])
            elif language == 1: self.parent.setWindowTitle(self.attributes['labels'][1])