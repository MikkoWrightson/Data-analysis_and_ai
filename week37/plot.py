#!/usr/bin/python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

age_groups = np.arange(5, 76, 5)
df['age_group'] = df.apply(lambda row: age_groups[np.where(age_groups > row.Age)[0][0]], axis=1)

counts = df.age_group.value_counts().sort_index()
counts.plot(kind='bar')
plt.show()

total = len(df)
survived = df.query("Survived == 1")
plot_data = survived.GenderCode.value_counts()
plot_data.plot(kind='pie', ylabel='', labels=['miehet', 'naiset'], autopct='%1.1f%%', startangle=270, title=f"""
   matkustajia: {total}
   selviytyneet miehet: {plot_data[0]}
   selviytyneet naiset: {plot_data[1]}
""")
plt.show()