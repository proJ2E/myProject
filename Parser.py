from bs4 import  BeautifulSoup
import requests
import time
from time import sleep

class HTMLControl :
    def getHTML(self,url):
        self.req = requests.get(url)
        HTML = self.req.text
        return HTML

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
    def __init__(self):
        self.URL = "http://ref.comgal.info/sjzb.php?id=cgref&page="
        self.html = ""
        self.articlelist = []
        self.mondetect = False
    def Article(self,day,mon=''):
        c = 1
        page = 1
        while c > 0 :
            self.html = self.getHTML(self.URL+str(page))
            c = self.processData(day,mon)
            page += 1
            sleep(0.05)
        return self.articlelist

    def processData(self,day,mon):
        count =0
        while self.html.find('cart') >=0 :
            # Cart value를 단위로 처리
            self.html = self.cutString(self.html,'cart','',2,0)
            # 거르기
            if not self._Num():
                continue
            elif not self._Day(day,mon):
                break
            elif self._Day(day,mon) == 'pass' :
                count += 1
                continue

            # 글 리스트 만들기
            self.articlelist.append({'no': self._Num(),'title': self._Title(),'coNum':self._coNum(),'views':self._Views()})
            count += 1
        return count

    # 날짜 설정 형식 today or yyyy/mm/dd or month
    # 지정한 날짜의 글만 긁어오기
    def _Day(self,day,mon):
        h = self.cutString(self.html, 'span title','',0,0)
        art_mon = self.cutString(h,'년','월',2,0)
        date = self.cutString(h,'초', '</span>', 3, 0)

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

        else :
            if date==day :
                return True
            elif len(date) < 7 :
                #print('P ' + date + ' ' + art_mon)
                return 'pass'
            else :
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
    def _Views(self):
        i=0
        while i<2:
            i+=1
            self.html=self.cutString(self.html,'font color','',10,0)
        views = self.cutString(self.html,'>','<',1,0)
        return views


    ''' soup를 이용한 PARSER
     def func(self):
        soup = BeautifulSoup(self.URL,'html.parser')
        print(soup)
        Articles =[]
        articles = soup.select(
            'tr'
        )
        c=0
        i=0
        j=0
        no=""
        name=""
        for article in articles:
            noNname = article.select('td > span')
            fonts = article.select('td > font')
            views = article.select('td > font > span')

            # 필요없는 부분 삭제
            t = str(article)
            print(t)
            #print(views)
            if article.text.find('공지') > 0:
                continue
            if t.find('cart') < 0 :
                continue
            #여기부터 파싱
            #글번호 / 닉네임
            for noname in noNname:
                if i%2 == 0:
                    no = noname.text
                else:
                    name = noname.text
                i+=1

            # 코멘트 개수
            i=0
            for font in fonts:
                text = font.text
                slice = text.find(']')
                if slice == 0 :
                    continue
                co_no = text[1:slice]
            if not co_no :
                co_no ="0"
            Articles.append({'no': no,'name':name,'co_no':co_no})
            j+=1


        for a in Articles:
            print("NO : " + a['no'])
            print("NAME : " + a['name'])
            print("CO_NO : "+ a['co_no'])
    '''
