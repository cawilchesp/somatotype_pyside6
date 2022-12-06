from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QSettings

import sys

from components.md3_window import MD3Window
from components.md3_card import MD3Card
from components.md3_label import MD3Label
from components.md3_button import MD3Button


# ----------------
# About App Dialog
# ----------------
class AboutApp(QtWidgets.QDialog):
    def __init__(self):
        """ About Me Dialog """
        super().__init__()

        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.aboutapp_widgets = {}


        # -----------
        # Main Window
        # -----------
        (width, height) = (320, 408)
        self.aboutapp_widgets['main_window'] = MD3Window( {
            'parent': self, 
            'size': (width, height),
            'labels': ('Acerca de...','About...'),
            'theme': self.theme_value, 
            'language': self.language_value } )
        self.setMaximumSize(width, height)
        self.setMinimumSize(width, height)


        # -----------
        # Card Dialog
        # -----------
        self.aboutapp_widgets['aboutapp_dialog_card'] = MD3Card(self, { 
            'name': 'aboutapp_dialog_card',
            'position': (8, 8),
            'size': (width-16, height-16),
            'theme': self.theme_value,
            'labels': ('Calculadora de Somatotipo', 'Somatotype Calculator'), 
            'language': self.language_value } )

        self.aboutapp_widgets['version_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'version_label', 
            'position': (8, 48), 
            'width': width - 32,
            'type': 'subtitle',
            'labels': ('Versión: 1.0', 'Version: 1.0'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['developed_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'developed_label', 
            'position': (8, 96), 
            'width': width - 32,
            'type': 'subtitle',
            'labels': ('Desarrollado por:', 'Developed by:'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['person_icon'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'person_icon', 
            'position': (8, 144),
            'type': 'icon',
            'icon': 'person',
            'theme': self.theme_value } )

        self.aboutapp_widgets['name_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'name_label', 
            'position': (48, 152), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('Carlos Andrés Wilches Pérez', 'Carlos Andrés Wilches Pérez'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['profession_icon'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'profession_icon', 
            'position': (8, 174),
            'type': 'icon',
            'icon': 'school',
            'theme': self.theme_value } )

        self.aboutapp_widgets['profession_1_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'profession_1_label', 
            'position': (48, 182), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('Ingeniero Electrónico, BSc. MSc. PhD.', 'Electronic Engineer, BSc. MSc. PhD.'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['profession_2_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'profession_2_label', 
            'position': (48, 206), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('Universidad Nacional de Colombia', 'Nacional University of Colombia'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['profession_3_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'profession_3_label', 
            'position': (48, 238), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('Maestría en Ingeniería Electrónica', 'Master in Electronic Engineering'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['profession_4_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'profession_4_label', 
            'position': (48, 262), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('Doctor en Ingeniería', 'Doctor in Engineering'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['profession_5_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'profession_5_label', 
            'position': (48, 286), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('Pontificia Universidad Javeriana', 'Xaverian Pontifical University'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.aboutapp_widgets['email_icon'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'email_icon', 
            'position': (8, 310),
            'type': 'icon',
            'icon': 'mail',
            'theme': self.theme_value } )

        self.aboutapp_widgets['email_label'] = MD3Label(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'email_label', 
            'position': (48, 318), 
            'width': width - 80,
            'type': 'subtitle',
            'labels': ('cawilchesp@outlook.com', 'cawilchesp@outlook.com'),
            'theme': self.theme_value,
            'language': self.language_value } )

        # ---------
        # Button Ok
        # ---------
        self.aboutapp_widgets['ok_button'] = MD3Button(self.aboutapp_widgets['aboutapp_dialog_card'], {
            'name': 'ok_button',
            'position': (self.aboutapp_widgets['aboutapp_dialog_card'].width() - 108, self.aboutapp_widgets['aboutapp_dialog_card'].height() - 40),
            'width': 100,
            'type': 'text',
            'labels': ('Aceptar', 'Ok'),
            'theme': self.theme_value,
            'language': self.language_value } )
        self.aboutapp_widgets['ok_button'].clicked.connect(self.on_ok_button_clicked)


    def on_ok_button_clicked(self):
        """ Close dialog """
        self.close()