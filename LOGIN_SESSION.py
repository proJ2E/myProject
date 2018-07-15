import requests
from time import sleep
'''
피난갤 로그인 소스
'''
#'http://ref.comgal.info/login_check.php'

def Login(url,user_id,password):
    with requests.session() as s:
        #LOGIN INFO의 값을 따로 추출해서 지정할 것
        LOGIN_INFO = {
            'user_id': user_id,
            'password': password
        }
        login_req = s.post(url, data=LOGIN_INFO)

        if login_req.status_code==200 :
            return s
        else:
            print("LOGINFAILED")
            return False
