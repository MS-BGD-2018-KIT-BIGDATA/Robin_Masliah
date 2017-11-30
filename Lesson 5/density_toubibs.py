#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 09:17:23 2017

@author: robin
"""

import pandas as pd
import pygal
import re


#from pygal.maps.fr import aggregate_regions


def display_densite_medecin():
    densite_medecin = pd.read_csv("TCRD_068-2.csv", sep=',');
    
    densite_medecin['Ensemble des médecins'] = densite_medecin['Ensemble des médecins'].apply(lambda x: re.sub("[^0-9]", "", x))
    densite_medecin['Numéro département']
    densite_medecin_by_dep = dict([(b,int(a)) for b, a in zip(densite_medecin['Numéro département'], densite_medecin['Ensemble des médecins'])])
    
    fr_chart = pygal.maps.fr.Departments(human_readable=True)
    fr_chart.title = 'Densité des médecins par département'
    fr_chart.add('En 2016', densite_medecin_by_dep)
    fr_chart.render_to_png('densite_medecins_par_departement.png')
    

def main():
    display_densite_medecin()


if __name__ == '__main__':
    main()