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

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

import sys

import material3_components as mt3


class Database(QtWidgets.QDialog):
    def __init__(self):
        """ UI Database dialog class """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.regExp1 = QRegularExpressionValidator(QRegularExpression('[0-9.]{1,7}'), self)

        self.database_data = None

        # ----------------
        # Generación de UI
        # ----------------
        width = 304
        height = 412
        screen_x = int(self.screen().availableGeometry().width() / 2 - (width / 2))
        screen_y = int(self.screen().availableGeometry().height() / 2 - (height / 2))

        if self.language_value == 0: self.setWindowTitle('Base de Datos')
        elif self.language_value == 1: self.setWindowTitle('Database')
        self.setGeometry(screen_x, screen_y, width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.setModal(True)
        self.setObjectName('object_database')
        if self.theme_value:
            self.setStyleSheet(f'QWidget#object_database {{ background-color: #E5E9F0;'
                f'color: #000000 }}')
        else:
            self.setStyleSheet(f'QWidget#object_database {{ background-color: #3B4253;'
                f'color: #E5E9F0 }}')


        self.database_card = mt3.Card(self, 'database_card', (8, 8, width-16, height-16),
            ('Información de la Base de Datos', 'Database Information'), 
            self.theme_value, self.language_value)
        
        y, w = 48, width - 32
        self.host_text = mt3.TextField(self.database_card,
            (8, y, w), ('Host', 'Host'), self.theme_value, self.language_value)

        y += 60
        self.port_text = mt3.TextField(self.database_card,
            (8, y, w), ('Puerto', 'Port'), self.theme_value, self.language_value)
        self.port_text.text_field.setValidator(self.regExp1)

        y += 60
        self.name_text = mt3.TextField(self.database_card,
            (8, y, w), ('Nombre', 'Name'), self.theme_value, self.language_value)
        
        y += 60
        self.user_text = mt3.TextField(self.database_card,
            (8, y, w), ('Usuario', 'Username'), self.theme_value, self.language_value)

        y += 60
        self.password_text = mt3.TextField(self.database_card,
            (8, y, w), ('Contraseña', 'Password'), self.theme_value, self.language_value)
        
        y += 68
        self.aceptar_button = mt3.TextButton(self.database_card, 'aceptar_button',
            (w-200, y, 100), ('Aceptar', 'Ok'), 'done.png', self.theme_value, self.language_value)
        self.aceptar_button.clicked.connect(self.on_aceptar_button_clicked)

        self.cancelar_button = mt3.TextButton(self.database_card, 'cancelar_button',
            (w-92, y, 100), ('Cancelar', 'Cancel'), 'close.png', self.theme_value, self.language_value)
        self.cancelar_button.clicked.connect(self.on_cancelar_button_clicked)

    # ---------
    # Funciones
    # ---------
    def on_aceptar_button_clicked(self):
        """ Save database information in settings file """
        if (self.host_text.text_field.text() == '' or self.port_text.text_field.text() == '' or 
                self.name_text.text_field.text() == '' or self.user_text.text_field.text() == '' or 
                self.password_text.text_field.text() == ''):
                
            if self.language_value == 0:
                QtWidgets.QMessageBox.critical(self, 'Error en el Formulario', 'Hace falta información de la base de datos')
            elif self.language_value == 1:
                QtWidgets.QMessageBox.critical(self, 'Form Error', 'Database information is missing')
        else:
            self.database_data = {
                'db_host': self.host_text.text_field.text(),
                'db_port': self.port_text.text_field.text(),
                'db_name': self.name_text.text_field.text(),
                'db_user': self.user_text.text_field.text(),
                'db_password': self.password_text.text_field.text()
            }

            self.settings.setValue('db_host', self.host_text.text_field.text())
            self.settings.setValue('db_port', self.port_text.text_field.text())
            self.settings.setValue('db_name', self.name_text.text_field.text())
            self.settings.setValue('db_user', self.user_text.text_field.text())
            self.settings.setValue('db_password', self.password_text.text_field.text())

            self.settings.sync()

            self.close()

    def on_cancelar_button_clicked(self):
        """ Close dialog window without saving """
        self.close()