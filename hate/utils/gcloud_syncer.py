import os
import logging
import zipfile

from google.cloud import storage
from hate.exception import NerException
import sys


class GCloudSyncer:
    def __init__(self):
        try: 
            self.client = storage.Client()
            logging.info("Initializied GCloudSyncer with GCP CLIENT")
        except Exception as e:
            error_message = "Failed to initialize a GCloudSyncer with GCP Clinet"
            logging.error(error_message)
            raise NerException(error_message, sys) from e
        
    
    def _create_directory(self, directory_path: str) -> None:
        try:
            os.makedirs(directory_path, exist_ok=True)
            logging.info(f"Created folder: {directory_path}")
        except Exception as e:
            raise NerException(e, sys) from e
        
    
    def download_file(self, bucket_name: str, file_name: str, save_path: str) -> None:
        try: 
            logging.info(f"Fetching file: {file_name} from GCP Bucket , {bucket_name}")
            bucket = self.client.get_bucket(bucket_name)
            blob = bucket.blob(file_name)

            self._create_directory(os.path.dirname(save_path))

            blob.download_to_filename(save_path)
            logging.info(f"Downloaded file to {save_path}")
        
        except Exception as e: 
            error_message = f"Failed to download file {file_name} from GCP BUkcet {bucket_name}"
            logging.error(error_message)
            raise NerException(error_message, sys) from e
        
    
    def extract_zip(self, zip_file_path:str, extract_path: str)  -> None:
        try: 
            logging.info(f"Extractinf zip file from {zip_file_path}")
            self._create_directory(extract_path)
            with zipfile.ZipFile(zip_file_path, "r") as zip_obj:
                zip_obj.extractall(extract_path)
            
            logging.info(f"Extracted files to {extract_path}")
        except Exception as e:
            error_message = f"Failed to extract zip file from {zip_file_path}"
            logging.error(error_message)
            raise NerException(error_message, sys) from e
    

    def upload_file(self, bucket_name: str, file_path: str, gcp_path: str) -> None:
        """Uploads a file to google Cloud storage.
            ARgs: 
                bucket_name: The name of the GCP Bucket
                file_path: The local path of the file to upload
                gcp_path: The path in the GCP bucket to save the file
        """
        try: 
            logging.info(f"Uploading file '{file_path}' to GCP bukcet '{bucket_name}' at {gcp_path}")
            bucket = self.client.get_bucket(bucket_name)
            blob = bucket.blob(gcp_path)
            blob.upload_from_filename(file_path)
            logging.info(f"Uploaded file to GCP at gs: //{bucket_name}/{gcp_path}")

        except Exception as e:
            error_message = f"Failed to uplad file '{file_path}' to GCP bucket '{bucket_name}"
            logging.error(error_message)
            raise NerException(error_message, sys) from e

        
