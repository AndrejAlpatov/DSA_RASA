from flask import Flask
#import spacy
#from spacy.lang.de.examples import sentences

#nlp = spacy.load("de_core_news_sm")
#doc = nlp(sentences[0])
#print(doc.text)
#for token in doc:
#    print(token.text, token.pos_, token.dep_)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
