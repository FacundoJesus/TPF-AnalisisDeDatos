import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the file
df = pd.read_csv('Bank_Churn.csv')

print("--- INFORMACIÓN BÁSICA ---")
print(df.info())
print("\n--- NULOS Y DUPLICADOS ---")
print("Nulos:\n", df.isnull().sum())
print("Duplicados:", df.duplicated().sum())
print("\n--- PRIMERAS FILAS ---")
print(df.head())

# Calcular métricas clave para las preguntas
churn_rate_by_geo = df.groupby('Geography')['Exited'].mean()
print("\n--- CHURN POR PAÍS ---")
print(churn_rate_by_geo)

avg_balance_by_geo = df.groupby('Geography')['Balance'].mean()
print("\n--- SALDO PROMEDIO POR PAÍS ---")
print(avg_balance_by_geo)