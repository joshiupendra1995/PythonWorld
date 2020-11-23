import PyPDF2
import pyttsx3

# audio settings

language = 'en'

# first will open the pdf file
pdfFileObj = open('Java-Interview-Questions.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# get number of pages in pdf file
num = pdfReader.numPages

# read text
engine = pyttsx3.init()
for i in range(10, num):
    pageObj = pdfReader.getPage(i)
    engine.say(pageObj.extractText())
    engine.runAndWait()
pdfFileObj.close()
