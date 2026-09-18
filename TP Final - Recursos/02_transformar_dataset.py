import pandas as pd

# 1. Importar el dataset original
df = pd.read_csv('Bank_Churn_Original.csv')

# 2. Transformación 1: Eliminar variables no predictivas
df_clean = df.drop(columns=['CustomerId', 'Surname'])

# 3. Transformación 2: Etiquetado semántico de variables categóricas
df_clean['Exited_Str'] = df_clean['Exited'].map({0: 'No Abandono', 1: 'Abandono'})
df_clean['IsActive_Str'] = df_clean['IsActiveMember'].map({0: 'Inactivo', 1: 'Activo'})

# 4. Exportar el dataset limpio a un nuevo archivo CSV
df_clean.to_csv('Bank_Churn_Limpio.csv', index=False, encoding='utf-8')

print("El dataset limpio ha sido exportado exitosamente como 'Bank_Churn_Limpio.csv'")