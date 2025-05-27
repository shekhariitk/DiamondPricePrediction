import os
import sys
from dataclasses import dataclass
import numpy as np
from sklearn.linear_model import Ridge, LinearRegression, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_obj, evaluate_model

@dataclass
class ModelTrainerconfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.joblib")

class ModelTrainerClass:
    def __init__(self):
        self.model_trainer_config = ModelTrainerconfig()

    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("Splitting independent and dependent variables")
            X_train, y_train = train_arr[:, :-1], train_arr[:, -1]
            X_test, y_test = test_arr[:, :-1], test_arr[:, -1]

            models = {
                "LinearRegression": LinearRegression(),
                "Lasso": Lasso(alpha=0.01),
                "Ridge": Ridge(alpha=1.0),
                "ElasticNet": ElasticNet(alpha=0.01, l1_ratio=0.5),
                "DecisionTreeRegressor": DecisionTreeRegressor(max_depth=10),
                "RandomForestRegressor": RandomForestRegressor(n_estimators=50, max_depth=10, n_jobs=-1)
            }

            model_report = evaluate_model(X_train, y_train, X_test, y_test, models)
            logging.info(f"Model report: {model_report}")

            best_model_score = max(model_report.values())
            best_model_name = max(model_report, key=model_report.get)
            best_model = models[best_model_name]

            logging.info(f"Best Model: {best_model_name}, R2 Score: {best_model_score:.4f}")
            print(f"✅ Best Model: {best_model_name}, R2 Score: {best_model_score:.4f}")

            save_obj(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)

            # Optional: Check file size
            file_size = os.path.getsize(self.model_trainer_config.trained_model_file_path) / (1024 * 1024)
            print(f"💾 Model file size: {file_size:.2f} MB")

        except Exception as e:
            logging.error("Error occurred during model training.")
            raise CustomException(e, sys)
