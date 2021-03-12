import web
import app
import json
import classify as classify
import base64
from requests.auth import HTTPBasicAuth

classify = classify.Classify()

users = (
    ("user","pass"),
    ("admin","admin")
)
class Api():

    def POST(self):
        try:
            env = web.ctx.env
            # print(env)
            auth = env.get("HTTP_AUTHORIZATION")

            '''
            Validate user and password
            '''
            auth = auth.replace("Basic ","")
            u = base64.b64decode(auth).decode("utf-8", "ignore")
            user,password = u.split(":")
            print(user)
            print(password)

            if (user,password) in users:
            # if auth == "1234": # Validate TOKEN
                form = web.input(image={})
                result ={}
                filedir = 'downloads' # change this to the directory you want to store the file in.
                if 'image' in form: # to check if the file-object is created
                    filepath = form.image.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
                    filename = filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
                    # fout = open( filename,'wb') # creates the file where the uploaded file should be stored
                    fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
                    fout.write(form.image.file.read()) # writes the uploaded file to the newly created file.
                    fout.close() # closes the file, upload complete.
                filename = filepath.split('/')[-1]
                result = classify.machineLearning(filedir +'/'+ filename)
                web.webapi.header('Content-Type', 'application/json', unique=True)
                web.webapi.OK(data='OK', headers={})
                return json.dumps(result)
            else:
                result = {}
                result["status"] = 400
                result["message"] = "Authentication error"
                return json.dumps(result)
        except Exception as error:
            result ={}
            result["status"] = "400"
            result["error"] = error.args[0]
            print("Error 101: {}".format(error.args[0]))
            return result
