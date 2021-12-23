import requests
from pprint import pprint

class Character:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.powerstats = {}
    
    def get_id_via_api(self, url):
        resp = requests.get(f'{url}/search/{self.name}/')
        if resp.json() == {'error': 'character with given name not found', 'response': 'error'}:
            print(f'Невозможно получить ID персонажа {self.name}')
        else:
            self.id = resp.json()['results'][0]['id']
    
    def get_powerstats_via_api(self, url):
        if self.id == None:
            print(f'ID персонажа {self.name} ещё не известен')
        else:
            resp = requests.get(f'{url}/{self.id}/powerstats')
            self.powerstats = resp.json()

def make_list_of_objects(list_of_characters, url):
    for character in list_of_characters:
        list_of_characters.insert(list_of_characters.index(character), Character(character))
        list_of_characters.remove(character)
    for character in list_of_characters:
        character.get_id_via_api(url)
        if character.id != None:
            character.get_powerstats_via_api(url)
        else:
            list_of_characters.remove(character)
    return list_of_characters

def sort_by_intelligence(list_of_characters):
    for i in range(len(list_of_characters) - 1):
        for j in range(len(list_of_characters) - 1):
            if int(list_of_characters[j].powerstats['intelligence']) < int(list_of_characters[j+1].powerstats['intelligence']):
                list_of_characters[j], list_of_characters[j+1] = list_of_characters[j+1], list_of_characters[j]
    return list_of_characters

def main():
    #type your token below
    api_token = ''
    api_url = f"https://superheroapi.com/api/{api_token}"

    characters_list = [ 'Hulk', 'Captain America', 'Thanos' ]
    characters_list = make_list_of_objects(characters_list, api_url)   
    characters_list = sort_by_intelligence(characters_list)
    for index, character in enumerate(characters_list):
        print(f"{index+1}. Имя - {character.name}, ID - {character.id}, Intelligence - {character.powerstats['intelligence']}")

main()
