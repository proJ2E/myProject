import UPLOAD
import LOGIN
import PARSER
import MAKEUP


# MAIN
session = LOGIN.Login()
uploader = UPLOAD.Upload(session.GetSession())
parser = PARSER.Parsing()
maker = MAKEUP.Makeup(parser.Get_article_info())
content = maker.Makeup_upload_data()
uploader.WriteMyPost(content)
