# 配套重写示例，非课程源码逐行转录。
import requests
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
session = requests.Session()
session.proxies.update(proxies)
print("代理配置键:", sorted(session.proxies))
session.close()
print("未发送请求：示例地址未运行真实代理服务")
