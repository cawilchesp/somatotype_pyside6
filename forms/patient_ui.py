"""
Patient Dialog

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
from PySide6.QtCore import QSettings

from components.md3_button import MD3Button
from components.md3_card import MD3Card
from components.md3_datepicker import MD3DatePicker
from components.md3_label import MD3Label
from components.md3_segmentedbutton import MD3SegmentedButton
from components.md3_textfield import MD3TextField
from components.md3_window import MD3Window

import sys


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

        self.patient_widgets = {}

        # -------------
        # Dialog Window
        # -------------
        (width, height) = (348, 588)
        self.patient_widgets['patient_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'minimum_size': (width, height),
            'maximum_size': (width, height),
            'labels': ('Datos del Paciente',"Patient's Data"),
            'theme': self.theme_value, 
            'language': self.language_value } )
        
        # -------------
        # Card Paciente
        # -------------
        self.patient_widgets['patient_form_card'] = MD3Card(parent, { 
            'name': 'patient_form_card',
            'position': (8, 8),
            'size': (width-16, height-16),
            'type': 'filled',
            'labels': ('Información del Paciente', 'Patient Information'), 
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.patient_widgets['last_name_textfield'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'last_name_textfield',
            'position': (8, 68),
            'width': width - 32,
            'labels': ('Apellidos', 'Last Name'),
            'type': 'text',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_last_name_textEdited } )
 
        self.patient_widgets['first_name_textfield'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'first_name_textfield',
            'position': (8, 136),
            'width': width - 32,
            'labels': ('Nombres', 'First Name'),
            'type': 'text',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_first_name_textEdited } )

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
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_cc_button_clicked } )

        self.patient_widgets['ti_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'ti_button',
            'position': (84, 224),
            'width': 76,
            'labels': ('TI', 'TI'),
            'check_icon': True,
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_ti_button_clicked } )

        self.patient_widgets['id_textfield'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'id_textfield',
            'position': (168, 204),
            'width': 156,
            'labels': ('Número de ID', 'ID Number'),
            'type': 'integer',
            'size': 10,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_id_textEdited } )

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

        self.patient_widgets['female_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'female_button',
            'position': (188, 292),
            'width': 68,
            'labels': ('F', 'F'),
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_female_button_clicked } )

        self.patient_widgets['male_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'male_button',
            'position': (256, 292),
            'width': 68,
            'labels': ('M', 'M'),
            'check_icon': True,
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_male_button_clicked } )

        self.patient_widgets['weight_textfield'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'weight_textfield',
            'position': (8, 340),
            'width': 100,
            'labels': ('Peso', 'Weight'),
            'type': 'weight',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_weight_textEdited } )

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
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_kg_button_clicked } )

        self.patient_widgets['lb_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'lb_button',
            'position': (192, 360),
            'width': 76,
            'labels': ('Lb', 'Lb'),
            'check_icon': True,
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_lb_button_clicked } )

        self.patient_widgets['height_textfield'] = MD3TextField(self.patient_widgets['patient_form_card'], {
            'name': 'height_textfield',
            'position': (8, 408),
            'width': 100,
            'labels': ('Altura', 'Height'),
            'type': 'height_si',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_height_textEdited } )

        self.patient_widgets['height_unit_label'] = MD3Label(self.patient_widgets['patient_form_card'], {
            'name': 'height_unit_label',
            'position': (116, 408),
            'width': 164,
            'type': 'subtitle',
            'labels': ('Unidad de Altura', 'Height Unit'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.patient_widgets['m_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'm_button',
            'position': (116, 428),
            'width': 76,
            'labels': ('m', 'm'),
            'check_icon': True,
            'location': 'left',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_m_button_clicked } )

        self.patient_widgets['ft_in_button'] = MD3SegmentedButton(self.patient_widgets['patient_form_card'], {
            'name': 'ft_in_button',
            'position': (192, 428),
            'width': 76,
            'labels': ('ft\'in\"', 'ft\'in\"'),
            'check_icon': True,
            'location': 'right',
            'state': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_ft_in_button_clicked } )

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
            'border_color': '#000000' if self.theme_value else '#FFFFFF',
            'theme': self.theme_value } )
        
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
            'language': self.language_value,
            'clicked': parent.on_cancel_button_clicked } )

        self.patient_widgets['ok_button'] = MD3Button(self.patient_widgets['patient_form_card'], {
            'name': 'ok_button',
            'position': (width - 124, height - 56),
            'width': 100,
            'type': 'text',
            'enabled': False,
            'labels': ('Aceptar', 'Ok'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_ok_button_clicked } )

        