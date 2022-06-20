"""
Backend

This file contains supplementary methods and classes applied to the frontend.

1. Class MPLCanvas: configuration of the plot canvas
2. Analysis methods: methods to process and analyze anthropometric measurements
3. Database methods: methods of the database operations
4. About class and method: Dialogs of information about me and Qt

"""

from PyQt6 import QtWidgets
from PyQt6.QtCore import QSettings

import sys
import numpy as np
import pandas as pd
import psycopg2

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import material3_components as mt3

light = {
    'surface': '#B2B2B2',
    'on_surface': '#000000'
}

dark = {
    'surface': '#2E3441',
    'on_surface': '#E5E9F0'
}

class MPLCanvas(FigureCanvasQTAgg):
    def __init__(self, parent, theme: bool) -> None:
        """ Canvas settings for plotting signals """
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)

        FigureCanvasQTAgg.__init__(self, self.fig)
        self.setParent(parent)

        self.apply_styleSheet(theme)

    def apply_styleSheet(self, theme):
        self.fig.subplots_adjust(left=0.05, bottom=0.15, right=1, top=0.95, wspace=0, hspace=0)
        self.axes.spines['top'].set_visible(False)
        self.axes.spines['right'].set_visible(False)
        self.axes.spines['bottom'].set_visible(False)
        self.axes.spines['left'].set_visible(False)
        if theme:
            self.fig.set_facecolor(f'{light["surface"]}')
            self.axes.set_facecolor(f'{light["surface"]}')
            self.axes.xaxis.label.set_color(f'{light["on_surface"]}')
            self.axes.yaxis.label.set_color(f'{light["on_surface"]}')
            self.axes.tick_params(axis='both', colors=f'{light["on_surface"]}', labelsize=8)
        else:
            self.fig.set_facecolor(f'{dark["surface"]}')
            self.axes.set_facecolor(f'{dark["surface"]}')
            self.axes.xaxis.label.set_color(f'{dark["on_surface"]}')
            self.axes.yaxis.label.set_color(f'{dark["on_surface"]}')
            self.axes.tick_params(axis='both', colors=f'{dark["on_surface"]}', labelsize=8)


# ---------------------------
# Funciones Análisis de Datos
# ---------------------------
def analisis(df: pd.DataFrame) -> dict:
    """ Analysis of anthropometric measurements

    Parameters
    ----------
    df: pd.DataFrame
        Pandas dataframe converted from balance signal data from file
    
    Returns
    -------
    results: dict
        Results of dataframe analysis of lateral, antero-posterior, and
        center of pressure oscillations
        data_x: pd.DataFrame
            Lateral signal
        data_y: pd.DataFrame
            Antero-posterior signal
        data_t: 
            Time signal
        lat_max: float
            Lateral signal maximum value
        lat_t_max: float
            Lateral signal correspondent time value for maximum value
        lat_min: float
            Lateral signal minimum value
        lat_t_min: float
            Lateral signal correspondent time value for minimum value
        
    """
    # results = {}

    # data_x = df.iloc[:,0]
    # data_y = df.iloc[:,1]
    # data_t = np.linspace(0, len(df) / 10, len(df))

    # results['data_x'] = data_x
    # results['data_y'] = data_y
    # results['data_t'] = data_t

    # x_max = data_x.max()
    # x_min = data_x.min()
    # y_max = data_y.max()
    # y_min = data_y.min()

    # results['lat_max'] = x_max
    # results['lat_t_max'] = data_x.idxmax() / 10
    # results['lat_min'] = x_min
    # results['lat_t_min'] = data_x.idxmin() / 10

    # results['ap_max'] = y_max
    # results['ap_t_max'] = data_y.idxmax() / 10
    # results['ap_min'] = y_min
    # results['ap_t_min'] = data_y.idxmin() / 10

    # results['lat_rango'] = x_max - x_min
    # results['ap_rango'] = y_max - y_min

    # tAnalisis = len(df) / 10
    # time_analysis = len(df) - 1
    # den = tAnalisis / len(df)

    # # SEÑAL X ----------------------------------------------------------------
    # avgX = data_x.sum() / len(df)

    # numX = abs(data_x.diff()).dropna()
    # velSgnX = numX / den
    # results['lat_vel'] = velSgnX.sum() / time_analysis

    # numRMSX = (data_x - avgX) * (data_x - avgX)
    # results['lat_rms'] = np.sqrt(numRMSX.sum() / time_analysis)
    
    # # SEÑAL Y ----------------------------------------------------------------
    # avgY = data_y.sum() / len(df)

    # numY = abs(data_y.diff()).dropna()
    # velSgnY = numY / den
    # results['ap_vel'] = velSgnY.sum() / time_analysis

    # numRMSY = (data_y - avgY) * (data_y - avgY)
    # results['ap_rms'] = np.sqrt(numRMSY.sum() / time_analysis)

    # # SEÑALES X Y ------------------------------------------------------------
    # num2 = np.sqrt((numX * numX) + (numY * numY))
    # numVMT = num2 / tAnalisis
    # results['centro_vel'] = numVMT.sum()

    # numDist = np.sqrt((data_x * data_x) + (data_y * data_y))
    # distM = numDist / tAnalisis

    # results['centro_dist'] = distM.sum()
    # results['centro_frec'] = numVMT.sum() / (2 * np.pi)

    # return results


# -----------------------
# Funciones Base de Datos
# -----------------------
def create_db(db_table: str) -> list:
    """ Creates database tables if they don't exist and returns table data
    
    Parameters
    ----------
    db_table: str
        Database table name
    
    Returns
    -------
    table_data: list
        Data of table if exists (empty if table don't exist)
    """
    settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
    db_host = settings.value('db_host')
    db_port = settings.value('db_port')
    db_name = settings.value('db_name')
    db_user = settings.value('db_user')
    db_password = settings.value('db_password')
    try:
        connection = psycopg2.connect(user=db_user, 
                                  password=db_password, 
                                  host=db_host, 
                                  port=db_port, 
                                  database=db_name)
    except psycopg2.OperationalError as err:
        return err

    cursor = connection.cursor()

    if db_table == 'pacientes':
        cursor.execute("""CREATE TABLE IF NOT EXISTS pacientes (
                        id serial PRIMARY KEY,
                        last_name VARCHAR(128) NOT NULL,
                        first_name VARCHAR(128) NOT NULL,
                        id_type CHAR(2) NOT NULL,
                        id_number BIGINT UNIQUE NOT NULL,
                        birth_date VARCHAR(128) NOT NULL,
                        sex CHAR(1) NOT NULL,
                        weight NUMERIC(5,2) NOT NULL,
                        weight_unit CHAR(2) NOT NULL,
                        height NUMERIC(3,2) NOT NULL,
                        height_unit VARCHAR(7) NOT NULL,
                        bmi NUMERIC(4,2) NOT NULL
                        )""")
    elif db_table == 'estudios':
        cursor.execute("""CREATE TABLE IF NOT EXISTS estudios (
                        id serial PRIMARY KEY,
                        id_number BIGINT NOT NULL,
                        triceps_endo SMALLINT NOT NULL,
                        subescapular_endo SMALLINT NOT NULL,
                        supraespinal_endo SMALLINT NOT NULL,
                        calf_endo SMALLINT NOT NULL,
                        altura_meso NUMERIC(3,2) NOT NULL,
                        humero_meso NUMERIC(4,2) NOT NULL,
                        femur_meso NUMERIC(4,2) NOT NULL,
                        biceps_meso NUMERIC(4,2) NOT NULL,
                        tricipital_meso NUMERIC(4,2) NOT NULL,
                        calf_perimetro_meso NUMERIC(4,2) NOT NULL,
                        calf_pliegue_meso NUMERIC(4,2) NOT NULL,
                        peso_ecto NUMERIC(5,2) NOT NULL
                        )""")

    connection.commit()

    table_data = None
    if db_table == 'pacientes':
        cursor.execute('SELECT * FROM pacientes ORDER BY id ASC')
        table_data = cursor.fetchall()
    
    connection.close()

    return table_data


def add_db(db_table: str, data: dict) -> list:
    """ Adds data to database table and returns table data updated
    
    Parameters
    ----------
    db_table: str
        Database table name
    data: dict
        Data from patient or study file
    
    Returns
    -------
    table_data: list
        Data of table updated
    """
    if db_table == 'pacientes':
        last_name_value = data['last_name']
        first_name_value = data['first_name']
        id_type_value = data['id_type']
        id_value = data['id']
        birth_date_value = data['birth_date']
        sex_value = data['sex']
        weight_value = data['weight']
        weight_unit = data['weight_unit']
        height_value = data['height']
        height_unit = data['height_unit']
        bmi_value = data['bmi']
    # elif db_table == 'estudios':
    #     id_value = data['id_number']
    #     file_name_value = data['file_name']
    #     file_path_value = data['file_path']

    settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
    db_host = settings.value('db_host')
    db_port = settings.value('db_port')
    db_name = settings.value('db_name')
    db_user = settings.value('db_user')
    db_password = settings.value('db_password')
    connection = psycopg2.connect(user=db_user, 
                                  password=db_password, 
                                  host=db_host, 
                                  port=db_port, 
                                  database=db_name)
    cursor = connection.cursor()

    insert_query = None
    if db_table == 'pacientes':
        insert_query = f"""INSERT INTO pacientes (last_name, first_name, id_type, id_number, birth_date, sex, weight, weight_unit, height, height_unit, bmi) 
                    VALUES ('{last_name_value}', '{first_name_value}', '{id_type_value}', '{id_value}', '{birth_date_value}', '{sex_value}', '{weight_value}', '{weight_unit}', '{height_value}', '{height_unit}', '{bmi_value}')"""
    # elif db_table == 'estudios':
    #     insert_query = f"""INSERT INTO estudios (id_number, file_name, file_path) 
    #                 VALUES ('{id_value}', '{file_name_value}', '{file_path_value}')"""

    cursor.execute(insert_query)
    connection.commit()

    table_data = None
    if db_table == 'pacientes':
        cursor.execute('SELECT * FROM pacientes ORDER BY id ASC')
        table_data = cursor.fetchall()
    # elif db_table == 'estudios':
    #     cursor.execute(f"SELECT * FROM estudios WHERE id_number='{id_value}' ORDER BY id ASC")
    #     table_data = cursor.fetchall()
    
    connection.close()

    return table_data


def get_db(db_table: str, data_id: str) -> list:
    """ Get data from database table
    
    Parameters
    ----------
    db_table: str
        Database table name
    data_id: str
        Patient id number
    
    Returns
    -------
    table_data: list
        Data of table
    """
    settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
    db_host = settings.value('db_host')
    db_port = settings.value('db_port')
    db_name = settings.value('db_name')
    db_user = settings.value('db_user')
    db_password = settings.value('db_password')
    connection = psycopg2.connect(user=db_user, 
                                  password=db_password, 
                                  host=db_host, 
                                  port=db_port, 
                                  database=db_name)
    cursor = connection.cursor()

    table_data = None
    if db_table == 'pacientes':
        cursor.execute(f"SELECT * FROM pacientes WHERE id_number='{data_id}'")
    elif db_table == 'estudios':
        cursor.execute(f"SELECT * FROM estudios WHERE id_number='{data_id}'")
    table_data = cursor.fetchall()
    connection.close()
    
    return table_data


def edit_db(db_table: str, id_db: int, data: dict) -> list:
    """ Edit data of a database table and returns table data updated
    
    Parameters
    ----------
    db_table: str
        Database table name
    id_db: int
        Database item id from table
    data: dict
        Data from patient or study file
    
    Returns
    -------
    table_data: list
        Data of table updated
    """
    if db_table == 'pacientes':
        last_name_value = data['last_name']
        first_name_value = data['first_name']
        id_type_value = data['id_type']
        id_value = data['id']
        birth_date_value = data['birth_date']
        sex_value = data['sex']
        weight_value = data['weight']
        weight_unit = data['weight_unit']
        height_value = data['height']
        height_unit = data['height_unit']
        bmi_value = data['bmi']
    # elif db_table == 'estudios':
    #     id_value = data['id']
    #     file_name_value = data['file_name']
    #     file_path_value = data['file_path']

    settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
    db_host = settings.value('db_host')
    db_port = settings.value('db_port')
    db_name = settings.value('db_name')
    db_user = settings.value('db_user')
    db_password = settings.value('db_password')
    connection = psycopg2.connect(user=db_user, 
                                  password=db_password, 
                                  host=db_host, 
                                  port=db_port, 
                                  database=db_name)
    cursor = connection.cursor()    
    
    update_query = None
    if db_table == 'pacientes':
        update_query = f"""UPDATE pacientes 
                    SET (last_name, first_name, id_type, id_number, birth_date, sex, weight, weight_unit, height, height_unit, bmi)
                    = ('{last_name_value}', '{first_name_value}', '{id_type_value}', '{id_value}', '{birth_date_value}', '{sex_value}', '{weight_value}', '{weight_unit}', '{height_value}', '{height_unit}', '{bmi_value}') 
                    WHERE id = '{id_db}' """
    # elif db_table == 'estudios':
    #     update_query = f"""UPDATE estudios 
    #                 SET (id_number, file_name, file_path)
    #                 = ('{id_value}', '{file_name_value}', '{file_path_value}') 
    #                 WHERE id = '{id_db}' """
    
    cursor.execute(update_query)
    connection.commit()

    table_data = None
    if db_table == 'pacientes':
        cursor.execute('SELECT * FROM pacientes ORDER BY id ASC')
        table_data = cursor.fetchall()
    elif db_table == 'estudios':
        cursor.execute('SELECT * FROM estudios')
        table_data = cursor.fetchall()
    
    connection.close()

    return table_data


def delete_db(db_table: str, data: str) -> list:
    """ Delete data from database table and returns table data updated
    
    Parameters
    ----------
    db_table: str
        Database table name
    data: str
        From patient: id number
        From study: study file
    
    Returns
    -------
    table_data: list
        Data of table updated
    """
    settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
    db_host = settings.value('db_host')
    db_port = settings.value('db_port')
    db_name = settings.value('db_name')
    db_user = settings.value('db_user')
    db_password = settings.value('db_password')
    connection = psycopg2.connect(user=db_user, 
                                  password=db_password, 
                                  host=db_host, 
                                  port=db_port, 
                                  database=db_name)
    cursor = connection.cursor()

    delete_query = None
    if db_table == 'pacientes':
        delete_query = f"DELETE FROM pacientes WHERE id_number='{data}'"
    elif db_table == 'estudios':
        delete_query = f"DELETE FROM estudios WHERE file_name='{data}'"
    cursor.execute(delete_query)
    connection.commit()

    table_data = None
    if db_table == 'pacientes':
        cursor.execute('SELECT * FROM pacientes ORDER BY id ASC')
        table_data = cursor.fetchall()
    elif db_table == 'estudios':
        cursor.execute('SELECT * FROM estudios')
        table_data = cursor.fetchall()
    
    connection.close()

    return table_data


# ----------------
# About App Dialog
# ----------------
class AboutApp(QtWidgets.QDialog):
    def __init__(self) -> None:
        """ About Me Dialog """
        super().__init__()
        # --------
        # Settings
        # --------
        self.settings = QSettings(f'{sys.path[0]}/settings.ini', QSettings.Format.IniFormat)
        self.language_value = int(self.settings.value('language'))
        self.theme_value = eval(self.settings.value('theme'))

        # ----------------
        # Generación de UI
        # ----------------
        width = 320
        height = 408
        screen_x = int(self.screen().availableGeometry().width() / 2 - (width / 2))
        screen_y = int(self.screen().availableGeometry().height() / 2 - (height / 2))

        if self.language_value == 0:
            self.setWindowTitle('Acerca de...')
        elif self.language_value == 1:
            self.setWindowTitle('About...')
        self.setGeometry(screen_x, screen_y, width, height)
        self.setMinimumSize(width, height)
        self.setMaximumSize(width, height)
        self.setModal(True)
        self.setObjectName('object_about')
        if self.theme_value:
            self.setStyleSheet(f'QWidget#object_about {{ background-color: #E5E9F0;'
                f'color: #000000 }}')
        else:
            self.setStyleSheet(f'QWidget#object_about {{ background-color: #3B4253;'
                f'color: #E5E9F0 }}')


        self.about_card = mt3.Card(self, 'about_card',
            (8, 8, width-16, height-16), ('Somatotipo', 'Somatotype'), 
            self.theme_value, self.language_value)

        y, w = 48, width - 32
        mt3.FieldLabel(self.about_card, 'version_label',
            (8, y), ('Versión: 1.0', 'Version: 1.0'), self.theme_value, self.language_value)

        y += 48
        mt3.FieldLabel(self.about_card, 'desarrollado_label',
            (8, y), ('Desarrollado por:', 'Developed by:'), self.theme_value, self.language_value)

        y += 48
        mt3.IconLabel(self.about_card, 'nombre_icon',
            (8, y), 'person', self.theme_value)

        y += 6
        mt3.FieldLabel(self.about_card, 'nombre_label',
            (48, y), ('Carlos Andrés Wilches Pérez', 'Carlos Andrés Wilches Pérez'), self.theme_value, self.language_value)

        y += 30
        mt3.IconLabel(self.about_card, 'profesion_icon',
            (8, y), 'school', self.theme_value)
        
        y += 6
        mt3.FieldLabel(self.about_card, 'profesion_label',
            (48, y), ('Ingeniero Electrónico, BSc. MSc. PhD.', 'Electronic Engineer, BSc. MSc. PhD.'), self.theme_value, self.language_value)
        
        y += 24
        mt3.FieldLabel(self.about_card, 'profesion_label',
            (48, y), ('Universidad Nacional de Colombia', 'Universidad Nacional de Colombia'), self.theme_value, self.language_value)

        y += 32
        mt3.FieldLabel(self.about_card, 'profesion_label',
            (48, y), ('Maestría en Ingeniería Electrónica', 'Master in Electronic Engineering'), self.theme_value, self.language_value)

        y += 24
        mt3.FieldLabel(self.about_card, 'profesion_label',
            (48, y), ('Doctor en Ingeniería', 'Doctor in Engineering'), self.theme_value, self.language_value)

        y += 24
        mt3.FieldLabel(self.about_card, 'profesion_label',
            (48, y), ('Pontificia Universidad Javeriana', 'Pontificia Universidad Javeriana'), self.theme_value, self.language_value)

        y += 24
        mt3.IconLabel(self.about_card, 'email_icon',
            (8, y), 'mail', self.theme_value)

        y += 6
        mt3.FieldLabel(self.about_card, 'email_label',
            (48, y), ('cawilchesp@outlook.com', 'cawilchesp@outlook.com'), self.theme_value, self.language_value)

        y += 32
        self.aceptar_button = mt3.TextButton(self.about_card, 'aceptar_button',
            (w-92, y, 100), ('Aceptar', 'Ok'), 'done.png', self.theme_value, self.language_value)
        self.aceptar_button.clicked.connect(self.on_aceptar_button_clicked)

    def on_aceptar_button_clicked(self):
        self.close()

# ---------------
# About Qt Dialog
# ---------------
def about_qt_dialog(parent, language: int) -> None:
    """ About Qt Dialog """
    if language == 0:   title = 'Acerca de Qt...'
    elif language == 1: title = 'About Qt...'
    QtWidgets.QMessageBox.aboutQt(parent, title)