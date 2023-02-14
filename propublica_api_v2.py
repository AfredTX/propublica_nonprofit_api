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

    def get_orgs(self, org_list):
        frames = []
        for i in org_list:
            try:
                att_url = self.url + f"{i}" + ".json"
                response = requests.get(att_url, headers=self.header)
                print(att_url)
                print(response)
                response = response.json()
                record_dict = response['organization']
                print(record_dict)
                df = pd.DataFrame(record_dict, index=[0])
                frames.append(df)
            except requests.exceptions.JSONDecodeError:
                continue
            except KeyError:
                break

        df = pd.concat(frames)
        return df


