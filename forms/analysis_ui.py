"""
Image

This file contains class Image Dialog.

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

from components.md3_button import MD3Button
from components.md3_card import MD3Card
from components.md3_divider import MD3Divider
from components.md3_iconbutton import MD3IconButton
from components.md3_label import MD3Label
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

        self.image_widgets = {}
        minimum_label = ('Mínimo', 'Minimum')
        maximum_label = ('Máximo', 'Maximum')

        # -------------
        # Dialog Window
        # -------------
        (width, height) = (348, 576)
        self.image_widgets['image_window'] = MD3Window( {
            'parent': parent, 
            'size': (width, height),
            'minimum_size': (width, height),
            'maximum_size': (width, height),
            'labels': ('Datos de la Imagen', 'Image Data'),
            'theme': self.theme_value, 
            'language': self.language_value } )

        # ---------------
        # Card Image Form
        # ---------------
        self.image_widgets['image_form_card'] = MD3Card(parent, { 
            'name': 'image_form_card',
            'position': (8, 8),
            'size': (width-16, height - 16), 
            'type': 'filled',
            'labels': ('Información de la Imagen', 'Image Information'),
            'theme': self.theme_value,
            'language': self.language_value } )

        self.image_widgets['filename_textfield'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'filename_textfield',
            'position': (8, 68),
            'width': width - 72,
            'labels': ('Archivo de Imagen', 'Image File'),
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['filename_button'] = MD3IconButton(self.image_widgets['image_form_card'], {
            'name': 'filename_button',
            'position': (width - 56, 82),
            'type': 'tonal',
            'icon': 'image', 
            'theme': self.theme_value,
            'clicked': parent.on_filename_button_clicked } )

        self.image_widgets['line_1_divider'] = MD3Divider(self.image_widgets['image_form_card'], {
            'name': 'line_1_divider',
            'position': (8, 128),
            'shape': 'horizontal',
            'length': width - 32,
            'theme': self.theme_value } )

        self.image_widgets['left_minimum_XT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'left_minimum_XT_text',
            'position': (8, 144),
            'width': int((width - 80) / 2),
            'labels': minimum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['left_XT_label'] = MD3Label(self.image_widgets['image_form_card'], {
            'name': 'left_XT_label',
            'position': (16 + (width - 80) / 2, 158),
            'type': 'icon',
            'icon': 'left_foot',
            'theme': self.theme_value } )

        self.image_widgets['left_maximum_XT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'left_maximum_XT_text',
            'position': (56 + (width - 80) / 2, 144),
            'width': int((width - 80) / 2),
            'labels': maximum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )
        
        self.image_widgets['center_minimum_XT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'center_minimum_XT_text',
            'position': (8, 204),
            'width': int((width - 80) / 2),
            'labels': minimum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['center_XT_label'] = MD3Label(self.image_widgets['image_form_card'], {
            'name': 'center_XT_label',
            'position': (16 + (width - 80) / 2, 218),
            'type': 'icon',
            'icon': 'feet',
            'theme': self.theme_value } )

        self.image_widgets['center_maximum_XT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'center_maximum_XT_text',
            'position': (56 + (width - 80) / 2, 204),
            'width': int((width - 80) / 2),
            'labels': maximum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['right_minimum_XT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'right_minimum_XT_text',
            'position': (8, 264),
            'width': int((width - 80) / 2),
            'labels': minimum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['right_XT_label'] = MD3Label(self.image_widgets['image_form_card'], {
            'name': 'right_XT_label',
            'position': (16 + (width - 80) / 2, 278),
            'type': 'icon',
            'icon': 'right_foot',
            'theme': self.theme_value } )

        self.image_widgets['right_maximum_XT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'right_maximum_XT_text',
            'position': (56 + (width - 80) / 2, 264),
            'width': int((width - 80) / 2),
            'labels': maximum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['line_2_divider'] = MD3Divider(self.image_widgets['image_form_card'], {
            'name': 'line_2_divider',
            'position': (8, 324),
            'shape': 'horizontal',
            'length': width - 32,
            'theme': self.theme_value } )

        self.image_widgets['left_minimum_YT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'left_minimum_YT_text',
            'position': (8, 340),
            'width': int((width - 80) / 2),
            'labels': minimum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['left_YT_label'] = MD3Label(self.image_widgets['image_form_card'], {
            'name': 'left_YT_label',
            'position': (16 + (width - 80) / 2, 354),
            'type': 'icon',
            'icon': 'left_foot',
            'theme': self.theme_value } )

        self.image_widgets['left_maximum_YT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'left_maximum_YT_text',
            'position': (56 + (width - 80) / 2, 340),
            'width': int((width - 80) / 2),
            'labels': maximum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['center_minimum_YT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'center_minimum_YT_text',
            'position': (8, 400),
            'width': int((width - 80) / 2),
            'labels': minimum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['center_YT_label'] = MD3Label(self.image_widgets['image_form_card'], {
            'name': 'center_YT_label',
            'position': (16 + (width - 80) / 2, 414),
            'type': 'icon',
            'icon': 'feet',
            'theme': self.theme_value } )

        self.image_widgets['center_maximum_YT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'center_maximum_YT_text',
            'position': (56 + (width - 80) / 2, 400),
            'width': int((width - 80) / 2),
            'labels': maximum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['right_minimum_YT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'right_minimum_YT_text',
            'position': (8, 460),
            'width': int((width - 80) / 2),
            'labels': minimum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        self.image_widgets['right_YT_label'] = MD3Label(self.image_widgets['image_form_card'], {
            'name': 'right_YT_label',
            'position': (16 + (width - 80) / 2, 474),
            'type': 'icon',
            'icon': 'right_foot',
            'theme': self.theme_value } )

        self.image_widgets['right_maximum_YT_text'] = MD3TextField(self.image_widgets['image_form_card'], {
            'name': 'right_maximum_YT_text',
            'position': (56 + (width - 80) / 2, 460),
            'width': int((width - 80) / 2),
            'labels': maximum_label,
            'type': 'double',
            'size': 7,
            'theme': self.theme_value,
            'language': self.language_value,
            'text_edited': parent.on_textEdited } )

        # ---------------------
        # Buttons Ok and Cancel
        # ---------------------
        self.image_widgets['cancel_button'] = MD3Button(self.image_widgets['image_form_card'], {
            'name': 'cancel_button',
            'position': (width - 232, height - 56),
            'width': 100,
            'type': 'text',
            'labels': ('Cancelar', 'Cancel'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_cancel_button_clicked } )

        self.image_widgets['ok_button'] = MD3Button(self.image_widgets['image_form_card'], {
            'name': 'ok_button',
            'position': (width - 124, height - 56),
            'width': 100,
            'type': 'text',
            'enabled': False,
            'labels': ('Aceptar', 'Ok'),
            'theme': self.theme_value,
            'language': self.language_value,
            'clicked': parent.on_ok_button_clicked } )

        