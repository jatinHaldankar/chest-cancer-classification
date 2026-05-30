import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        try:
            dataset_url = self.config.source_url
            zip_local_data_file = self.config.local_data_file

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_local_data_file)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_local_data_file}")
        
        except Exception as e:
            raise e
    
    def extract_file(self):
        unzip_path = self.config.unzip_dir

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)