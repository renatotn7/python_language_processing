import requests
import re
from bs4 import BeautifulSoup
import StringIO
import urllib


def main():
    
    urllib.urlretrieve ("http://www.bing.com/translator/api/language/Speak?locale=en-US&gender=male&media=audio/mp3&text=Try",	"1.mp3")
    r = requests.get("https://www.coursera.org/api/subtitleAssetProxy.v1/FE4eZY8zQk6OHmWPMwJOrQ?expiry=1456790400000&hmac=d1yz-X_aQjU7CmJ_UWOJJaspeK8Bt7-Ju53BLg1e9VY&fileExtension=vtt")
    
    arq2 = open('legenda.srt', 'r')
    arq3 = open('referencia.txt', 'r')
    
    strcont2 = arq3.read()
    strcont= arq2.read()

    arq = open('conhecidas.csv', 'r')
    strcont=strcont.lower()
    strcont2=strcont2.lower()
    
    txtconh = arq.read()
    txtconh=txtconh.lower()
    
    wordscon = re.compile("\r|\n").split(txtconh)
    arq.close()
    
    wordset = set()
    wordlist = list()
    wordref = list()
    lines = re.compile("\r|\n").split(strcont)
    linesref = re.compile("\r|\n").split(strcont2)
    
    for line in lines:
        if ("-->" not in line) and len(line)>6 :
            
            words = re.compile("\s").split(line)
            
            for word in words:
                word = word.replace("\'d","").replace("\'re","").replace("\'m","").replace("\'s","").replace("!","").replace("<i>","").replace("</i>","").replace("\'ll","").replace("\"","").replace("\'t","").replace("\'ve","")
                wordset.add(word.replace(",","").replace(".","").replace("?","").replace("]","").replace("[","").replace("(","").replace(")","").replace(":",""))
                wordlist.append(word.replace(",","").replace(".","").replace("?","").replace("]","").replace("[","").replace("(","").replace(")","").replace(":",""))

    for line in linesref:
        if ("-->" not in line) and len(line)>6 :
            
            words = re.compile("\s").split(line)
            
            for word in words:
                word = word.replace("\'d","").replace("\'re","").replace("\'m","").replace("\'s","").replace("!","").replace("<i>","").replace("</i>","").replace("\'ll","").replace("\"","").replace("\'t","").replace("\'ve","")
                wordref.append(word.replace(",","").replace(".","").replace("?","").replace("]","").replace("[","").replace("(","").replace(")","").replace(":",""))
    strfinal=''

#    for item in wordset:
#        if item not in wordscon:
#            iter = re.findall("\d", item)
#            if len(iter) == 0 and len(item)>1:
#                print str(wordref.count(item))+";"+item
    

    for item in wordset:
        if item not in wordscon:
            iter = re.findall("\d", item)
            if len(iter) == 0 and len(item)>1:    
                strfrase=""
                strfinal=""
                for idx, line in enumerate(lines):
                    if item in line:
                        strfrase = str(line)
                        if(idx > 0):
                             strfrase = str(lines[idx-1]) + " " +strfrase 
                        if(idx < len(lines)):
                              strfrase = strfrase + " "  + lines[idx+1]

                              strfinal = strfinal + " <br/> " + strfrase.replace(item,"<b>"+item+"</b>")

            
                    
                        
     
                
                r = requests.get("http://wordnetweb.princeton.edu/perl/webwn?sub=Search+WordNet&o2=1&o0=1&o8=1&o1=1&o7=&o5=&o9=&o6=&o3=&o4=&h=0000&s="+str(item))
                 
                #print r.content
                soup = BeautifulSoup(r.content, 'html.parser')
                s1=r.content
                #encontra as entradas de trabalho para a camada 1 do html
                
                letters = soup.find_all("div", class_="form")
                
                #for letters1 in letters:
                print  str(wordref.count(item))+";"+item+";"+strfinal+"<br/><br/>"+str(letters).replace(";","")
        
                #http://www.bing.com/translator/api/Dictionary/Lookup?from=en&to=pt&text=bias
                #http://www.bing.com/translator/api/language/Speak?locale=en-US&gender=male&media=audio/mp3&text=bias

if __name__ == "__main__":
    main()
