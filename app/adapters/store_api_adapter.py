import json
import logging
from typing import List

import pydantic_core
import requests

from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_gateway import StoreGateway

from config import STORE_API_BASE_URL


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        """
        Save the processed road data to the Store API.
        Parameters:
            processed_agent_data_batch (dict): Processed road data to be saved.
        Returns:
            bool: True if the data is successfully saved, False otherwise.
        """
        response = requests.post(f"{STORE_API_BASE_URL}/processed_agent_data", data=f'[{",".join([model.json() for model in processed_agent_data_batch])}]',)

        try:
            response.raise_for_status()    
        except Exception as e:
            logging.error(e)
