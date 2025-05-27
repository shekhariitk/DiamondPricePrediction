import os
import sys
import joblib
from sklearn.metrics import r2_score
from src.exception import CustomException
from src.logger import logging

def save_obj(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            joblib.dump(obj, file_obj, compress=3)  # Compress the file

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            score = r2_score(y_test, y_pred)
            report[name] = score
        return report

    except Exception as e:
        logging.error("Error occurred during model evaluation.")
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return joblib.load(file_obj)

    except Exception as e:
        logging.error("Error occurred during model loading.")
        raise CustomException(e, sys)
