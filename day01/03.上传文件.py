import requests

url = "http://127.0.0.1:8080/carRental/file/uploadFile.action"
# 本地存在的文件
file = "E:/1.jpg"
with open(file, mode='rb') as f:
    # {'name':file - tuple}
    cs = {"mf": (file, f, "image/png")}
    r = requests.post(url, files=cs)
    # 获取图片的路径
    uploadPath = r.json()['data']['src']

# 租车系统上传图片
url = "http://127.0.0.1:8080/carRental/car/addCar.action"
cs = {
    "carnumber": "晋66", "cartype": "劳斯莱斯", "color": "黑色",
    "carimg": uploadPath, "description": "2020年定制款",
    "price": 5000000, "rentprice": 10000, "deposit": 1233, "isrenting": 0
}
head = {"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
r = requests.post(url, data=cs, headers=head)
print(r.text)
