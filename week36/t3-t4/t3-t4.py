#!/usr/bin/python3
import pandas as pd

#Lataa Titanic csv tiedostot pythoniin pandas dataframeen (Titanic_data.csv, Titanic_names.csv)
df_data = pd.read_csv('./Titanic_data.csv', header=0)
df_names = pd.read_csv('./Titanic_names.csv', header=0)


#Tulosta ipyhon consoliin dataframien info ja describe. Tee histogrammi  df_titanic_data ( bins=4) dataframesta. 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html?highlight=info#pandas.DataFrame.info
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html?highlight=describe#pandas.DataFrame.describe
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html?highlight=hist#pandas.DataFrame.hist

#Yhdistä dataframet (df_titanic_data, df_titanic_names) uudeksi dataframeksi df. Käytä how='inner' on='id'.
df = pd.merge(df_data, df_names, how='inner', on='id')

#montako henkilö on aineistossa?
persons_count = df.shape[0]

#montako miestä ja naista on aineistossa?
m_count = sum(df.GenderCode == 0)
f_count = sum(df.GenderCode==1)

#matkustajien keski-ikä?
avg_age = df.Age.mean()

#kuinka monta nollan ikäistä matkustajaa?
zero_age_amount = sum(df.Age == 0)

#Huomataan, että on paljon nollan ikäisiä matkustajia. Lasketaan ei-nollan ikäisten matkustajien keski-ikä, ja päivitetään nollan ikäisten matkustajien iäksi tämä laskettu keskiarvo


#Tulosta yksikäsitteiset PClasses arvot. Output: ['1st' '2nd' '*' '3rd']


#Etsi, kenen PClass on: *


#Laske selviytyneiden ja ei-selviytyneiden lukumäärä. Tulosta arvot myös prosentteina


#Laske selviytyminen ja ei-selviytyminen miesten ja naisten kohdalla 

