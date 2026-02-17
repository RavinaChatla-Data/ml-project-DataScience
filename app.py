from src.MLProject.logger import logging
from src.MLProject.exception import CustomException
import sys
from src.MLProject.components.data_ingestion import DataIngestion
from src.MLProject.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    print("The execution has started")    ##logging.info

    try:
        ##DataIngestionConfig = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        print("Custom Exception")  ##logging.info
        raise CustomException(e,sys)
    

