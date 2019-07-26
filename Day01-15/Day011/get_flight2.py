"""

@Author:jyang
@Date:7/4/2019
"""
import requests
from requests.exceptions import ConnectionError
import time
import re
import datetime
from bs4 import BeautifulSoup
from urllib import request,parse
from docx import Document
from docx.oxml.ns import qn


def get(date, dep, arr, type):
    # https://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E6%AD%A6%E6%B1%89&searchArrivalAirport=%E4%B8%BD%E6%B1%9F&searchDepartureTime=2019-07-06&searchArrivalTime=2019-07-09&nextNDays=0&startSearch=true&fromCode=WUH&toCode=LJG&from=flight_dom_search&lowestPrice=null
    host = 'https://flight.qunar.com/site/oneway_list.htm?'
    search_dics = {
        'searchDepartureAirport':'%E6%AD%A6%E6%B1%89',
        'searchArrivalAirport':'%E4%B8%BD%E6%B1%9F',
        'searchDepartureTime': '2019-07-06',
        'searchArrivalTime': ''
    }
    url = host + ''.format(date, dep, arr, type)
    content = requests.get(url)
    soup = BeautifulSoup(content, 'html.parser')

if __name__ == '__main__':
    pass