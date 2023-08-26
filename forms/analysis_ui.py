"""
Analysis

This file contains class Analysis Dialog.

To provide the analysis information, it requires:

Endomorphy:
Triceps skinfold thickness (mm)
Subscapular skinfold thickness (mm)
Supraspinale skinfold thickness (mm)
Height (cm)

Mesomorphy:
Biceps girth (cm)
Forearm girth (cm)
Humeral breadth (cm)
Femoral breadth (cm)
Knee breadth (cm)
Height (cm)
Weight (kg)

Ectomorphy:
Weight (kg)
"""

from PySide6 import QtWidgets
from PySide6.QtCore import QSettings

from components.md3_button import MD3Button
from components.md3_card import MD3Card
from components.md3_textfield import MD3TextField
from components.md3_window import MD3Window

import sys


class AnalysisUI(QtWidgets.QDialog):
    def __init__(self, parent):
        """ UI Patient dialog class """
        super(AnalysisUI, self).__init__(parent)
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.analysis_widgets = {}

        # -------------
        # Dialog Window
        # -------------
        (width, height) = (975, 476)
        self.analysis_widgets['image_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'minimum_size': (width, height),
            'maximum_size': (width, height),
            'labels': ('Datos del Somatotipo', 'Somatotype Data'),
            'theme': self.theme_value, 
            'language': self.language_value } )

        # ------------
        # Card Patient
        # ------------
        self.analysis_widgets['patient_card'] = MD3Card(parent, { 
            'name': 'patient_card',
            'position': (8, 8),
            'size': ((width / 2) - 12, 168), 
            'type': 'filled',
            'labels': ('Paciente', 'Patient'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.analysis_widgets['height_textfield'] = MD3TextField(self.analysis_widgets['patient_card'], {
            'name': 'height_textfield',
            'position': (8, 48),
            'width': self.analysis_widgets['patient_card'].width() - 16,
            'labels': ('Altura (cm)', 'Height (cm)'),
            'type': 'integer',
            'size': 3,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['weight_textfield'] = MD3TextField(self.analysis_widgets['patient_card'], {
            'name': 'weight_textfield',
            'position': (8, 108),
            'width': self.analysis_widgets['patient_card'].width() - 16,
            'labels': ('Peso (Kg)', 'Weight (Kg)'),
            'type': 'weight',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        # --------------
        # Card Skinfolds
        # --------------
        self.analysis_widgets['skinfolds_card'] = MD3Card(parent, { 
            'name': 'skinfolds_card',
            'position': (8, 244),
            'size': ((width / 2) - 12, 228), 
            'type': 'filled',
            'labels': ('Pliegues Cutáneos', 'Skinfolds'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.analysis_widgets['triceps_textfield'] = MD3TextField(self.analysis_widgets['skinfolds_card'], {
            'name': 'triceps_textfield',
            'position': (8, 48),
            'width': self.analysis_widgets['skinfolds_card'].width() - 16,
            'labels': ('Tríceps (mm)', 'Triceps (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['subscapular_textfield'] = MD3TextField(self.analysis_widgets['skinfolds_card'], {
            'name': 'subscapular_textfield',
            'position': (8, 108),
            'width': self.analysis_widgets['skinfolds_card'].width() - 16,
            'labels': ('Subescapular (mm)', 'Subscapular (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['supraspinale_textfield'] = MD3TextField(self.analysis_widgets['skinfolds_card'], {
            'name': 'supraspinale_textfield',
            'position': (8, 168),
            'width': self.analysis_widgets['skinfolds_card'].width() - 16,
            'labels': ('Supraespinal (mm)', 'Supraspinale (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.analysis_widgets['calf_fold_textfield'] = MD3TextField(self.analysis_widgets['skinfolds_card'], {
            'name': 'calf_fold_textfield',
            'position': (8, 228),
            'width': self.analysis_widgets['skinfolds_card'].width() - 16,
            'labels': ('Pantorrilla (mm)', 'Calf (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        # --------------------
        # Card Girths/Breadths
        # --------------------
        self.analysis_widgets['girths_card'] = MD3Card(parent, { 
            'name': 'girths_card',
            'position': ((width / 2) + 4, 8),
            'size': ((width / 2) - 12, 288),
            'type': 'filled',
            'labels': ('Circunferencias/Anchos', 'Girths/Breadths'),
            'theme': self.theme_value, 
            'language': self.language_value } )
        
        self.analysis_widgets['biceps_textfield'] = MD3TextField(self.analysis_widgets['girths_card'], {
            'name': 'biceps_textfield',
            'position': (8, 48),
            'width': self.analysis_widgets['girths_card'].width() - 16,
            'labels': ('Bíceps (cm)', 'Biceps (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['calf_textfield'] = MD3TextField(self.analysis_widgets['girths_card'], {
            'name': 'calf_textfield',
            'position': (8, 108),
            'width': self.analysis_widgets['girths_card'].width() - 16,
            'labels': ('Pantorrilla (cm)', 'Calf (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['humerus_textfield'] = MD3TextField(self.analysis_widgets['girths_card'], {
            'name': 'humerus_textfield',
            'position': (8, 168),
            'width': self.analysis_widgets['girths_card'].width() - 16,
            'labels': ('Húmero (cm)', 'Humeral (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['femur_textfield'] = MD3TextField(self.analysis_widgets['girths_card'], {
            'name': 'femur_textfield',
            'position': (8, 228),
            'width': self.analysis_widgets['girths_card'].width() - 16,
            'labels': ('Fémur (cm)', 'Femoral (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        # --------------------------
        # Card Buttons Ok and Cancel
        # --------------------------
        self.analysis_widgets['buttons_bar_card'] = MD3Card(parent, { 
            'name': 'buttons_bar_card',
            'position': (8, height - 56), 
            'size': (width - 16, 48),
            'type': 'filled',
            'theme': self.theme_value, 
            'language': self.language_value } )

        self.analysis_widgets['cancel_button'] = MD3Button(self.analysis_widgets['buttons_bar_card'], {
            'name': 'cancel_button',
            'position': (width - 232, 8),
            'width': 100,
            'type': 'text',
            'labels': ('Cancelar', 'Cancel'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_cancel_button_clicked } )

        self.analysis_widgets['ok_button'] = MD3Button(self.analysis_widgets['buttons_bar_card'], {
            'name': 'ok_button',
            'position': (width - 124, 8),
            'width': 100,
            'type': 'text',
            'enabled': False,
            'labels': ('Aceptar', 'Ok'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_ok_button_clicked } )
