#to find zoho.com in the url 


#first method 

url ="https://mailadmin.zoho.com/cpanel/home.do#dashboard"

res = re.search("zoho.com", url)
print(res.group())



#Second method


import re
url ="https://mailadmin.zoho.com/cpanel/home.do#dashboard"
pattern = r"https://mailadmin.(.*?)/"

match = re.search(pattern, url)
res=match.group(1)
print(res)



#below is another method

# if match:
#     domain=match.group(1)
#     print("Domain name -", domain)
# else:
#     print("Domain name not found in the URL")




