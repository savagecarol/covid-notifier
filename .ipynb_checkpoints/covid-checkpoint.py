import requests
from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier 
url = "https://www.worldometers.info/coronavirus/country/india/"
req=requests.get(url)
soup = bs(req.text)
a=soup.find("li",{"class":"news_li"}).strong.text.split()[0]
b=list(soup.find("li",{"class":"news_li"}).strong.next_siblings)[1].text.split()[0]
message = "cases " + a + "\nDeaths " + b
toast = ToastNotifier()
toast.show_toast(title="COVID 19 UPDATES" , msg = message , duration = 10)