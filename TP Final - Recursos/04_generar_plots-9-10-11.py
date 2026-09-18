import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Bank_Churn.csv')

# Configuración visual
sns.set_theme(style="whitegrid", palette="muted")

# 9. Gráfico de Torta: Proporción Global de Deserción
plt.figure(figsize=(8, 6))
churn_counts = df['Exited'].value_counts()
plt.pie(churn_counts, labels=['No Abandonó (0)', 'Abandonó (1)'], autopct='%1.1f%%', startangle=90, colors=['#4C72B0', '#DD8452'], explode=(0, 0.1), shadow=True)
plt.title("9. Proporción Global de Deserción (Churn Rate Base)", fontsize=14)
plt.savefig("plot9_pie_churn.png", bbox_inches='tight')
plt.show()

# 10. Gráfico de Torta: Distribución por País
plt.figure(figsize=(8, 6))
geo_counts = df['Geography'].value_counts()
plt.pie(geo_counts, labels=geo_counts.index, autopct='%1.1f%%', startangle=140, colors=['#4C72B0', '#55A868', '#C44E52'])
plt.title("10. Distribución de la Clientela por País", fontsize=14)
plt.savefig("plot10_pie_geo.png", bbox_inches='tight')
plt.show()

# 11. Gráfico de Barras: Tasa de Abandono por Antigüedad (Tenure)
plt.figure(figsize=(10, 6))
churn_tenure = df.groupby('Tenure')['Exited'].mean().reset_index()
sns.barplot(data=churn_tenure, x='Tenure', y='Exited', palette="coolwarm")
plt.title("11. Tasa de Abandono según Años de Antigüedad (Tenure)", fontsize=14)
plt.ylabel("Tasa de Abandono")
plt.xlabel("Años de Antigüedad")
for i, v in enumerate(churn_tenure['Exited']):
    plt.text(i, v + 0.005, f"{v*100:.1f}%", ha='center', fontsize=9)
plt.savefig("plot11_tenure_churn.png", bbox_inches='tight')
plt.show()