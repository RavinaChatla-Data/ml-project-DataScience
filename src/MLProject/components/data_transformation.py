import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.MLProject.exception import CustomException
from src.MLProject.logger import logging
import os
from src.MLProject.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transform_object():
        '''
        This function is responsible for data transformation 
        '''
        try:
            numerical_columns = ["writing_score","reading_score"]
            categoral_columns = ["gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course"]

            num_pipeline = Pipeline(steps=[
                ("imputer", SimpleImputer(strategy='median')),
                ('scalar', StandardScalar())
            ])
            cat_pipeline = Pipeline([
                ('imputer', SimpleImputer(strategy="most frequent")),
                ('one_hot_encode', OneHotEncoder()),
                ('scalar', StandardScaler(with_mean=False))
            ])

            logging.info(f"Categoral Columns: {categoral_columns}")
            logging.info(f"Numerical Columns: {numerical_columns}")

            preprocessor = ColumnTransformer([
                ("num_pipline", num_pipeline, numerical_columns),
                ("cat_pipline", cat_pipeline, categoral_columns)
            ])

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
        
    def initate_data_transformation(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test file")

            preprocessing_obj = self.data_get_transformer-object()

            target_column_name = "math_score"
            numerical_columns = ["writing_score","reading_score"]

            #Diving train dataset into independent and dependent feature

            input_features_train_df = train_df.drop(columns = [target_column_name],axis = 1)
            target_feature_train_df = train_df[target_column_name]

        #Diving test dataset into independent and dependent feature

            input_features_test_df = test_df.drop(columns = [target_column_name],axis = 1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying Preprocessing on train and test data")

            input_feature_train_arr = preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[
            input_feature_train_arr,np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
            input_feature_test_arr, np.c_(target_feature_test_df)
            ]

            logging.info("Saved Preprocesing Object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)

