import UPLOAD
import LOGIN
import PARSER
import MAKEUP
from USER_INPUT import Get_Values



# MAIN
user_input_data= Get_Values()
session = LOGIN.Login(user_input_data)
uploader = UPLOAD.Upload(session.GetSession())
parser = PARSER.Parsing(user_input_data)
maker = MAKEUP.Makeup(parser.Get_article_info(),user_input_data)
content = maker.Makeup_upload_data()
uploader.WriteMyPost(content)
