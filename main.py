# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# if __name__ == "__main__":
#     app.run(debug=True)



# import pycurl
# import certifi
# from io import BytesIO
# byteobj = BytesIO()
# curlobj = pycurl.Curl()
# curlobj.setopt(curlobj.URL, 'https://www.scaler.com/topics/search/?q=python&page=1&tab=all')
# curlobj.setopt(curlobj.WRITEDATA, byteobj)
# curlobj.setopt(curlobj.CAINFO, certifi.where())
# curlobj.perform()
# curlobj.close()
# body = byteobj.getvalue()
# print(body.decode('iso-8859-1'))



import pycurl
from urllib.parse import urlencode
import certifi
curlobj = pycurl.Curl()
curlobj.setopt(curlobj.URL, 'https://api/post')
post_data = {'field': 'value'} # data to be posted
postfields = urlencode(post_data) # encoding the string to be used as a query
curlobj.setopt(curlobj.POSTFIELDS, postfields) #setting the cURL for POST operation
curlobj.setopt(curlobj.CAINFO, certifi.where())
curlobj.perform() # perform file transfer
curlobj.close() # end of session
