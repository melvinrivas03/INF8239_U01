from pathlib import Path

import pytest

from inf8239_u01.data import DEFAULT_PATH, TARGET, load_data

pytestmark = pytest.mark.skipif(not Path(DEFAULT_PATH).exists(),
                                reason="Ejecutar primero la descarga del dataset")
REQUIRED = {TARGET, "Curricular units 1st sem (approved)", "Age at enrollment"}


def test_dataset_is_not_empty():
    assert not load_data().empty


def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns)


def test_target_has_no_missing_and_three_classes():
    y = load_data()[TARGET]
    assert y.notna().all()
    assert set(y.unique()) == {"Dropout", "Enrolled", "Graduate"}
