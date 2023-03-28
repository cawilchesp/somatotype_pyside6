"""
Patient

This file contains class Patient Dialog.

To provide the patient information, it requires:

Image Filename

Minimum and Maximum value of Left Foot XT Signal
Minimum and Maximum value of Center Foot XT Signal
Minimum and Maximum value of Right Foot XT Signal

Minimum and Maximum value of Left Foot YT Signal
Minimum and Maximum value of Center Foot YT Signal
Minimum and Maximum value of Right Foot YT Signal
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
        self.default_path = self.settings.value('default_path')

        self.image_data = None

        self.form_fill_state = {
            'filename_textfield': False,
            'left_minimum_XT_text': False,
            'left_maximum_XT_text': False,
            'center_minimum_XT_text': False,
            'center_maximum_XT_text': False,
            'right_minimum_XT_text': False,
            'right_maximum_XT_text': False,
            'left_minimum_YT_text': False,
            'left_maximum_YT_text': False,
            'center_minimum_YT_text': False,
            'center_maximum_YT_text': False,
            'right_minimum_YT_text': False,
            'right_maximum_YT_text': False
        }

        # ----------------
        # Generación de UI
        # ----------------
        self.analysis_ui = AnalysisUI(self)


    def on_filename_button_clicked(self) -> None:
        selected_file = QtWidgets.QFileDialog.getOpenFileName(None,
                'Seleccione la imagen de datos', self.default_path,
                'Archivos de Imágenes (*.png *.jpg *.bmp)')[0]

        if selected_file:
            self.default_path = self.settings.setValue('default_path', str(Path(selected_file).parent))
            self.analysis_ui.image_widgets['filename_textfield'].text_field.setText(selected_file)


    def on_textEdited(self) -> None:
        self.enable_ok_button()


    def on_ok_button_clicked(self) -> None:
        """ Saving form values """
        self.image_data = {
            'image_filename': self.analysis_ui.image_widgets['filename_textfield'].text_field.text(),
            'left_min_xt': self.analysis_ui.image_widgets['left_minimum_XT_text'].text_field.text(),
            'left_max_xt': self.analysis_ui.image_widgets['left_maximum_XT_text'].text_field.text(),
            'center_min_xt': self.analysis_ui.image_widgets['center_minimum_XT_text'].text_field.text(),
            'center_max_xt': self.analysis_ui.image_widgets['center_maximum_XT_text'].text_field.text(),
            'right_min_xt': self.analysis_ui.image_widgets['right_minimum_XT_text'].text_field.text(),
            'right_max_xt': self.analysis_ui.image_widgets['right_maximum_XT_text'].text_field.text(),
            'left_min_yt': self.analysis_ui.image_widgets['left_minimum_YT_text'].text_field.text(),
            'left_max_yt': self.analysis_ui.image_widgets['left_maximum_YT_text'].text_field.text(),
            'center_min_yt': self.analysis_ui.image_widgets['center_minimum_YT_text'].text_field.text(),
            'center_max_yt': self.analysis_ui.image_widgets['center_maximum_YT_text'].text_field.text(),
            'right_min_yt': self.analysis_ui.image_widgets['right_minimum_YT_text'].text_field.text(),
            'right_max_yt': self.analysis_ui.image_widgets['right_maximum_YT_text'].text_field.text()
        }
        self.close()


    def on_cancel_button_clicked(self) -> None:
        """ Close dialog window without saving """
        self.close()

    
    def enable_ok_button(self) -> bool:
        """ Enable OK button if all form spaces are filled """
        for key in self.analysis_ui.image_widgets.keys():
            if (isinstance(self.analysis_ui.image_widgets[key], MD3TextField)
                    and self.analysis_ui.image_widgets[key].text_field.text() == ''):
                self.form_fill_state[key] = False
            else: 
                self.form_fill_state[key] = True

        if False in self.form_fill_state.values():
            return self.analysis_ui.image_widgets['ok_button'].setEnabled(False)
        else:
            return self.analysis_ui.image_widgets['ok_button'].setEnabled(True)