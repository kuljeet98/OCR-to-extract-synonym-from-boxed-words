from lib import*
from line_removal import*
class tesract:
    def __init__(self,name):
        self.name = name
#def pro performs the image to text operation and returns def
    def pro(self):
        text = pytesseract.image_to_string(self.name+'_.png')
        syns = wordnet.synsets(text)
        return (text,"means:",syns[0].definition())
        # dictionary=PyDictionary()
        # return (dictionary.meaning(text)) #defintion extraction from the processed image
#def syn returns the synonyms of the word fetched above
    def syn(self):
        synonyms = []
        text = pytesseract.image_to_string(self.name+'_.png')
        for syn in wordnet.synsets(text):
            for l in syn.lemmas():
                synonyms.append(l.name()) # synonym extraction
                # if l.antonyms():
                #     antonyms.append(l.antonyms()[0].name())
        return (text,"synonyms are:",synonyms)

