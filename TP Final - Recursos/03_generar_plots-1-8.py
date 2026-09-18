import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Bank_Churn.csv')

# Drop irrelevant columns for analysis
df_clean = df.drop(columns=['CustomerId', 'Surname'])

# Configuración visual
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams['figure.figsize'] = (10, 6)

# 1. Boxplot de Edad según Deserción (Churn)
plt.figure()
sns.boxplot(data=df_clean, x='Exited', y='Age')
plt.title("1. Distribución de Edad según Estado de Deserción (Exited)", fontsize=14)
plt.xticks([0, 1], ['No Abandonó (0)', 'Abandonó (1)'])
plt.savefig("plot1_age_exited.png", bbox_inches='tight')
plt.show()

# 2. Matriz de Correlación
plt.figure(figsize=(10, 8))
corr = df_clean.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title("2. Matriz de Correlación de Variables Numéricas", fontsize=14)
plt.savefig("plot2_correlation.png", bbox_inches='tight')
plt.show()

# 3. Distribución Demográfica: Edad y Género
plt.figure()
sns.histplot(data=df_clean, x='Age', hue='Gender', multiple="stack", bins=30, kde=True)
plt.title("3. Perfil Demográfico: Distribución de Edad por Género", fontsize=14)
plt.savefig("plot3_demographics.png", bbox_inches='tight')
plt.show()

# 4. Saldo Bancario (Balance) por País (Geography)
plt.figure()
sns.boxplot(data=df_clean, x='Geography', y='Balance')
plt.title("4. Comportamiento de Cuentas: Saldo Bancario por País", fontsize=14)
plt.savefig("plot4_balance_geo.png", bbox_inches='tight')
plt.show()

# 5. Cantidad de Productos por País
plt.figure()
sns.countplot(data=df_clean, x='Geography', hue='NumOfProducts')
plt.title("5. Comportamiento de Cuentas: Cantidad de Productos por País", fontsize=14)
plt.legend(title='N° Productos', loc='upper right')
plt.savefig("plot5_products_geo.png", bbox_inches='tight')
plt.show()

# 6. Tasa de Deserción por País
plt.figure()
churn_geo = df_clean.groupby('Geography')['Exited'].mean().reset_index()
sns.barplot(data=churn_geo, x='Geography', y='Exited', palette="viridis")
plt.title("6. Tasa de Abandono (Churn Rate) por País", fontsize=14)
plt.ylabel("Tasa de Abandono")
for i, v in enumerate(churn_geo['Exited']):
    plt.text(i, v + 0.01, f"{v*100:.1f}%", ha='center', fontweight='bold')
plt.savefig("plot6_churn_geo.png", bbox_inches='tight')
plt.show()

# 7. Segmentos: Nivel de Actividad y Saldo
plt.figure()
sns.violinplot(data=df_clean, x='IsActiveMember', y='Balance', hue='Exited', split=True)
plt.title("7. Segmentación: Saldo vs Miembro Activo (por Deserción)", fontsize=14)
plt.xticks([0, 1], ['Inactivo', 'Activo'])
plt.savefig("plot7_segments.png", bbox_inches='tight')
plt.show()

# 8. Densidad de Saldo (Balance) según Deserción
plt.figure()
sns.kdeplot(data=df_clean, x='Balance', hue='Exited', fill=True, common_norm=False, alpha=0.5)
plt.title("8. Distribución de Saldo Bancario según Deserción", fontsize=14)
plt.legend(title='Exited', labels=['Abandonó (1)', 'No Abandonó (0)'])
plt.savefig("plot8_balance_exited.png", bbox_inches='tight')
plt.show()

print("Plots generados con éxito.")