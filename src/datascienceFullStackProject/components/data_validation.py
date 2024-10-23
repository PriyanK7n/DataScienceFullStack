import os
import pandas as pd
from src.datascienceFullStackProject import logger
from src.datascienceFullStackProject.entity.config_entity import (DataValidationConfig)
from src.datascienceFullStackProject.config.configuration import (ConfigurationManager)

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:      
        try:         
            validation_status = None # default
            data = pd.read_csv(self.config.unzip_data_dir)
            # List of Columns of new data received that need to be validated 
            all_cols = list(data.columns)
            # Orignal Data columns view (behaves like a set and can be iterated over, check for membership, and more memory efficient than list) which we compare the new data with
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema: # check for membership
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
        
        except Exception as e:
            raise e
    


