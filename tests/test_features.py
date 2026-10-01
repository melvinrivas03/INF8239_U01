import pandas as pd

from inf8239_u01.features import build_preprocess, split_xy


def _toy():
    return pd.DataFrame({
        "Course": [1, 2, 1, 2],
        "Age at enrollment": [18, 20, 19, 25],
        "Curricular units 1st sem (approved)": [5, 6, 0, 4],
        "Curricular units 2nd sem (approved)": [5, 6, 0, 4],
        "Target": ["Graduate", "Dropout", "Dropout", "Enrolled"],
    })


def test_second_semester_columns_are_excluded():
    X, y = split_xy(_toy())
    assert not any(c.startswith("Curricular units 2nd sem") for c in X.columns)
    assert "Target" not in X.columns
    assert len(y) == 4


def test_preprocess_outputs_one_row_per_input():
    X, _ = split_xy(_toy())
    out = build_preprocess(X).fit_transform(X)
    assert out.shape[0] == len(X)
