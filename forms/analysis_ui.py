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
        (width, height) = (500, 540)
        self.analysis_widgets['image_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'minimum_size': (width, height),
            'maximum_size': (width, height),
            'labels': ('Datos del Somatotipo', 'Somatotype Data'),
            'theme': self.theme_value, 
            'language': self.language_value } )

        # ---------------
        # Card Endomorphy
        # ---------------
        self.analysis_widgets['endomorph_card'] = MD3Card(parent, { 
            'name': 'endomorph_card',
            'position': (8, 8),
            'size': ((width / 2) - 12, 288), 
            'type': 'filled',
            'labels': ('Endomorfismo', 'Endomorphy'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.analysis_widgets['triceps_text'] = MD3TextField(self.analysis_widgets['endomorph_card'], {
            'name': 'triceps_text',
            'position': (8, 48),
            'width': self.analysis_widgets['endomorph_card'].width() - 16,
            'labels': ('Tríceps (mm)', 'Triceps (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['subescapular_text'] = MD3TextField(self.analysis_widgets['endomorph_card'], {
            'name': 'subescapular_text',
            'position': (8, 108),
            'width': self.analysis_widgets['endomorph_card'].width() - 16,
            'labels': ('Subescapular (mm)', 'Subescapular (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['supraespinal_text'] = MD3TextField(self.analysis_widgets['endomorph_card'], {
            'name': 'supraespinal_text',
            'position': (8, 168),
            'width': self.analysis_widgets['endomorph_card'].width() - 16,
            'labels': ('Supraespinal (mm)', 'Supraespinal (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['pantorrilla_text'] = MD3TextField(self.analysis_widgets['endomorph_card'], {
            'name': 'pantorrilla_text',
            'position': (8, 228),
            'width': self.analysis_widgets['endomorph_card'].width() - 16,
            'labels': ('Pantorrilla (mm)', 'Calf (mm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        # ---------------
        # Card Mesomorphy
        # ---------------
        self.analysis_widgets['mesomorph_card'] = MD3Card(parent, { 
            'name': 'mesomorph_card',
            'position': ((width / 2) + 4, 8),
            'size': ((width / 2) - 12, 468),
            'type': 'filled',
            'labels': ('Mesomorfismo', 'Mesomorphy'),
            'theme': self.theme_value, 
            'language': self.language_value } )
        
        self.analysis_widgets['altura_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'altura_text',
            'position': (8, 48),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Altura (cm)', 'Height (cm)'),
            'type': 'height_si',
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['humero_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'humero_text',
            'position': (8, 108),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Diámetro Húmero (cm)', 'Humerus Diameter (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['femur_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'femur_text',
            'position': (8, 168),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Diámetro Fémur (cm)', 'Femur Diameter (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.analysis_widgets['biceps_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'biceps_text',
            'position': (8, 228),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Perímetro Bíceps (cm)', 'Biceps Perimeter (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.analysis_widgets['tricipital_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'tricipital_text',
            'position': (8, 288),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Pliegue Tricipital (cm)', 'Tricipital Fold (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.analysis_widgets['pantorrilla_perimetro_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'pantorrilla_perimetro_text',
            'position': (8, 348),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Perímetro Pantorrilla (cm)', 'Calf Perimeter (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.analysis_widgets['pantorrilla_pliegue_text'] = MD3TextField(self.analysis_widgets['mesomorph_card'], {
            'name': 'pantorrilla_pliegue_text',
            'position': (8, 408),
            'width': self.analysis_widgets['mesomorph_card'].width() - 16,
            'labels': ('Pliegue Pantorrilla (cm)', 'Calf Fold (cm)'),
            'type': 'integer',
            'size': 2,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        # ---------------
        # Card Ectomorphy
        # ---------------
        self.analysis_widgets['ectomorph_card'] = MD3Card(parent, { 
            'name': 'ectomorph_card',
            'position': (8, 304),
            'size': ((width / 2) - 12, 108),
            'type': 'filled',
            'labels': ('Ectomorfismo', 'Ectomorphy'),
            'theme': self.theme_value, 
            'language': self.language_value } )
        
        self.analysis_widgets['weight_textfield'] = MD3TextField(self.analysis_widgets['ectomorph_card'], {
            'name': 'weight_textfield',
            'position': (8, 48),
            'width': self.analysis_widgets['ectomorph_card'].width() - 16,
            'labels': ('Peso (Kg)', 'Weight (Kg)'),
            'type': 'weight',
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

        