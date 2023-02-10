import configparser
import os

import pandas as pd
import requests


class PropublicaAPI:
    """A class to define attributes of Propublica's Nonprofit Explorer API V2"""

    def __init__(self, API):
        config = configparser.ConfigParser()
        config.read(f'{os.path.dirname(__file__)}/config.ini')
        self.url = config.get(API, 'url')
        #self.attribute = config.get(API, 'response')
        self.header = {'content-type': 'application/json'}

    def get(self):
        page = 0
        frames = []
        while True:
            att_url = self.url + f"&page={page}"
            response = requests.get(att_url, headers=self.header)
            response = response.json()
            print(response)
            record_list = list(response['organizations'])
            df = pd.DataFrame(record_list)
            frames.append(df)
            page += 1
            if response['cur_page'] >= response['num_pages']:
                break
        df = pd.concat(frames)
        return df


