import requests


def get_token():
    SECRET = 'd8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o'
    ID = 'wwca233d5d5e521b32'
    url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'
    r = requests.get(url)
    token = r.json()['access_token']
    return token

def test_create_member():
    create_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "zhangsan111",
        "name": "张三test",
        "mobile": "+86 13800022222",
        "department": [1]
    }
    r = requests.post(url=create_url,json=data)
    print(r.json())


def test_delete_member():
    delete_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=zhangsan111'
    r = requests.get(delete_url)

