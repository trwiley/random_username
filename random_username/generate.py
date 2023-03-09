import os
import random
import json

def generate_username(num_results=1):
    directory_path = os.path.dirname(__file__)
    adjectives, nouns = [], []

    word_file = open(os.path.join(directory_path, 'data', 'words.json'), 'r')
    words = json.load(word_file);

    adjectives = words['adjectives']
    nouns = words['nouns']

    usernames = []
    for _ in range(num_results):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns).capitalize()
        num = str(random.randrange(100))
        usernames.append(adjective + noun + num)
    
    return usernames
