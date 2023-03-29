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
            'triceps_text' : False,
            'subescapular_text' : False,
            'supraespinal_text' : False,
            'pantorrilla_text' : False,
            'altura_text' : False,
            'humero_text' : False,
            'femur_text' : False,
            'biceps_text' : False,
            'tricipital_text' : False,
            'pantorrilla_perimetro_text' : False,
            'pantorrilla_pliegue_text' : False,
            'weight_textfield' : False
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
            'triceps_text' : self.analysis_ui.analysis_widgets['triceps_text'].text_field.text(),
            'subescapular_text' : self.analysis_ui.analysis_widgets['subescapular_text'].text_field.text(),
            'supraespinal_text' : self.analysis_ui.analysis_widgets['supraespinal_text'].text_field.text(),
            'pantorrilla_text' : self.analysis_ui.analysis_widgets['pantorrilla_text'].text_field.text(),
            'altura_text' : self.analysis_ui.analysis_widgets['altura_text'].text_field.text(),
            'humero_text' : self.analysis_ui.analysis_widgets['humero_text'].text_field.text(),
            'femur_text' : self.analysis_ui.analysis_widgets['femur_text'].text_field.text(),
            'biceps_text' : self.analysis_ui.analysis_widgets['biceps_text'].text_field.text(),
            'tricipital_text' : self.analysis_ui.analysis_widgets['tricipital_text'].text_field.text(),
            'pantorrilla_perimetro_text' : self.analysis_ui.analysis_widgets['pantorrilla_perimetro_text'].text_field.text(),
            'pantorrilla_pliegue_text' : self.analysis_ui.analysis_widgets['pantorrilla_pliegue_text'].text_field.text(),
            'weight_textfield' : self.analysis_ui.analysis_widgets['weight_textfield'].text_field.text()
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