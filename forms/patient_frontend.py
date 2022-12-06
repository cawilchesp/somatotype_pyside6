"""
Patient

This file contains class Patient Dialog.

To provide the patient information, it requires:

Last Name
First Name
ID Type:
    CC, TI
ID Number
Birth Date
Sex:
    F, M
Weight
Weight Unit: Kg, Lb
Height
Height Unit: m, ft - in
    Examples for ft - in:
    Correct:
    5.09: 5 ft, 9 in
    5.11: 5 ft, 11 in
    Wrong:
    5.9: 5 ft, 90 in
    5.13: 5 ft, 13 in
Body Mass Index:
    BMI is calculated from weight and height values and units
"""

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings

import sys
import math

from forms.patient_ui import Patient_UI
from backend import ftin2m, lb2kg, bmi


class PatientForm(QtWidgets.QDialog):
    def __init__(self):
        """ UI Patient dialog class """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.patient_data = None

        # ----------------
        # Generación de UI
        # ----------------
        self.patient_ui = Patient_UI(self)

    # ---------
    # Funciones
    # ---------
    def on_last_name_text_textEdited(self) -> None:
        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_first_name_text_textEdited(self) -> None:
        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_id_text_textEdited(self) -> None:
        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_cc_button_clicked(self) -> None:
        """ Id type option for segmented buttons """
        self.patient_ui.patient_widgets['cc_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['ti_button'].isChecked():
            self.patient_ui.patient_widgets['ti_button'].set_state(False, self.theme_value)

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_ti_button_clicked(self) -> None:
        """ Id type option for segmented buttons """
        self.patient_ui.patient_widgets['ti_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['cc_button'].isChecked():
            self.patient_ui.patient_widgets['cc_button'].set_state(False, self.theme_value)

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_f_button_clicked(self) -> None:
        """ Sex option for segmented buttons """
        self.patient_ui.patient_widgets['f_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['m_button'].isChecked():
            self.patient_ui.patient_widgets['m_button'].set_state(False, self.theme_value)

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_m_button_clicked(self) -> None:
        """ Sex option for segmented buttons """
        self.patient_ui.patient_widgets['m_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['f_button'].isChecked():
            self.patient_ui.patient_widgets['f_button'].set_state(False, self.theme_value)

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_kg_button_clicked(self) -> None:
        """ Weight unit option for segmented buttons """
        self.patient_ui.patient_widgets['kg_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['lb_button'].isChecked():
            self.patient_ui.patient_widgets['lb_button'].set_state(False, self.theme_value)

        if (self.patient_ui.patient_widgets['weight_text'].text_field.text() != '' 
                and self.patient_ui.patient_widgets['height_text'].text_field.text() != ''):
            height_value = float(self.patient_ui.patient_widgets['height_text'].text_field.text())
            weight_value = float(self.patient_ui.patient_widgets['weight_text'].text_field.text())
            
            if self.patient_ui.patient_widgets['fi_button'].isChecked():
                height_ft = math.floor(height_value)
                height_in = (height_value - height_ft) * 100
                height_m = ftin2m(height_ft, height_in)
            else:
                height_m = height_value
                    
            self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{bmi(weight_value, height_m):.1f}')
        
        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_lb_button_clicked(self) -> None:
        """ Weight unit option for segmented buttons """
        self.patient_ui.patient_widgets['lb_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['kg_button'].isChecked():
            self.patient_ui.patient_widgets['kg_button'].set_state(False, self.theme_value)

        if (self.patient_ui.patient_widgets['weight_text'].text_field.text() != '' 
                and self.patient_ui.patient_widgets['height_text'].text_field.text() != ''):
            height_value = float(self.patient_ui.patient_widgets['height_text'].text_field.text())
            weight_value = float(self.patient_ui.patient_widgets['weight_text'].text_field.text())

            if self.patient_ui.patient_widgets['fi_button'].isChecked():
                height_ft = math.floor(height_value)
                height_in = (height_value - height_ft) * 100
                height_m = ftin2m(height_ft, height_in)
            else:
                height_m = height_value
        
            self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{bmi(lb2kg(weight_value), height_m):.1f}')

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_mt_button_clicked(self) -> None:
        """ Height unit option for segmented buttons """
        self.patient_ui.patient_widgets['mt_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['fi_button'].isChecked():
            self.patient_ui.patient_widgets['fi_button'].set_state(False, self.theme_value)

        if (self.patient_ui.patient_widgets['weight_text'].text_field.text() != '' 
                and self.patient_ui.patient_widgets['height_text'].text_field.text() != ''):
            height_value = float(self.patient_ui.patient_widgets['height_text'].text_field.text())
            weight_value = float(self.patient_ui.patient_widgets['weight_text'].text_field.text())

            if self.patient_ui.patient_widgets['lb_button'].isChecked():
                weight_kg = lb2kg(weight_value)
            else:
                weight_kg = weight_value
            
            self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{bmi(weight_kg, height_value):.1f}')

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_fi_button_clicked(self) -> None:
        """ Height unit option for segmented buttons """
        self.patient_ui.patient_widgets['fi_button'].set_state(True, self.theme_value)
        
        if self.patient_ui.patient_widgets['mt_button'].isChecked():
            self.patient_ui.patient_widgets['mt_button'].set_state(False, self.theme_value)

        if (self.patient_ui.patient_widgets['weight_text'].text_field.text() != '' 
                and self.patient_ui.patient_widgets['height_text'].text_field.text() != ''):
            height_value = float(self.patient_ui.patient_widgets['height_text'].text_field.text())
            weight_value = float(self.patient_ui.patient_widgets['weight_text'].text_field.text())

            if self.patient_ui.patient_widgets['lb_button'].isChecked():
                weight_kg = lb2kg(weight_value)
            else:
                weight_kg = weight_value

            height_ft = math.floor(height_value)
            height_in = (height_value - height_ft) * 100
            height_m = ftin2m(height_ft, height_in)

            self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{bmi(weight_kg, height_m):.1f}')

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_weight_text_textEdited(self) -> None:
        """ Weight value to calculate BMI """
        if (self.patient_ui.patient_widgets['weight_text'].text_field.text() != '' 
                and self.patient_ui.patient_widgets['height_text'].text_field.text() != ''):
            height_value = float(self.patient_ui.patient_widgets['height_text'].text_field.text())
            weight_value = float(self.patient_ui.patient_widgets['weight_text'].text_field.text())

            if self.patient_ui.patient_widgets['lb_button'].isChecked():
                weight_kg = lb2kg(weight_value)
            else:
                weight_kg = weight_value

            if self.patient_ui.patient_widgets['fi_button'].isChecked():
                height_ft = math.floor(height_value)
                height_in = (height_value - height_ft) * 100
                height_m = ftin2m(height_ft, height_in)
            else:
                height_m = height_value

            self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{bmi(weight_kg, height_m):.1f}')

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_height_text_textEdited(self) -> None:
        """ Height value to calculate BMI """
        if (self.patient_ui.patient_widgets['weight_text'].text_field.text() != '' 
                and self.patient_ui.patient_widgets['height_text'].text_field.text() != ''):
            height_value = float(self.patient_ui.patient_widgets['height_text'].text_field.text())
            weight_value = float(self.patient_ui.patient_widgets['weight_text'].text_field.text())
            
            if self.patient_ui.patient_widgets['lb_button'].isChecked():
                weight_kg = lb2kg(weight_value)
            else:
                weight_kg = weight_value

            if self.patient_ui.patient_widgets['fi_button'].isChecked():
                height_ft = math.floor(height_value)
                height_in = (height_value - height_ft) * 100
                height_m = ftin2m(height_ft, height_in)
            else:
                height_m = height_value

            self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{bmi(weight_kg, height_m):.1f}')

        if self.check_form_fill(): self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        else: self.patient_ui.patient_widgets['ok_button'].setEnabled(False)


    def on_ok_button_clicked(self) -> None:
        """ Checking and saving form values """
        if self.patient_ui.patient_widgets['cc_button'].isChecked(): id_type = self.patient_ui.patient_widgets['cc_button'].text()
        elif self.patient_ui.patient_widgets['ti_button'].isChecked(): id_type = self.patient_ui.patient_widgets['ti_button'].text()
        if self.patient_ui.patient_widgets['f_button'].isChecked(): sex = self.patient_ui.patient_widgets['f_button'].text()
        elif self.patient_ui.patient_widgets['m_button'].isChecked(): sex = self.patient_ui.patient_widgets['m_button'].text()
        if self.patient_ui.patient_widgets['kg_button'].isChecked(): peso_unit = self.patient_ui.patient_widgets['kg_button'].text()
        elif self.patient_ui.patient_widgets['lb_button'].isChecked(): peso_unit = self.patient_ui.patient_widgets['lb_button'].text()
        if self.patient_ui.patient_widgets['mt_button'].isChecked(): altura_unit = self.patient_ui.patient_widgets['mt_button'].text()
        elif self.patient_ui.patient_widgets['fi_button'].isChecked(): altura_unit = self.patient_ui.patient_widgets['fi_button'].text() 

        self.patient_data = {
            'last_name': self.patient_ui.patient_widgets['last_name_text'].text_field.text(),
            'first_name': self.patient_ui.patient_widgets['first_name_text'].text_field.text(),
            'id_type': f'{id_type}',
            'id': f'{self.patient_ui.patient_widgets["id_text"].text_field.text()}',
            'birth_date': self.patient_ui.patient_widgets['birth_date'].text_field.text(),
            'sex': sex,
            'weight': f'{self.patient_ui.patient_widgets["weight_text"].text_field.text()}',
            'weight_unit': f'{peso_unit}',
            'height': f'{self.patient_ui.patient_widgets["height_text"].text_field.text()}',
            'height_unit': f'{altura_unit}',
            'bmi': self.patient_ui.patient_widgets['bmi_value_label'].text()
        }
        self.close()


    def on_cancel_button_clicked(self) -> None:
        """ Close dialog window without saving """
        self.close()


    def check_form_fill(self) -> bool:
        """ Check if all form spaces are filled """
        if (self.patient_ui.patient_widgets['last_name_text'].text_field.text() == '' or
            self.patient_ui.patient_widgets['first_name_text'].text_field.text() == '' or 
            (not self.patient_ui.patient_widgets['cc_button'].isChecked() and
                not self.patient_ui.patient_widgets['ti_button'].isChecked()) or
            self.patient_ui.patient_widgets['id_text'].text_field.text() == '' or
            self.patient_ui.patient_widgets['birth_date'].text_field.text() == '' or 
            (not self.patient_ui.patient_widgets['f_button'].isChecked() and 
                not self.patient_ui.patient_widgets['m_button'].isChecked()) or 
            (not self.patient_ui.patient_widgets['kg_button'].isChecked() and
                not self.patient_ui.patient_widgets['lb_button'].isChecked()) or
            (not self.patient_ui.patient_widgets['mt_button'].isChecked() and 
                not self.patient_ui.patient_widgets['fi_button'].isChecked()) or 
            self.patient_ui.patient_widgets['weight_text'].text_field.text() == '' or 
            self.patient_ui.patient_widgets['height_text'].text_field.text() == ''):

            return False
        else:
            return True