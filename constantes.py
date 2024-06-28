dico_categorie = {
    0: "Indéterminable", 
    1: "Bicyclette", 
    2: "Cyclomoteur <50cm3", 
    3: "Voiturette (Quadricycle à moteur carrossé) (anciennement \"voiturette ou tricycle à moteur\")", 
    4: "Référence inSutilisée depuis 2006 (scooter immatriculé)", 
    5: "Référence inutilisée depuis 2006 (motocyclette)", 
    6: "Référence inutilisée depuis 2006 (side-car)", 
    7: "VL seul",
    8: "Référence inutilisée depuis 2006 (VL + caravane)", 
    9: "Référence inutilisée depuis 2006 (VL + remorque)", 
    10: "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC<= 3,5T)", 
    11: "Référence inutilisée depuis 2006 (VU (10) + caravane)" ,
    12: "Référence inutilisée depuis 2006 (VU (10) + remorque)", 
    13: "PL seul 3,5T <PTCA <= 7,5T" ,
    14: "PL seul > 7,5T" ,
    15: "PL > 3,5T + remorque" ,
    16: "Tracteur routier seul" ,
    17: "Tracteur routier + semi-remorque" ,
    18: "Référence inutilisée depuis 2006 (transport en commun)" ,
    19: "Référence inutilisée depuis 2006 (tramway)" ,
    20: "Engin spécial" ,
    21: "Tracteur agricole" ,
    30: "Scooter < 50 cm3" ,
    31: "Motocyclette > 50 cm3 et <= 125 cm3" ,
    32: "Scooter > 50 cm3 et <= 125 cm3" ,
    33: "Motocyclette > 125 cm3" ,
    34: "Scooter > 125 cm3 ",
    35: "Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)" ,
    36: "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)" ,
    37: "Autobus" ,
    38: "Autocar", 
    39: "Train", 
    40: "Tramway" ,
    41: "3RM <= 50 cm3" ,
    42: "3RM > 50 cm3 <= 125 cm3" ,
    43: "3RM > 125 cm3" ,
    50: "EDP à moteur" ,
    60: "EDP sans moteur" ,
    80: "VAE" ,
    99: "Autre véhicule "
}

dico_type_trajet = {
    -1: "Non renseigné",
    0: "Non renseigné" ,
    1: "Domicile: travail", 
    2: "Domicile: école", 
    3: "Courses: achats", 
    4: "Utilisation professionnelle", 
    5: "Promenade: loisirs", 
    9: "Autre"
}

dico_conditions_atmospherique = {
    -1: "Non renseigné",
    1: "Normale", 
    2: "Pluie légère", 
    3: "Pluie forte", 
    4: "Neige - grêle",
    5: "Brouillard - fumée", 
    6: "Vent fort - tempête", 
    7: "Temps éblouissant", 
    8: "Temps couvert", 
    9: "Autre" 
}

dico_obstacle = {
    -1: "Non renseigné",
    0: "Aucun", 
    1: "Piéton", 
    2: "Véhicule", 
    4: "Véhicule sur rail", 
    5: "Animal domestique", 
    6: "Animal sauvage", 
    9: "Autre",
}

dicoAtm = {-1 :  '– Non renseigné'}
dicoAtm[1] = 'Normale'
dicoAtm[2] = 'Pluie légère'
dicoAtm[3] = 'Pluie forte'
dicoAtm[4] = 'Neige - grêle'
dicoAtm[5] = 'Brouillard - fumée'
dicoAtm[6] = 'Vent fort - tempête'
dicoAtm[7] = 'Temps éblouissant'
dicoAtm[8] = 'Temps couvert'
dicoAtm[9] = 'Autre'
 
dicoLum = {1: 'Plein jour'}
dicoLum[2] = 'Crépuscule ou aube'
dicoLum[3] = 'Nuit sans éclairage public'
dicoLum[4] = 'Nuit avec éclairage public non allumé'
dicoLum[5] = 'Nuit avec éclairage public allumé'
 
dicoAgg = {1: 'Hors agglomération'}
dicoAgg[2] = 'En agglomération'
 
dicoCatr =  {1: 'Autoroute'}
dicoCatr[2] = 'Route nationale'
dicoCatr[3] = 'Route Départementale'
dicoCatr[4] = 'Voie Communales'
dicoCatr[5] = 'Hors réseau public'
dicoCatr[6] = 'Parc de stationnement ouvert à la circulation publique'
dicoCatr[7] = 'Routes de métropole urbaine'
dicoCatr[9] = 'autre'
 
dicoCol = {-1 : 'Non renseigné'}
dicoCol[1] = 'Deux véhicules - frontale'
dicoCol[2] = 'Deux véhicules – par l’arrière'
dicoCol[3] = 'Deux véhicules – par le coté'
dicoCol[4] = 'Trois véhicules et plus – en chaîne'
dicoCol[5] = 'Trois véhicules et plus - collisions multiples'
dicoCol[6] = 'Autre collision'
dicoCol[7] = 'Sans collision'
 
dicoDep = {'01' : '01 - Ain'}
 
dico_categorie = {
    0: "Indéterminable",
    1: "Bicyclette",
    2: "Cyclomoteur <50cm3",
    3: "Voiturette (Quadricycle à moteur carrossé) (anciennement \"voiturette ou tricycle à moteur\")",
    4: "Référence inSutilisée depuis 2006 (scooter immatriculé)",
    5: "Référence inutilisée depuis 2006 (motocyclette)",
    6: "Référence inutilisée depuis 2006 (side-car)",
    7: "VL seul",
    8: "Référence inutilisée depuis 2006 (VL + caravane)",
    9: "Référence inutilisée depuis 2006 (VL + remorque)",
    10: "VU seul 1,5T <= PTAC <= 3,5T avec ou sans remorque (anciennement VU seul 1,5T <= PTAC<= 3,5T)",
    11: "Référence inutilisée depuis 2006 (VU (10) + caravane)" ,
    12: "Référence inutilisée depuis 2006 (VU (10) + remorque)",
    13: "PL seul 3,5T <PTCA <= 7,5T" ,
    14: "PL seul > 7,5T" ,
    15: "PL > 3,5T + remorque" ,
    16: "Tracteur routier seul" ,
    17: "Tracteur routier + semi-remorque" ,
    18: "Référence inutilisée depuis 2006 (transport en commun)" ,
    19: "Référence inutilisée depuis 2006 (tramway)" ,
    20: "Engin spécial" ,
    21: "Tracteur agricole" ,
    30: "Scooter < 50 cm3" ,
    31: "Motocyclette > 50 cm3 et <= 125 cm3" ,
    32: "Scooter > 50 cm3 et <= 125 cm3" ,
    33: "Motocyclette > 125 cm3" ,
    34: "Scooter > 125 cm3 ",
    35: "Quad léger <= 50 cm3 (Quadricycle à moteur non carrossé)" ,
    36: "Quad lourd > 50 cm3 (Quadricycle à moteur non carrossé)" ,
    37: "Autobus" ,
    38: "Autocar",
    39: "Train",
    40: "Tramway" ,
    41: "3RM <= 50 cm3" ,
    42: "3RM > 50 cm3 <= 125 cm3" ,
    43: "3RM > 125 cm3" ,
    50: "EDP à moteur" ,
    60: "EDP sans moteur" ,
    80: "VAE" ,
    99: "Autre véhicule "
}
 
dico_type_trajet = {
    -1: "Non renseigné",
    0: "Non renseigné" ,
    1: "Domicile: travail",
    2: "Domicile: école",
    3: "Courses: achats",
    4: "Utilisation professionnelle",
    5: "Promenade: loisirs",
    9: "Autre"
}
 
dico_conditions_atmospherique = {
    -1: "Non renseigné",
    1: "Normale",
    2: "Pluie légère",
    3: "Pluie forte",
    4: "Neige - grêle",
    5: "Brouillard - fumée",
    6: "Vent fort - tempête",
    7: "Temps éblouissant",
    8: "Temps couvert",
    9: "Autre"
}
 
dico_obstacle = {
    -1: "Non renseigné",
    0: "Aucun",
    1: "Piéton",
    2: "Véhicule",
    4: "Véhicule sur rail",
    5: "Animal domestique",
    6: "Animal sauvage",
    9: "Autre",
}
 
dico_mois = {
    1: "Janvier",
    2: "Février",
    3: "Mars",
    4: 'Avril',
    5: "Mai",
    6: 'Juin',
    7: 'Juillet',
    8: 'Août',
    9: 'Septembre',
    10: 'Octobre',
    11: 'Novembre',
    12: 'Décembre'
}

dico_gravite = {
    1: "Indemne", 
    2: "Tué", 
    3: "Blessé hospitalisé", 
    4: "Blessé léger" 
}