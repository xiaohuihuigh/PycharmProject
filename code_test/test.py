import json
import re
with open('test.html','r')as f:
    raw_html = f.read()
raw_html = raw_html.replace("\n"," ")
# print raw_html
raw_html = re.findall(r"var allData =(.*) var adData",raw_html)
# print raw_html
if raw_html:
    raw_html = raw_html[0]
json_list = json.loads(raw_html.rstrip(" ")[:-1])['newsstream']

print json_list