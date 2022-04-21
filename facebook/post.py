import facebook
import os, random

path =
pathDone = 
image = random.choice(os.listdir(path)
image_fullpath = path + image
image_newpath = pathDone + image
caption = random.choice(os.listdir("./captions"))
hashtag = random.choice(os.listdir("./hashtags"))
with open(f'./captions/{caption}', 'r') as file:
    data = file.read()
with open(f'./hashtags/{hashtag}', 'r') as file:
    data = data + file.read()

page_access_token = ""
graph = facebook.GraphAPI(page_access_token)
facebook_page_id = ""
#graph.put_photo(image=open(image, 'rb'),message=data)
#graph.put_object(facebook_page_id, "feed",image=open(image, 'rb'), message=data)
graph.put_photo(image=open(image_fullpath , 'rb'),message=data)

os.rename(image_fullpath, image_newpath)
