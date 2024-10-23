import os
import pandas as pd
from src.datascienceFullStackProject import logger
from src.datascienceFullStackProject.entity.config_entity import (DataTransformationConfig) 
from src.datascienceFullStackProject.config.configuration import (ConfigurationManager)
from sklearn.model_selection import train_test_split

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: We can add different data transformation techniques such as Scaler, PCA and all
    # If needed we can perform all kinds of EDA in ML cycle here before passing this data to the model
    # In this File I have not added transformations and performing only train_test_spliting due to data being already cleaned

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        


