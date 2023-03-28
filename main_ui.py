from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QSettings, Qt

from components.md3_card import MD3Card
from components.md3_chip import MD3Chip
from components.md3_iconbutton import MD3IconButton
from components.md3_label import MD3Label
from components.md3_menu import MD3Menu
from components.md3_segmentedbutton import MD3SegmentedButton
from components.md3_window import MD3Window
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

        self.idioma_dict = {0: ('ESP', 'SPA'), 1: ('ING', 'ENG')}

        self.gui_widgets = {}

        # -----------
        # Main Window
        # -----------
        (width, height) = (1300, 700)
        self.gui_widgets['main_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'minimum_size': (width, height),
            'labels': ('Calculadora de Somatotipo', 'Somatotype Calculator'),
            'theme': self.theme_value, 
            'language': self.language_value } )

        # -----------
        # Card Título
        # -----------
        self.gui_widgets['title_bar_card'] = MD3Card(parent, { 
            'name': 'title_bar_card',
            'position': (8, 8), 
            'size': (width - 16, 48),
            'type': 'filled',
            'theme': self.theme_value, 
            'language': self.language_value } )


        # Espacio para título de la aplicación, logo, etc.

        
        self.gui_widgets['language_menu'] = MD3Menu(self.gui_widgets['title_bar_card'], {
            'name': 'language_menu',
            'width': 72,
            'options': {0: ('ESP', 'SPA'), 1: ('ING', 'ENG')},
            'set': self.language_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'index_changed': parent.on_language_changed } )

        self.gui_widgets['light_theme_button'] = MD3SegmentedButton(self.gui_widgets['title_bar_card'], {
            'name': 'light_theme_button',
            'width': 40,
            'icon': 'light_mode',
            'check_icon': False,
            'location': 'left',
            'state': self.theme_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_light_theme_clicked } )

        self.gui_widgets['dark_theme_button'] = MD3SegmentedButton(self.gui_widgets['title_bar_card'], {
            'name': 'dark_theme_button',
            'width': 40,
            'icon': 'dark_mode',
            'check_icon': False,
            'location': 'right',
            'state': not self.theme_value,
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_dark_theme_clicked } )

        self.gui_widgets['database_button'] = MD3IconButton(self.gui_widgets['title_bar_card'], {
            'name': 'database_button',
            'type': 'tonal',
            'icon': 'database', 
            'theme': self.theme_value,
            'clicked': parent.on_database_button_clicked } )

        self.gui_widgets['manual_button'] = MD3IconButton(self.gui_widgets['title_bar_card'], {
            'name': 'manual_button',
            'type': 'tonal',
            'icon': 'help', 
            'theme': self.theme_value,
            'clicked': parent.on_manual_button_clicked } )

        self.gui_widgets['about_button'] = MD3IconButton(self.gui_widgets['title_bar_card'], {
            'name': 'about_button',
            'type': 'tonal',
            'icon': 'mail', 
            'theme': self.theme_value,
            'clicked': parent.on_about_button_clicked } )

        self.gui_widgets['about_qt_button'] = MD3IconButton(self.gui_widgets['title_bar_card'], {
            'name': 'about_qt_button',
            'type': 'tonal',
            'icon': 'about_qt', 
            'theme': self.theme_value,
            'clicked': parent.on_about_qt_button_clicked } )
        

        # -------------
        # Card Análisis
        # -------------
        self.gui_widgets['analysis_card'] = MD3Card(parent, { 
            'name': 'analysis_card',
            'position': (8, 64), 
            'size': (180, 128),
            'type': 'filled',
            'labels': ('Análisis', 'Analysis'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['analysis_menu'] = MD3Menu(self.gui_widgets['analysis_card'], {
            'name': 'analysis_menu',
            'position': (8, 48),
            'width': 164,
            'set': -1,
            'enabled': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_activated': parent.on_analysis_activated } )

        self.gui_widgets['analysis_add_button'] = MD3IconButton(self.gui_widgets['analysis_card'], {
            'name': 'analysis_add_button',
            'position': (100, 88),
            'type': 'tonal',
            'icon': 'new',
            'theme': self.theme_value,
            'clicked': parent.on_analysis_add_clicked } )

        self.gui_widgets['analysis_delete_button'] = MD3IconButton(self.gui_widgets['analysis_card'], {
            'name': 'analysis_delete_button',
            'position': (140, 88),
            'type': 'tonal',
            'icon': 'delete', 
            'enabled': False,
            'theme': self.theme_value,
            'clicked': parent.on_analysis_delete_clicked } )

        # -------------
        # Card Paciente
        # -------------
        self.gui_widgets['patient_card'] = MD3Card(parent, { 
            'name': 'patient_card',
            'position': (8, 200), 
            'size': (180, 128),
            'type': 'filled',
            'labels': ('Paciente', 'Patient'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['patient_menu'] = MD3Menu(self.gui_widgets['patient_card'], {
            'name': 'patient_menu',
            'position': (8, 48),
            'width': 164,
            'set': -1,
            'enabled': False,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_activated': parent.on_patients_activated } )
        
        self.gui_widgets['patient_add_button'] = MD3IconButton(self.gui_widgets['patient_card'], {
            'name': 'patient_add_button',
            'position': (60, 88),
            'type': 'tonal',
            'icon': 'person_add',
            'theme': self.theme_value,
            'clicked': parent.on_patient_add_clicked } )
        
        self.gui_widgets['patient_edit_button'] = MD3IconButton(self.gui_widgets['patient_card'], {
            'name': 'patient_edit_button',
            'position': (100, 88),
            'type': 'tonal',
            'icon': 'person_edit',
            'enabled': False,
            'theme': self.theme_value,
            'clicked': parent.on_patient_edit_clicked } )
        
        self.gui_widgets['patient_delete_button'] = MD3IconButton(self.gui_widgets['patient_card'], {
            'name': 'patient_delete_button',
            'position': (140, 88),
            'type': 'tonal',
            'icon': 'person_off',
            'enabled': False,
            'theme': self.theme_value,
            'clicked': parent.on_patient_delete_clicked } )

        # ----------------
        # Card Información
        # ----------------
        self.gui_widgets['info_card'] = MD3Card(parent, { 
            'name': 'info_card',
            'position': (8, 336), 
            'size': (180, 312),
            'type': 'filled',
            'labels': ('Información', 'Information'),
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['last_name_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'last_name_value',
            'position': (8, 56),
            'width': 164,
            'type': 'subtitle',
            'align': 'left',
            'labels': ('Apellido', 'Last Name'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['first_name_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'first_name_value',
            'position': (8, 88),
            'width': 164,
            'type': 'subtitle',
            'align': 'left',
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
            'align': 'left',
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
            'align': 'left',
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
            'align': 'left',
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
            'align': 'left',
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
            'align': 'left',
            'labels': ('Altura', 'Height'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.gui_widgets['bmi_value'] = MD3Label(self.gui_widgets['info_card'], {
            'name': 'bmi_value',
            'position': (48, 280),
            'width': 124,
            'type': 'subtitle',
            'align': 'left',
            'labels': ('IMC', 'BMI'),
            'theme': self.theme_value,
            'language': self.language_value } )

        # --------------------
        # Card Somatotype Plot
        # --------------------
        self.gui_widgets['somatotype_plot_card'] = MD3Card(parent, { 
            'name': 'somatotype_plot_card',
            'type': 'filled',
            'labels': ('Somatotipo','Somatotype'), 
            'theme': self.theme_value,
            'language': self.language_value } )
        
        self.gui_widgets['somatotype_plot'] = MPLCanvas(self.gui_widgets['somatotype_plot_card'], {
            'position': (8, 48),
            'theme': self.theme_value } )
        


        # # ---------------
        # # Card Endomorphy
        # # ---------------
        # self.gui_widgets['endomorph_card'] = MD3Card(parent, { 
        #     'name': 'endomorph_card',
        #     'size': (208, 288), 
        #     'theme': self.theme_value, 
        #     'labels': ('Endomorfismo', 'Endomorphy'),
        #     'language': self.language_value } )

        # self.gui_widgets['triceps_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
        #     'name': 'triceps_text',
        #     'position': (8, 48),
        #     'width': self.gui_widgets['endomorph_card'].width() - 16,
        #     'labels': ('Tríceps (mm)', 'Triceps (mm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['triceps_text'].text_field.textEdited.connect(parent.on_triceps_text_textEdited)

        # self.gui_widgets['subescapular_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
        #     'name': 'subescapular_text',
        #     'position': (8, 108),
        #     'width': self.gui_widgets['endomorph_card'].width() - 16,
        #     'labels': ('Subescapular (mm)', 'Subescapular (mm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['subescapular_text'].text_field.textEdited.connect(parent.on_subescapular_text_textEdited)

        # self.gui_widgets['supraespinal_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
        #     'name': 'supraespinal_text',
        #     'position': (8, 168),
        #     'width': self.gui_widgets['endomorph_card'].width() - 16,
        #     'labels': ('Supraespinal (mm)', 'Supraespinal (mm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['supraespinal_text'].text_field.textEdited.connect(parent.on_supraespinal_text_textEdited)

        # self.gui_widgets['pantorrilla_text'] = MD3TextField(self.gui_widgets['endomorph_card'], {
        #     'name': 'pantorrilla_text',
        #     'position': (8, 228),
        #     'width': self.gui_widgets['endomorph_card'].width() - 16,
        #     'labels': ('Pantorrilla (mm)', 'Calf (mm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['pantorrilla_text'].text_field.textEdited.connect(parent.on_pantorrilla_text_textEdited)

        # # ---------------
        # # Card Mesomorphy
        # # ---------------
        # self.gui_widgets['mesomorph_card'] = MD3Card(parent, { 
        #     'name': 'mesomorph_card',
        #     'size': (208, 468), 
        #     'theme': self.theme_value, 
        #     'labels': ('Mesomorfismo', 'Mesomorphy'),
        #     'language': self.language_value } )

        # self.gui_widgets['altura_meso_label'] = MD3Label(self.gui_widgets['mesomorph_card'], {
        #     'name': 'altura_meso_label',
        #     'position': (8, 48),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Altura (cm)', 'Height (cm)'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['altura_meso_value_label'] = MD3Label(self.gui_widgets['mesomorph_card'], {
        #     'name': 'altura_meso_value_label',
        #     'position': (8, 68),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'align': 'center',
        #     'type': 'value',
        #     'color': '255, 255, 255' if self.theme_value else '0, 0, 0',
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['humero_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
        #     'name': 'humero_text',
        #     'position': (8, 108),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'labels': ('Diámetro Húmero (cm)', 'Humerus Diameter (cm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['humero_text'].text_field.textEdited.connect(parent.on_humero_text_textEdited)

        # self.gui_widgets['femur_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
        #     'name': 'femur_text',
        #     'position': (8, 168),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'labels': ('Diámetro Fémur (cm)', 'Femur Diameter (cm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['femur_text'].text_field.textEdited.connect(parent.on_femur_text_textEdited)

        # self.gui_widgets['biceps_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
        #     'name': 'biceps_text',
        #     'position': (8, 228),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'labels': ('Perímetro Bíceps (cm)', 'Biceps Perimeter (cm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['biceps_text'].text_field.textEdited.connect(parent.on_biceps_text_textEdited)

        # self.gui_widgets['tricipital_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
        #     'name': 'tricipital_text',
        #     'position': (8, 288),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'labels': ('Pliegue Tricipital (cm)', 'Tricipital Fold (cm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['tricipital_text'].text_field.textEdited.connect(parent.on_tricipital_text_textEdited)

        # self.gui_widgets['pantorrilla_perimetro_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
        #     'name': 'pantorrilla_perimetro_text',
        #     'position': (8, 348),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'labels': ('Perímetro Pantorrilla (cm)', 'Calf Perimeter (cm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['pantorrilla_perimetro_text'].text_field.textEdited.connect(parent.on_pantorrilla_perimetro_text_textEdited)

        # self.gui_widgets['pantorrilla_pliegue_text'] = MD3TextField(self.gui_widgets['mesomorph_card'], {
        #     'name': 'pantorrilla_pliegue_text',
        #     'position': (8, 408),
        #     'width': self.gui_widgets['mesomorph_card'].width() - 16,
        #     'labels': ('Pliegue Pantorrilla (cm)', 'Calf Fold (cm)'),
        #     'regular_expression': self.regExp3,
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
        # # self.gui_widgets['pantorrilla_pliegue_text'].text_field.textEdited.connect(parent.on_pantorrilla_pliegue_text_textEdited)

        # # ---------------
        # # Card Ectomorphy
        # # ---------------
        # self.gui_widgets['ectomorph_card'] = MD3Card(parent, { 
        #     'name': 'ectomorph_card',
        #     'size': (208, 128), 
        #     'theme': self.theme_value, 
        #     'labels': ('Ectomorfismo', 'Ectomorphy'),
        #     'language': self.language_value } )

        # self.gui_widgets['peso_ecto_label'] = MD3Label(self.gui_widgets['ectomorph_card'], {
        #     'name': 'peso_ecto_label',
        #     'position': (8, 48),
        #     'width': self.gui_widgets['ectomorph_card'].width() - 16,
        #     'type': 'subtitle',
        #     'labels': ('Peso (Kg)', 'Weight (Kg)'),
        #     'theme': self.theme_value,
        #     'language': self.language_value } )

        # self.gui_widgets['peso_ecto_value_label'] = MD3Label(self.gui_widgets['ectomorph_card'], {
        #     'name': 'peso_ecto_value_label',
        #     'position': (8, 68),
        #     'width': self.gui_widgets['ectomorph_card'].width() - 16,
        #     'align': 'center',
        #     'type': 'value',
        #     'color': '255, 255, 255' if self.theme_value else '0, 0, 0',
        #     'theme': self.theme_value,
        #     'language': self.language_value } )
