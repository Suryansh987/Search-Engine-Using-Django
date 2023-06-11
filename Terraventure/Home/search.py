from Home.API_settings import *
from . import db_Functions
import pandas as pd
import requests
from urllib.parse import quote_plus
from .Fetch_Keywords import extract_main_words


#search function use google api to fetch values regarding to fields
#Change RESULT_COUNT in API_settings to get more/less results related to your query
def search(query, pages=int(RESULT_COUNT/10)): 
    results=[]
    for i in range(0, pages):
        start = i*10+i
        # API_settings 
        #SEARCH_KEY = "YOUR API KEY"
        # SEARCH_ID = "cx value from the script link"
        # COUNTRY = 'YOUR REGION CODE'
        # SEARCH_URL="https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&gl=" + COUNTRY
        # RESULT_COUNT = 10 can be changed as per need

        url = SEARCH_URL.format(key=SEARCH_KEY, cx=SEARCH_ID, query=quote_plus(query), start=start)
        response = requests.get(url)

        # Change the resonse into json format
        data = response.json()

        # Fetch the values from Json like(query,snippet,tittle,html,etc...)
        results += data["items"]

    # Create a pandas DataFrame of the results Fetched
    res_df = pd.DataFrame.from_dict(results)

    # Ranked the values of the Results Fetched
    res_df["rank"] = list(range(1, res_df.shape[0]+1))

    # res_df = res_df[["link","rank","snippet","title"]]
    res_df = res_df[["rank","title","link","displayLink","htmlSnippet"]]
    return res_df


#called from views.py
def terra_search(query):
    queries = extract_main_words(query)
    db_data = db_Functions.fetch_values_from_table_for_genral_terms(queries)
    # print(db_data.count())

    #if value present in db then return the QUerySET Object 
    if db_data.count() > 10:
        # print(db_data.count(),type(db_data))
        # for data in db_data:
            # print(data.title, data.link, data.displayLink, data.htmlSnippet, data.created,sep='  ', end='\n\n')
        return db_data
    # when value is not [resent in database will call the search function to fetch  the data from google api
    else:
        res_df = search(query)
        res_df.apply(lambda row: db_Functions.insert_into_table(row),axis=1)
        return res_df
    