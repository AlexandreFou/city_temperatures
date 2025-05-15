import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#style sns
sns.set_theme()
sns.set_palette('viridis')

#transfert des données
file_path = "GlobalLandTemperaturesByMajorCity.csv"
city_df = pd.read_csv(file_path)

#Aperçu des données
print(city_df.head())

#dimension dataset
print("\n Dimensions du dataset :", city_df.shape)

#type de données
print("\n type de données du dataset :", city_df.dtypes)

#Statistiques descriptives
print("\n statistiques descriptives du dataset :", city_df.describe())

#valeurs manquantes
print("\n nombre de valeurs manquantes :") 
print(city_df.isnull().sum())

#doublons
print("\n valeurs en double :")
print(city_df.duplicated().sum())

#distribution des temperatures moyennes
plt.figure(figsize=(10,6))
sns.histplot(city_df['AverageTemperature'], kde=True, bins=30)
plt.title("Frequence des temperatures moyennes")
plt.xlabel("températures moyennes")
plt.ylabel("fréquence")
plt.show()

#distribution des marges d'erreur de temperatures
plt.figure(figsize=(10,6))
sns.histplot(city_df["AverageTemperatureUncertainty"], kde=True, bins=30)
plt.title("Fréquence des marges d'erreur")
plt.xlabel("marges d'erreur")
plt.ylabel("fréquence")
plt.show()

# === Identification des anomalies ===
print("\n Indentification des anomalies")

#valeurs extrêmes pour la temperature
plt.figure(figsize=(10,6))
sns.boxplot(data=city_df, x="AverageTemperature" )
plt.title("Boxplot des températures moyennes")
plt.show()

#valeurs extrêmes pour l'incertitude 
plt.figure(figsize=(10,6))
sns.boxplot(data=city_df, x="AverageTemperatureUncertainty")
plt.title("Boxplot des moyennes de marges d'erreur")
plt.show()

#vérification des données géographiques
print("\nvérification des données géographiques :")
print("Latitude :", city_df['Latitude'].unique())
print("Longitue :", city_df['Longitude'].unique())

#vérification des dates
print("\nvérification des dates :")
city_df['dt'] = pd.to_datetime(city_df['dt'])
print("date mim :", city_df['dt'].min())
print("date max :", city_df['dt'].max())

# === Nettoyage des données ===
print("\nNettoyage des données :")

#Valeurs manquantes avant traitement
print("\nValeurs manquantes avant traitement")
print(city_df.isnull().sum())

#Suppression des valeurs AverageTemperature manquantes
print("\nSuppression des valeurs AverageTemperature manquantes :")
first_len = len(city_df)
city_df = city_df.dropna(subset=['AverageTemperature'])
print("Nombre de valeurs supprimées :", (first_len - len(city_df)))

#Suppression des doublons
print("\nSuppression des doublons :")
second_len = len(city_df)
city_df = city_df.drop_duplicates()
print("Nombre de valeurs supprimées :", (second_len - len(city_df)))

#Valeurs manquantes après traitement
print("\nValeurs manquantes après traitement :")
print(city_df.isnull().sum())
print("dimension du dataset :", city_df.shape)


