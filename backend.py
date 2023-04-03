"""
Backend

This file contains supplementary methods and classes applied to the frontend.

1. Analysis methods: methods to process and analyze anthropometric measurements
2. About class and method: Dialog of information about Qt
"""

from PySide6 import QtWidgets


# -------------------
# Somatotype Function
# -------------------
def somatotype_calculation(measurements: dict) -> dict:
    """ Analysis of anthropometric measurements

    Parameters
    ----------
    measurements: dict
        anthropometric measurements
        height (cm)
        weight (Kg)
        triceps (mm)
        subscapular (mm)
        supraspinale (mm)
        biceps (cm)
        forearm (cm)
        humerus (cm)
        femur (cm)
        knee (cm)
    
    Returns
    -------
    results: dict
        Results of measurements analysis
        endomorphy score
        mesomorphy score
        ectomorphy score
        
    """
    height = measurements['height_textfield']
    weight = measurements['weight_textfield']
    triceps = measurements['triceps_textfield']
    subscapular = measurements['subscapular_textfield']
    supraspinale = measurements['supraspinale_textfield']
    biceps = measurements['biceps_textfield']
    forearm = measurements['forearm_textfield']
    humerus = measurements['humerus_textfield']
    femur = measurements['femur_textfield']
    knee = measurements['knee_textfield']

    endomorphy = 0.143 * (triceps + subscapular + supraspinale) - 0.436 * (height) + 28.57
    mesomorphy = 0.858 * (biceps + forearm) + 0.601 * (humerus + femur) - 0.064 * (height) + 0.04 * (weight) + 3.64
    ectomorphy = 0.732 * (weight) - 0.157

    results = {}

    results['endomorphy'] = endomorphy
    results['mesomorphy'] = mesomorphy
    results['ectomorphy'] = ectomorphy

    return results


# ---------------
# About Qt Dialog
# ---------------
def about_qt_dialog(parent, language: int) -> None:
    """ About Qt Dialog """
    if language == 0:   title = 'Acerca de Qt...'
    elif language == 1: title = 'About Qt...'
    QtWidgets.QMessageBox.aboutQt(parent, title)