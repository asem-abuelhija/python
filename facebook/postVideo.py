import facebook
import os, random

path = 
pathDone = 
video = random.choice(os.listdir(path))
video_fullpath = path + video
video_newpath = pathDone + video
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
#page_graph.put_video(video=open(video_fullpath , 'rb'),description=data)
# Add a link and write a message about it.
graph.put_object(
   parent_object="me",
   connection_name="feed",
   message=data,
   video= video_fullpath)

#os.rename(video_fullpath, video_newpath)
