from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request
from nlp_core import *
import random
import re

# from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# CORS(app)
db = SQLAlchemy(app)


# Defining model

class Triple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(300), nullable=False)
    predicate = db.Column(db.String(300), nullable=False)
    object = db.Column(db.String(400), nullable=False)

    def __repr__(self):
        return f'<{self.subject}><{self.predicate}><{self.object}>'


# Defining views

@app.route('/')
def train_view():
    """
    Main page
    :return:
    """
    return render_template("main.html")


@app.route('/train/intents')
def intents_view():
    """
    Main page
    :return:
    """
    return render_template("intents.html")


# NLP methods
@app.route('/nlp/tokenize/sentences', methods=['POST'])
def tokenize_sentences_view():
    if request.method == 'POST':
        return {"tokenized_sentence": tokenize_sentences(request.json["sentence"])}
    else:
        return {"error": "Method now allowed"}


@app.route('/nlp/tokenize', methods=['POST'])
def tokenize():
    if request.method == 'POST':
        return {"tokens": process_sentence(request.json["sentence"], "TOKEN")}
    else:
        return {"error": "Method now allowed"}


@app.route('/nlp/pos', methods=['POST'])
def pos_tagging():
    if request.method == 'POST':
        return {"pos": process_sentence(request.json["sentence"], "POS")}
    else:
        return {"error": "Method now allowed"}


@app.route('/nlp/ner', methods=['POST'])
def ner():
    if request.method == 'POST':
        return {"pos": process_sentence(request.json["sentence"], "NER")}
    else:
        return {"error": "Method now allowed"}


@app.route('/nlp/lemmas', methods=['POST'])
def lemmatization():
    if request.method == 'POST':
        return {"lemmas": process_sentence(request.json["sentence"], "LEMMA")}
    else:
        return {"error": "Method now allowed"}


@app.route('/nlp/similarity', methods=['POST'])
def word_similarity_view():
    if request.method == 'POST':
        return {"similarity": word_similarity(request.json["word1"], request.json["word2"])}
    else:
        return {"error": "Method now allowed"}


# Working views
@app.route('/intents', methods=['GET'])
def get_intents():
    intents = Triple.query.filter_by(predicate='rdf:type', object="Intent").all()
    options = []
    for intent in intents:
        # print(intent)
        option = Triple.query.filter_by(subject=intent.subject, predicate="hasDescription").first()
        # print(option)
        options.append({"intent": intent.subject, "description": option.object})
    return {"options": options}


@app.route('/intents/example', methods=['POST'])
def get_intent_example():
    example = Triple.query.filter_by(subject=request.json["intent"], predicate='hasSentence').all()
    if len(example) > 0:
        example = example[random.randint(0, len(example) - 1)]
        return {"example": example.object}
    else:
        return {"example": "No existen ejemplos todavia"}


@app.route('/intents/sentences', methods=['POST'])
def get_intent_sentences():
    sentences = Triple.query.filter_by(subject=request.json["intent"], predicate='hasSentence').all()
    result = {"sentences": []}
    for sentence in sentences:
        # print(sentence.object)
        new_sentence, entities, instances = decompose_sentence(sentence.object)
        result["sentences"].append(
            {"sentence": new_sentence, "entities": entities, "instances": instances, "id": sentence.id})
    return result


@app.route('/process', methods=['POST'])
def extract_info():
    result = {"sentences": []}
    for sentence in request.json["sentences"]:
        if len(sentence) > 0:
            sentence_object = Triple(subject=request.json["intent"], predicate='hasNewSentence', object=sentence)
            db.session.add(sentence_object)
            new_sentence, entities, instances, tokens = decompose_sentence(sentence)
            db.session.commit()
            key_words_aux = Triple.query.filter_by(subject=request.json["intent"], predicate='hasKeyword')
            key_words = []
            for aux in key_words_aux:
                word = Triple.query.filter_by(subject=aux.object, predicate='hasWord').first()
                pos = Triple.query.filter_by(subject=aux.object, predicate='hasPOS').first()
                key_words.append([word.object, pos.object, aux.object])

            result["sentences"].append(
                {"sentence": new_sentence, "entities": entities, "instances": instances, "id": sentence_object.id,
                 "tokens": tokens, "key_words": key_words})
            print(result)
    return result


@app.route('/add/keyword', methods=['POST'])
def new_key_words():
    if len(request.json["options"]) > 0:
        key_words_aux = Triple.query.filter_by(subject=request.json["intent"], predicate='hasProposedKeyword').all()
        if len(key_words_aux) > 0:
            key_words_aux = key_words_aux[len(key_words_aux) - 1]
            number = int(re.findall(r'\d+', key_words_aux.object)[0]) + 1
        else:
            number = 0
            for option in request.json["options"]:
                # print(option)
                key_subject = request.json["intent"] + "-Keyword" + str(number)
                db.session.add(Triple(subject=request.json["intent"], predicate='hasProposedKeyword', object=key_subject))
                db.session.add(Triple(subject=key_subject, predicate='hasWord', object=option["word"]))
                db.session.add(Triple(subject=key_subject, predicate='hasPOS', object=option["pos"]))
                db.session.add(Triple(subject=key_subject, predicate='refersTo', object=option["subject"]))
                number += 1
        db.session.commit()

    return {"status": 200}


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
