#!/usr/bin/python3
from datetime import datetime, timedelta
from numpy import NaN
import pandas as pd

df_emp = pd.read_csv('./employees.csv', header=0)
df_dep = pd.read_csv('./departments.csv', header=0)


#    Yhdistä kaksi dataframea yhdeksi käyttäen pandas merge ominaisuutta. Käytä inner-liitosta (how='inner'), ja tee liitos dep:n perusteella (on='dep'). Tämä on dataframe, jota jatkossa käytetään.
df =pd.merge(df_emp, df_dep, how='left', on='dep')
#    Poista image sarake dataframesta
df.drop('image', inplace=True, axis=1)


#laske montako työntekijää on dataframessa
emp_count= df.shape[0]
rows, cols = df.shape

#laske montako miestä (gender=0) ja naista (gender=1) on työtekijöissä
m_count = sum(df['gender'] == 0)
f_count = sum(df.gender==1)

#laske myös em. prosenttiosuudet yhdellä desimaalilla
m_percentage = round(m_count / emp_count * 100,1)
f_percentage = round(f_count / emp_count * 100,1)

#laske työtekijöiden minimi, maksimi ja keskipalkka
min_salary = min(df.salary)
max_salary = max(df.salary)
avg_salary = df.salary.mean()

#laske 'Tuotekehitys' osaston keskipalkka
rd_avg_salary = df[df.dname == 'Tuotekehitys'.salary].mean()


#laske monellako työntekijällä ei ole kakkospuhelinta (phone2)
no_phone2 = sum(df.phone2.isna())

#lisää dataframeen uusi sarake: 'age', ja laske siihen jokaisen työntekijän ikä vuosina
df['age'] = pd.to_datetime(df.bdate).map(lambda x: (datetime.now() - x) // timedelta(days=365.2425))

