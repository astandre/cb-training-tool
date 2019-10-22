import spacy

# Loading nlp model

# nlp = spacy.load("es_core_news_md")
# nlp = spacy.load("es_core_news_sm")
nlp = spacy.load("es_core_news_ast")
print("Model Ready")


def tokenize_sentences(sentence):
    tokens = []
    for token in nlp(sentence):
        tokens.append(token.text)
    return tokens


def process_sentence(sentence, method):
    result = []
    sentence = nlp(sentence)
    if method == "NER":
        entities = sentence.ents
        if len(entities) > 0:
            for ent in entities:
                result.append([ent.text, ent.label_, ent.start_char, ent.end_char])
    else:
        for token in sentence:
            if method == "TOKEN":
                result.append(token.text)
            elif method == "POS":
                result.append(token.pos_)
            elif method == "LEMMA":
                result.append(token.lemma_)
    return result


def word_similarity(word1, word2):
    word1 = nlp(word1)
    word2 = nlp(word2)
    return word1.similarity(word2)


def decompose_sentence(sentence):
    ner_items = process_sentence(sentence, "NER")
    tokens_aux = process_sentence(sentence, "TOKEN")
    pos = process_sentence(sentence, "POS")
    tokens = []
    for i in range(0, len(tokens_aux)):
        tokens.append([tokens_aux[i], pos[i]])
    new_sentence = []
    entities = []
    instances = []
    if len(ner_items) > 0:
        begin = 0
        end = 0
        for text, type, b_char, e_char in ner_items:
            # new_sentence.append(text)
            new_sentence.append({"type": "text", "text": sentence[begin:b_char]})
            new_sentence.append({"type": "entity", "text": sentence[b_char:e_char], "nature": type})
            begin = e_char + 1
            end = e_char + 1
            # Adding instances
            instances.append([text, type])

            # Adding entity types
            exists = False
            for entity in entities:
                if entity == type:
                    exists = True
                    break
            if exists is False:
                entities.append(type)
        new_sentence.append({"type": "text", "text": sentence[end:len(sentence)]})
        # print(ner_items)
    else:
        new_sentence.append({"type": "text", "text": sentence})
    return new_sentence, entities, instances, tokens
