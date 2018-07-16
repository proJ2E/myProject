from operator import itemgetter
import math

class Makeup:
    def __init__(self,ParsedList,user_input):
        self.article_content=''
        self.comment_content=''
        self.exposed_num = user_input['exposed_num']
        self.ParsedList = ParsedList
    def Makeup_upload_data(self):
        count = 1
        self.Calculate_average()
        self.Sort_data()
        # 보낼 글로 변환해서 저장
        self.article_content += f' 검색일 조회수 평균 :{round(self.ave_data["ave_views"],2)} \n' \
                                f'          댓글수 평균 :{round(self.ave_data["ave_coNum"],2)}\n\n' \
                                f"댓글에 글 제목을 누르면 링크로 이동합니다."
        for a in self.ParsedList :
            #self.article_content += f' 제목 :   {a["title"]} ' \
            #                        f'[{a["coNum"]}]'+\
            #                        f'{"조회수":>10}'+\
            #                        f' : {a["views"]} ' \
            #                        f'\n\n'
            self.comment_content += '<a href="http://ref.comgal.info/sjzb.php?id=cgref&no='\
                                    +a['no']+'"><b> - '\
                                    +a['title']+f'  [{a["coNum"]}]</b>'\
                                    +'</a><br>'+f'조회수: {a["views"]}'\
                                    +f'{"&nbsp;"*(20-len(a["views"]))}'+f'작성자 :{a["name"]}'\
                                    +'<br><br>'
            if count >= self.exposed_num :
                break
            count += 1
        self.subject = 'Hot Post 10'
        content  = {'article_content':self.article_content,'comment_content': self.comment_content}
        print(content['article_content'])
        return content

    def Calculate_average(self):
        sum_views = 0
        sum_comnum = 0
        count = 0
        for a in self.ParsedList:
            sum_views += int(a['views'])
            sum_comnum += int(a['coNum'])
            count += 1
        self.ave_data  = {'ave_views' : sum_views/count ,'ave_coNum' : sum_comnum/count }
        print(self.ave_data)

    def Sort_data(self):
        # Score에 따라서 내림차순 정리
        for a in self.ParsedList :
                a['score'] = self.Give_score(a)
        self.ParsedList = sorted(self.ParsedList, key=itemgetter('score'), reverse=True)

    def Give_score(self,a):
        c = int(a['coNum'])
        v = int(a['views'])
        ave_v = self.ave_data['ave_views']
        ave_c = self.ave_data['ave_coNum']
        # 코멘트에 대한 점수
        if c <= 20 :
            comment_score = 1.5*(c-ave_c)
        else:
            # 불타는 정치글 방지
            if v < ave_v * 2.2 :
                comment_score = -2*(c-20)
            else:
                comment_score = 1.5 * (c - ave_c)
        # 조회수에 대한 점수
        if v>=ave_v*1.3:
            x = int(v-ave_v*1.2) * 5
            views_score = (math.sqrt(x))*1.2
        else:
            views_score = v-ave_v

        score = comment_score + views_score

        return score