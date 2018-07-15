import UPLOAD
import LOGIN
import PARSER
import MAKEUP
from PARSER import HTMLControl
import time
from time import sleep
# MAIN
session = LOGIN.Login()
uploader = UPLOAD.Upload(session.GetSession())
parser = PARSER.Parsing()
maker = MAKEUP.Makeup(parser.Get_article_info())
content = maker.Makeup_upload_data()
uploader.WriteMyPost(content)

'''
#리퀘스트를 위한 경로
URL=  "http://ref.comgal.info/sjzb.php?id=cgref&page="
writeURL ="http://ref.comgal.info/write_ok.php?id=cgref"
commentURL = "http://ref.comgal.info/comment_ok.php?id=cgref"
refURL = "http://ref.comgal.info/write.php?id=cgref"
logURL = 'http://ref.comgal.info/login_check.php'

#로그인 세션 얻기
user_id = ''
password = ''
session = LOGIN.Login(logURL, user_id, password)

# day설정 : today / month / 'yyyy/mm/dd'
day = 'month'
mon = '6'
p = PARSER.Parsing()
ParsedList = p.Article(day,mon)
content = ''
links=''

# SORT
count = 0
for a in ParsedList :
    a['score'] = int(a['views']) + 4*int(a['coNum'])
ParsedList = sorted(ParsedList,key=itemgetter('score'),reverse=True)

# 보낼 글로 변환해서 저장
for a in ParsedList :
    content += f'글번호 : {a["no"]}   제목 :   {a["title"]} [{a["coNum"]}]'+f'{"조회수":>10}'+f' : {a["views"]} \n\n'
    links += '<a href="http://ref.comgal.info/sjzb.php?id=cgref&no='+a['no']+'"><b> - '+a['title']+'</b><br><br>'
    if count > 10 :
        break
    count += 1
content += "댓글에 글 제목을 누르면 링크로 이동합니다."
t = time.localtime()

if day=='month' : day=str(mon)+"월의"
print(content)


r= UPLOAD.REQ(session)
res = r.Article(f'{day} Hot Post 10 ',content)
num = p.cutString(res,'no','cat',3,1)
sleep(0.1)
r.Comment(num,links)


'''
