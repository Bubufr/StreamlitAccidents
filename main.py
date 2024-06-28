import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import subprocess
from dataframes import *
from filtrer import *
# Lancement du chargement des dataframes
subprocess.run(["python", "dataframes.py"])

st.title("Statistiques des accidents routiers sur 2022")
## Affichage des statistiques
ct_accidents=st.container(border=True)
with ct_accidents:
    st.subheader(':boom: Nombre d\'accidents')
    st.header(nb_accidents)


col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader(':racing_car: Nombre de véhicules impliqués')
        st.header(nb_vehicules)
    
    with st.container(border=True):
        st.subheader(':skull_and_crossbones: Nombre de décès')
        st.header(nb_deces)


with col2:
    with st.container(border=True):
        st.subheader(':walking: Nombre d\'usagers impliqués')
        st.header(nb_usagers)

    with st.container(border=True):
        st.subheader(':100: Taux de létalité')
        st.header("{:0.2%}".format(taux_letalite))


## Graphique nb accidents par mois
line_chart = alt.Chart(df_acc_par_mois.sort_values("mois", ascending=True)).mark_bar().encode(
    x=alt.X('label_mois', sort=None).title('Mois de survenance'),
    y=alt.Y('count').title('Nombre d\'accidents'),
)
st.altair_chart(line_chart, use_container_width=True)

## Graphique nb accidents par jour
st.line_chart(df_acc_par_jour, x='date', y='Accident_Id', x_label='Date', y_label='Nb d\'accidents')

## Graphique répartition par gravité
labels = f'{df_usagers_par_gravite.iloc[0,0]} ({df_usagers_par_gravite.iloc[0,1]})', \
    f'{df_usagers_par_gravite.iloc[1,0]} ({df_usagers_par_gravite.iloc[1,1]}), ', \
    f'{df_usagers_par_gravite.iloc[2,0]} ({df_usagers_par_gravite.iloc[2,1]}), ', \
    f'{df_usagers_par_gravite.iloc[3,0]} ({df_usagers_par_gravite.iloc[3,1]}), '
valeurs = [ df_usagers_par_gravite.iloc[0,1], \
            df_usagers_par_gravite.iloc[1,1], \
            df_usagers_par_gravite.iloc[2,1], \
            df_usagers_par_gravite.iloc[3,1]]

fig1, ax1 = plt.subplots()
ax1.pie(valeurs, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
st.pyplot(fig1)


## Graphique répartition par type de véhicule
line_chart = alt.Chart(df_acc_par_type_vehicule.sort_values("Num_Acc", ascending=False)).mark_bar().encode(
    x=alt.X('Num_Acc').title('Nombre d\'accidents'),
    y=alt.Y('catv', sort=None).title('Type de véhicule'),
)
st.altair_chart(line_chart, use_container_width=True)

## Graphique répartition par type de trajet
st.bar_chart(df_acc_par_type_trajet, x='trajet', y='Num_Acc', x_label="Type de trajet", y_label="Nombre d'accidents")

## Graphique répartition par sexe
labels = f'Hommes ({nb_acc_hommes})', f'Femmes ({nb_acc_femmes})'
valeurs = [nb_acc_hommes, nb_acc_femmes]
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(valeurs, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
st.pyplot(fig1)

## Graphique nb accidents par conditions atmosphériques
line_chart = alt.Chart(df_acc_par_meteo.sort_values("Accident_Id", ascending=False)).mark_bar().encode(
    y=alt.Y('atm', sort=None).title('Conditions atomsphériques'),
    x=alt.X('Accident_Id', sort=None).title('Nombre d\'accidents'),
)
st.altair_chart(line_chart, use_container_width=True)

## Graphique de répartition des obstacles mobiles heurtés
line_chart = alt.Chart(df_obstacles_heurtes_par_type.sort_values("Num_Acc", ascending=False)).mark_bar().encode(
    x=alt.X('obsm', sort=None).title('Type d\'obstacle mobile'),
    y=alt.Y('Num_Acc').title('Nombre d\'accidents'),
)
st.altair_chart(line_chart, use_container_width=True)

#Listes pour filtres
listeDep = df_carac_lieux['dep'].unique()
#Les conditions atmosphériques.
listeAtm = df_carac_lieux['atm'].unique()
#Les conditions d'éclairage.
listeLum = df_carac_lieux['lum'].unique()
#La localisation (en ou hors agglomération).
listeAgg = df_carac_lieux['agg'].unique()
#La catégorie de route.
listeCatr = df_carac_lieux['catr'].unique()
#Le type de collision.
listeCol = df_carac_lieux['col'].unique()

with st.sidebar:
    stFilter = st.toggle("Filtrer")
#Filtres streamlit
    stDep = st.selectbox(
    "Département",sorted(listeDep), index = None, placeholder = "Tous"
    ,format_func=lambda x: dicoDep.get(x)
    )
#Les conditions atmosphériques.
    stAtm = st.selectbox(
    "Conditions atmosphériques",sorted(listeAtm), index = None, placeholder = "Tous"
    ,format_func=lambda x: dicoAtm.get(x)
    )
#Les conditions d'éclairage.
    stLum = st.selectbox(
    "Conditions d'éclairage",sorted(listeLum), index = None, placeholder = "Tous"
    ,format_func=lambda x: dicoLum.get(x)
    )
#La localisation (en ou hors agglomération).
    stAgg = st.selectbox(
    "Localisation",sorted(listeAgg), index = None, placeholder = "Tous"
    ,format_func=lambda x: dicoAgg.get(x)
    )
#La catégorie de route.
    stCatr = st.selectbox(
    "Catégorie de route",sorted(listeCatr),index = None, placeholder = "Tous"
    ,format_func=lambda x: dicoCatr.get(x)
    )
#Le type de collision.
    stCol = st.selectbox(
    "Type de collision", sorted(listeCol), index = None, placeholder = "Tous"
    ,format_func=lambda x: dicoCol.get(x)
    )

if stFilter:
    df_carac_lieuxFilter = appliquerFiltres(df_carac_lieux,stDep,stAtm,stLum,stAgg,stCatr,stCol)
    df_carac_vehiculesFilter = appliquerFiltres(df_carac_vehicules,stDep,stAtm,stLum,stAgg,stCatr,stCol)
    df_carac_usagersFilter = appliquerFiltres(df_carac_usagers,stDep,stAtm,stLum,stAgg,stCatr,stCol)
    nb_accidents_filter = len(df_carac_lieuxFilter)
    nb_vehicules_filter = len(df_carac_vehiculesFilter)
    nb_usagers_filter = len(df_carac_usagersFilter)
    nb_deces_filter = len(df_carac_usagersFilter[(df_carac_usagersFilter['grav'] == 2)])
    taux_letalite_filter = nb_deces_filter / nb_accidents_filter
else:
    df_carac_lieuxFilter = df_carac_lieux.copy()
    df_carac_vehiculesFilter = df_carac_vehicules.copy()
    df_carac_usagersFilter = df_carac_usagers.copy()
    nb_accidents_filter = nb_accidents
    nb_vehicules_filter = nb_vehicules
    nb_usagers_filter = nb_usagers
    nb_deces_filter = nb_deces
    taux_letalite_filter = taux_letalite

indic0, indic1, indic2, indic3, indic4 = st.columns(5)
with indic0:
    st.caption(':boom: Nombre d\'accidents')
    st.subheader(nb_accidents_filter)
with indic1:
    st.caption(':racing_car: Nombre de véhicules impliqués')
    st.subheader(nb_vehicules_filter)
with indic2:
    st.caption(':walking: Nombre d\'usagers impliqués')
    st.subheader(nb_usagers_filter)
with indic3:
    st.caption(':skull_and_crossbones: Nombre de décès')
    st.write('')
    st.subheader(nb_deces_filter)
with indic4:
    st.caption(':100: Taux de létalité.')
    st.write('')
    st.subheader("{:0.2%}".format(taux_letalite_filter))
st.map(df_carac_lieuxFilter,latitude = 'latitude', longitude = 'longitude')
