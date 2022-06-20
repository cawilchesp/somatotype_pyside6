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
from PyQt6.QtCore import QSettings, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

import sys
import math

import material3_components as mt3

class Patient(QtWidgets.QDialog):
    def __init__(self):
        """ UI Patient dialog class """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.regExp1 = QRegularExpressionValidator(QRegularExpression('[A-Za-zÁÉÍÓÚáéíóú ]{1,30}'), self)
        self.regExp2 = QRegularExpressionValidator(QRegularExpression('[0-9]{1,10}'), self)
        self.regExp3 = QRegularExpressionValidator(QRegularExpression('[0-9.]{1,5}'), self)

        self.patient_data = None

        # ----------------
        # Generación de UI
        # ----------------
        width = 348
        height = 600
        screen_x = int(self.screen().availableGeometry().width() / 2 - (width / 2))
        screen_y = int(self.screen().availableGeometry().height() / 2 - (height / 2))

        if self.language_value == 0:
            self.setWindowTitle('Datos del Paciente')
        elif self.language_value == 1:
            self.setWindowTitle("Patient's Data")
        self.setGeometry(screen_x, screen_y, width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.setModal(True)
        self.setObjectName('object_patient')
        if self.theme_value:
            self.setStyleSheet(f'QWidget#object_patient {{ background-color: #E5E9F0;'
                f'color: #000000 }}')
        else:
            self.setStyleSheet(f'QWidget#object_patient {{ background-color: #3B4253;'
                f'color: #E5E9F0 }}')


        self.paciente_card = mt3.Card(self, 'paciente_card',
            (8, 8, width-16, height-16), ('Información del Paciente', 'Patient Information'), 
            self.theme_value, self.language_value)
        
        y, w = 68, width - 32
        self.apellido_text = mt3.TextField(self.paciente_card,
            (8, y, w), ('Apellidos', 'Last Name'), self.theme_value, self.language_value)
        self.apellido_text.text_field.setValidator(self.regExp1)

        y += 68
        self.nombre_text = mt3.TextField(self.paciente_card,
            (8, y, w), ('Nombres', 'First Name'), 
            self.theme_value, self.language_value)
        self.nombre_text.text_field.setValidator(self.regExp1)

        y += 68
        self.id_label = mt3.FieldLabel(self.paciente_card, 'id_label',
            (8, y), ('Tipo de ID', 'ID Type'), self.theme_value, self.language_value)

        self.cc_button = mt3.SegmentedButton(self.paciente_card, 'cc_button',
            (8, y+20, 76), ('CC', 'CC'), ('done.png','none.png'), 'left', 
            False, self.theme_value, self.language_value)
        self.cc_button.clicked.connect(self.on_cc_button_clicked)

        self.ti_button = mt3.SegmentedButton(self.paciente_card, 'ti_button',
            (84, y+20, 76), ('TI', 'TI'), ('done.png','none.png'), 'right', 
            False, self.theme_value, self.language_value)
        self.ti_button.clicked.connect(self.on_ti_button_clicked)

        self.id_text = mt3.TextField(self.paciente_card,
            (168, y, 156), ('Número de ID', 'ID Number'), 
            self.theme_value, self.language_value)
        self.id_text.text_field.setValidator(self.regExp2)

        y += 68
        self.fecha_date = mt3.DateField(self.paciente_card,
            (8, y, 164), ('Fecha de Nacimiento', 'Birth Date'), 
            self.theme_value, self.language_value)
        
        self.sexo_label = mt3.FieldLabel(self.paciente_card, 'sexo_label',
            (188, y), ('Sexo', 'Sex'), self.theme_value, self.language_value)

        self.f_button = mt3.SegmentedButton(self.paciente_card, 'f_button',
            (188, y+20, 68), ('F', 'F'), ('done.png','none.png'), 'left', 
            False, self.theme_value, self.language_value)
        self.f_button.clicked.connect(self.on_f_button_clicked)

        self.m_button = mt3.SegmentedButton(self.paciente_card, 'm_button',
            (256, y+20, 68), ('M', 'M'), ('done.png','none.png'), 'right', 
            False, self.theme_value, self.language_value)
        self.m_button.clicked.connect(self.on_m_button_clicked)

        y += 68
        self.peso_text = mt3.TextField(self.paciente_card,
            (8, y, 100), ('Peso', 'Weight'), 
            self.theme_value, self.language_value)
        self.peso_text.text_field.setValidator(self.regExp3)
        self.peso_text.text_field.textEdited.connect(self.on_peso_text_textEdited)

        self.peso_unit_label = mt3.FieldLabel(self.paciente_card, 'peso_unit_label',
            (116, y), ('Unidad de Peso', 'Weight Unit'), self.theme_value, self.language_value)

        self.kg_button = mt3.SegmentedButton(self.paciente_card, 'kg_button',
            (116, y+20, 76), ('Kg', 'Kg'), ('done.png','none.png'), 'left', 
            False, self.theme_value, self.language_value)
        self.kg_button.clicked.connect(self.on_kg_button_clicked)

        self.lb_button = mt3.SegmentedButton(self.paciente_card, 'lb_button',
            (192, y+20, 76), ('Lb', 'Lb'), ('done.png','none.png'), 'right', 
            False, self.theme_value, self.language_value)
        self.lb_button.clicked.connect(self.on_lb_button_clicked)

        y += 68
        self.altura_text = mt3.TextField(self.paciente_card,
            (8, y, 100), ('Altura', 'Height'), 
            self.theme_value, self.language_value)
        self.altura_text.text_field.setValidator(self.regExp3)
        self.altura_text.text_field.textEdited.connect(self.on_altura_text_textEdited)

        self.altura_unit_label = mt3.FieldLabel(self.paciente_card, 'altura_unit_label',
            (116, y), ('Unidad de Altura', 'Height Unit'), self.theme_value, self.language_value)

        self.mt_button = mt3.SegmentedButton(self.paciente_card, 'mt_button',
            (116, y+20, 76), ('m', 'm'), ('done.png','none.png'), 'left', 
            False, self.theme_value, self.language_value)
        self.mt_button.clicked.connect(self.on_mt_button_clicked)

        self.fi_button = mt3.SegmentedButton(self.paciente_card, 'fi_button',
            (192, y+20, 76), ('ft - in', 'ft - in'), ('done.png','none.png'), 'right', 
            False, self.theme_value, self.language_value)
        self.fi_button.clicked.connect(self.on_fi_button_clicked)

        y += 68
        self.bmi_label = mt3.FieldLabel(self.paciente_card, 'bmi_label',
            (8, y), ('Índice de Masa Corporal', 'Body Mass Index'), self.theme_value, self.language_value)

        self.bmi_value_label = mt3.ValueLabel(self.paciente_card, 'bmi_value_label',
            (8, y+20, w), self.theme_value)
        
        y += 68
        self.aceptar_button = mt3.TextButton(self.paciente_card, 'aceptar_button',
            (w-200, y, 100), ('Aceptar', 'Ok'), 'done.png', self.theme_value, self.language_value)
        self.aceptar_button.clicked.connect(self.on_aceptar_button_clicked)

        self.cancelar_button = mt3.TextButton(self.paciente_card, 'cancelar_button',
            (w-92, y, 100), ('Cancelar', 'Cancel'), 'close.png', self.theme_value, self.language_value)
        self.cancelar_button.clicked.connect(self.on_cancelar_button_clicked)


    # ---------
    # Funciones
    # ---------
    def on_cc_button_clicked(self) -> None:
        """ Id type option for segmented buttons """
        self.cc_button.set_state(True)
        
        if self.ti_button.isChecked():
            self.ti_button.set_state(False)


    def on_ti_button_clicked(self) -> None:
        """ Id type option for segmented buttons """
        self.ti_button.set_state(True)
        
        if self.cc_button.isChecked():
            self.cc_button.set_state(False)


    def on_f_button_clicked(self) -> None:
        """ Sex option for segmented buttons """
        self.f_button.set_state(True)
        
        if self.m_button.isChecked():
            self.m_button.set_state(False)


    def on_m_button_clicked(self) -> None:
        """ Sex option for segmented buttons """
        self.m_button.set_state(True)
        
        if self.f_button.isChecked():
            self.f_button.set_state(False)


    def on_kg_button_clicked(self) -> None:
        """ Weight unit option for segmented buttons """
        self.kg_button.set_state(True)
        
        if self.lb_button.isChecked():
            self.lb_button.set_state(False)

        if self.peso_text.text_field.text() != '' and self.altura_text.text_field.text() != '':
            if (self.mt_button.isChecked() or self.fi_button.isChecked()):
                altura_m = 0.0
                if self.mt_button.isChecked():
                    altura_m = float(self.altura_text.text_field.text())
                elif self.fi_button.isChecked():
                    altura_ft = math.floor(float(self.altura_text.text_field.text()))
                    altura_in = (float(self.altura_text.text_field.text()) - altura_ft) * 100
                    altura_m = ((altura_ft * 12) + altura_in) * 2.54 / 100

                bmi_value = float(self.peso_text.text_field.text()) / (altura_m * altura_m)
                self.bmi_value_label.setText(f'{bmi_value:.1f}')


    def on_lb_button_clicked(self) -> None:
        """ Weight unit option for segmented buttons """
        self.lb_button.set_state(True)
        
        if self.kg_button.isChecked():
            self.kg_button.set_state(False)

        if self.peso_text.text_field.text() != '' and self.altura_text.text_field.text() != '':
            if (self.mt_button.isChecked() or self.fi_button.isChecked()):
                altura_m = 0.0
                if self.mt_button.isChecked():
                    altura_m = float(self.altura_text.text_field.text())
                elif self.fi_button.isChecked():
                    altura_ft = math.floor(float(self.altura_text.text_field.text()))
                    altura_in = (float(self.altura_text.text_field.text()) - altura_ft) * 100
                    altura_m = ((altura_ft * 12) + altura_in) * 2.54 / 100

                bmi_value = float(self.peso_text.text_field.text()) * 0.454 / (altura_m * altura_m)
                self.bmi_value_label.setText(f'{bmi_value:.1f}')


    def on_mt_button_clicked(self) -> None:
        """ Height unit option for segmented buttons """
        self.mt_button.set_state(True)
        
        if self.fi_button.isChecked():
            self.fi_button.set_state(False)

        if self.peso_text.text_field.text() != '' and self.altura_text.text_field.text() != '':
            if (self.kg_button.isChecked() or self.lb_button.isChecked()):
                peso_kg = 0.0
                if self.kg_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text())
                elif self.lb_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text()) * 0.454

                bmi_value = peso_kg / (float(self.altura_text.text_field.text()) * float(self.altura_text.text_field.text()))
                self.bmi_value_label.setText(f'{bmi_value:.1f}')


    def on_fi_button_clicked(self) -> None:
        """ Height unit option for segmented buttons """
        self.fi_button.set_state(True)
        
        if self.mt_button.isChecked():
            self.mt_button.set_state(False)

        if self.peso_text.text_field.text() != '' and self.altura_text.text_field.text() != '':
            if (self.kg_button.isChecked() or self.lb_button.isChecked()):
                peso_kg = 0.0
                if self.kg_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text())
                elif self.lb_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text()) * 0.454

                altura_ft = math.floor(float(self.altura_text.text_field.text()))
                altura_in = (float(self.altura_text.text_field.text()) - altura_ft) * 100
                altura_m = ((altura_ft * 12) + altura_in) * 2.54 / 100

                bmi_value = peso_kg / (altura_m * altura_m)
                self.bmi_value_label.setText(f'{bmi_value:.1f}')


    def on_peso_text_textEdited(self) -> None:
        """ Weight value to calculate BMI """
        if self.peso_text.text_field.text() != '' and self.altura_text.text_field.text() != '':
            bmi_value = 0.0
            
            if (self.kg_button.isChecked() or self.lb_button.isChecked()):
                peso_kg = 0.0
                if self.kg_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text())
                elif self.lb_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text()) * 0.454
                bmi_value = peso_kg

            if (self.mt_button.isChecked() or self.fi_button.isChecked()):
                altura_m = 0.0
                if self.mt_button.isChecked():
                    altura_m = float(self.altura_text.text_field.text())
                elif self.fi_button.isChecked():
                    altura_ft = math.floor(float(self.altura_text.text_field.text()))
                    altura_in = (float(self.altura_text.text_field.text()) - altura_ft) * 100
                    altura_m = ((altura_ft * 12) + altura_in) * 2.54 / 100
                bmi_value = bmi_value / (altura_m * altura_m)

            self.bmi_value_label.setText(f'{bmi_value:.1f}')


    def on_altura_text_textEdited(self) -> None:
        """ Height value to calculate BMI """
        if self.peso_text.text_field.text() != '' and self.altura_text.text_field.text() != '':
            bmi_value = 0.0
            
            if (self.kg_button.isChecked() or self.lb_button.isChecked()):
                peso_kg = 0.0
                if self.kg_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text())
                elif self.lb_button.isChecked():
                    peso_kg = float(self.peso_text.text_field.text()) * 0.454
                bmi_value = peso_kg

            if (self.mt_button.isChecked() or self.fi_button.isChecked()):
                altura_m = 0.0
                if self.mt_button.isChecked():
                    altura_m = float(self.altura_text.text_field.text())
                elif self.fi_button.isChecked():
                    altura_ft = math.floor(float(self.altura_text.text_field.text()))
                    altura_in = (float(self.altura_text.text_field.text()) - altura_ft) * 100
                    altura_m = ((altura_ft * 12) + altura_in) * 2.54 / 100
                bmi_value = bmi_value / (altura_m * altura_m)

            self.bmi_value_label.setText(f'{bmi_value:.1f}')


    def on_aceptar_button_clicked(self) -> None:
        """ Checking and saving form values """
        if (self.apellido_text.text_field.text() == '' or self.nombre_text.text_field.text() == '' or 
                (not self.cc_button.isChecked() and not self.ti_button.isChecked()) or
                self.id_text.text_field.text() == '' or self.fecha_date.text_field.text() == '' or 
                (not self.f_button.isChecked() and not self.m_button.isChecked()) or
                (not self.kg_button.isChecked() and not self.lb_button.isChecked()) or
                (not self.mt_button.isChecked() and not self.fi_button.isChecked()) or
                self.peso_text.text_field.text() == '' or self.altura_text.text_field.text() == ''):
                
            if self.language_value == 0:
                QtWidgets.QMessageBox.critical(self, 'Error en el Formulario', 'Hacen falta datos del paciente')
            elif self.language_value == 1:
                QtWidgets.QMessageBox.critical(self, 'Form Error', 'Patient data is missing')
        else:
            if self.cc_button.isChecked(): id_type = self.cc_button.text()
            elif self.ti_button.isChecked(): id_type = self.ti_button.text()

            if self.f_button.isChecked(): sex = self.f_button.text()
            elif self.m_button.isChecked(): sex = self.m_button.text()

            if self.kg_button.isChecked(): peso_unit = self.kg_button.text()
            elif self.lb_button.isChecked(): peso_unit = self.lb_button.text()

            if self.mt_button.isChecked(): altura_unit = self.mt_button.text()
            elif self.fi_button.isChecked(): altura_unit = self.fi_button.text()

            self.patient_data = {
                'last_name': self.apellido_text.text_field.text(),
                'first_name': self.nombre_text.text_field.text(),
                'id_type': f'{id_type}',
                'id': f'{self.id_text.text_field.text()}',
                'birth_date': self.fecha_date.text_field.text(),
                'sex': sex,
                'weight': f'{self.peso_text.text_field.text()}',
                'weight_unit': f'{peso_unit}',
                'height': f'{self.altura_text.text_field.text()}',
                'height_unit': f'{altura_unit}',
                'bmi': self.bmi_value_label.text()
            }
            self.close()


    def on_cancelar_button_clicked(self) -> None:
        """ Close dialog window without saving """
        self.close()