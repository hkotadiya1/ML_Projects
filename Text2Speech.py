import pyttsx3
import PyPDF2
book = open('/home/harshal/TMWSHF.pdf', 'rb') # rb= read binary
pdfReader=PyPDF2.PdfFileReader(book) #read book
pages=pdfReader.numPages #NumberOfPages
print(pages)
speak = pyttsx3.init() #object
for i in range(10,pages):
    page = pdfReader.getPage(i) #page by page read
    text = page.extractText() #ExtractText
    speak.setProperty('rate', 111)  #Sets speed percent Can be more than 100
    speak.setProperty('volume', 0.3) #Set volume 0-1
    speak.say(text)
    speak.runAndWait() #To run the s