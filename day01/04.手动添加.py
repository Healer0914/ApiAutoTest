'''
Cookie 用来识别用户
'''

import requests

# 没有登录时调用，返回跳转到登录页面
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 发送请求时，带上cookie信息
head = {
    "Cookie": '_ga=GA1.2.462281248.1611731272; __auc=636eedf417742ab8f82edfb653b; MEIQIA_TRACK_ID=1ndssWLEeigTDtCg4D20mZmqK0u; __asc=44b45bf417747de4c0ca14600bd; Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1611731274,1611818487; MEIQIA_VISIT_ID=1ngjAjWchoSOMyGiXNxgraQDxTm; _gid=GA1.2.1251901040.1611818501; _gat=1; BAGSESSIONID=d340960e-ef69-499e-9306-d6ecdb6c2edf; JSESSIONID=0D09C4758C16BD06E0E3B40C29F8445D; Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1611818593; BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1; BAG_EVENT_CK_KEY_="2780487875@qq.com"; BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38'
}

r = requests.get(url, headers=head)
print(r.text)
with open(r"D:\tools\1.html", "w", encoding='utf8') as f:
    f.write(r.text)
assert "<title>百格活动 - 账户总览</title>"

'''
缺点：
1.cookie会失效，失效后需要重新获取
2.登录后的每个接口，需要带着cookie
'''