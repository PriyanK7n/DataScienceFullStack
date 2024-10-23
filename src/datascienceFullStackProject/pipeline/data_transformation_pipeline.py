from src.datascienceFullStackProject.entity.config_entity import (DataTransformationConfig) 
from src.datascienceFullStackProject.components.data_transformation import (DataTransformation) # component
from src.datascienceFullStackProject.config.configuration import (ConfigurationManager)
from pathlib import Path

STAGE_NAME = "Data Transformation STAGE"
class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    # Data Transformation Pipeline Run
    def initiate_data_Transformation_run(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":              
                config = ConfigurationManager()
                data_Transformation_config = config.get_data_transformation_config()
                data_Transformation = DataTransformation(config=data_Transformation_config)      
                data_Transformation.train_test_spliting()
                
            else:
                raise Exception("Your new/current data schema to apply transformation on is not valid")

        except Exception as e:
            print(e)



        
