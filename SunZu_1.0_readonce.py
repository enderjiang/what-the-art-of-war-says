import PyPDF2
import time

contentlist=[]
fulllist=[]
fileobj=open('/Users/ender/Dropbox/Python/Test/Artofwar/The_Art_Of_War.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(fileobj)
number=pdfReader.numPages
#for i in range(number):
for i in range(number):    
    pageObj = pdfReader.getPage(i)
    item=pageObj.extractText()
    itemlist=item.split('.')
    contentlist=contentlist+itemlist
#print(contentlist)
print(len(contentlist))
question=input('what sunzu said today to you, let me know what do you really want to learn:')
questionlist=question.split()
#full=questionlist.append(question)
print(questionlist)
print(fulllist)
for j in range(len(contentlist)):
    searchelement=contentlist[j].find(question)
    if searchelement != -1:
        #print(singlefilepath)
        #print(whattofind)
        extracted=contentlist[j].strip()
        time.sleep(1.5)
        print(extracted)
fileobj.close()