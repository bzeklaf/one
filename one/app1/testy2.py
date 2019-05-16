import docx2txt

def testy():
    a1 = "at the relevant fuck"
    text = docx2txt.process("C1.docx")
    if a1 in text:
        print('replace "at the relevant time" with "at the time of specification"')
    else:
        print("nothing found")

testy()