from src.datascienceFullStackProject import logger
from src.datascienceFullStackProject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascienceFullStackProject.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascienceFullStackProject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline



STAGE_NAME = "Data Ingestion STAGE"

try:
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} started<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion_run()
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} finished<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation STAGE"

try:
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} started<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation_run()
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} finished<<<<<\n\nx======x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation STAGE"

try:
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} started<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.initiate_data_Transformation_run()
    logger.info(f">>>>>>>> Stage: {STAGE_NAME} finished<<<<<\n\nx======x")

except Exception as e:
    logger.exception(e)
    raise e