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

from components.md3_window import MD3Window
from components.md3_card import MD3Card
from components.md3_textfield import MD3TextField
from components.md3_label import MD3Label
from components.md3_segmentedbutton import MD3SegmentedButton
from components.md3_datepicker import MD3DatePicker
from components.md3_button import MD3Button

class Patient_UI(QtWidgets.QDialog):
    def __init__(self, parent):
        """ UI Patient dialog class """
        super(Patient_UI, self).__init__(parent)
        
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.regExp1 = QRegularExpressionValidator(QRegularExpression('[A-Za-zÁÉÍÓÚáéíóú ]{1,30}'), self)
        self.regExp2 = QRegularExpressionValidator(QRegularExpression('[0-9]{1,10}'), self)
        self.regExp3 = QRegularExpressionValidator(QRegularExpression('[0-9.]{1,5}'), self)

        self.patient_widgets = {}

        # -------------
        # Dialog Window
        # -------------
        (width, height) = (348, 588)
        self.patient_widgets['patient_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'labels': ('Datos del Paciente',"Patient's Data"),
            'theme': self.theme_value, 
            'language': self.language_value } )
        parent.setMaximumSize(width, height)
        
        # -------------
        # Card Paciente
        # -------------
        self.patient_widgets['patient_form_card'] = MD3Card(parent, { 
            'name': 'patient_form_card',
            'position': (8, 8),
            'size': (width-16, height-16),
            'theme': self.theme_value,
            'labels': ('Información del Paciente', 'Patient Information'), 
            'language': self.language_value } )
 
        self.patient_widgets['last_name_text'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'last_name_text',
            'position': (8, 68),
            'width': width - 32,
            'labels': ('Apellidos', 'Last Name'),
            'regular_expression': self.regExp1,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['last_name_text'].text_field.textEdited.connect(parent.on_last_name_text_textEdited)

        self.patient_widgets['first_name_text'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'first_name_text',
            'position': (8, 136),
            'width': width - 32,
            'labels': ('Nombres', 'First Name'),
            'regular_expression': self.regExp1,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['first_name_text'].text_field.textEdited.connect(parent.on_first_name_text_textEdited)

        self.patient_widgets['id_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'id_label', 
            'position': (8, 204), 
            'width': 164,
            'type': 'subtitle',
            'labels': ('Tipo de ID', 'ID Type'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['cc_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'cc_button',
            'position': (8, 224),
            'width': 76,
            'labels': ('CC', 'CC'),
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } ) 
        self.patient_widgets['cc_button'].clicked.connect(parent.on_cc_button_clicked)

        self.patient_widgets['ti_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'ti_button',
            'position': (84, 224),
            'width': 76,
            'labels': ('TI', 'TI'),
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } ) 
        self.patient_widgets['ti_button'].clicked.connect(parent.on_ti_button_clicked)

        self.patient_widgets['id_text'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'id_text',
            'position': (168, 204),
            'width': 156,
            'labels': ('Número de ID', 'ID Number'),
            'regular_expression': self.regExp2,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['id_text'].text_field.textEdited.connect(parent.on_id_text_textEdited)

        self.patient_widgets['birth_date'] = MD3DatePicker(self.patient_widgets['patient_form_card'], {
            'name': 'birth_date',
            'position': (8, 272),
            'width': 164,
            'labels': ('Fecha de Nacimiento', 'Birth Date'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['sex_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'sex_label',
            'position': (188, 272),
            'width': 164,
            'type': 'subtitle',
            'labels': ('Sexo', 'Sex'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['f_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'f_button',
            'position': (188, 292),
            'width': 68,
            'labels': ('F', 'F'),
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['f_button'].clicked.connect(parent.on_f_button_clicked)

        self.patient_widgets['m_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'm_button',
            'position': (256, 292),
            'width': 68,
            'labels': ('M', 'M'),
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['m_button'].clicked.connect(parent.on_m_button_clicked)

        self.patient_widgets['weight_text'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'weight_text',
            'position': (8, 340),
            'width': 100,
            'labels': ('Peso', 'Weight'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['weight_text'].text_field.textEdited.connect(parent.on_weight_text_textEdited)

        self.patient_widgets['weight_unit_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'weight_unit_label',
            'position': (116, 340),
            'width': 164,
            'type': 'subtitle',
            'labels': ('Unidad de Peso', 'Weight Unit'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['kg_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'kg_button',
            'position': (116, 360),
            'width': 76,
            'labels': ('Kg', 'Kg'),
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['kg_button'].clicked.connect(parent.on_kg_button_clicked)

        self.patient_widgets['lb_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'lb_button',
            'position': (192, 360),
            'width': 76,
            'labels': ('Lb', 'Lb'),
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['lb_button'].clicked.connect(parent.on_lb_button_clicked)

        self.patient_widgets['height_text'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'height_text',
            'position': (8, 408),
            'width': 100,
            'labels': ('Altura', 'Height'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['height_text'].text_field.textEdited.connect(parent.on_height_text_textEdited)

        self.patient_widgets['height_unit_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'height_unit_label',
            'position': (116, 408),
            'width': 164,
            'type': 'subtitle',
            'labels': ('Unidad de Altura', 'Height Unit'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['mt_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'mt_button',
            'position': (116, 428),
            'width': 76,
            'labels': ('m', 'm'),
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['mt_button'].clicked.connect(parent.on_mt_button_clicked)

        self.patient_widgets['fi_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'fi_button',
            'position': (192, 428),
            'width': 76,
            'labels': ('ft.in', 'ft.in'),
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['fi_button'].clicked.connect(parent.on_fi_button_clicked)

        self.patient_widgets['bmi_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'bmi_label',
            'position': (8, 472),
            'width': 164,
            'type': 'subtitle',
            'labels': ('Índice de Masa Corporal', 'Body Mass Index'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['bmi_value_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'bmi_value_label',
            'position': (8, 492),
            'width': 164,
            'align': 'center',
            'type': 'value',
            'color': '255, 255, 255' if self.theme_value else '0, 0, 0',
            'theme': self.theme_value,
            'language': self.language_value } )

        # ---------------------
        # Buttons Ok and Cancel
        # ---------------------
        self.patient_widgets['cancel_button'] = MD3Button(self.patient_widgets['patient_form_card'], {
            'name': 'cancel_button',
            'position': (width - 232, height - 56),
            'width': 100,
            'type': 'text',
            'labels': ('Cancelar', 'Cancel'),
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['cancel_button'].clicked.connect(parent.on_cancel_button_clicked)

        self.patient_widgets['ok_button'] = MD3Button(self.patient_widgets['patient_form_card'], {
            'name': 'ok_button',
            'position': (width - 124, height - 56),
            'width': 100,
            'type': 'text',
            'labels': ('Aceptar', 'Ok'),
            'theme': self.theme_value,
            'language': self.language_value } )
        self.patient_widgets['ok_button'].setEnabled(False)
        self.patient_widgets['ok_button'].clicked.connect(parent.on_ok_button_clicked)

        