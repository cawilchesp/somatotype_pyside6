"""
Database

This file contains class Database Dialog.

To configure the database access, it requires:

Host: Host IP address or 'localhost'
Port: Port number
Name: Database name previously created
Username: Database access username
Password: Database access password
"""

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings

from components.md3_button import MD3Button
from components.md3_card import MD3Card
from components.md3_textfield import MD3TextField
from components.md3_window import MD3Window

import sys


class Database_UI(QtWidgets.QDialog):
    def __init__(self, parent):
        """ UI Database dialog class """
        super(Database_UI, self).__init__(parent)
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.database_widgets = {}

        # -------------
        # Dialog Window
        # -------------
        (width, height) = (304, 412)
        self.database_widgets['database_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'minimum_size': (width, height),
            'maximum_size': (width, height),
            'labels': ('Configuración de la Base de Datos', 'Database Settings'),
            'theme': self.theme_value, 
            'language': self.language_value } )
        
        # ------------------
        # Card Database Form
        # ------------------
        self.database_widgets['database_form_card'] = MD3Card(parent, { 
            'name': 'database_form_card',
            'position': (8, 8),
            'size': (width-16, height - 16), 
            'type': 'filled',
            'labels': ('Información de la Base de Datos', 'Database Information'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.database_widgets['host_textfield'] = MD3TextField(self.database_widgets['database_form_card'], {
            'name': 'host_textfield',
            'position': (8, 48),
            'width': width - 32,
            'labels': ('Host', 'Host'),
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.database_widgets['port_textfield'] = MD3TextField(self.database_widgets['database_form_card'], {
            'name': 'port_textfield',
            'position': (8, 108),
            'width': width - 32,
            'labels': ('Puerto', 'Port'),
            'type': 'integer',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.database_widgets['name_textfield'] = MD3TextField(self.database_widgets['database_form_card'], {
            'name': 'name_textfield',
            'position': (8, 168),
            'width': width - 32,
            'labels': ('Nombre', 'Name'),
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.database_widgets['user_textfield'] = MD3TextField(self.database_widgets['database_form_card'], {
            'name': 'user_textfield',
            'position': (8, 228),
            'width': width - 32,
            'labels': ('Usuario', 'Username'),
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.database_widgets['password_textfield'] = MD3TextField(self.database_widgets['database_form_card'], {
            'name': 'password_textfield',
            'position': (8, 288),
            'width': width - 32,
            'labels': ('Contraseña', 'Password'),
            'type': 'password',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        # ---------------------
        # Buttons Ok and Cancel
        # ---------------------
        self.database_widgets['cancel_button'] = MD3Button(self.database_widgets['database_form_card'], {
            'name': 'cancel_button',
            'position': (width - 232, height - 56),
            'width': 100,
            'type': 'text',
            'labels': ('Cancelar', 'Cancel'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_cancel_button_clicked } )

        self.database_widgets['ok_button'] = MD3Button(self.database_widgets['database_form_card'], {
            'name': 'ok_button',
            'position': (width - 124, height - 56),
            'width': 100,
            'type': 'text',
            'enabled': False,
            'labels': ('Aceptar', 'Ok'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_ok_button_clicked } )
