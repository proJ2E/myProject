from operator import itemgetter

class Makeup:
    def __init__(self,ParsedList):
        self.article_content=''
        self.comment_content=''
        self.exposed_num = 10
        self.ParsedList = ParsedList

    def Makeup_upload_data(self):
        self.exposed_num = int(input('Best 글의 개수를 정해주세요 : '))
        count = 1
        benefit = 4
        # Score에 따라서 내림차순 정리
        for a in self.ParsedList :
            a['score'] = int(a['views']) + benefit*int(a['coNum'])
        self.ParsedList = sorted(self.ParsedList,key=itemgetter('score'),reverse=True)

        # 보낼 글로 변환해서 저장
        for a in self.ParsedList :
            self.article_content += f'글번호 : {a["no"]}  ' \
                                    f' 제목 :   {a["title"]} ' \
                                    f'[{a["coNum"]}]'+\
                                    f'{"조회수":>10}'+\
                                    f' : {a["views"]} ' \
                                    f'\n\n'
            self.comment_content += '<a href="http://ref.comgal.info/sjzb.php?id=cgref&no='\
                                    +a['no']+'"><b> - '\
                                    +a['title']+'</b><br><br>'
            if count >= self.exposed_num :
                self.article_content += "댓글에 글 제목을 누르면 링크로 이동합니다."
                break
            count += 1
        self.subject = 'Hot Post 10'
        content  = {'article_content':self.article_content,'comment_content': self.comment_content}
        return content