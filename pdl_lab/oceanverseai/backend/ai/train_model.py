import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


# =====================================================
# LOAD DATASET
# =====================================================

data = pd.read_csv("ocean_data.csv")


# =====================================================
# INPUT FEATURES
# =====================================================

features = [
    "temperature",
    "salinity",
    "turbidity",
    "chlorophyll",
    "ph"
]

X = data[features]

y = data["algal_bloom"]


# =====================================================
# SPLIT DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# =====================================================
# CREATE MODEL
# =====================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# =====================================================
# TRAIN MODEL
# =====================================================

model.fit(
    X_train,
    y_train
)


# =====================================================
# TEST MODEL
# =====================================================

predictions = model.predict(X_test)


# =====================================================
# EVALUATION
# =====================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    zero_division=0
)


print("\n===================================")
print("🌊 ALGAL BLOOM AI MODEL")
print("===================================")

print(f"Accuracy  : {accuracy:.2%}")
print(f"Precision : {precision:.2%}")
print(f"Recall    : {recall:.2%}")
print(f"F1 Score  : {f1:.2%}")


# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(
    model,
    "algal_bloom_model.pkl"
)


print("\n✅ Model saved as:")
print("algal_bloom_model.pkl")