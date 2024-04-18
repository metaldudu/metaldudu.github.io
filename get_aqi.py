import requests
from bs4 import BeautifulSoup 
import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}

linkurl = 'https://www.iqair.cn/cn/china/hebei/shijiazhuang/xinhua' #url对应空气监测站点
air_site = linkurl.split('/')[-1] #获取唯一的站点名称

res = requests.get(linkurl, headers=headers)
soup = BeautifulSoup(res.content, 'html.parser')

# 初始化HTML内容
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>空气质量</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 10px;
            text-align: center;
        }
        h1 {
            font-size: 24px;
        }
        p {
            font-size: 18px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
<h1>空气质量</h1>
"""

air_aqi = soup.find("p", class_="aqi-value__value").string #aqi数值
    
air_all = soup.find("table", class_="aqi-overview-detail__other-pollution-table") #空气质量table

pm25 = air_all.find_all('tr')[1]  # 第二个tr
pm25_num = pm25.find_all('td')[2].select('span')[0].string

pm10 = air_all.find_all('tr')[2]
pm10_num = pm10.find_all('td')[2].select('span')[0].string

weather = soup.find("div", class_="weather") #天气部分
temperature = weather.table.find_all('tr')[1].find_all('td')[1].string
humidity = weather.table.find_all('tr')[2].find_all('td')[1].string

html_content += f"<p>AQI : {html.escape(air_aqi)}</p>"
html_content += f"<p>PM2.5 : {html.escape(pm25_num)}</p>"
html_content += f"<p>PM10 : {html.escape(pm10_num)}</p>"
html_content += f"<p>TMP : {html.escape(temperature)}</p>"
html_content += f"<p>HUM : {html.escape(humidity)}</p>"


# 添加HTML文件的结尾标签
html_content += "</body></html>"

# 将HTML内容写入文件
with open('aqi.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML文件已生成。")
