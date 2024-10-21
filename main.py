from src.datascienceFullStackProject import logger
from src.datascienceFullStackProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Pipeline"

try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion_run()
    logger.info(f">>>>>>>> stage {STAGE_NAME} finished<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
