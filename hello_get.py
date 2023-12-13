import cgi 
import os

print("Content-Type : text/html\n")
form = cgi.FieldStorage()

firstname = form.getvalue('firstname')
lastname = form.getvalue('lastname')
email = form.getvalue('email')
message = form.getvalue('message')

print(firstname)

# if not firstname or not lastname:
#     print("Firstname and lastname should not be empty")
# elif not email or '@' not in email:
#     print("Invalid Email adress")
# else:
#     upload_dir = "uploads"
#     if not os.path.exists(upload_dir):
#         os.makedir(upload_dir)
#     if 'file' in form:
#         file_item = form['file']
#         if file_item.filename:
#             with open(os.path.join(upload_dir,file_item.filename),'ws') as file:
#                 file.write(file_item.file.read())
#             print("Your message is submited and your file is uploaded ")
#         else:
#             print("your message is submitted")
#     else:
#         print("no file uploaded")