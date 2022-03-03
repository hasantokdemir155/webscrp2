from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import requests

from bs4 import BeautifulSoup




dv_pth="chromedriver"
brw=webdriver.Chrome(dv_pth)
#brw.get("https://www.youtube.com/")
#brw.get("https://www.hurriyet.com.tr/")
brw.get("https://www.gittigidiyor.com")

searchinpt=brw.find_element_by_xpath("/html/body/div[1]/header/div[3]/div/div/div/div[2]/form/div/div[1]/div[2]/input")
time.sleep(1)

a=input('ürün gir')
searchinpt.send_keys(str(a))
searchinpt.send_keys(Keys.ENTER)
print (brw.current_url)
input()

r=requests.get(brw.current_url)

soup=BeautifulSoup(r.text,'lxml')


imx= soup.find_all('h3',{'class':'medium'})


spans = soup.find_all('span', {'class':'buy-price'})    

for i,s in zip(imx,spans):
     print(i.string.strip()+' '+s.string.lstrip())




button = brw.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div/div[3]/div[4]/nav/ul/li[12]/a/span")
                                    


for i in range(1,99):
    #button = brw.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div/div[3]/div[4]/nav/ul/li[12]/a/span")
    brw.execute_script("arguments[0].click();", button)
    
    r=requests.get(brw.current_url)

    
    soup=BeautifulSoup(r.text,'lxml')
        
    
    imx= soup.find_all('h3',{'class':'medium'})


    spans = soup.find_all('span', {'class':'buy-price'})    

    vrm = soup.find_all('li',{'class':'sc-12aj18f-2 jwZJjs'})
    #vrm = soup.find_all('a')[tabindex]
    #print(vrm)   

    #print(soup.find_all('a',{'title':'Sonraki sayfa'}))
    vsm=soup.find_all('a',{'title':'Sonraki sayfa'}) 
    
    for y in vsm:
         c=y.get('tabindex')
         print(y.get('tabindex'))           
         if c== '-1':
             print('haltttt')
             
             
    
    for i,s in zip(imx,spans):
         print(i.string.strip()+' '+s.string.lstrip())


    
#print(button)

#button.click
time.sleep(3)
halt

searchinpt=brw.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/input")
time.sleep(1)
a=input('ürün gir')
searchinpt.send_keys(str(a))
searchinpt.send_keys(Keys.ENTER)
print (brw.current_url)
time.sleep(5)


r=requests.get(brw.current_url)


soup=BeautifulSoup(r.text,'lxml')
print(soup)

vrx=soup.find_all('span', {'class':'prdct-desc-cntnr-ttl'})

vrxx=soup.find_all('span', {'class':'prdct-desc-cntnr-name hasRatings'})

vr1=soup.find('div',{'class':'prdct-cntnr-wrppr'})
spans = soup.findAll('span',)
vrmm=soup.find_all('div',{'class':'prc-box-sllng'})

for i,s,m in zip(vrx,vrxx,vrmm):
     print(i.string+' '+s.string+' '+m.string)






halt
rslt=brw.find_elements_by_css_selector(".g a")
for i in rslt:
    print(i.text)
time.sleep(5)
#brw.back()
#browser.close()
print(brw.title)
brw.quit()
