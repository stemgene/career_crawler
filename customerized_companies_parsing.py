import requests
from bs4 import BeautifulSoup
import re
import json
import ast
from selectolax.parser import HTMLParser
import chompjs

def handler(**kwargs):
    company_name = kwargs['company_name'].lower()
    func_name = "parsing_" + company_name
    if func_name in globals(): # 当前模块（py文件）中所有的变量
        func = globals()[func_name]
        position_list = func(**kwargs)
    return position_list
    



def check_available(url):
    response = requests.get(url)
    if response.status_code == 200:
        # # 输出页面内容
        # soup = BeautifulSoup(response.text, 'html.parser')
        # content = soup.prettify()
        # output_txt(content)
        return response
    else:
        print("Network is not available.")

def output_txt(content):
    with open("page_content.txt", 'w', encoding='utf-8') as f:
        f.write(content)

def parsing_tripleten(**kwargs):
    response = check_available(kwargs['URL'])
    html = HTMLParser(response.text)
    data = html.css("script[type='text/javascript']")
    js_objects = []
    position_list = []
    for script in data:
        try:
            script_text = script.text()
            if kwargs['parameters']['search_key'] in script_text:
                company_positions_data = chompjs.parse_js_objects(script_text)
                for item in company_positions_data:
                    js_objects.append(item)
        except:
            pass
    company_positions = js_objects[kwargs['parameters']['index_num']]
    for position in company_positions:
        if position['location']['name'] == 'USA' or position['location']['name'] == 'Remote':
            #print(position['name'], position['location']['name'])
            position_list.append(position['name'] + " " + position['location']['name'])
    return position_list

def parsing_mobi(**kwargs): # for all data in greenhouse website
    position_list = []
    response = check_available(kwargs['URL'])
    soup = BeautifulSoup(response.text, 'html.parser')
    script_tag = soup.find_all('script')[2].string
    json_text = re.search(r'\{.*\}', script_tag).group()
    data_dict = json.loads(json_text)
    job_list = data_dict['state']['loaderData']['routes/$url_token']['jobPosts']['data']
    for item in job_list:
        position_list.append(item['title'])
    return position_list