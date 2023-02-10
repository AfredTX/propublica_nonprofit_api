import propublica_api_v2

result = propublica_api_v2.PropublicaAPI('NONPROFITEXPLORER').get()

result.to_csv(fr"C:\Users\fredr\PycharmProjects\propublica_nonprofit_api\nonprofit_explorer.csv")