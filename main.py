"""
Frontend

This file contains main UI class and methods to control components operations.
"""

from PySide6 import QtGui, QtWidgets, QtCore
from PySide6.QtWidgets import QWidget, QApplication, QMainWindow
from PySide6.QtCore import QSettings

import sys
import pandas as pd
from pathlib import Path

from main_ui import UI
import backend

from forms.patient_frontend import PatientForm

from dialogs.about_app import AboutApp


class MainWindow(QMainWindow):
    def __init__(self):
        """ UI main application """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        self.idioma_dict = {0: ('ESP', 'SPA'), 1: ('ING', 'ENG')}
    
        # ---------
        # Variables
        # ---------
        self.patient_data = None
        self.data_lat_max = 0.0
        self.data_lat_t_max = 0.0
        self.data_lat_min = 0.0
        self.data_lat_t_min = 0.0
        self.data_ap_max = 0.0
        self.data_ap_t_max = 0.0
        self.data_ap_min = 0.0
        self.data_ap_t_min = 0.0
        self.lat_text_1 = None
        self.lat_text_2 = None
        self.ap_text_1 = None
        self.ap_text_2 = None

        # ----------------
        # Generación de UI
        # ----------------
        self.ui = UI(self)

        # # -------------
        # # Base de Datos
        # # -------------
        # try:
        #     self.patientes_list = backend.create_db('pacientes')
        #     self.estudios_list = backend.create_db('estudios')

        #     for data in self.patientes_list:
        #         self.pacientes_menu.addItem(str(data[4]))
        #     self.pacientes_menu.setCurrentIndex(-1)
        # except:
        #     self.pacientes_menu.setEnabled(False)
        #     self.paciente_add_button.setEnabled(False)
        #     self.paciente_edit_button.setEnabled(False)
        #     self.paciente_del_button.setEnabled(False)
            
        #     if self.language_value == 0:
        #         QtWidgets.QMessageBox.critical(self, 'Error de Base de Datos', 'La base de datos no está configurada')
        #     elif self.language_value == 1:
        #         QtWidgets.QMessageBox.critical(self, 'Database Error', 'Database not configured')

    # -----
    # Title
    # -----
    def on_language_changed(self, index: int) -> None:
        """ Language menu control to change components text language
        
        Parameters
        ----------
        index: int
            Index of language menu control
        
        Returns
        -------
        None
        """
        for key in self.ui.gui_widgets.keys():
            if hasattr(self.ui.gui_widgets[key], 'setLanguage'):
                self.ui.gui_widgets[key].setLanguage(index)

        self.settings.setValue('language', str(index))
        self.language_value = int(self.settings.value('language'))

    
    def on_light_theme_clicked(self, state: bool) -> None:
        """ Light theme segmented control to change components stylesheet
        
        Parameters
        ----------
        state: bool
            State of light theme segmented control
        
        Returns
        -------
        None
        """
        if state: 
            for key in self.ui.gui_widgets.keys():
                self.ui.gui_widgets[key].setThemeStyle(True)
            self.ui.gui_widgets['dark_theme_button'].setState(False, True)

            self.ui.gui_widgets['somatotype_plot'].draw()

            self.settings.setValue('theme', f'{True}')
            self.theme_value = eval(self.settings.value('theme'))
        
        self.ui.gui_widgets['light_theme_button'].setState(True, True)


    def on_dark_theme_clicked(self, state: bool) -> None:
        """ Dark theme segmented control to change components stylesheet
        
        Parameters
        ----------
        state: bool
            State of dark theme segmented control
        
        Returns
        -------
        None
        """
        if state: 
            for key in self.ui.gui_widgets.keys():
                self.ui.gui_widgets[key].setThemeStyle(False)
            self.ui.gui_widgets['light_theme_button'].setState(False, False)

            self.ui.gui_widgets['somatotype_plot'].draw()

            self.settings.setValue('theme', f'{False}')
            self.theme_value = eval(self.settings.value('theme'))

        self.ui.gui_widgets['dark_theme_button'].setState(True, False)


    def on_database_button_clicked(self) -> None:
        """ Database button to configure the database """
        
        self.db_info = DatabaseForm()
        self.db_info.exec()
        
    #     if self.db_info.database_data:
    #         self.patientes_list = backend.create_db('pacientes')
    #         self.estudios_list = backend.create_db('estudios')

    #         for data in self.patientes_list:
    #             self.pacientes_menu.addItem(str(data[4]))
    #         self.pacientes_menu.setCurrentIndex(-1)

    #         self.pacientes_menu.setEnabled(True)
    #         self.paciente_add_button.setEnabled(True)
    #         self.paciente_edit_button.setEnabled(True)
    #         self.paciente_del_button.setEnabled(True)

    #         if self.language_value == 0:
    #             QtWidgets.QMessageBox.information(self, 'Datos Guardados', 'Base de datos configurada')
    #         elif self.language_value == 1:
    #             QtWidgets.QMessageBox.information(self, 'Data Saved', 'Database configured')
    #     else:
    #         if self.language_value == 0:
    #             QtWidgets.QMessageBox.critical(self, 'Error de Datos', 'No se dio información de la base de datos')
    #         elif self.language_value == 1:
    #             QtWidgets.QMessageBox.critical(self, 'Data Error', 'No information on the database was given')


    def on_manual_button_clicked(self) -> None:
        """ Manual button to open manual window """
        return None


    def on_about_button_clicked(self) -> None:
        """ About app button to open about app window dialog """
        self.about_app = AboutApp()
        self.about_app.exec()


    def on_about_qt_button_clicked(self) -> None:
        """ About Qt button to open about Qt window dialog """
        backend.about_qt_dialog(self, self.language_value)
        
    
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """ Resize event to control size and position of app components """
        width = self.geometry().width()
        height = self.geometry().height()

        self.ui.gui_widgets['title_bar_card'].resize(width - 16, 48)
        self.ui.gui_widgets['language_menu'].move(width - 344, 8)
        self.ui.gui_widgets['light_theme_button'].move(width - 264, 8)
        self.ui.gui_widgets['dark_theme_button'].move(width - 224, 8)
        self.ui.gui_widgets['database_button'].move(width - 176, 8)
        self.ui.gui_widgets['manual_button'].move(width - 136, 8)
        self.ui.gui_widgets['about_button'].move(width - 96, 8)
        self.ui.gui_widgets['about_qt_button'].move(width - 56, 8)

        self.ui.gui_widgets['somatotype_plot_card'].setGeometry(196, 64, width - 420, height - 72)
        self.ui.gui_widgets['somatotype_plot_card'].title.resize(width - 652, 32)
        self.ui.gui_widgets['somatotype_plot'].resize(self.ui.gui_widgets['somatotype_plot_card'].width()-16, self.ui.gui_widgets['somatotype_plot_card'].height()-56)
        
        





        # self.ui.gui_widgets['parameters_XT_card'].move(width - 216, 64)
        # self.ui.gui_widgets['parameters_YT_card'].move(width - 216, 200)
        # self.ui.gui_widgets['parameters_XY_card'].move(width - 216, 336)
        # self.ui.gui_widgets['areas_card'].move(width - 216, 472)

        return super().resizeEvent(a0)

    # -------
    # Patient
    # -------
    def on_patient_add_clicked(self) -> None:
        """ Add patient button to the database """
        return None
    #     self.patient_window = PatientForm()
    #     self.patient_window.exec()
        
    #     if self.patient_window.patient_data:
    #         self.ui.gui_widgets['last_name_value'].setText(self.patient_window.patient_data['last_name'])
    #         self.ui.gui_widgets['first_name_value'].setText(self.patient_window.patient_data['first_name'])
    #         self.ui.gui_widgets['id_value'].setText(f'{self.patient_window.patient_data["id_type"]} {self.patient_window.patient_data["id"]}')
    #         self.ui.gui_widgets['date_value'].setText(self.patient_window.patient_data['birth_date'])
    #         if self.patient_window.patient_data['sex'] == 'F':
    #             self.ui.gui_widgets['sex_icon'].set_icon('woman', self.theme_value)
    #         elif self.patient_window.patient_data['sex'] == 'M':
    #             self.ui.gui_widgets['sex_icon'].set_icon('man', self.theme_value)
    #         self.ui.gui_widgets['sex_value'].setText(self.patient_window.patient_data['sex'])
    #         self.ui.gui_widgets['weight_value'].setText(f'{self.patient_window.patient_data["weight"]} {self.patient_window.patient_data["weight_unit"]}')
    #         self.ui.gui_widgets['height_value'].setText(f'{self.patient_window.patient_data["height"]} {self.patient_window.patient_data["height_unit"]}')
    #         self.ui.gui_widgets['bmi_value'].setText(self.patient_window.patient_data['bmi'])

    # #         # -------------
    # #         # Base de datos
    # #         # -------------
    # #         self.patientes_list = backend.add_db('pacientes', self.patient_window.patient_data)
            
    # #         self.pacientes_menu.clear()
    # #         for data in self.patientes_list:
    # #             self.pacientes_menu.addItem(str(data[4]))
    # #         self.pacientes_menu.setCurrentIndex(len(self.patientes_list)-1)

    # #         self.analisis_add_button.setEnabled(True)
    # #         self.analisis_del_button.setEnabled(True)
    # #         self.analisis_menu.setEnabled(True)

    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.information(self, 'Datos Guardados', 'Paciente agregado a la base de datos')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.information(self, 'Data Saved', 'Patient added to database')
    # #     else:
    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.critical(self, 'Error de Datos', 'No se dio información de un paciente nuevo')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.critical(self, 'Data Error', 'No information on a new patient was given')


    def on_patient_edit_clicked(self) -> None:
        """ Edit patient button in the database """
        return None
    # #     patient_id = self.pacientes_menu.currentText()

    # #     if patient_id != '':
    # #         patient_data = backend.get_db('pacientes', patient_id)

    # #         id_db = patient_data[0][0]
    # #         self.patient_window = patient.Patient()
    # #         self.patient_window.apellido_text.text_field.setText(patient_data[0][1])
    # #         self.patient_window.nombre_text.text_field.setText(patient_data[0][2])
    # #         if patient_data[0][3] == 'CC':
    # #             self.patient_window.cc_button.set_state(True)
    # #         elif patient_data[0][3] == 'TI':
    # #             self.patient_window.ti_button.set_state(True)
    # #         self.patient_window.id_text.text_field.setText(str(patient_data[0][4]))
    # #         self.patient_window.fecha_date.text_field.setDate(QtCore.QDate.fromString(patient_data[0][5], 'dd/MM/yyyy'))
    # #         if patient_data[0][6] == 'F':
    # #             self.patient_window.f_button.set_state(True)
    # #         elif patient_data[0][6] == 'M':
    # #             self.patient_window.m_button.set_state(True)
    # #         self.patient_window.peso_text.text_field.setText(str(patient_data[0][7]))
    # #         if patient_data[0][8] == 'Kg':
    # #             self.patient_window.kg_button.set_state(True)
    # #         elif patient_data[0][8] == 'Lb':
    # #             self.patient_window.lb_button.set_state(True)
    # #         self.patient_window.altura_text.text_field.setText(str(patient_data[0][9]))
    # #         if patient_data[0][10] == 'm':
    # #             self.patient_window.mt_button.set_state(True)
    # #         elif patient_data[0][10] == 'ft - in':
    # #             self.patient_window.fi_button.set_state(True)
    # #         self.patient_window.bmi_value_label.setText(str(patient_data[0][11]))

    # #         self.patient_window.exec()

    # #         if self.patient_window.patient_data:
    # #             self.patientes_list = backend.edit_db('pacientes', id_db, self.patient_window.patient_data)

    # #             self.pacientes_menu.clear()
    # #             for data in self.patientes_list:
    # #                 self.pacientes_menu.addItem(str(data[4]))
    # #             self.pacientes_menu.setCurrentIndex(-1)

    # #             self.analisis_add_button.setEnabled(False)
    # #             self.analisis_del_button.setEnabled(False)
    # #             self.analisis_menu.setEnabled(False)

    # #             self.apellido_value.setText('')
    # #             self.nombre_value.setText('')
    # #             self.id_value.setText('')
    # #             self.fecha_value.setText('')
    # #             self.sex_value.setText('')
    # #             self.sex_label.set_icon('', self.theme_value)
    # #             self.peso_value.setText('')
    # #             self.altura_value.setText('')
    # #             self.bmi_value.setText('')

    # #             if self.language_value == 0:
    # #                 QtWidgets.QMessageBox.information(self, 'Datos Guardados', 'Paciente editado en la base de datos')
    # #             elif self.language_value == 1:
    # #                 QtWidgets.QMessageBox.information(self, 'Data Saved', 'Patient edited in database')
    # #         else:
    # #             if self.language_value == 0:
    # #                 QtWidgets.QMessageBox.critical(self, 'Error de Datos', 'No se dio información del paciente')
    # #             elif self.language_value == 1:
    # #                 QtWidgets.QMessageBox.critical(self, 'Data Error', 'No information on a patient was given')
    # #     else:
    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.critical(self, 'Error de Paciente', 'No se seleccionó un paciente')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.critical(self, 'Patient Error', 'No patient selected')


    def on_patient_delete_clicked(self) -> None:
        """ Delete patient button from the database """
        return None
    # #     patient_id = self.pacientes_menu.currentText()

    # #     if patient_id != '':
    # #         self.patientes_list = backend.delete_db('pacientes', patient_id)

    # #         self.pacientes_menu.clear()
    # #         for data in self.patientes_list:
    # #             self.pacientes_menu.addItem(str(data[4]))
    # #         self.pacientes_menu.setCurrentIndex(-1)

    # #         self.analisis_add_button.setEnabled(False)
    # #         self.analisis_del_button.setEnabled(False)
    # #         self.analisis_menu.setEnabled(False)

    # #         self.apellido_value.setText('')
    # #         self.nombre_value.setText('')
    # #         self.id_value.setText('')
    # #         self.fecha_value.setText('')
    # #         self.sex_value.setText('')
    # #         self.sex_label.set_icon('', self.theme_value)
    # #         self.peso_value.setText('')
    # #         self.altura_value.setText('')
    # #         self.bmi_value.setText('')

    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.information(self, 'Datos Guardados', 'Paciente eliminado de la base de datos')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.information(self, 'Data Saved', 'Patient deleted from database')
    # #     else:
    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.critical(self, 'Error de Paciente', 'No se seleccionó un paciente')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.critical(self, 'Patient Error', 'No patient selected')


    def on_patients_activated(self, current_pacient: str) -> None:
        """ Change active patient and present previously saved studies and information
        
        Parameters
        ----------
        current_pacient: str
            Current pacient text
        
        Returns
        -------
        None
        """
        return None
    # #     patient_data = backend.get_db('pacientes', current_pacient)

    # #     if patient_data[0][6] == 'F':
    # #         self.sex_label.set_icon('woman', self.theme_value)
    # #     elif patient_data[0][6] == 'M':
    # #         self.sex_label.set_icon('man', self.theme_value)

    # #     self.apellido_value.setText(patient_data[0][1])
    # #     self.nombre_value.setText(patient_data[0][2])
    # #     self.id_value.setText(f'{patient_data[0][3]} {patient_data[0][4]}')
    # #     self.fecha_value.setText(patient_data[0][5])
    # #     self.sex_value.setText(patient_data[0][6])
    # #     self.peso_value.setText(f'{patient_data[0][7]} {patient_data[0][8]}')
    # #     self.altura_value.setText(f'{patient_data[0][9]} {patient_data[0][10]}')
    # #     self.bmi_value.setText(str(patient_data[0][11]))

    # #     self.analisis_add_button.setEnabled(True)
    # #     self.analisis_del_button.setEnabled(True)
    # #     self.analisis_menu.setEnabled(True)

    # #     self.estudios_list = backend.get_db('estudios', current_pacient)
    # #     self.analisis_menu.clear()
    # #     for data in self.estudios_list:
    # #         self.analisis_menu.addItem(data[2])
    # #     self.analisis_menu.setCurrentIndex(-1)

    # #     self.lateral_plot.axes.cla()
    # #     self.lateral_plot.draw()
    # #     self.antePost_plot.axes.cla()
    # #     self.antePost_plot.draw()
    # #     self.elipse_plot.axes.cla()
    # #     self.elipse_plot.draw()
    # #     self.hull_plot.axes.cla()
    # #     self.hull_plot.draw()
    # #     self.pca_plot.axes.cla()
    # #     self.pca_plot.draw()

    # #     self.lat_rango_value.setText('')
    # #     self.lat_vel_value.setText('')
    # #     self.lat_rms_value.setText('')
    # #     self.ap_rango_value.setText('')
    # #     self.ap_vel_value.setText('')
    # #     self.ap_rms_value.setText('')
    # #     self.cop_vel_value.setText('')
    # #     self.distancia_value.setText('')
    # #     self.frecuencia_value.setText('')
    # #     self.elipse_value.setText('')
    # #     self.hull_value.setText('')
    # #     self.pca_value.setText('')

    
    # -----------------
    # Funciones Estudio
    # -----------------
    def on_analysis_add_clicked(self) -> None:
        """ Add analysis button to the database """
        return None
    # #     selected_file = QtWidgets.QFileDialog.getOpenFileName(None,
    # #             'Seleccione el archivo de datos', 'D:/Data/Asdhar Alonso/',
    # #             'Archivos de Datos (*.csv *.txt *.emt)')[0]

    # #     if selected_file:
    # #         df = pd.read_csv(selected_file, sep='\t', skiprows=43, encoding='ISO-8859-1')

    # #         results = backend.analisis(df)
            
    # #         # ----------------
    # #         # Gráficas Señales
    # #         # ----------------
    # #         data_lat = results['data_x']
    # #         data_ap = results['data_y']
    # #         data_t = results['data_t']

    # #         self.data_lat_max = results['lat_max']
    # #         self.data_lat_t_max = results['lat_t_max']
    # #         self.data_lat_min = results['lat_min']
    # #         self.data_lat_t_min = results['lat_t_min']

    # #         self.lateral_plot.axes.cla()
    # #         self.lateral_plot.fig.subplots_adjust(left=0.05, bottom=0.15, right=1, top=0.95, wspace=0, hspace=0)
    # #         self.lateral_plot.axes.plot(data_t, data_lat, '#42A4F5')
    # #         self.lateral_plot.axes.plot(self.data_lat_t_max, self.data_lat_max, marker="o", markersize=3, markeredgecolor='#FF2D55', markerfacecolor='#FF2D55')
    # #         self.lateral_plot.axes.plot(self.data_lat_t_min, self.data_lat_min, marker="o", markersize=3, markeredgecolor='#FF2D55', markerfacecolor='#FF2D55')
    # #         if self.theme_value:
    # #             self.lat_text_1 = self.lateral_plot.axes.text(self.data_lat_t_max, self.data_lat_max, f'{self.data_lat_max:.2f}', color='#000000')
    # #             self.lat_text_2 = self.lateral_plot.axes.text(self.data_lat_t_min, self.data_lat_min, f'{self.data_lat_min:.2f}', color='#000000')
    # #         else:
    # #             self.lat_text_1 = self.lateral_plot.axes.text(self.data_lat_t_max, self.data_lat_max, f'{self.data_lat_max:.2f}', color='#E5E9F0')
    # #             self.lat_text_2 = self.lateral_plot.axes.text(self.data_lat_t_min, self.data_lat_min, f'{self.data_lat_min:.2f}', color='#E5E9F0')
    # #         self.lateral_plot.draw()

    # #         self.data_ap_max = results['ap_max']
    # #         self.data_ap_t_max = results['ap_t_max']
    # #         self.data_ap_min = results['ap_min']
    # #         self.data_ap_t_min = results['ap_t_min']

    # #         self.antePost_plot.axes.cla()
    # #         self.antePost_plot.fig.subplots_adjust(left=0.05, bottom=0.15, right=1, top=0.95, wspace=0, hspace=0)
    # #         self.antePost_plot.axes.plot(data_t, data_ap, '#42A4F5')
    # #         self.antePost_plot.axes.plot(self.data_ap_t_max, self.data_ap_max, marker="o", markersize=3, markeredgecolor='#FF2D55', markerfacecolor='#FF2D55')
    # #         self.antePost_plot.axes.plot(self.data_ap_t_min, self.data_ap_min, marker="o", markersize=3, markeredgecolor='#FF2D55', markerfacecolor='#FF2D55')
    # #         if self.theme_value:
    # #             self.ap_text_1 = self.antePost_plot.axes.text(self.data_ap_t_max, self.data_ap_max, f'{self.data_ap_max:.2f}', color='#000000')
    # #             self.ap_text_2 = self.antePost_plot.axes.text(self.data_ap_t_min, self.data_ap_min, f'{self.data_ap_min:.2f}', color='#000000')
    # #         else:
    # #             self.ap_text_1 = self.antePost_plot.axes.text(self.data_ap_t_max, self.data_ap_max, f'{self.data_ap_max:.2f}', color='#E5E9F0')
    # #             self.ap_text_2 = self.antePost_plot.axes.text(self.data_ap_t_min, self.data_ap_min, f'{self.data_ap_min:.2f}', color='#E5E9F0')
    # #         self.antePost_plot.draw()

    # #         # --------------
    # #         # Gráficas Áreas
    # #         # --------------
    # #         data_elipse = backend.ellipseStandard(df)
    # #         self.elipse_plot.axes.cla()
    # #         self.elipse_plot.fig.subplots_adjust(left=0.1, bottom=0.1, right=1, top=0.95, wspace=0, hspace=0)
    # #         self.elipse_plot.axes.scatter(data_lat, data_ap, marker='.', color='#42A4F5')
    # #         self.elipse_plot.axes.plot(data_elipse['x'], data_elipse['y'], '#FF2D55')
    # #         self.elipse_plot.axes.axis('equal')
    # #         self.elipse_plot.draw()

    # #         data_convex = backend.convexHull(df)
    # #         self.hull_plot.axes.cla()
    # #         self.hull_plot.fig.subplots_adjust(left=0.1, bottom=0.1, right=1, top=0.95, wspace=0, hspace=0)
    # #         self.hull_plot.axes.scatter(data_lat, data_ap, marker='.', color='#42A4F5')
    # #         self.hull_plot.axes.fill(data_convex['x'], data_convex['y'], edgecolor='#FF2D55', fill=False, linewidth=2)
    # #         self.hull_plot.axes.axis('equal')
    # #         self.hull_plot.draw()

    # #         data_pca = backend.ellipsePCA(df)
    # #         self.pca_plot.axes.cla()
    # #         self.pca_plot.fig.subplots_adjust(left=0.1, bottom=0.1, right=1, top=0.95, wspace=0, hspace=0)
    # #         self.pca_plot.axes.scatter(data_lat, data_ap, marker='.', color='#42A4F5')
    # #         self.pca_plot.axes.plot(data_pca['x'], data_pca['y'], '#FF2D55')
    # #         self.pca_plot.axes.axis('equal')
    # #         self.pca_plot.draw()

    # #         # --------------------------
    # #         # Presentación de resultados
    # #         # --------------------------
    # #         self.lat_rango_value.setText(f'{results["lat_rango"]:.2f}')
    # #         self.lat_vel_value.setText(f'{results["lat_vel"]:.2f}')
    # #         self.lat_rms_value.setText(f'{results["lat_rms"]:.2f}')

    # #         self.ap_rango_value.setText(f'{results["ap_rango"]:.2f}')
    # #         self.ap_vel_value.setText(f'{results["ap_vel"]:.2f}')
    # #         self.ap_rms_value.setText(f'{results["ap_rms"]:.2f}')

    # #         self.cop_vel_value.setText(f'{results["centro_vel"]:.2f}')
    # #         self.distancia_value.setText(f'{results["centro_dist"]:.2f}')
    # #         self.frecuencia_value.setText(f'{results["centro_frec"]:.2f}')

    # #         self.elipse_value.setText(f'{data_elipse["area"]:.2f}')
    # #         self.hull_value.setText(f'{data_convex["area"]:.2f}')
    # #         self.pca_value.setText(f'{data_pca["area"]:.2f}')

    # #         # -------------
    # #         # Base de datos
    # #         # -------------
    # #         study_data = {
    # #             'id_number': self.pacientes_menu.currentText(),
    # #             'file_name': Path(selected_file).name,
    # #             'file_path': selected_file
    # #             }
    # #         self.estudios_list = backend.add_db('estudios', study_data)
            
    # #         self.analisis_menu.clear()
    # #         for data in self.estudios_list:
    # #             self.analisis_menu.addItem(data[2])
    # #         self.analisis_menu.setCurrentIndex(len(self.patientes_list)-1)

    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.information(self, 'Datos Guardados', 'Estudio agregado a la base de datos')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.information(self, 'Data Saved', 'Study added to database')
    # #     else:
    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.critical(self, 'Error de Datos', 'No se seleccióno un archivo para el estudio')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.critical(self, 'Data Error', 'No file for a study was given')


    def on_analysis_delete_clicked(self) -> None:
        """ Delete analysis button from the database """
        return None
    # #     current_study = self.analisis_menu.currentText()

    # #     if current_study != '':
    # #         self.estudios_list = backend.delete_db('estudios', current_study)
            
    # #         self.analisis_menu.clear()
    # #         for data in self.estudios_list:
    # #             self.analisis_menu.addItem(data[2])
    # #         self.analisis_menu.setCurrentIndex(-1)

    # #         self.lateral_plot.axes.cla()
    # #         self.lateral_plot.draw()
    # #         self.antePost_plot.axes.cla()
    # #         self.antePost_plot.draw()
    # #         self.elipse_plot.axes.cla()
    # #         self.elipse_plot.draw()
    # #         self.hull_plot.axes.cla()
    # #         self.hull_plot.draw()
    # #         self.pca_plot.axes.cla()
    # #         self.pca_plot.draw()

    # #         self.lat_rango_value.setText('')
    # #         self.lat_vel_value.setText('')
    # #         self.lat_rms_value.setText('')
    # #         self.ap_rango_value.setText('')
    # #         self.ap_vel_value.setText('')
    # #         self.ap_rms_value.setText('')
    # #         self.cop_vel_value.setText('')
    # #         self.distancia_value.setText('')
    # #         self.frecuencia_value.setText('')
    # #         self.elipse_value.setText('')
    # #         self.hull_value.setText('')
    # #         self.pca_value.setText('')

    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.information(self, 'Datos Guardados', 'Análisis eliminado de la base de datos')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.information(self, 'Data Saved', 'Analysis deleted from database')
    # #     else:
    # #         if self.language_value == 0:
    # #             QtWidgets.QMessageBox.critical(self, 'Error de Análisis', 'No se seleccionó un análisis')
    # #         elif self.language_value == 1:
    # #             QtWidgets.QMessageBox.critical(self, 'Analysis Error', 'No analysis selected')


    def on_analysis_activated(self, current_study: str):
        """ Change analysis and present results
        
        Parameters
        ----------
        current_study: str
            Current study text
        
        Returns
        -------
        None
        """
        return None
    # #     analisis_data = backend.get_db('estudios', self.pacientes_menu.currentText())
    # #     study_path = [item for item in analisis_data if item[2] == current_study][0][3]

    # #     df = pd.read_csv(study_path, sep='\t', skiprows=43, encoding='ISO-8859-1')

    # #     results = backend.analisis(df)
        
    # #     # ----------------
    # #     # Gráficas Señales
    # #     # ----------------
    # #     data_lat = results['data_x']
    # #     data_ap = results['data_y']
    # #     data_t = results['data_t']

    # #     self.data_lat_max = results['lat_max']
    # #     self.data_lat_t_max = results['lat_t_max']
    # #     self.data_lat_min = results['lat_min']
    # #     self.data_lat_t_min = results['lat_t_min']

    # #     self.lateral_plot.axes.cla()
    # #     self.lateral_plot.fig.subplots_adjust(left=0.05, bottom=0.1, right=1, top=0.95, wspace=0, hspace=0)
    # #     self.lateral_plot.axes.plot(data_t, data_lat, '#42A4F5')
    # #     self.lateral_plot.axes.plot(self.data_lat_t_max, self.data_lat_max, marker="o", markersize=3, markeredgecolor='#FF2D55', markerfacecolor='#FF2D55')
    # #     self.lateral_plot.axes.plot(self.data_lat_t_min, self.data_lat_min, marker="o", markersize=3, markeredgecolor='#FF2D55', markerfacecolor='#FF2D55')
    # #     if self.theme_value:
    # #         self.lat_text_1 = self.lateral_plot.axes.text(self.data_lat_t_max, self.data_lat_max, f'{self.data_lat_max:.2f}', color='#000000')
    # #         self.lat_text_2 = self.lateral_plot.axes.text(self.data_lat_t_min, self.data_lat_min, f'{self.data_lat_min:.2f}', color='#000000')
    # #     else:
    # #         self.lat_text_1 = self.lateral_plot.axes.text(self.data_lat_t_max, self.data_lat_max, f'{self.data_lat_max:.2f}', color='#E5E9F0')
    # #         self.lat_text_2 = self.lateral_plot.axes.text(self.data_lat_t_min, self.data_lat_min, f'{self.data_lat_min:.2f}', color='#E5E9F0')
    # #     self.lateral_plot.draw()

    # #     self.data_ap_max = results['ap_max']
    # #     self.data_ap_t_max = results['ap_t_max']
    # #     self.data_ap_min = results['ap_min']
    # #     self.data_ap_t_min = results['ap_t_min']

    # #     # --------------------------
    # #     # Presentación de resultados
    # #     # --------------------------
    # #     self.lat_rango_value.setText(f'{results["lat_rango"]:.2f}')
    # #     self.lat_vel_value.setText(f'{results["lat_vel"]:.2f}')
    # #     self.lat_rms_value.setText(f'{results["lat_rms"]:.2f}')

    # #     self.ap_rango_value.setText(f'{results["ap_rango"]:.2f}')
    # #     self.ap_vel_value.setText(f'{results["ap_vel"]:.2f}')
    # #     self.ap_rms_value.setText(f'{results["ap_rms"]:.2f}')

    # #     self.cop_vel_value.setText(f'{results["centro_vel"]:.2f}')
    # #     self.distancia_value.setText(f'{results["centro_dist"]:.2f}')
    # #     self.frecuencia_value.setText(f'{results["centro_frec"]:.2f}')

    # #     self.elipse_value.setText(f'{data_elipse["area"]:.2f}')
    # #     self.hull_value.setText(f'{data_convex["area"]:.2f}')
    # #     self.pca_value.setText(f'{data_pca["area"]:.2f}')


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
