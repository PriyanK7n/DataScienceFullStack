import os
from src.datascienceFullStackProject import logger
from src.datascienceFullStackProject.entity.config_entity import (DataValidationConfig)
from src.datascienceFullStackProject.config.configuration import (ConfigurationManager)
from src.datascienceFullStackProject.components.data_validation import (DataValidation) # DataValidation component

STAGE_NAME = "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    # Data validation Pipeline Run
    def initiate_data_validation_run(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} started<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation_run()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} finished<<<<<\n\nx======x")
    
    except Exception as e:
        logger.exception(e)
        raise e