from PyQt6 import QtGui, QtWidgets, QtCore
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtCore import QSettings, Qt, QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator

from components.md3_window import MD3Window
from components.md3_card import MD3Card
from components.md3_menu import MD3Menu
from components.md3_iconbutton import MD3IconButton
from components.md3_switch import MD3Switch
from components.md3_label import MD3Label
from components.md3_textfield import MD3TextField
from components.mpl_canvas import MPLCanvas

import sys


class UI(QWidget):
    def __init__(self, parent):
        super(UI, self).__init__(parent)

        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.regExp3 = QRegularExpressionValidator(QRegularExpression('[0-9.]{1,5}'), self)

        self.idioma_dict = {0: ('ESP', 'SPA'), 1: ('ING', 'ENG')}

        self.gui_widgets = {}

        # -----------
        # Main Window
        # -----------
        (width, height) = (1300, 700)
        self.gui_widgets['main_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'labels': ('Calculadora de Somatotipo', 'Somatotype Calculator'),
            'theme': self.theme_value, 
            'language': self.language_value } )

        # -----------
        # Card Título
        # -----------
        self.gui_widgets['titulo_card'] = MD3Card(parent, {
            'name': 'titulo_card',
            'position': (8, 8), 
            'size': (width-16, 48), 
            'theme': self.theme_value } )


        # Espacio para título de la aplicación, logo, etc.

        
        self.gui_widgets['idioma_menu'] = MD3Menu(self.gui_widgets['titulo_card'], {
            'name': 'idioma_menu',
            'size': (72, 32),
            'options': self.idioma_dict,
            'language': self.language_value,
            'theme': self.theme_value } )
        self.gui_widgets['idioma_menu'].setCurrentIndex(self.language_value)
        self.gui_widgets['idioma_menu'].currentIndexChanged.connect(parent.on_idioma_menu_currentIndexChanged)

        self.gui_widgets['tema_switch_light'] = MD3Switch(self.gui_widgets['titulo_card'], {
            'name': 'tema_switch_light',
            'side': 'left',
            'icons': ('light_mode_L.png', 'none.png'),
            'state': self.theme_value,
            'language': self.language_value,
            'theme': self.theme_value } )
        self.gui_widgets['tema_switch_light'].clicked.connect(parent.on_tema_switch_light_clicked)

        self.gui_widgets['tema_switch_dark'] = MD3Switch(self.gui_widgets['titulo_card'], {
            'name': 'tema_switch_dark',
            'side': 'right',
            'icons': ('dark_mode_L.png', 'none.png'),
            'state': not self.theme_value,
            'language': self.language_value,
            'theme': self.theme_value } )
        self.gui_widgets['tema_switch_dark'].clicked.connect(parent.on_tema_switch_dark_clicked)

        self.gui_widgets['database_button'] = MD3IconButton(self.gui_widgets['titulo_card'], {
            'name': 'database_button',
            'type': 'filled',
            'icon': 'database', 
            'theme': self.theme_value } )
        # self.database_button.clicked.connect(self.on_database_button_clicked)

        self.gui_widgets['manual_button'] = MD3IconButton(self.gui_widgets['titulo_card'], {
            'name': 'manual_button',
            'type': 'filled',
            'icon': 'help', 
            'theme': self.theme_value } )
        # self.manual_button.clicked.connect(self.on_manual_button_clicked)

        self.gui_widgets['about_button'] = MD3IconButton(self.gui_widgets['titulo_card'], {
            'name': 'about_button',
            'type': 'filled',
            'icon': 'mail', 
            'theme': self.theme_value } )
        self.gui_widgets['about_button'].clicked.connect(parent.on_about_button_clicked)

        self.gui_widgets['aboutQt_button'] = MD3IconButton(self.gui_widgets['titulo_card'], {
            'name': 'aboutQt_button',
            'type': 'filled',
            'icon': 'about_qt', 
            'theme': self.theme_value } )
        self.gui_widgets['aboutQt_button'].clicked.connect(parent.on_aboutQt_button_clicked)

        # -------------
        # Card Análisis
        # -------------
        self.gui_widgets['analisis_card'] = MD3Card(parent, { 
            'name': 'analisis_card',
            'position': (8, 64), 
            'size': (180, 128), 
            'theme': self.theme_value, 
            'labels': ('Análsis', 'Analysis'), 
            'language': self.language_value } )

        self.gui_widgets['analisis_menu'] = MD3Menu(self.gui_widgets['analisis_card'], {
            'name': 'analisis_menu',
            'position': (8, 48),
            'size': (164, 32),
            'language': self.language_value,
            'theme': self.theme_value } )
        # self.analisis_menu.setEnabled(False)
        # self.analisis_menu.textActivated.connect(self.on_analisis_menu_textActivated)

        self.gui_widgets['analisis_add_button'] = MD3IconButton(self.gui_widgets['analisis_card'], {
            'name': 'analisis_add_button',
            'type': 'filled',
            'position': (100, 88),
            'icon': 'new', 
            'theme': self.theme_value } )
        # self.analisis_add_button.setEnabled(False)
        # self.gui_widgets['analisis_add_button'].clicked.connect(parent.on_analisis_add_button_clicked)

        self.gui_widgets['analisis_del_button'] = MD3IconButton(self.gui_widgets['analisis_card'], {
            'name': 'analisis_del_button',
            'type': 'filled',
            'position': (140, 88),
            'icon': 'delete', 
            'theme': self.theme_value } )
        # self.analisis_del_button.setEnabled(False)
        # self.analisis_del_button.clicked.connect(self.on_analisis_del_button_clicked)

        # -------------
        # Card Paciente
        # -------------
        self.gui_widgets['paciente_card'] = MD3Card(parent, { 
            'name': 'paciente_card',
            'position': (8, 200), 
            'size': (180, 128), 
            'theme': self.theme_value, 
            'labels': ('Paciente', 'Patient'), 
            'language': self.language_value } )
        
        self.gui_widgets['pacientes_menu'] = MD3Menu(self.gui_widgets['paciente_card'], {
            'name': 'pacientes_menu',
            'position': (8, 48),
            'size': (164, 32),
            'language': self.language_value,
            'theme': self.theme_value } )
        # self.pacientes_menu.textActivated.connect(self.on_pacientes_menu_textActivated)

        self.gui_widgets['paciente_add_button'] = MD3IconButton(self.gui_widgets['paciente_card'], {
            'name': 'paciente_add_button',
            'type': 'filled',
            'position': (60, 88),
            'icon': 'person_add', 
            'theme': self.theme_value } )
        self.gui_widgets['paciente_add_button'].clicked.connect(parent.on_paciente_add_button_clicked)

        self.gui_widgets['paciente_edit_button'] = MD3IconButton(self.gui_widgets['paciente_card'], {
            'name': 'paciente_edit_button',
            'type': 'filled',
            'position': (100, 88),
            'icon': 'person_edit', 
            'theme': self.theme_value } )
        # self.paciente_edit_button.clicked.connect(self.on_paciente_edit_button_clicked)

        self.gui_widgets['paciente_del_button'] = MD3IconButton(self.gui_widgets['paciente_card'], {
            'name': 'paciente_del_button',
            'type': 'filled',
            'position': (140, 88),
            'icon': 'person_off', 
            'theme': self.theme_value } )
        # self.paciente_del_button.clicked.connect(self.on_paciente_del_button_clicked)

        # ----------------
        # Card Información
        # ----------------
        self.gui_widgets['info_card'] = MD3Card(parent, { 
            'name': 'info_card',
            'position': (8, 336), 
            'size': (180, 312), 
            'theme': self.theme_value, 
            'labels': ('Información', 'Information'), 
            'language': self.language_value } )
        
        self.gui_widgets['last_name_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'last_name_value', 
            'position': (8, 56), 
            'width': 164,
            'type': 'subtitle',
            'labels': ('Apellido', 'Last Name'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['first_name_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'nombre_value', 
            'position': (8, 88), 
            'width': 164,
            'type': 'subtitle',
            'labels': ('Nombre', 'First Name'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['id_icon'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'id_icon', 
            'position': (8, 112),
            'type': 'icon',
            'icon': 'id',
            'theme': self.theme_value } )

        self.gui_widgets['id_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'id_value',
            'position': (48, 120),
            'width': 124,
            'type': 'subtitle',
            'labels': ('Identificación', 'Identification'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['date_icon'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'date_icon',
            'position': (8, 144),
            'type': 'icon',
            'icon': 'calendar',
            'theme': self.theme_value } )

        self.gui_widgets['date_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'date_value', 
            'position': (48, 152), 
            'width': 124,
            'type': 'subtitle',
            'labels': ('Fecha de Nacimiento', 'Birth Date'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['sex_icon'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'sex_icon', 
            'position': (8, 176),
            'type': 'icon',
            'icon': 'man_woman',
            'theme': self.theme_value } )

        self.gui_widgets['sex_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'sex_value', 
            'position': (48, 184), 
            'width': 124,
            'type': 'subtitle',
            'labels': ('Sexo', 'Sex'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['weight_icon'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'weight_icon', 
            'position': (8, 208),
            'type': 'icon',
            'icon': 'weight',
            'theme': self.theme_value } )

        self.gui_widgets['weight_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'weight_value', 
            'position': (48, 216), 
            'width': 124,
            'type': 'subtitle',
            'labels': ('Peso', 'Weight'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['height_icon'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'height_icon', 
            'position': (8, 240),
            'type': 'icon',
            'icon': 'height',
            'theme': self.theme_value } )

        self.gui_widgets['height_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'height_value', 
            'position': (48, 248), 
            'width': 124,
            'type': 'subtitle',
            'labels': ('Altura', 'Height'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['bmi_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'bmi_value', 
            'position': (48, 280), 
            'width': 124,
            'type': 'subtitle',
            'labels': ('IMC', 'BMI'),
            'theme': self.theme_value,
            'language': self.language_value } )

        # --------------------
        # Card Somatotype Plot
        # --------------------
        self.gui_widgets['somatotype_plot_card'] = MD3Card(parent, { 
            'name': 'somatotype_plot_card',
            'theme': self.theme_value, 
            'labels': ('Somatotipo','Somatotype'), 
            'language': self.language_value } )
        
        self.gui_widgets['somatotype_plot'] = MPLCanvas(self.gui_widgets['somatotype_plot_card'], self.theme_value)

        # ---------------
        # Card Endomorphy
        # ---------------
        self.gui_widgets['endomorph_card'] = MD3Card(parent, { 
            'name': 'endomorph_card',
            'size': (208, 288), 
            'theme': self.theme_value, 
            'labels': ('Endomorfismo', 'Endomorphy'),
            'language': self.language_value } )

        self.gui_widgets['triceps_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
            'name': 'triceps_text',
            'position': (8, 48),
            'width': self.gui_widgets['endomorph_card'].width() - 16,
            'labels': ('Tríceps (mm)', 'Triceps (mm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['triceps_text'].text_field.textEdited.connect(parent.on_triceps_text_textEdited)

        self.gui_widgets['subescapular_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
            'name': 'subescapular_text',
            'position': (8, 108),
            'width': self.gui_widgets['endomorph_card'].width() - 16,
            'labels': ('Subescapular (mm)', 'Subescapular (mm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['subescapular_text'].text_field.textEdited.connect(parent.on_subescapular_text_textEdited)

        self.gui_widgets['supraespinal_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
            'name': 'supraespinal_text',
            'position': (8, 168),
            'width': self.gui_widgets['endomorph_card'].width() - 16,
            'labels': ('Supraespinal (mm)', 'Supraespinal (mm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['supraespinal_text'].text_field.textEdited.connect(parent.on_supraespinal_text_textEdited)

        self.gui_widgets['pantorrilla_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
            'name': 'pantorrilla_text',
            'position': (8, 228),
            'width': self.gui_widgets['endomorph_card'].width() - 16,
            'labels': ('Pantorrilla (mm)', 'Calf (mm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['pantorrilla_text'].text_field.textEdited.connect(parent.on_pantorrilla_text_textEdited)

        # ---------------
        # Card Mesomorphy
        # ---------------
        self.gui_widgets['mesomorph_card'] = MD3Card(parent, { 
            'name': 'mesomorph_card',
            'size': (208, 468), 
            'theme': self.theme_value, 
            'labels': ('Mesomorfismo', 'Mesomorphy'),
            'language': self.language_value } )

        self.gui_widgets['altura_meso_label'] = MD3Label(self.gui_widgets['mesomorph_card'], {
            'name': 'altura_meso_label',
            'position': (8, 48),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'type': 'subtitle',
            'labels': ('Altura (cm)', 'Height (cm)'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['altura_meso_value_label'] = MD3Label(self.gui_widgets['mesomorph_card'], {
            'name': 'altura_meso_value_label',
            'position': (8, 68),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'align': 'center',
            'type': 'value',
            'color': '255, 255, 255' if self.theme_value else '0, 0, 0',
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['humero_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
            'name': 'humero_text',
            'position': (8, 108),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'labels': ('Diámetro Húmero (cm)', 'Humerus Diameter (cm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['humero_text'].text_field.textEdited.connect(parent.on_humero_text_textEdited)

        self.gui_widgets['femur_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
            'name': 'femur_text',
            'position': (8, 168),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'labels': ('Diámetro Fémur (cm)', 'Femur Diameter (cm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['femur_text'].text_field.textEdited.connect(parent.on_femur_text_textEdited)

        self.gui_widgets['biceps_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
            'name': 'biceps_text',
            'position': (8, 228),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'labels': ('Perímetro Bíceps (cm)', 'Biceps Perimeter (cm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['biceps_text'].text_field.textEdited.connect(parent.on_biceps_text_textEdited)

        self.gui_widgets['tricipital_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
            'name': 'tricipital_text',
            'position': (8, 288),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'labels': ('Pliegue Tricipital (cm)', 'Tricipital Fold (cm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['tricipital_text'].text_field.textEdited.connect(parent.on_tricipital_text_textEdited)

        self.gui_widgets['pantorrilla_perimetro_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
            'name': 'pantorrilla_perimetro_text',
            'position': (8, 348),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'labels': ('Perímetro Pantorrilla (cm)', 'Calf Perimeter (cm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['pantorrilla_perimetro_text'].text_field.textEdited.connect(parent.on_pantorrilla_perimetro_text_textEdited)

        self.gui_widgets['pantorrilla_pliegue_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
            'name': 'pantorrilla_pliegue_text',
            'position': (8, 408),
            'width': self.gui_widgets['mesomorph_card'].width() - 16,
            'labels': ('Pliegue Pantorrilla (cm)', 'Calf Fold (cm)'),
            'regular_expression': self.regExp3,
            'theme': self.theme_value,
            'language': self.language_value } )
        # self.gui_widgets['pantorrilla_pliegue_text'].text_field.textEdited.connect(parent.on_pantorrilla_pliegue_text_textEdited)

        # ---------------
        # Card Ectomorphy
        # ---------------
        self.gui_widgets['ectomorph_card'] = MD3Card(parent, { 
            'name': 'ectomorph_card',
            'size': (208, 128), 
            'theme': self.theme_value, 
            'labels': ('Ectomorfismo', 'Ectomorphy'),
            'language': self.language_value } )

        self.gui_widgets['peso_ecto_label'] = MD3Label(self.gui_widgets['ectomorph_card'], {
            'name': 'peso_ecto_label',
            'position': (8, 48),
            'width': self.gui_widgets['ectomorph_card'].width() - 16,
            'type': 'subtitle',
            'labels': ('Peso (Kg)', 'Weight (Kg)'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['peso_ecto_value_label'] = MD3Label(self.gui_widgets['ectomorph_card'], {
            'name': 'peso_ecto_value_label',
            'position': (8, 68),
            'width': self.gui_widgets['ectomorph_card'].width() - 16,
            'align': 'center',
            'type': 'value',
            'color': '255, 255, 255' if self.theme_value else '0, 0, 0',
            'theme': self.theme_value,
            'language': self.language_value } )
