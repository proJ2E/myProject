import html
from time import sleep

class REQ:
    def __init__(self,url,s):
        self.URL= url
        self.session = s

    #File Path parma으로 추가해야함
    def Article(self,subject,content,link1):
        # 추후 FIle의 경로는 따로 변경.
        '''
        files ={
            'file1': open(fileDir,'rb')
        }
        '''

        sendData = {
            'subject' : str(subject),
            'memo' : content,
            'link1' : link1
        }
        # file upload 때문에 Content-Type 지정이 필요없다.
        custom = {
            #"http://ref.comgal.info/write.php?id=cgref",
            'Referer' : "http://ref.comgal.info/write.php?id=cgref",
            'Method': 'POST',
            'Content-Length': str(len(str(sendData)))
        }
        #REQ
        writeReq =  self.session.post(self.URL,headers=custom,data=sendData)
        if writeReq.status_code==200 :
            print("POSTED")
        else:
            print("FAILED")
            print(writeReq.status_code)


    def Comment(self,no,text):
        sendData = {
            'no': str(no),
            'memo': text
        }
        custom = {
            'Referer': "http://ref.comgal.info/sjzb.php?id=cgref",
            'Method': 'POST',
            'Content-Length': str(len(str(sendData)))
        }
        writeReq = self.session.post(self.URL,headers=custom,data=sendData)
        if writeReq.status_code == 200:
            print("POSTED")
            # print(writeReq.headers)
            # print(writeReq.text)
        else:
            print("FAILED")
            print(writeReq.status_code)