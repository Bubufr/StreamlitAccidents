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


dicoDep = {'01' : '01 - Ain'}
dicoDep['02'] = "02 - Aisne"
dicoDep['03'] = "03 - Allier"
dicoDep['04'] = "04 - Alpes-de-Haute-Provence"
dicoDep['05'] = "05 - Hautes-Alpes"
dicoDep['06'] = "06 - Alpes-Maritimes"
dicoDep['07'] = "07 - Ardèche"
dicoDep['08'] = "08 - Ardennes"
dicoDep['09'] = "09 - Ariège"
dicoDep['10'] = "10 - Aube"
dicoDep['11'] = "11 - Aude"
dicoDep['12'] = "12 - Aveyron"
dicoDep['13'] = "13 - Bouches-du-Rhône"
dicoDep['14'] = "14 - Calvados"
dicoDep['15'] = "15 - Cantal"
dicoDep['16'] = "16 - Charente"
dicoDep['17'] = "17 - Charente-Maritime"
dicoDep['18'] = "18 - Cher"
dicoDep['19'] = "19 - Corrèze"
dicoDep['2A'] = "2A - Corse-du-Sud"
dicoDep['2B'] = "2B - Haute-Corse"
dicoDep['21'] = "21 - Côte-d'Or"
dicoDep['22'] = "22 - Côtes-d'Armor"
dicoDep['23'] = "23 - Creuse"
dicoDep['24'] = "24 - Dordogne"
dicoDep['25'] = "25 - Doubs"
dicoDep['26'] = "26 - Drôme"
dicoDep['27'] = "27 - Eure"
dicoDep['28'] = "28 - Eure-et-Loir"
dicoDep['29'] = "29 - Finistère"
dicoDep['30'] = "30 - Gard"
dicoDep['31'] = "31 - Haute-Garonne"
dicoDep['32'] = "32 - Gers"
dicoDep['33'] = "33 - Gironde"
dicoDep['34'] = "34 - Hérault"
dicoDep['35'] = "35 - Ille-et-Vilaine"
dicoDep['36'] = "36 - Indre"
dicoDep['37'] = "37 - Indre-et-Loire"
dicoDep['38'] = "38 - Isère"
dicoDep['39'] = "39 - Jura"
dicoDep['40'] = "40 - Landes"
dicoDep['41'] = "41 - Loir-et-Cher"
dicoDep['42'] = "42 - Loire"
dicoDep['43'] = "43 - Haute-Loire"
dicoDep['44'] = "44 - Loire-Atlantique"
dicoDep['45'] = "45 - Loiret"
dicoDep['46'] = "46 - Lot"
dicoDep['47'] = "47 - Lot-et-Garonne"
dicoDep['48'] = "48 - Lozère"
dicoDep['49'] = "49 - Maine-et-Loire"
dicoDep['50'] = "50 - Manche"
dicoDep['51'] = "51 - Marne"
dicoDep['52'] = "52 - Haute-Marne"
dicoDep['53'] = "53 - Mayenne"
dicoDep['54'] = "54 - Meurthe-et-Moselle"
dicoDep['55'] = "55 - Meuse"
dicoDep['56'] = "56 - Morbihan"
dicoDep['57'] = "57 - Moselle"
dicoDep['58'] = "58 - Nièvre"
dicoDep['59'] = "59 - Nord"
dicoDep['60'] = "60 - Oise"
dicoDep['61'] = "61 - Orne"
dicoDep['62'] = "62 - Pas-de-Calais"
dicoDep['63'] = "63 - Puy-de-Dôme"
dicoDep['64'] = "64 - Pyrénées-Atlantiques"
dicoDep['65'] = "65 - Hautes-Pyrénées"
dicoDep['66'] = "66 - Pyrénées-Orientales"
dicoDep['67'] = "67 - Bas-Rhin"
dicoDep['68'] = "68 - Haut-Rhin"
dicoDep['69'] = "69 - Rhône"
dicoDep['70'] = "70 - Haute-Saône"
dicoDep['71'] = "71 - Saône-et-Loire"
dicoDep['72'] = "72 - Sarthe"
dicoDep['73'] = "73 - Savoie"
dicoDep['74'] = "74 - Haute-Savoie"
dicoDep['75'] = "75 - Paris"
dicoDep['76'] = "76 - Seine-Maritime"
dicoDep['77'] = "77 - Seine-et-Marne"
dicoDep['78'] = "78 - Yvelines"
dicoDep['79'] = "79 - Deux-Sèvres"
dicoDep['80'] = "80 - Somme"
dicoDep['81'] = "81 - Tarn"
dicoDep['82'] = "82 - Tarn-et-Garonne"
dicoDep['83'] = "83 - Var"
dicoDep['84'] = "84 - Vaucluse"
dicoDep['85'] = "85 - Vendée"
dicoDep['86'] = "86 - Vienne"
dicoDep['87'] = "87 - Haute-Vienne"
dicoDep['88'] = "88 - Vosges"
dicoDep['89'] = "89 - Yonne"
dicoDep['90'] = "90 - Territoire de Belfort"
dicoDep['91'] = "91 - Essonne"
dicoDep['92'] = "92 - Hauts-de-Seine"
dicoDep['93'] = "93 - Seine-Saint-Denis"
dicoDep['94'] = "94 - Val-de-Marne"
dicoDep['95'] = "95 - Val-d'Oise"
dicoDep['971'] = "971 - Guadeloupe"
dicoDep['972'] = "972 - Martinique"
dicoDep['973'] = "973 - Guyane"
dicoDep['974'] = "974 - La Réunion"
dicoDep['975'] = "975 - Saint-Pierre-et-Miquelon"
dicoDep['976'] = "976 - Mayotte"
dicoDep['977'] = "977 - Saint-Barthélemy"
dicoDep['978'] = "978 - Saint-Martin"
dicoDep['986'] = "986 - Wallis-et-Futuna"
dicoDep['987'] = "987 - Polynésie française"
dicoDep['988'] = "988 - Nouvelle-Calédonie"