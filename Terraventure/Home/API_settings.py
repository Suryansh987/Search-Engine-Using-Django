SEARCH_KEY = "Enter Your API key"
SEARCH_ID = "Enter cx Value"
COUNTRY = 'Enter your region code'

SEARCH_URL="https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&q={query}&start={start}&gl=" + COUNTRY
RESULT_COUNT = 10



# print(SEARCH_URL.format(key=SEARCH_KEY,cx=SEARCH_ID,query="Youtube",start=0))