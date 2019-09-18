# __author__ == "Priya"
"""Create a custom search engine in this link - https://cse.google.com/cse/all
Get API key by creating a new project here - https://developers.google.com/custom-search/v1/overview?csw=1"""
import os
import json
from googleapiclient.discovery import build


API_KEY=os.environ["MY_API_KEY"]
CSE_ID= os.environ["MY_CSE_ID"]

def gsearch(search_text):
    gbuild = build("customsearch", "v1", developerKey=API_KEY)
    output = gbuild.cse().list(q=search_text, cx=CSE_ID).execute()
    return output

def get_urls(search_out):
    for each in search_out['items']:
        print(each["link"])



if __name__ =="__main__":
    search_out = gsearch('Harry Potter')
    get_urls(search_out)
