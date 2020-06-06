import lang_parser

lp = lang_parser.LangParser()

def test_find_the_word():
    text1 = "coucou GrandPy, comment ça va ? Tu peux me parler d'Openclassrooms stp "
    assert lp.find_the_word(text1) == 'Openclassrooms'
