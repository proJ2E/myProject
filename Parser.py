from bs4 import  BeautifulSoup
import requests

class HTMLControl :
    def getHTML(self,url):
        req = requests.get(url)
        HTML = self.req.text
        return HTML

    def cutString(self,strS,s1,s2='',l1=1,l2=1):
        # l1,l2는 찾은 문자열로부터의 거리
        # recommend: l1 = len(str(s1))
        if s2=='':
            index1 = strS.find(s1) + l1
            index2 = strS.find(s2) - l2
            result = strS[index1:index2]
        else :
            index1 = strS.find(s1) +l1
            result = strS[index1:]
        return result


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
