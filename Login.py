import requests
'''
피난갤 로그인 소스
'''
class Login:
    def __init__(self,user_input):
        self.url = "http://ref.comgal.info/login_check.php"
        self.user_id = user_input['user_id']
        self.password = user_input['password']

    def GetSession(self):
        with requests.session() as s:
            LOGIN_INFO = {
                'user_id': self.user_id,
                'password': self.password
            }
            login_req = s.post(self.url, data=LOGIN_INFO)

            if login_req.status_code==200 :
                return s
            else:
                print("LOGINFAILED")
                return False
