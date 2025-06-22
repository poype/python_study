import requests
from bs4 import BeautifulSoup
import json

# 测试api请求
def test_api():
    url = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查请求是否成功

        # 解析JSON响应
        data = response.json()

        if data.get('ok') and data.get('data'):
            # 提取所有name值
            business_types = [item.get('name') for item in data.get('data')]
            print(business_types)
        else:
            print("响应数据格式不正确或未找到业务类型数据")

    except requests.exceptions.RequestException as e:
        print(f"请求异常: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
        return []
    except Exception as e:
        print(f"发生错误: {e}")
        return []

def test_static_html():
    url = ''

    # 设置请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        # 发送HTTP请求
        response = requests.get(url, headers=headers)

        # 检查状态码
        response.raise_for_status()  # 如果状态码不是200，会抛出HTTPError异常

        # 解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找并打印标题
        title = soup.find('title')
        if title:
            print(f"页面标题: {title.text}")
        else:
            print("未找到页面标题")
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP错误发生: {http_err}')
    except requests.exceptions.RequestException as req_err:
        print(f'请求异常发生: {req_err}')
    except Exception as err:
        print(f'其他错误发生: {err}')


if __name__ == '__main__':
    test_static_html()
    test_api()





