import requests
import xml.etree.ElementTree as ET
import html

# 发送请求获取XML内容
url = "http://218.11.10.130:8080/api/hour/130000.xml"
response = requests.get(url)
xml_content = response.content

# 解析XML
root = ET.fromstring(xml_content)

# 初始化HTML内容
html_content = "<html><head><title>空气质量</title></head><body>"

# 查找符合条件的部分
for pointer in root.findall(".//Pointer"):
    name_element = pointer.find("Name")
    if name_element is not None and name_element.text == "市区职工医院":
        # 找到符合条件的节点
        html_content += "<h1>市区职工医院空气情况：</h1>"
        
        # 提取<DataTime>和<AQI>的内容
        data_time = pointer.find("DataTime").text
        aqi = pointer.find("AQI").text
        html_content += f"<p>DataTime: {html.escape(data_time)}</p>"
        html_content += f"<p>AQI: {html.escape(aqi)}</p>"
        
        # 提取<Polls>下面<Name>为“PM2.5”和“PM10”的部分
        polls = pointer.find("Polls")
        for poll in polls.findall(".//Poll"):
            name = poll.find("Name").text
            value = poll.find("Value").text
            if name == "PM2.5" or name == "PM10":
                html_content += f"<p>{name} : {html.escape(value)}</p>"

# 添加HTML文件的结尾标签
html_content += "</body></html>"

# 将HTML内容写入文件
with open('../../aqi.html', 'w', encoding='utf-8') as file:
    file.write(html_content)

print("HTML文件已生成。")
