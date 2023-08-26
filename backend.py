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
        anthropometric measurements:
        height (cm)
        weight (Kg)
        triceps skinfold (mm)
        subscapular skinfold (mm)
        supraspinale skinfold (mm)
        biceps (cm)
        calf (cm)
        humerus (cm)
        femur (cm)
        calf skinfold (cm)
    
    Returns
    -------
    results: dict
        Results of measurements analysis:
        endomorphy score
        mesomorphy score
        ectomorphy score







Determination of Somatotypes
The somatotype values of the participants were determined using Heath Carter method of somatotyping. Based 
on this method, body weight, height, biceps and calf circumference during flexion, humerus and femur breadth, 
triceps, subscapular, suprailiac and calf skinfold as well as following formulas (Ross and Marfell-Jones, 1991; 
Carter, 2002) are used to calculate somatotype values. In addition, “SOMATOTURK” program was used for 
calculations (Marangoz and Özbalcı, 2017).

2.1.1. Determination of Endomorph 
A = triceps + subscapular + suprailiac
B= (170.18 / height) (Adjustment coefficient for height)
Adjusted sum X = A x B 
Endomorph= - 0.7182 + 0.1451 (X) - 0.00068 (X^2) + 0.0000014 (X^3)

2.1.2. Determination of Mesomorph
Mesomorph = (0.858 HB + 0.601 FB +0.188 CAG + 0.161 CCG) - (0.131 H) + 4.5
HB : Humerus breadth (cm) 
FB : Femur breadth (cm) 
CAG : Arm circumference during flexion – (Triceps skinfold /10 )
CCG : Maximal calf circumference – (Calf skinfold /10)
H : Height (cm)

2.1.3. Determination of Ectomorph
Height and weight are calculated in cm and kg, respectively. Height is divided by the cube root of weight to 
calculate HWR (HWR=height/cube root of weight). Ectomorph is calculated based on HWR value using one of 
the formulas below: 
IF HWR ≥ 40.75, Ectomorph = 0.732× HWR– 28.58
IF 38.25 < HWR < 40.75, Ectomorph = 0.463× HWR– 17.63
IF HWR ≤ 38.25, Ectomorph = 0.1










    """
    height = int(measurements['height_value'])
    weight = int(measurements['weight_value'])
    triceps = int(measurements['triceps_value'])
    subscapular = int(measurements['subscapular_value'])
    supraspinale = int(measurements['supraspinale_value'])
    biceps = int(measurements['biceps_value'])
    forearm = int(measurements['forearm_value'])
    humerus = int(measurements['humerus_value'])
    femur = int(measurements['femur_value'])
    knee = int(measurements['knee_value'])

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