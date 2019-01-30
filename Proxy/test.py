# import json
#
# import re
#
# with open('t.json','r')as f:
#     raw_html = f.read()
# raw_jqery = "".join(re.findall(r"try{jQuery\((.*?)\);}", raw_html))
# # print(raw_query)
#
# t = json.loads(raw_jqery)
# json_list = t["result"]["data"]['feed']['list']
#
# # print(len(t))
# # import time
import requests
html = requests.get('http://www.ometal.com/news_china.htm').text
print(html)