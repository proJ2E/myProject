import requests
import time
from time import sleep

class HTMLControl :
    def getHTML(self,url):
        self.req = requests.get(url)
        HTML = self.req.text
        return HTML
    # 문자열 커팅 편하게하는 함수
    def cutString(self,strS,s1,s2='',l1=1,l2=1):
        # l1,l2는 찾은 문자열로부터의 거리
        # recommend: l1 = len(str(s1))
        if not s2=='':
            index1 = strS.find(s1) + l1
            index2 = strS.find(s2) - l2
            result = strS[index1:index2]
        else :
            index1 = strS.find(s1) +l1
            result = strS[index1:]
        return result


class Parsing(HTMLControl) :
    def __init__(self,user_input):
        self.URL = "http://ref.comgal.info/sjzb.php?id=cgref&page="
        self.html = ""
        self.articlelist = []
        self.mondetect = False
        self.day= user_input['day']
        self.mon= user_input['mon']

    def Get_article_info(self):
        searchDetect = True
        page = 1
        # searchDetect 는 해당 페이지에 더 이상 검색할 내용이 없음을 감지해줌
        while searchDetect :
            self.html = self.getHTML(self.URL+str(page))
            searchDetect = self.ProcessData(self.day,self.mon)
            page += 1
            sleep(0.05)
        return self.articlelist

    def ProcessData(self,day,mon):
        detect = False
        while self.html.find('cart') >=0 :
            # Cart value를 기준으로 나누면서 처리
            self.html = self.cutString(self.html,'cart','',2,0)

            # 공지사항 / 필요없는 글 거르기
            # pass 따로 처리 안하면 그냥 멈춤
            if not self._Num():
                continue
            elif not self._Day(day,mon):
                break
            elif self._Day(day,mon) == 'pass' :
                detect = True
                continue

            # 글 리스트 만들기
            self.articlelist.append({'no': self._Num(),'title': self._Title(),'name':self._Name(),'coNum':self._coNum(),'views':self._Views()})
            detect = True

        return detect

    # 날짜 설정 형식 today or yyyy/mm/dd or month
    # 지정한 날짜의 글만 긁어오기위해 판별을 해주는 함수
    # 페이지에서 직접 보이는 날짜 = date
    # yyyy/mm/dd/hh/mm/ss 형식에서 추출 = art_mon
    # 완전히 뜯어고칠 필요가 있는 부분
    def _Day(self,day,mon):
        # 글의 날짜부분만 따로 긁어옴
        h = self.cutString(self.html, 'span title','',0,0)
        art_mon = self.cutString(h,'년','월',2,0)
        date = self.cutString(h,'초', '</span>', 3, 0)
        # 판별
        if day == 'today':
            if len(date) > 6 :
                return False
            else :
                return True
        elif day == 'month':
            t = time.localtime()
            # mon 검색월 , now_mon = 현월 ,art_mon = 작성월
            # 현월 설정
            now_mon = str(t.tm_mon)
            if len(now_mon)==1 : now_mon = "0" + now_mon
            if len(mon) == 1: mon = "0" + mon

            # 필요없는거 지나치기
            # 1. 해당되지 않는 월 pass
            # 2. 해당되면 detect 처리
            if art_mon != mon and self.mondetect == False:
                return 'pass'
            elif art_mon == mon :
                if not self.mondetect :
                    self.mondetect = True
                return True
            else :
                return False
        # yyyy/mm/dd 형식으로 입력받았을때
        else :
            if date == day:
                self.mondetect = True
                return True
            elif len(date) < 6:
                #print('P ' + date + ' ' + art_mon)
                return 'pass'
            else:
                if not self.mondetect :
                    return "pass"
                return False


    # 글 내용 파싱하는 부분
    def _Num(self):
        no = self.cutString(self.html, 'color="', '</span', 15, 0)
        return no
    def _Title(self):
        self.html = self.cutString(self.html,'a href','',4,1)
        title = self.cutString(self.html,'>','<',1,0)
        return title
    def _coNum(self):
        self.html = self.cutString(self.html,'font style','',10,0)
        coNo = self.cutString(self.html,'>','<',2,0)
        if not coNo :
            coNo="0"
        else :
            coNo=self.cutString(coNo,'[',']',1,0)
        return coNo
    def _Name(self):
        ml = self.cutString(self.html,'hand','',4,1)
        name = self.cutString(ml,'>','span',1,2)
        return name
    def _Views(self):
        i=0
        while i<2:
            i+=1
            self.html=self.cutString(self.html,'font color','',10,0)
        views = self.cutString(self.html,'>','<',1,0)
        return views
