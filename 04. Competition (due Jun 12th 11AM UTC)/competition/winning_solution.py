import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

train = pd.read_csv('input/train.csv')
test = pd.read_csv('input/test.csv')
full = pd.concat([train, test], sort=False).reset_index(drop=True)

gm = train['Drafted'].mean()

# Feature Engineering
full['BMI'] = full['Weight'] / (full['Height'] ** 2)

for grp in ['Position', 'Player_Type']:
    agg = train.groupby(grp)['Drafted'].mean()
    full[f'{grp}_rate'] = full[grp].map(agg).fillna(gm)

full['School_rate'] = full['School'].map(train.groupby('School')['Drafted'].mean()).fillna(gm)

for col in ['Sprint_40yd', 'Vertical_Jump', 'Bench_Press_Reps', 'Broad_Jump', 'Agility_3cone', 'Shuttle']:
    full[col] = full[col].fillna(full[col].median())

full['Athleticism'] = (
    -full['Sprint_40yd'] + full['Vertical_Jump'] * 0.5 + full['Bench_Press_Reps'] * 0.3
    - full['Broad_Jump'] - full['Agility_3cone'] - full['Shuttle']
)

for col in ['Sprint_40yd', 'Vertical_Jump']:
    full[f'{col}_pct'] = full.groupby('Position')[col].transform(lambda x: x.rank(pct=True))

for col in ['Age', 'Sprint_40yd', 'Vertical_Jump', 'Bench_Press_Reps', 'Broad_Jump', 'Agility_3cone', 'Shuttle']:
    full[f'{col}_na'] = full[col].isnull().astype(int)

for col in ['School', 'Player_Type', 'Position_Type', 'Position']:
    full[col] = LabelEncoder().fit_transform(full[col].astype(str))

full['HW_ratio'] = full['Height'] / full['Weight']

features = [c for c in full.columns if c not in ['Id', 'Drafted']]
X = full.iloc[:len(train)][features]
y = full.iloc[:len(train)]['Drafted']
X_test = full.iloc[len(train):][features]

print(f"Features: {len(features)}, Train: {X.shape}")

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

def train_oof(model, X, y):
    oof = np.zeros(len(X))
    for tr, vl in skf.split(X, y):
        model.fit(X.iloc[tr], y.iloc[tr])
        oof[vl] = model.predict_proba(X.iloc[vl])[:, 1]
    return roc_auc_score(y, oof), oof

print("Training RandomForestClassifier...")
rf = RandomForestClassifier(n_estimators=200, max_depth=6, min_samples_leaf=20, random_state=42, n_jobs=-1)
s_rf, oof_rf = train_oof(rf, X, y)
print(f"RF CV: {s_rf:.5f}")

print("Training ExtraTrees...")
et = ExtraTreesClassifier(n_estimators=200, max_depth=6, min_samples_leaf=20, random_state=42, n_jobs=-1)
s_et, oof_et = train_oof(et, X, y)
print(f"ET CV: {s_et:.5f}")

# Simple Ensemble
final_oof = (oof_rf + oof_et) / 2
print(f"\nEnsemble CV ROC-AUC: {roc_auc_score(y, final_oof):.5f}")

rf.fit(X, y)
et.fit(X, y)
pred = (rf.predict_proba(X_test)[:, 1] + et.predict_proba(X_test)[:, 1]) / 2

pd.DataFrame({'Id': test['Id'], 'Drafted': pred}).to_csv('submission.csv', index=False)
print(f"Saved submission.csv: {len(test)} predictions")