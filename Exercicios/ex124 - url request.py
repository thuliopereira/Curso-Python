import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print("Não consegui acessar o site")
else:
    print("O site Pudim esta acessivel no momento")