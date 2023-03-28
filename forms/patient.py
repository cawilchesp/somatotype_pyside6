"""
Patient

This file contains class Patient Dialog.

To provide the patient information, it requires:

Last Name
First Name
ID Type: CC, TI
ID Number
Birth Date
Sex: F, M
Weight
Weight Unit: Kg, Lb
Height
Height Unit: m, ft'in"
Body Mass Index: BMI is calculated from weight and height values and units
"""

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings, QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator

import sys

from forms.patient_ui import PatientUI


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

        self.patient_data = {
            'last_name': None,
            'first_name': None,
            'id_type': None,
            'id': None,
            'birth_date': None,
            'sex': None,
            'weight': None,
            'weight_unit': None,
            'height': None,
            'height_unit': None,
            'bmi': None
        }

        self.form_fill_state = {
            'last_name_state': False,
            'first_name_state': False,
            'id_button_state': False,
            'id_textfield_state': False,
            'sex_button_state': False,
            'weight_button_state': False,
            'weight_textfield_state': False,
            'height_button_state': False,
            'height_textfield_state': False
        }

        # ----------------
        # Generación de UI
        # ----------------
        self.patient_ui = PatientUI(self)

    # ---------
    # Funciones
    # ---------
    def on_last_name_textEdited(self) -> None:
        if self.patient_ui.patient_widgets['last_name_textfield'].text_field.text() == '':
            self.form_fill_state['last_name_state'] = False
        else:
            self.form_fill_state['last_name_state'] = True
        self.enable_ok_button()


    def on_first_name_textEdited(self) -> None:
        if self.patient_ui.patient_widgets['first_name_textfield'].text_field.text() == '':
            self.form_fill_state['first_name_state'] = False
        else:
            self.form_fill_state['first_name_state'] = True
        self.enable_ok_button()


    def on_cc_button_clicked(self) -> None:
        """ Id type option for segmented buttons """
        self.patient_ui.patient_widgets['cc_button'].setState(True, self.theme_value)
        self.patient_ui.patient_widgets['ti_button'].setState(False, self.theme_value)

        if (self.patient_ui.patient_widgets['cc_button'].isChecked() or
            self.patient_ui.patient_widgets['ti_button'].isChecked()):
            self.form_fill_state['id_button_state'] = True
        else:
            self.form_fill_state['id_button_state'] = False
        self.enable_ok_button()


    def on_ti_button_clicked(self) -> None:
        """ Id type option for segmented buttons """
        self.patient_ui.patient_widgets['cc_button'].setState(False, self.theme_value)
        self.patient_ui.patient_widgets['ti_button'].setState(True, self.theme_value)

        if (self.patient_ui.patient_widgets['cc_button'].isChecked() or
            self.patient_ui.patient_widgets['ti_button'].isChecked()):
            self.form_fill_state['id_button_state'] = True
        else:
            self.form_fill_state['id_button_state'] = False
        self.enable_ok_button()


    def on_id_textEdited(self) -> None:
        if self.patient_ui.patient_widgets['id_textfield'].text_field.text() == '':
            self.form_fill_state['id_textfield_state'] = False
        else:
            self.form_fill_state['id_textfield_state'] = True
        self.enable_ok_button()


    def on_female_button_clicked(self) -> None:
        """ Sex option for segmented buttons """
        self.patient_ui.patient_widgets['female_button'].setState(True, self.theme_value)
        self.patient_ui.patient_widgets['male_button'].setState(False, self.theme_value)

        if (self.patient_ui.patient_widgets['female_button'].isChecked() or
            self.patient_ui.patient_widgets['male_button'].isChecked()):
            self.form_fill_state['sex_button_state'] = True
        else:
            self.form_fill_state['sex_button_state'] = False
        self.enable_ok_button()


    def on_male_button_clicked(self) -> None:
        """ Sex option for segmented buttons """
        self.patient_ui.patient_widgets['female_button'].setState(False, self.theme_value)
        self.patient_ui.patient_widgets['male_button'].setState(True, self.theme_value)

        if (self.patient_ui.patient_widgets['female_button'].isChecked() or
            self.patient_ui.patient_widgets['male_button'].isChecked()):
            self.form_fill_state['sex_button_state'] = True
        else:
            self.form_fill_state['sex_button_state'] = False
        self.enable_ok_button()


    def on_weight_textEdited(self) -> None:
        """ Weight value to calculate BMI """
        if self.patient_ui.patient_widgets['weight_textfield'].text_field.text() == '':
            self.form_fill_state['weight_textfield_state'] = False
        else:
            self.form_fill_state['weight_textfield_state'] = True
        self.enable_ok_button()
    
        self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{self.bmi_calculation():.1f}')


    def on_kg_button_clicked(self, state: bool) -> None:
        """ Weight unit option for segmented buttons """
        self.patient_ui.patient_widgets['kg_button'].setState(True, self.theme_value)
        self.patient_ui.patient_widgets['lb_button'].setState(False, self.theme_value)
       
        if (self.patient_ui.patient_widgets['kg_button'].isChecked() or
            self.patient_ui.patient_widgets['lb_button'].isChecked()):
            self.form_fill_state['weight_button_state'] = True
        else:
            self.form_fill_state['weight_button_state'] = False
        self.enable_ok_button()

        self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{self.bmi_calculation():.1f}')


    def on_lb_button_clicked(self, state: bool) -> None:
        """ Weight unit option for segmented buttons """
        self.patient_ui.patient_widgets['kg_button'].setState(False, self.theme_value)
        self.patient_ui.patient_widgets['lb_button'].setState(True, self.theme_value)
        
        if (self.patient_ui.patient_widgets['kg_button'].isChecked() or
            self.patient_ui.patient_widgets['lb_button'].isChecked()):
            self.form_fill_state['weight_button_state'] = True
        else:
            self.form_fill_state['weight_button_state'] = False
        self.enable_ok_button()

        self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{self.bmi_calculation():.1f}')


    def on_height_textEdited(self) -> None:
        """ Height value to calculate BMI """
        if self.patient_ui.patient_widgets['height_textfield'].text_field.text() == '':
            self.form_fill_state['height_textfield_state'] = False
        else:
            self.form_fill_state['height_textfield_state'] = True
        self.enable_ok_button()

        self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{self.bmi_calculation():.1f}')


    def on_m_button_clicked(self) -> None:
        """ Height unit option for segmented buttons """
        self.patient_ui.patient_widgets['m_button'].setState(True, self.theme_value)
        self.patient_ui.patient_widgets['ft_in_button'].setState(False, self.theme_value)
        
        pattern = r'[0-3]\.(\d{1,2})'
        reg_exp = QRegularExpressionValidator(QRegularExpression(f'{pattern}'))
        self.patient_ui.patient_widgets['height_textfield'].text_field.setValidator(reg_exp)

        if (self.patient_ui.patient_widgets['m_button'].isChecked() or
            self.patient_ui.patient_widgets['ft_in_button'].isChecked()):
            self.form_fill_state['height_button_state'] = True
        else:
            self.form_fill_state['height_button_state'] = False
        self.patient_ui.patient_widgets['height_textfield'].text_field.setText('')
        self.form_fill_state['height_textfield_state'] = False

        self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{self.bmi_calculation():.1f}')


    def on_ft_in_button_clicked(self) -> None:
        """ Height unit option for segmented buttons """
        self.patient_ui.patient_widgets['m_button'].setState(False, self.theme_value)
        self.patient_ui.patient_widgets['ft_in_button'].setState(True, self.theme_value)
        
        pattern = r'[0-9]\'([0-9]|10|11|12)\"'
        reg_exp = QRegularExpressionValidator(QRegularExpression(f'{pattern}'))
        self.patient_ui.patient_widgets['height_textfield'].text_field.setValidator(reg_exp)

        if (self.patient_ui.patient_widgets['m_button'].isChecked() or
            self.patient_ui.patient_widgets['ft_in_button'].isChecked()):
            self.form_fill_state['height_button_state'] = True
        else:
            self.form_fill_state['height_button_state'] = False
        self.patient_ui.patient_widgets['height_textfield'].text_field.setText('')
        self.form_fill_state['height_textfield_state'] = False

        self.patient_ui.patient_widgets['bmi_value_label'].setText(f'{self.bmi_calculation():.1f}')
        

    def on_ok_button_clicked(self) -> None:
        """ Checking and saving form values """

        self.patient_data['last_name'] = self.patient_ui.patient_widgets['last_name_textfield'].text_field.text()
        self.patient_data['first_name'] = self.patient_ui.patient_widgets['first_name_textfield'].text_field.text()
        if self.patient_ui.patient_widgets['cc_button'].isChecked():
            self.patient_data['id_type'] = self.patient_ui.patient_widgets['cc_button'].text()
        elif self.patient_ui.patient_widgets['ti_button'].isChecked():
            self.patient_data['id_type'] = self.patient_ui.patient_widgets['ti_button'].text()
        self.patient_data['id'] = self.patient_ui.patient_widgets["id_textfield"].text_field.text()
        self.patient_data['birth_date'] = self.patient_ui.patient_widgets['birth_date'].text_field.text()
        if self.patient_ui.patient_widgets['female_button'].isChecked():
            self.patient_data['sex'] = self.patient_ui.patient_widgets['female_button'].text()
        elif self.patient_ui.patient_widgets['male_button'].isChecked():
            self.patient_data['sex'] = self.patient_ui.patient_widgets['male_button'].text()
        self.patient_data['weight'] = self.patient_ui.patient_widgets["weight_textfield"].text_field.text()
        if self.patient_ui.patient_widgets['kg_button'].isChecked():
            self.patient_data['weight_unit'] = self.patient_ui.patient_widgets['kg_button'].text()
        elif self.patient_ui.patient_widgets['lb_button'].isChecked():
            self.patient_data['weight_unit'] = self.patient_ui.patient_widgets['lb_button'].text()
        self.patient_data['height'] = self.patient_ui.patient_widgets["height_textfield"].text_field.text()
        if self.patient_ui.patient_widgets['m_button'].isChecked():
            self.patient_data['height_unit'] = self.patient_ui.patient_widgets['m_button'].text()
        elif self.patient_ui.patient_widgets['ft_in_button'].isChecked():
            self.patient_data['height_unit'] = self.patient_ui.patient_widgets['ft_in_button'].text()
        self.patient_data['bmi'] = self.patient_ui.patient_widgets['bmi_value_label'].text()

        self.close()


    def on_cancel_button_clicked(self) -> None:
        """ Close dialog window without saving """
        self.close()


    def enable_ok_button(self) -> bool:
        """ Enable OK button if all form spaces are filled """
        if False in self.form_fill_state.values():
            return self.patient_ui.patient_widgets['ok_button'].setEnabled(False)
        else:
            return self.patient_ui.patient_widgets['ok_button'].setEnabled(True)
        
    
    def bmi_calculation(self) -> float:
        """ Calculate BMI from weight and height values """
        if (self.form_fill_state['weight_textfield_state']
            and self.form_fill_state['weight_button_state']
            and self.form_fill_state['height_textfield_state']
            and self.form_fill_state['height_button_state'] ):

            weight_value = float(self.patient_ui.patient_widgets['weight_textfield'].text_field.text())
            if self.patient_ui.patient_widgets['lb_button'].isChecked():
                weight_kg = weight_value * 0.454
            else:
                weight_kg = weight_value

            height_value = self.patient_ui.patient_widgets['height_textfield'].text_field.text()
            if self.patient_ui.patient_widgets['ft_in_button'].isChecked():
                if len(height_value) > 3:
                    height_value = height_value.replace("'","").replace("\"","")
                    height_in = float(height_value[0]) * 12 + float(height_value[1:])
                    height_m = height_in * 0.0254
                else:
                    height_m = 1.0
            else:
                height_m = float(height_value)

            return weight_kg / (height_m * height_m)
        else:
            return 0.0