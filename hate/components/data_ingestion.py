import os
import logging

from hate.exception import NerException
from hate.utils.logger import setup_loggin
from hate.utils.gcloud_syncer import GCloudSyncer
from hate.entity.data_ingestion_artifacts import DatIngestionArtifacts
import sys

class DataIngestion:
    def __init__(self, data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud_syncer = GCloudSyncer()
        setup_loggin()
        logging.info("Starting the DataIngestion class")

    
    def _create_directory(self, directory_path:str)-> None:
        try: 
            os.makedirs(directory_path,exist_ok=True)
            logging.info(f"Created folder at: {directory_path}")

        except Exception as e:
            raise NerException(e, sys) from e
    

    def initiate_data_ingestion(self) -> DatIngestionArtifacts:
        """Starts the process: gets the csv file from GCP and prepares it for next spep
            Returns:
                DataIngestionArtifacts: An object with the path to the CSVfile.

        """
        try:
            #Crreate a folder to store our data
            self._create_directory(self.data_ingestion_config.data_ingestion_artifacts_dir)

            #Step2: Get the CSV file from GCP using GCloudSyncer
            self.gcloud_syncer.download_file(
                bucket_name=self.data_ingestion_config.bucket_name,
                file_name= self.data_ingestion_config.gcp_data_file_name,
                save_path= self.data_ingestion_config.gcp_data_file_path, 
            )

            #Step 3: Keep track of where we saved the file
            data_ingestion_artifact = DatIngestionArtifacts(
                csv_data_file_path = self.data_ingestion_config.csv_data_file_path,
            )

            logging.info("Finished data ingestion process")
            return data_ingestion_artifact
        except Exception as e:
            error_message = "Failed to complete data ingestion process"
            logging.error(error_message)
            raise NerException(error_message, sys) from e


        