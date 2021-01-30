import PyPDF2
import pyttsx3
import argparse


class Audiobook:
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def read_file(self, f_name, f_mode):
        print("\n*********Into Read File Method*********")
        # first will open the pdf file
        pdf_file_obj = open(f_name, f_mode)
        # creating a pdf reader object
        pdf_reader_obj = PyPDF2.PdfFileReader(pdf_file_obj)
        # get number of pages in pdf file
        num = pdf_reader_obj.numPages
        # read text
        engine = pyttsx3.init()
        for i in range(10, num):
            page_obj = pdf_reader_obj.getPage(i)
            engine.say(page_obj.extractText())
            engine.runAndWait()
        pdf_file_obj.close()
        print("\n********End Of Read File Method***********")

    def main(self, file_name, file_mode):
        self.read_file(file_name, file_mode)


if __name__ == '__main__':
    print("\n****Entered into main method()****")
    parser = argparse.ArgumentParser()
    parser.add_argument("--file_name", nargs='?', help="Enter file name keep it in same location!!",
                        metavar='file_name', required=True)
    args = parser.parse_args()
    audiobook = Audiobook(args.file_name, 'rb')
    audiobook.main(audiobook.file_name, audiobook.file_mode)
    print("\n*****End Of Main method()******")
