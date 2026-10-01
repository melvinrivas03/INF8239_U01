"""Definición de predictores, exclusiones por fuga y preprocesamiento."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from inf8239_u01.data import TARGET

# Momento de predicción: fin del 1.er semestre.
# Todo lo medido en el 2.º semestre aún no existe en ese momento -> fuga.
LEAKAGE_PREFIX = "Curricular units 2nd sem"

# Variables codificadas con enteros pero de naturaleza nominal.
NOMINAL_COLS = [
    "Marital status", "Application mode", "Course", "Previous qualification",
    "Nacionality", "Mother's qualification", "Father's qualification",
    "Mother's occupation", "Father's occupation",
]

RANDOM_STATE = 42
TEST_SIZE = 0.20


def leakage_columns(frame: pd.DataFrame) -> list[str]:
    return [c for c in frame.columns if c.startswith(LEAKAGE_PREFIX)]


def split_xy(frame: pd.DataFrame, extra_drop: list[str] | None = None):
    drop = [TARGET] + leakage_columns(frame) + list(extra_drop or [])
    return frame.drop(columns=drop), frame[TARGET]


def split_train_test(X, y):
    """Partición única usada en los Ejercicios 01 y 02."""
    return train_test_split(X, y, test_size=TEST_SIZE,
                            random_state=RANDOM_STATE, stratify=y)


def column_groups(X: pd.DataFrame):
    cat_cols = [c for c in NOMINAL_COLS if c in X.columns]
    num_cols = [c for c in X.columns if c not in cat_cols]
    return num_cols, cat_cols


def build_preprocess(X: pd.DataFrame) -> ColumnTransformer:
    num_cols, cat_cols = column_groups(X)
    num_pipe = Pipeline([("imputer", SimpleImputer(strategy="median")),
                         ("scale", StandardScaler())])
    cat_pipe = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                         ("onehot", OneHotEncoder(handle_unknown="infrequent_if_exist",
                                                  min_frequency=10,
                                                  sparse_output=False))])
    return ColumnTransformer([("num", num_pipe, num_cols),
                              ("cat", cat_pipe, cat_cols)])
