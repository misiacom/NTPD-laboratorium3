import numpy as np
from model import train_and_predict, get_accuracy


def test_predictions_not_none():
    """
    Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję.
    """
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."


def test_predictions_length():
    """
    Test 2: Sprawdza, czy długość predykcji jest większa od 0.
    """
    preds, y_test = train_and_predict()
    assert len(preds) > 0, "Predictions should not be empty."
    assert len(preds) == len(y_test), "Predictions length should match test data."


def test_predictions_value_range():
    """
    Test 3: Sprawdza czy wartości są w zakresie 0–2 (Iris dataset).
    """
    preds, _ = train_and_predict()
    assert np.all((preds >= 0) & (preds <= 2)), "Predictions out of range."


def test_model_accuracy():
    """
    Test 4: Sprawdza czy accuracy >= 70%.
    """
    accuracy = get_accuracy()
    assert accuracy >= 0.7, f"Accuracy too low: {accuracy}"