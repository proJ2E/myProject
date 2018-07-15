from bs4 import  BeautifulSoup
import requests

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
    def Article(self,day):
        c = 1
        page = 1
        while c > 0 :
            self.html = self.getHTML(self.URL+str(page))
            c = self.processData(day)
            page += 1
        return self.articlelist

    def processData(self,day):
        count =0
        while self.html.find('cart') >=0 :
            # Cart value를 단위로 처리
            self.html = self.cutString(self.html,'cart','',2,0)
            # 거르기
            if not self._Num():
                continue
            if not self._Day(day):
                break
            # 글 리스트 만들기
            self.articlelist.append({'no': self._Num(),'title': self._Title(),'coNum':self._coNum(),'views':self._Views()})
            count += 1
        return count

    # 날짜 설정 형식 today or yy/mm/dd or all
    # 지정한 날짜의 글만 긁어오기
    def _Day(self,day):
        h = self.cutString(self.html, 'span title','',0,0)
        date = self.cutString(h,'초', '</span>', 3, 0)

        if day == 'today':
            if len(date) > 6 :
                return False
            else :
                return True
        elif day == 'all':
            return True
        else :
            if date==day :
                return True
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
