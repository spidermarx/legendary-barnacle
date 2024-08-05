import pytest
from src.model_training import train_model, save_model

def test_save_model(tmpdir):
    model = "dummy_model"
    model_path = tmpdir.join("model.pkl")
    save_model(model, model_path)
    assert model_path.exists()