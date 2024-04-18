import requests
from bs4 import BeautifulSoup 
import html

def fetch_data(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查是否请求成功
        return response.content
    except requests.RequestException as e:
        print("请求失败:", e)
        return None

def parse_data(html_content):
    if not html_content:
        return None, None, None, None, None

    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        air_aqi = soup.find("p", class_="aqi-value__value").string
        air_all = soup.find("table", class_="aqi-overview-detail__other-pollution-table")
        pm25_num = air_all.find_all('tr')[1].find_all('td')[2].select('span')[0].string
        pm10_num = air_all.find_all('tr')[2].find_all('td')[2].select('span')[0].string
        weather = soup.find("div", class_="weather")
        temperature = weather.table.find_all('tr')[1].find_all('td')[1].string
        humidity = weather.table.find_all('tr')[2].find_all('td')[1].string
        return air_aqi, pm25_num, pm10_num, temperature, humidity
    except (AttributeError, IndexError) as e:
        print("解析数据出错:", e)
        return None, None, None, None, None

def generate_html(air_aqi, pm25_num, pm10_num, temperature, humidity):
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
    html_content += f"<p>AQI : {html.escape(air_aqi)}</p>"
    html_content += f"<p>PM2.5 : {html.escape(pm25_num)}</p>"
    html_content += f"<p>PM10 : {html.escape(pm10_num)}</p>"
    html_content += f"<p>TMP : {html.escape(temperature)}</p>"
    html_content += f"<p>HUM : {html.escape(humidity)}</p>"
    html_content += "</body></html>"
    return html_content

def save_html(html_content):
    if html_content:
        try:
            with open('aqi.html', 'w', encoding='utf-8') as file:
                file.write(html_content)
            print("HTML文件已生成。")
        except IOError as e:
            print("写入HTML文件出错:", e)

def main():
    linkurl = 'https://www.iqair.cn/cn/china/hebei/shijiazhuang/xinhua'
    air_site = linkurl.split('/')[-1]

    html_content = fetch_data(linkurl)
    air_aqi, pm25_num, pm10_num, temperature, humidity = parse_data(html_content)
    html_content = generate_html(air_aqi, pm25_num, pm10_num, temperature, humidity)
    save_html(html_content)

if __name__ == "__main__":
    main()
