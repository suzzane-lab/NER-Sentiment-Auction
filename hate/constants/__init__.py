import os
from datetime import datetime

TIMESTAMP: str = datetime.now(). strftime("%m_%d_%y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)
LOGS_DIR = "logs"
LOGS_FILE_NAME = "ner.log"

#Data Ingestion constants

GCP_DATA_FILE_NAME = "archive.zip"
CSV_DATA_FILE_NAME = "ner.csv"
DATA_INGESTION_ARTIFACTS_DIR ="DataIngestionArtifacts"
GCP_DATA_FILE_PATH = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR, GCP_DATA_FILE_NAME)
CSV_DATA_FILE_PATH = os.path.join(ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR, CSV_DATA_FILE_NAME)
BUCKET_NAME = "ner-bucket"

#Data Transformation Constants

DATA_TRANSFORMATION_ARTIFACTS_DIR = "DataTransformationArtifacts"
DATA_TRANSFORMATION_ARTIFACTS_DIR_PATH = os.path.join(ARTIFACTS_DIR, DATA_TRANSFORMATION_ARTIFACTS_DIR)