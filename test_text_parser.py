import text_parser
import stop_words as sw
import text_parser as tp

testing_texts = [   
"coucou GrandPy, comment ça va ? Tu peux me parler d'Openclassrooms stp ",
"quelle est l'adresse d'openclassrooms dans Paris ?",
"raconte-moi l'histoire du lycée tphonse daudet",
]

def test_is_string():
    for text in testing_texts:
        assert isinstance(tp.find_relevant_expression(text), str)

def test_len_max():
    for text in testing_texts:
        assert len(tp.find_relevant_expression(text)) >= 3

def test_no_stop_words():
    for text in testing_texts:
        splitted =tp.find_relevant_expression(text).split(" ")
        nb_stop_words = 0
        for word in splitted:
            nb_stop_words += sw.general.count(word)
        assert nb_stop_words == 0

