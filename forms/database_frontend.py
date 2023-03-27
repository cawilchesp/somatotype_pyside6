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

from components.md3_textfield import MD3TextField

import sys

from forms.database_ui import Database_UI


class DatabaseForm(QtWidgets.QDialog):
    def __init__(self):
        """ UI Database dialog class """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.database_data = None

        self.form_fill_state = {
            'host_textfield': False,
            'port_textfield': False,
            'name_textfield': False,
            'user_textfield': False,
            'password_textfield': False
        }

        # ----------------
        # Generación de UI
        # ----------------
        self.database_ui = Database_UI(self)


    def on_textEdited(self) -> None:
        self.enable_ok_button()


    def on_ok_button_clicked(self):
        """ Save database information in settings file """
        self.database_data = {
            'db_host': self.database_ui.database_widgets['host_textfield'].text_field.text(),
            'db_port': self.database_ui.database_widgets['port_textfield'].text_field.text(),
            'db_name': self.database_ui.database_widgets['name_textfield'].text_field.text(),
            'db_user': self.database_ui.database_widgets['user_textfield'].text_field.text(),
            'db_password': self.database_ui.database_widgets['password_textfield'].text_field.text()
        }

        # self.settings.setValue('db_host', self.host_text.text_field.text())
        # self.settings.setValue('db_port', self.port_text.text_field.text())
        # self.settings.setValue('db_name', self.name_text.text_field.text())
        # self.settings.setValue('db_user', self.user_text.text_field.text())
        # self.settings.setValue('db_password', self.password_text.text_field.text())

        # self.settings.sync()

        self.close()

    def on_cancel_button_clicked(self):
        """ Close dialog window without saving """
        self.close()


    def enable_ok_button(self) -> bool:
        """ Enable OK button if all form spaces are filled """
        for key in self.database_ui.database_widgets.keys():
            if (isinstance(self.database_ui.database_widgets[key], MD3TextField)
                    and self.database_ui.database_widgets[key].text_field.text() == ''):
                self.form_fill_state[key] = False
            else: 
                self.form_fill_state[key] = True

        if False in self.form_fill_state.values():
            return self.database_ui.database_widgets['ok_button'].setEnabled(False)
        else:
            return self.database_ui.database_widgets['ok_button'].setEnabled(True)