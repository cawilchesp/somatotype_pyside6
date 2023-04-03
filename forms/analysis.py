"""
Analysis

This file contains class Analysis Dialog.

To provide the analysis information, it requires:

triceps
subescapular
supraespinal
pantorrilla

altura
humero
femur
biceps
tricipital
pantorrilla_perimetro
pantorrilla_pliegue

weight
"""

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings

from components.md3_textfield import MD3TextField

import sys
from pathlib import Path

from forms.analysis_ui import AnalysisUI


class AnalysisForm(QtWidgets.QDialog):
    def __init__(self):
        """ UI Patient dialog class """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.analysis_data = None

        self.form_fill_state = {
            'height_textfield' : False,
            'weight_textfield' : False,
            'triceps_textfield' : False,
            'subscapular_textfield' : False,
            'supraspinale_textfield' : False,
            'biceps_textfield' : False,
            'forearm_textfield' : False,
            'humerus_textfield' : False,
            'femur_textfield' : False,
            'knee_textfield' : False
        }

        # ----------------
        # Generación de UI
        # ----------------
        self.analysis_ui = AnalysisUI(self)


    def on_textEdited(self) -> None:
        self.enable_ok_button()


    def on_ok_button_clicked(self) -> None:
        """ Saving form values """
        self.analysis_data = {
            'height_value': self.analysis_ui.analysis_widgets['height_textfield'].text_field.text(),
            'weight_value': self.analysis_ui.analysis_widgets['weight_textfield'].text_field.text(),
            'triceps_value': self.analysis_ui.analysis_widgets['triceps_textfield'].text_field.text(),
            'subscapular_value': self.analysis_ui.analysis_widgets['subscapular_textfield'].text_field.text(),
            'supraspinale_value': self.analysis_ui.analysis_widgets['supraspinale_textfield'].text_field.text(),
            'biceps_value': self.analysis_ui.analysis_widgets['biceps_textfield'].text_field.text(),
            'forearm_value': self.analysis_ui.analysis_widgets['forearm_textfield'].text_field.text(),
            'humerus_value': self.analysis_ui.analysis_widgets['humerus_textfield'].text_field.text(),
            'femur_value': self.analysis_ui.analysis_widgets['femur_textfield'].text_field.text(),
            'knee_value': self.analysis_ui.analysis_widgets['knee_textfield'].text_field.text()
        }
        self.close()


    def on_cancel_button_clicked(self) -> None:
        """ Close dialog window without saving """
        self.close()

    
    def enable_ok_button(self) -> bool:
        """ Enable OK button if all form spaces are filled """
        for key in self.analysis_ui.analysis_widgets.keys():
            if (isinstance(self.analysis_ui.analysis_widgets[key], MD3TextField)
                    and self.analysis_ui.analysis_widgets[key].text_field.text() == ''):
                self.form_fill_state[key] = False
            else: 
                self.form_fill_state[key] = True

        if False in self.form_fill_state.values():
            return self.analysis_ui.analysis_widgets['ok_button'].setEnabled(False)
        else:
            return self.analysis_ui.analysis_widgets['ok_button'].setEnabled(True)