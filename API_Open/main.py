# Imports
import requests
import json

baseurl  = "https://rickandmortyapi.com/api/"
endpoint = "character"

def main_request(baseurl , endpoint, x):
    response = requests.get(baseurl+endpoint+ f"/?page={x}")
    return response

response = main_request(baseurl , endpoint, 1)
# print(response)

# To get the json response

# print(response.json())
# print(type(response.json()))

####---- Convert python dictionary to JSON Format String onject using json.dumps()

# print(json.dumps(response.json() , indent=4))

###--------------------------------------



### To get keys
# print(response.json().keys())

# Access specific key

# print(response.json()['info'])

def get_pages(response):
    pages = response.json()['info']['pages']
    return pages

print(get_pages(response=response))

# # Paginationto completed


# # Create a function returns all the name and number of episodes from that pages
def parse_page(response):
    for item in response.json()['results']:
        name = item['name']
        episodes = item['episode']
        print(name , len(episodes))

parse_page(response=response)


# # execute the parse page function for all 42 pages 

# main_list = []

# # for i in range(1, int(get_pages(response))+1):
# #     response = main_request(baseurl , endpoint, i)
# #     # <parse page>
# #     main_list.append(<data>)

# # print(main_list)

# # import pandas
# # df = pd.createDataFrame(main_list, columns)
# # print(df)

# # df.to_csv('results.csv')

