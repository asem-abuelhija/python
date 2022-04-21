import os, random

image = random.choice(os.listdir("../memes"))
image = "../" + image
caption = random.choice(os.listdir("captions"))
hashtag = random.choice(os.listdir("hashtags"))
with open(f'captions/{caption}', 'r') as file:
    data = file.read()
with open(f'hashtags/{hashtag}', 'r') as file:
    data = data + file.read()

