import PINAN_POST
import LOGIN_SESSION
import Parser

#리퀘스트를 위한 경로
URL=  "http://ref.comgal.info/sjzb.php?id=cgref&page="
writeURL ="http://ref.comgal.info/write_ok.php?id=cgref"
commentURL = "http://ref.comgal.info/comment_ok.php?id=cgref"
refURL = "http://ref.comgal.info/write.php?id=cgref"
logURL = 'http://ref.comgal.info/login_check.php'

#로그인 세션 얻기
user_id = ''
password = ''
#session = LOGIN_SESSION.Login(logURL, user_id, password)

p = Parser.Parsing()
#글 작성

