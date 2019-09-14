# __author__ == "Priya"
""" Here we are scraping python modules data from pymotw page"""
import os
import urllib.request
from bs4 import BeautifulSoup as bs
import pdfkit
import time


def get_module_data(soup):
    # Getting each module name and its link
    li = soup.find_all("li", class_= "toctree-l2")
    module_data = []
    for each in li:
        module_name = each.a.get_text()
        module_link = each.a["href"]
        if module_name == "References":
            break
        _list=[module_name, module_link]
        module_data.append(_list)
    return module_data

def create_module_pdfs(URL, data):
    Target_path = os.path.join(os.getcwd(), Target_folder)
    if not os.path.exists(Target_path):
        os.mkdir(Target_path)
    for module in data:
        file_path = os.path.join(Target_path, str(module[0].split()[0])+".pdf")
        pdfkit.from_url(URL+str(module[1]), file_path)
        time.sleep(2)

if __name__ == "__main__":
    Target_folder = "Python_Modules"
    URL = "https://pymotw.com/3/"
    page_html = urllib.request.urlopen(URL)
    page_data = page_html.read()
    soup = bs(page_data, features="lxml")
    module_data = get_module_data(soup)
    create_module_pdfs(URL, module_data)

