"""
PyQt Components adapted to follow Material Design 3 guidelines


"""

from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtCore import Qt

import sys

light = {
    'background': '#E5E9F0',
    'surface': '#B2B2B2',
    'primary': '#42A4F5',
    'secondary': '#FF2D55',
    'on_background': '#000000',
    'on_surface': '#000000',
    'on_primary': '#000000',
    'on_secondary': '#000000',
    'disable': '#B2B2B2',
    'error': ''
}

dark = {
    'background': '#3B4253',
    'surface': '#2E3441',
    'primary': '#42A4F5',
    'secondary': '#FF2D55',
    'on_background': '#E5E9F0',
    'on_surface': '#E5E9F0',
    'on_primary': '#000000',
    'on_secondary': '#000000',
    'disable': '#B2B2B2',
    'error': ''
}

current_path = sys.path[0].replace("\\","/")
images_path = f'{current_path}/images'

# ----
# Card
# ----
class Card(QtWidgets.QFrame):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Card

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Card position and size
            (x, y, w, h) -> x, y: upper left corner, w: width, h: height
        labels: tuple
            Card title text
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
        super(Card, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        x, y, w, h = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, h)

        self.title = QtWidgets.QLabel(self)
        self.title.setGeometry(8, 8, w-16, 32)
        self.title.setFont(QtGui.QFont('Segoe UI', 14))

        self.apply_styleSheet(theme)
        self.language_text(language)
    
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
        if language == 0:   self.title.setText(self.label_es)
        elif language == 1: self.title.setText(self.label_en)

# ----------
# Item Label
# ----------
class ItemLabel(QtWidgets.QLabel):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Item Label

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Item label position
            (x, y) -> x, y: upper left corner
        labels: tuple
            Item label text
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
        super(ItemLabel, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        x, y = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, parent.geometry().width()-16, 16)
        self.setFont(QtGui.QFont('Segoe UI', 9, QtGui.QFont.Weight.Bold))
        
        self.apply_styleSheet(theme)
        self.language_text(language)
    
    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
        self.setStyleSheet(f'QLabel#{self.name} {{ background-color: {background_color};'
                f'color: {color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.setText(self.label_es)
        elif language == 1: self.setText(self.label_en)

# -----------
# Value Label
# -----------
class ValueLabel(QtWidgets.QLabel):
    def __init__(self, parent, name: str, geometry: tuple, theme: bool) -> None:
        """ Material Design 3 Component: Value Label

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Value label position
            (x, y) -> x, y: upper left corner
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(ValueLabel, self).__init__(parent)

        self.name = name
        x, y, w = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        
        self.apply_styleSheet(theme)
    
    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
        self.setStyleSheet(f'QLabel#{self.name} {{ background-color: {background_color};'
                f'color: {color} }}')

# ----------
# Icon Label
# ----------
class IconLabel(QtWidgets.QLabel):
    def __init__(self, parent, name: str, geometry: tuple, icon: str, theme: bool) -> None:
        """ Material Design 3 Component: Icon Label

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Icon label position
            (x, y) -> x, y: upper left corner
        icon: str
            Icon file without extension, for the theme
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(IconLabel, self).__init__(parent)

        self.name = name
        x, y = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, 32, 32)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.set_icon(icon, theme)
        self.apply_styleSheet(theme)

    def set_icon(self, icon: str, theme: bool) -> None:
        """ Apply icon corresponding to the theme """
        if theme: self.setPixmap(QtGui.QIcon(f'{images_path}/{icon}_L.png').pixmap(24))
        else: self.setPixmap(QtGui.QIcon(f'{images_path}/{icon}_D.png').pixmap(24))

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
        self.setStyleSheet(f'QLabel#{self.name} {{ background-color: {background_color};'
                f'color: {color} }}')

# -----------
# Color Label
# -----------
class ColorLabel(QtWidgets.QLabel):
    def __init__(self, parent, name: str, geometry: tuple, color: str) -> None:
        """ Material Design 3 Component: Icon Label

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Color label position
            (x, y) -> x, y: upper left corner
        color: str
            Color string
            Format: 'R, G, B'
        
        Returns
        -------
        None
        """
        super(ColorLabel, self).__init__(parent)

        self.name = name
        x, y = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, 32, 32)
        self.set_color(color)

    def set_color(self, color: str) -> None:
        """ Apply custom color to component """
        self.setStyleSheet(f'QLabel#{self.name} {{ border: 2px solid {light["secondary"]};'
            f'border-radius: 15px; background-color: rgb({color}) }}')

# -----------
# Field Label
# -----------
class FieldLabel(QtWidgets.QLabel):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Field Label

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Field label position
            (x, y) -> x, y: upper left corner
        labels: tuple
            Field label text
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
        super(FieldLabel, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        x, y = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, 16, 16)

        self.apply_styleSheet(theme)
        self.language_text(language)
    
    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
        self.setStyleSheet(f'QLabel#{self.name} {{ border: 0px solid;'
                f'background-color: {background_color};'
                f'color: {color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.setText(self.label_es)
        elif language == 1: self.setText(self.label_en)
        self.adjustSize()

# -----------
# Text Button
# -----------
class TextButton(QtWidgets.QToolButton):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, icon: str, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Text Button

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Text button position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Text button text
            (label_es, label_en) -> label_es: label in spanish, label_en: label in english
        icon: str
            Icon file with extension. If is not necessary, use an empty string: ''.
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
        super(TextButton, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        x, y, w = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setAutoRaise(True)
        self.setIcon(QtGui.QIcon(f'{images_path}/{icon}'))

        self.apply_styleSheet(theme)
        self.language_text(language)
        
    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["primary"]
            color = light["on_primary"]
            hover_background_color = light["secondary"]
            hover_color = light["on_secondary"]
        else:
            background_color = dark["primary"]
            color = dark["on_primary"]
            hover_background_color = dark["secondary"]
            hover_color = dark["on_secondary"]
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 0px solid; border-radius: 16;'
                f'padding: 0 8 0 8; background-color: {background_color};'
                f'color: {color} }}'
                f'QToolButton#{self.name}:hover {{ background-color: {hover_background_color};'
                f'color: {hover_color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of button text """
        if language == 0:   self.setText(self.label_es)
        elif language == 1: self.setText(self.label_en)

# ----------------
# Segmented Button
# ----------------
class SegmentedButton(QtWidgets.QToolButton):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, icons: tuple, position: str, state: bool, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Segmented Button

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Segmented button position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Segmented button text
            (label_es, label_en) -> label_es: label in spanish, label_en: label in english
        icons: tuple
            Icon files with extension. Off state icon is a blank icon.
            (icon_on, icon_off) -> icon_on: On state icon, icon_off: Off state icon
        position: str
            Position of the segmented button in the group
            Options: 'left', 'center', 'right'
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
        super(SegmentedButton, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        self.icon_on, self.icon_off = icons
        self.position = position
        x, y, w = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)
        self.setEnabled(True)

        self.set_state(state)
        self.apply_styleSheet(theme)
        self.language_text(language)
        
    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        if state:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_on}'))
            self.setChecked(True)
        else:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_off}'))
            self.setChecked(False)

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if self.position == 'left':
            border_position = 'border-top-left-radius: 16; border-bottom-left-radius: 16'
        elif self.position == 'center':
            border_position = 'border-radius: 0'
        elif self.position == 'right':
            border_position = 'border-top-right-radius: 16; border-bottom-right-radius: 16'
        
        if theme:
            border_color = light["on_surface"]
            background_color = light["primary"]
            color = light["on_primary"]
            checked_background_color = light["secondary"]
            checked_color = light["on_secondary"]
        else:
            border_color = dark["on_surface"]
            background_color = dark["primary"]
            color = dark["on_primary"]
            checked_background_color = dark["secondary"]
            checked_color = dark["on_secondary"]
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 1px solid {border_color};'
                f'{border_position}; padding: 0 8 0 8;'
                f'background-color: {background_color}; color: {color} }}'
                f'QToolButton#{self.name}:checked {{ background-color: {checked_background_color};'
                f'color: {checked_color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of button text """
        if language == 0:   self.setText(self.label_es)
        elif language == 1: self.setText(self.label_en)

# -----------
# Icon Button
# -----------
class IconButton(QtWidgets.QToolButton):
    def __init__(self, parent, name: str, geometry: tuple, icon: str, theme: bool) -> None:
        """ Material Design 3 Component: Icon Button

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Icon button position
            (x, y, w) -> x, y: upper left corner, w: width
        icon: tuple
            Icon file with extension.
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(IconButton, self).__init__(parent)

        self.name = name
        x, y = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, 32, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.setAutoRaise(True)
        self.setEnabled(True)
        self.setIcon(QtGui.QIcon(f'{images_path}/{icon}'))

        self.apply_styleSheet(theme)
        
    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["primary"]
            color = light["on_primary"]
            hover_background_color = light["secondary"]
            hover_color = light["on_secondary"]
        else:
            background_color = dark["primary"]
            color = dark["on_primary"]
            hover_background_color = dark["secondary"]
            hover_color = dark["on_secondary"]
        
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 0px solid; border-radius: 16;'
                f'background-color: {background_color}; color: {color} }}'
                f'QToolButton#{self.name}:hover {{ border: 0px solid; border-radius: 16;'
                f'background-color: {hover_background_color}; color: {hover_color} }}')

# ------------
# Color Button
# ------------
class ColorButton(QtWidgets.QToolButton):
    def __init__(self, parent, name: str, geometry: tuple, color: str, theme: bool) -> None:
        """ Material Design 3 Component: Color Button

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Color button position
            (x, y,) -> x, y: upper left corner
        color: str
            Color string
            Format: 'R, G, B'
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(ColorButton, self).__init__(parent)

        self.name = name
        x, y = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, 32, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setAutoRaise(True)
        self.setEnabled(True)

        self.apply_styleSheet(theme, color)

    def apply_styleSheet(self, theme: bool, color: str) -> None:
        """ Apply theme style sheet and color to component """
        if theme:
            hover_border_color = light["secondary"]
        else:
            hover_border_color = dark["secondary"]
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 0px solid;'
                f'border-radius: 16; background-color: rgb({color}) }}'
                f'QToolButton#{self.name}:hover {{ border: 2px solid;'
                f'border-radius: 16; border-color: {hover_border_color} }}')

# ------
# Switch
# ------
class Switch(QtWidgets.QToolButton):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, icons: tuple, state: bool, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Switch

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Switch position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Switch text. If is not necessary, use an empty tuple: ('','')
            (label_es, label_en) -> label_es: label in spanish, label_en: label in english
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
        super(Switch, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        self.icon_on, self.icon_off = icons
        x, y, w = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)
        
        self.set_state(state)
        self.apply_styleSheet(theme)
        self.language_text(language)
        
    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        if state:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_on}'))
            self.setChecked(True)
        else:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_off}'))
            self.setChecked(False)

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["primary"]
            color = light["on_primary"]
            checked_background_color = light["secondary"]
            checked_color = light["on_secondary"]
        else:
            background_color = dark["primary"]
            color = dark["on_primary"]
            checked_background_color = dark["secondary"]
            checked_color = dark["on_secondary"]
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 0px solid; border-radius: 16;'
                f'padding: 0 16 0 16; background-color: {background_color}; color: {color} }}'
                f'QToolButton#{self.name}:checked {{ background-color: {checked_background_color};'
                f'color: {checked_color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of switch text """
        if language == 0:   self.setText(self.label_es)
        elif language == 1: self.setText(self.label_en)

# ----
# Chip
# ----
class Chip(QtWidgets.QToolButton):
    def __init__(self, parent, name: str, geometry: tuple, labels: tuple, icons: tuple, state: bool, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Segmented Button

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Chip button position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Chip button text
            (label_es, label_en) -> label_es: label in spanish, label_en: label in english
        icons: tuple
            Icon files with extension. Off state icon is a blank icon.
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
        super(Chip, self).__init__(parent)

        self.name = name
        self.label_es, self.label_en = labels
        self.icon_on, self.icon_off = icons
        x, y, w = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        self.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.setCheckable(True)
        self.setEnabled(True)

        self.set_state(state)
        self.apply_styleSheet(theme)
        self.language_text(language)
        
    def set_state(self, state: bool) -> None:
        """ Set button state and corresponding icon """
        if state:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_on}'))
            self.setChecked(True)
        else:
            self.setIcon(QtGui.QIcon(f'{images_path}/{self.icon_off}'))
            self.setChecked(False)

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            border_color = light["on_surface"]
            background_color = light["surface"]
            color = light["on_surface"]
            checked_background_color = light["secondary"]
            checked_color = light["on_secondary"]
        else:
            border_color = dark["on_surface"]
            background_color = dark["surface"]
            color = dark["on_surface"]
            checked_background_color = dark["secondary"]
            checked_color = dark["on_secondary"]
        self.setStyleSheet(f'QToolButton#{self.name} {{ border: 1px solid {border_color};'
                f'border-radius: 8; padding: 0 8 0 8;'
                f'background-color: {background_color}; color: {color} }}'
                f'QToolButton#{self.name}:checked {{ background-color: {checked_background_color};'
                f'color: {checked_color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of button text """
        if language == 0:   self.setText(self.label_es)
        elif language == 1: self.setText(self.label_en)

# ----------
# Text Field
# ----------
class TextField(QtWidgets.QFrame):
    def __init__(self, parent, geometry: tuple, labels: tuple, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Text Field

        Parameters
        ----------
        geometry: tuple
            Text Field position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Text Field text
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
        super(TextField, self).__init__(parent)

        self.label_es, self.label_en = labels
        x, y, w = geometry

        self.setGeometry(x, y, w, 52)

        self.text_field = QtWidgets.QLineEdit(self)
        self.text_field.setGeometry(0, 8, w, 44)
        self.text_field.setClearButtonEnabled(True)

        self.label_field = QtWidgets.QLabel(self)
        self.label_field.setGeometry(8, 0, 16, 16)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))
        
        self.apply_styleSheet(theme)
        self.language_text(language)

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
        self.setStyleSheet(f'QFrame {{ background-color: {background_color} }}'
                f'QLineEdit {{ border: 1px solid {color}; border-radius: 4;'
                f'padding: 0 8 0 8; background-color: {background_color}; color: {color}; }}'
                f'QLabel {{ border: 0px solid; padding: 0 4 0 4;'
                f'background-color: {background_color}; color: {color} }}')

    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.label_es)
        elif language == 1: self.label_field.setText(self.label_en)
        self.label_field.adjustSize()

# ----------
# Date Field
# ----------
class DateField(QtWidgets.QFrame):
    def __init__(self, parent, geometry: tuple, labels: tuple, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Date Field

        Parameters
        ----------
        geometry: tuple
            Date field position and width
            (x, y, w) -> x, y: upper left corner, w: width
        labels: tuple
            Date field text
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
        super(DateField, self).__init__(parent)

        self.label_es, self.label_en = labels
        x, y, w = geometry

        self.setGeometry(x, y, w, 52)

        self.text_field = QtWidgets.QDateEdit(self)
        self.text_field.setGeometry(0, 8, w, 44)
        self.text_field.setCalendarPopup(True)
        self.text_field.setFrame(False)
        self.text_field.setSpecialValueText('')
        self.text_field.setDate(QtCore.QDate.currentDate())
        
        self.label_field = QtWidgets.QLabel(self)
        self.label_field.setGeometry(8, 0, 16, 16)
        self.label_field.setFont(QtGui.QFont('Segoe UI', 9))

        self.apply_styleSheet(theme)
        self.language_text(language)

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme:
            background_color = light["surface"]
            color = light["on_surface"]
            drop_background_color = light["primary"]
        else:
            background_color = dark["surface"]
            color = dark["on_surface"]
            drop_background_color = dark["primary"]
        self.setStyleSheet(f'QLabel {{ border: 0px solid; padding: 0 4 0 4;'
                f'background-color: {background_color}; color: {color} }}'
                f'QDateEdit {{ border: 1px solid {color}; border-radius: 4; padding: 0 8 0 8;'
                f'background-color: {background_color}; color: {color}; }}'
                f'QDateEdit::drop-down {{ background-color: {drop_background_color};'
                f'width: 32; height: 32; subcontrol-position: center right; left: -4;'
                f'border-radius: 16 }}'
                f'QDateEdit::down-arrow {{ image: url({images_path}/calendar_L.png);'
                f'width: 16; height: 16 }}')

    def language_text(self, language: int) -> None:
        """ Change language of label text """
        if language == 0:   self.label_field.setText(self.label_es)
        elif language == 1: self.label_field.setText(self.label_en)
        self.label_field.adjustSize()

# ----
# Menú
# ----
class Menu(QtWidgets.QComboBox):
    def __init__(self, parent, name: str, geometry: tuple, max_items: int, max_count: int, options_dict: dict, theme: bool, language: int) -> None:
        """ Material Design 3 Component: Menu

        Parameters
        ----------
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
        super(Menu, self).__init__(parent)

        self.name = name
        x, y, w = geometry
        self.options_dict = options_dict

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        self.setMaxVisibleItems(max_items)
        self.setMaxCount(max_count)
        self.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.setCurrentIndex(-1)
        self.view().window().setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint | Qt.WindowType.NoDropShadowWindowHint)
        self.view().window().setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.apply_styleSheet(theme)
        self.language_text(language)

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
        for key, value in self.options_dict.items():
            self.addItem('')
            if language == 0:   self.setItemText(key, value[0])
            elif language == 1: self.setItemText(key, value[1])

# ------
# Slider
# ------
class Slider(QtWidgets.QSlider):
    def __init__(self, parent, name: str, geometry: tuple, theme: bool) -> None:
        """ Material Design 3 Component: Slider

        Parameters
        ----------
        name: str
            Widget name
        geometry: tuple
            Slider position and width
            (x, y, w) -> x, y: upper left corner, w: width
        theme: bool
            App theme
            True: Light theme, False: Dark theme
        
        Returns
        -------
        None
        """
        super(Slider, self).__init__(parent)

        self.name = name
        x, y, w = geometry

        self.setObjectName(self.name)
        self.setGeometry(x, y, w, 32)
        self.setOrientation(Qt.Orientation.Horizontal)
        self.setMinimum(0)
        self.setSingleStep(1)
        self.apply_styleSheet(theme)

    def apply_styleSheet(self, theme: bool) -> None:
        """ Apply theme style sheet to component """
        if theme: background_color = light["surface"]
        else: background_color = dark["surface"]
        self.setStyleSheet(f'QSlider#{self.name} {{ background-color: {background_color} }}')
