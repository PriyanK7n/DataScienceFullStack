from src.datascienceFullStackProject.entity.config_entity import (DataIngestionConfig) # input param constraints
from src.datascienceFullStackProject.components.data_ingestion import (DataIngestion) # component
from src.datascienceFullStackProject.config.configuration import (ConfigurationManager)

STAGE_NAME = "Data Ingestion STAGE"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    # Data Ingestion Pipeline Run
    def initiate_data_ingestion_run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} started<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion_run()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} finished<<<<<\n\nx======x")
    
    except Exception as e:
        logger.exception(e)
        raise e





