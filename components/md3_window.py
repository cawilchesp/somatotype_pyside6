"""
PyQt Main Window

"""

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


# ------
# Window
# ------
class MD3Window:
    def __init__(self, attributes):
        self.attributes = attributes

        self.parent = attributes['parent']

        w, h = attributes['size'] if 'size' in attributes else (1300, 700)
        screen_x = int(self.parent.screen().availableGeometry().width() / 2 - (w / 2))
        screen_y = int(self.parent.screen().availableGeometry().height() / 2 - (h / 2))
        x, y = attributes['position'] if 'position' in attributes else (screen_x,screen_y)
        self.parent.setGeometry(x, y, w, h)
        self.parent.setMinimumSize(w, h)

        self.apply_styleSheet(attributes['theme'])
        self.language_text(attributes['language'])
            
    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["background"]
            color = light["on_surface"]
            border_color = light['on_background']
            combo_color = light['surface']
        else:
            background_color = dark["background"]
            color = dark["on_surface"]
            border_color = dark['on_background']
            combo_color = dark['surface']
        self.parent.setStyleSheet(
            f'QWidget {{ background-color: {background_color}; color: #000000 }}'
            f'QComboBox QListView {{ border: 1px solid {border_color}; border-radius: 4;'
            f'background-color: {combo_color}; color: {color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of title text """
        if 'labels' in self.attributes:
            if language == 0:   self.parent.setWindowTitle(self.attributes['labels'][0])
            elif language == 1: self.parent.setWindowTitle(self.attributes['labels'][1])