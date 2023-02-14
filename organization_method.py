import pandas as pd

import propublica_api_v2

df = pd.read_csv(fr"C:\Users\fredr\PycharmProjects\propublica_nonprofit_api\nonprofit_explorer.csv")

org_list = df['ein']

result = propublica_api_v2.PropublicaAPI('ORGANIZATIONS').get_orgs(org_list)

result.to_csv(fr"C:\Users\fredr\PycharmProjects\propublica_nonprofit_api\filtered_explorer.csv")