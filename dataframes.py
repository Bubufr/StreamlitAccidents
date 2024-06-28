import numpy as np
import pandas as pd
from constantes import *
import streamlit as st

# Chargement des fichiers de données
lieux = pd.read_csv('data/lieux.csv', sep=";", low_memory=False)
caracteristiques = pd.read_csv('data/carcteristiques.csv', sep=";")
usagers = pd.read_csv('data/usagers.csv', sep=";")
vehicules = pd.read_csv('data/vehicules.csv', sep=";")

## Dataframe Nb accidents par mois
df_acc_par_mois=caracteristiques.copy()
df_acc_par_mois=df_acc_par_mois['mois'].value_counts().sort_index().reset_index()
df_acc_par_mois['label_mois']=df_acc_par_mois['mois'].map(lambda mois: dico_mois[mois])

## Dataframe Nb accidents par jour
df_acc_par_jour=caracteristiques.copy()
df_acc_par_jour=df_acc_par_jour[['Accident_Id', 'jour', 'mois']]
df_acc_par_jour['date'] = "2022-" + df_acc_par_jour['mois'].astype(str) + "-" + df_acc_par_jour['jour'].astype(str)
df_acc_par_jour['date'] = pd.to_datetime(df_acc_par_jour['date'])
df_acc_par_jour = df_acc_par_jour[['Accident_Id', 'date']].groupby(by='date').count().reset_index()

## Dataframe Répartition par gravité
df_usagers_par_gravite=usagers.copy()
df_usagers_par_gravite=df_usagers_par_gravite.loc[(df_usagers_par_gravite['grav'] != -1), 'grav'].value_counts().sort_index().reset_index()
df_usagers_par_gravite['grav']=df_usagers_par_gravite['grav'].map(lambda gravite: dico_gravite[gravite])

## Dataframe Répartition par type de véhicule
df_acc_par_type_vehicule=vehicules.copy()
df_acc_par_type_vehicule=df_acc_par_type_vehicule[(df_acc_par_type_vehicule['catv'] != -1)]
df_acc_par_type_vehicule=df_acc_par_type_vehicule[['Num_Acc', 'catv']].groupby(by='catv').count().reset_index()
df_acc_par_type_vehicule["catv"]=df_acc_par_type_vehicule["catv"].map(lambda cat: dico_categorie[cat])

## Dataframe Répartition par type de trajet
df_acc_par_type_trajet=usagers.copy()
df_acc_par_type_trajet = df_acc_par_type_trajet[['Num_Acc', 'trajet']].groupby(by='trajet').count().reset_index()
df_acc_par_type_trajet["trajet"]=df_acc_par_type_trajet["trajet"].map(lambda type: dico_type_trajet[type])
df_acc_par_type_trajet = df_acc_par_type_trajet.sort_values('Num_Acc', ascending=False)

## Variables Répartition par sexe
nb_usagers_par_sexe = usagers[['Num_Acc', 'sexe']]
nb_usagers_par_sexe = nb_usagers_par_sexe.groupby(by="sexe").count().reset_index()
nb_acc_hommes = nb_usagers_par_sexe[(nb_usagers_par_sexe['sexe'] == 1)].iloc[0,1]
nb_acc_femmes = nb_usagers_par_sexe[(nb_usagers_par_sexe['sexe'] == 2)].iloc[0,1]

## Dataframe Accidents par conditions atmosphériques
df_acc_par_meteo=caracteristiques.copy()
df_acc_par_meteo=df_acc_par_meteo[['Accident_Id', 'atm']].groupby(by='atm').count().reset_index()
df_acc_par_meteo=df_acc_par_meteo.loc[(df_acc_par_meteo['atm'] != -1)]
df_acc_par_meteo['atm']=df_acc_par_meteo['atm'].map(lambda code: dico_conditions_atmospherique[code])

## Dataframe Répartition des obstacles mobiles heurtés
df_obstacles_heurtes_par_type=vehicules.copy()
df_obstacles_heurtes_par_type=df_obstacles_heurtes_par_type.loc[(df_obstacles_heurtes_par_type['obsm'] != -1), ['Num_Acc', 'obsm']]
df_obstacles_heurtes_par_type = df_obstacles_heurtes_par_type.groupby(by='obsm').count().reset_index()
df_obstacles_heurtes_par_type['obsm'] = df_obstacles_heurtes_par_type['obsm'].map(lambda code: dico_obstacle[code])

## Rapprochement des lieux sur les caractéristiques
# Dataframe pour les lieux
df_carac_lieux = pd.merge(caracteristiques, lieux[['Num_Acc','catr']], how = 'left', left_on=['Accident_Id'], right_on = ['Num_Acc'])
df_carac_lieux['latitude'] = df_carac_lieux['lat'].str.replace(',','.',).astype(float)
df_carac_lieux['longitude'] = df_carac_lieux['long'].str.replace(',','.').astype(float)

# Dataframe pour les véhicules
df_carac_vehicules = pd.merge(df_carac_lieux, vehicules[['Num_Acc','id_vehicule']], how = 'left')

# Dataframe pour les véhicules
df_carac_usagers = pd.merge(df_carac_lieux, usagers[['Num_Acc','id_usager','grav']], how = 'left')

nb_accidents = len(df_carac_lieux)
nb_vehicules = len(df_carac_vehicules)
nb_usagers = len(df_carac_usagers)
nb_deces = len(df_carac_usagers[(df_carac_usagers['grav'] == 2)])
taux_letalite = nb_deces / nb_accidents