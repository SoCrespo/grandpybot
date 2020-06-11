# coding: utf-8

import text_parser as tp
import google_place_answer as gp
import google_static_map as gm
import wikipedia_answer as wiki
import error
import sys


def ask():
    return input("De quel endroit veux-tu que je te parle ? ")


def say_problem():
    print("Mon cerveau Google me joue des tours ! "
          "Reviens quand je serai plus en forme...")


def say_not_understood():
    print("Hmmm, je n'ai pas bien compris ta question... ", end="")


def ask_for_choice(list_of_place_objects):
    indexed_options = [f'{k+1}: {item.address}'
                       for k, item in enumerate(list_of_place_objects)]
    choices = (f"A quelle adresse ? {' ou '.join(indexed_options)} ? "
               f"Tape le numéro correspondant : ")
    place = list_of_place_objects[int(input(choices)) - 1]
    return place

def display_map(address):
    pass

def display_infos(place_object, answer, map):
    print(
        f"Ah, {place_object.name}, je connais cet endroit ! "
        f"C'est situé {place_object.address}."
        f"\nEt à ce sujet, savais-tu que {answer.extract}\n(la suite ici : {answer.url}, la carte là : {map})"
    )


def main():
    question_is_valid = False
    while not question_is_valid:
        text = ask()
        relevant_expression = tp.find_relevant_expression(text)
        api_answer = gp.GooglePlaceAnswer(relevant_expression)
        if api_answer.status == "ERROR":
            say_problem()
            sys.exit()
        elif api_answer.status != "OK" or api_answer.candidates == []:
            say_not_understood()
        else:
            question_is_valid = True
            if len(api_answer.candidates) > 1:
                place = ask_for_choice(api_answer.candidates)
            else:
                place = api_answer.candidates[0]
                print(place.address)
            try:
                answer = wiki.WikipediaAnswer(place.address)
                map = gm.get_map_url(place.address)
            except error.APIError:
                say_problem()
                sys.exit()
            
            display_infos(place, answer, map)


if __name__ == "__main__":
    main()
