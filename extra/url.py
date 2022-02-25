# import urllib.request

# url = "https://github.com/javierarce/palabras/blob/master/listado-general.txt"

# data = urllib.request.urlopen(url).read(20000) # read only 20 000 chars
# # data = data.split("\n") # then split it into lines


# contador  = 0

# for line in data:
#     contador += 1
#     print(line)
# print(contador)

#########################
import requests

url = "https://github.com/javierarce/palabras/blob/master/listado-general.txt"
req = requests.get(url)
filename = req.url[url.rfind('/')+1:]
# print(filename)

with open(filename, 'wb') as file:
    for chunk in req.iter_content(chunk_size=8192):
        if chunk:
            file.write(chunk)

# with open('file.txt', 'wb') as f:
#     f.write(res.content)

#########################

# import requests as req

# url = "https://github.com/javierarce/palabras/blob/master/listado-general.txt"
# res = req.get(url)

# file = open('filename.txt', 'w', encoding='utf-8')
# file.write(res.text)
# file.close()

###########################
# import requests

# url = "https://github.com/javierarce/palabras/blob/master/listado-general.txt"

# r = requests.get(url, allow_redirects=True)

# open('lista-general.txt', 'wb').write(r.content)

#############################
# from urllib.request import urlopen

# file = open("filename2.txt","w")
# url = urlopen("https://github.com/javierarce/palabras/blob/master/listado-general.txt")
# for line in url:
#     file.write(line + '\n')
# file.close()