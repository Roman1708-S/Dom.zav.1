import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

print("Biblioteki zavantazheno!")

np.random.seed(42)
n = 200

data = {
    'typ': np.random.choice(['shafa', 'stil', 'lizhko', 'komod', 'tumba'], n),
    'material': np.random.choice(['DSP', 'MDF', 'masyv_duba', 'masyv_sosny'], n),
    'shyryna_sm': np.random.randint(40, 250, n),
    'vysota_sm': np.random.randint(40, 220, n),
    'glybyna_sm': np.random.randint(30, 80, n),
    'premium_furnitura': np.random.choice([0, 1], n),
    'chas_vyrobnytstva': np.random.randint(2, 40, n),
}

df = pd.DataFrame(data)

base_prices = {'shafa': 5000, 'stil': 3000, 'lizhko': 6000, 'komod': 4000, 'tumba': 2000}
material_mult = {'DSP': 1.0, 'MDF': 1.4, 'masyv_sosny': 1.8, 'masyv_duba': 2.5}

df['tsina'] = df.apply(lambda row: 
    base_prices[row['typ']] * material_mult[row['material']] 
    + row['shyryna_sm'] * 15 
    + row['vysota_sm'] * 10
    + row['premium_furnitura'] * 1500
    + row['chas_vyrobnytstva'] * 100
    + np.random.randint(-500, 500), axis=1)

print(f"Records: {len(df)}")
print(f"Prices: {df['tsina'].min():.0f} - {df['tsina'].max():.0f} UAH")
print(df.head(10))

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.boxplot(data=df, x='typ', y='tsina', palette='Set2', ax=axes[0])
axes[0].set_title('Price by type')
sns.barplot(data=df, x='material', y='tsina', palette='viridis', ax=axes[1])
axes[1].set_title('Price by material')
axes[1].tick_params(axis='x', rotation=45)
axes[2].scatter(df['shyryna_sm'], df['tsina'], alpha=0.5, c='orange', edgecolors='brown')
axes[2].set_title('Width vs Price')
plt.tight_layout()
plt.savefig('grafiky_mebli.png', dpi=150)
plt.show()

le_type = LabelEncoder()
le_material = LabelEncoder()
df['typ_code'] = le_type.fit_transform(df['typ'])
df['material_code'] = le_material.fit_transform(df['material'])

features = ['typ_code', 'material_code', 'shyryna_sm', 'vysota_sm',
            'glybyna_sm', 'premium_furnitura', 'chas_vyrobnytstva']
X = df[features]
y = df['tsina']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    'Linear Regression': LinearRegression(),
    'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
    'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42),
}

best_model = None
best_score = -1

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    r2 = r2_score(y_test, pred)
    print(f"\n{name}: MAE={mae:.0f} UAH, R2={r2*100:.1f}%")
    if r2 > best_score:
        best_score = r2
        best_model = (name, model)

print(f"\nBEST: {best_model[0]} - {best_score*100:.1f}%!")

new = pd.DataFrame({
    'typ_code': le_type.transform(['shafa', 'stil', 'lizhko']),
    'material_code': le_material.transform(['masyv_duba', 'MDF', 'DSP']),
    'shyryna_sm': [180, 120, 160],
    'vysota_sm': [200, 75, 45],
    'glybyna_sm': [60, 70, 200],
    'premium_furnitura': [1, 0, 1],
    'chas_vyrobnytstva': [20, 8, 15],
})

prices = best_model[1].predict(new)
items = ["Shafa|oak|premium", "Table|MDF|standard", "Bed|DSP|premium"]
for item, price in zip(items, prices):
    print(f"  {item}: {price:,.0f} UAH")

importance = pd.DataFrame({
    'Feature': features,
    'Importance': best_model[1].feature_importances_
}).sort_values('Importance', ascending=True)

plt.figure(figsize=(10, 6))
plt.barh(importance['Feature'], importance['Importance'], color='teal')
plt.title('Feature Importance')
plt.tight_layout()
plt.savefig('feature_importance.png', dpi=150)
plt.show()

print(f"\nTop factor: {importance.iloc[-1]['Feature']} ({importance.iloc[-1]['Importance']*100:.1f}%)")
print("\nPROJECT COMPLETE!")