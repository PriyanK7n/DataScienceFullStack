from dataclasses import dataclass
from pathlib import Path

# Inputs to data Ingestion pipline
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# Inputs to data Validation pipline
@dataclass
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

# Inputs to data Transformation pipline
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    
