from dataclasses import dataclass
from pathlib import Path

# Inputs to data Ingestion pipline
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
