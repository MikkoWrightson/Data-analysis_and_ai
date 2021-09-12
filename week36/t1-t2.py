import pandas as pd

df_emp = pd.read_csv('./employees.csv', header=0)
df_dep = pd.read_csv('./departments.csv', header=0)

df =pd.merge(df_emp, df_dep, how='left', on='dep')

df.drop('image', inplace=True, axis=1)

emp_count= df.shape[0]
rows, cols = df.shape