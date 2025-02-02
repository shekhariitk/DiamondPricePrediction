import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging

# Model Training
from sklearn.linear_model import Ridge,LinearRegression,Lasso,ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


from src.utils import save_obj
from src.utils import evaluate_model

import os, sys
from dataclasses import dataclass

## Model Trainning Configuration

@dataclass
class ModelTrainerconfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")




## Model Training Class
class ModelTrainerClass:
    def __init__(self):
        self.model_trainer_config  = ModelTrainerconfig()

    def  initiate_model_training(self,train_arr, test_arr):
        try:
            logging.info("Splitting independent and Dependent Variable")
            X_train,y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]

            )

            models  = {

                "LinearRegression":LinearRegression(),
                "Lasso":Lasso(),
                "Ridge": Ridge(),
                "DecisionTreeRegressor":DecisionTreeRegressor(),
                "ElasticNet": ElasticNet(),
                "RandomForestRegressor":RandomForestRegressor()
            }

            model_report : dict = evaluate_model(X_train,y_train, X_test, y_test, models)
            print(model_report)
            print("\n ==================================================================================")
            logging.info(f"Model report info : {model_report}")

            ## To get best model from model dictionary
            best_model_score = max(sorted(model_report.values()))

            best_model_name  = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model = models[best_model_name]

            print(f"Best model found , Best model name is {best_model_name} and that R2 Score: {best_model_score}")
            print("\n=================================================================")
            logging.info(f"Best model found , Best model name is {best_model_name} and that R2 Score: {best_model_score}")


            save_obj(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

        except   Exception as e:
            logging.info("Error occured in model trainer path") 
            raise CustomException(e, sys)
        
        







