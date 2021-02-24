import requests

# 表单格式的数据：content-type：www-x-form-urlencoded,使用data传参
# 登录接口
url = "http://jy001:8081/futureloan/mvc/api/member/login"
cs = {
    "mobilephone": "15129938628",
    "pwd": "123456"
}
r = requests.post(url, data=cs)
print(r.text)
# 响应体
rjson = r.json()
assert rjson['status'] == 1
assert rjson['code'] == '10001'
assert rjson['msg'] == '登录成功'

# json格式的数据：content-type:application/json,使用json传参
# 具体使用data还是json传参，要看接口是怎么定义的。
'''
httpbin.org 是一个测试网站，不管发送什么类型的数据，
这个接口将发送的请求，封装成json格式的返回。'''

url = "http://www.httpbin.org/post"
cs = {"mobilephone": 15129938628, "pwd": "123456"}
r = requests.post(url, data=cs)
print("data传参===", r.text)
r = requests.post(url, json=cs)
print("json传参===", r.text)

# 租车系统，添加车辆
url = "http://127.0.0.1:8080/carRental/login/login.action"
cs = {
    "carnumber": "晋666",
    "cartype": "劳斯莱斯",
    "color": "黑色",
    "carimg": "images/defaultcarimage.jpg",
    "description": "2020年定制款",
    "price": 5000000,
    "rentprice": 10000,
    "deposit": 1233,
    "isrenting": 0
}
head = {
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
proxy = {
    "http": "http://127.0.0.1:8888", #http协议，使用这个代理
    "https": "http://127.0.0.1:8888", #https协议，使用这个代理
}
r = requests.post(url, data=cs, headers=head)
print(r.text)
