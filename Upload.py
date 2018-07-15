from time import sleep
from PARSER import HTMLControl
class Upload:
    def __init__(self,s):
        self.session = s
        self.fileDir = {}
        self.sendData = {}
        self.header = {}
        self.URL = ''

    def WriteMyPost(self,content):
        res = self.Article(input('제목을 입력해주세요 : '),content['article_content'])
        h = HTMLControl()
        num = h.cutString(str(res), 'no', 'cat', 3, 1)
        self.Comment(num,content['comment_content'])
        return

    # Upload Article
    def Article(self,subject,content, fileDir='',link1='',link2=''):
        self.Makeup_data_for_article(subject,content,self.fileDir,link1,link2)
        writeReq =  self.session.post(self.URL , headers=self.header,data=self.sendData)
        if writeReq.status_code==200 :
            print("POSTED")
            sleep(0.1)
            return writeReq.text
        else:
            print("FAILED")
            print(writeReq.status_code)
            return

    #전송할 데이터 정리
    def Makeup_data_for_article(self,subject,content,fileDir='',link1='',link2=''):
        if self.fileDir :
            self.files ={
                'file1': open(self.fileDir,'rb')
            }
        else :
            self.fileDir={}
        self.sendData = {
            'subject' : str(subject),
            'memo' : content,
            'link1' : link1
        }
        self.header = {
            'Referer' : "http://ref.comgal.info/write.php?id=cgref",
            'Method': 'POST',
            'Content-Length': str(len(str(self.sendData)))
        }
        self.URL = "http://ref.comgal.info/write_ok.php?id=cgref"
        return

    # Upload Comment
    def Comment(self,article_no,content):
        self.Makeup_data_for_comment(article_no,content)
        writeReq = self.session.post(self.URL,headers=self.header,data=self.sendData)
        if writeReq.status_code == 200:
            print("POSTED")
            return
        else:
            print("FAILED")
            print(writeReq.status_code)
            return

    #전송할 데이터 정리
    def Makeup_data_for_comment(self,article_no,content):
        self.sendData = {
            'no': str(article_no),
            'memo': content
        }
        self.header = {
            'Referer': "http://ref.comgal.info/sjzb.php?id=cgref",
            'Method': 'POST',
            'Content-Length': str(len(str(self.sendData)))
        }
        self.URL = "http://ref.comgal.info/comment_ok.php?id=cgref"
        return

