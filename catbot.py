import praw
import requests
from requests.structures import CaseInsensitiveDict
import os   


url =  "https://api.thecatapi.com/v1/images/search"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"

HEADERS = {'User-Agent' : 'MyAPI/0.1 by username'}

with open('pass.txt','r') as f:
    passwd = f.readlines()

def initialiseReddit(CLIENT_ID,CLIENT_SECRET,USERNAME,PASSWORD):
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = HEADERS,
        username = USERNAME,
        password = PASSWORD
    )
    return reddit

def details():
    #Login
    PASSWORD = passwd[0].strip()
    CLIENT_ID = passwd[1].strip()
    CLIENT_SECRET = passwd[2].strip()
    USERNAME = passwd[3].strip()
    return initialiseReddit(CLIENT_ID,CLIENT_SECRET,USERNAME,PASSWORD)



def submission(randomcat):
    #Initialise reddit instance
    reddit = details()

    #Detailing which subreddit to submit to
    mysubreddit = reddit.subreddit("CATPOSTING2")

    #Submission
    mysubreddit.submit_image("Randomcatpic", randomcat)


def createPic():
    #Send request to retrieve cat pic url
    resp = requests.get(url, headers=headers)
    diction = resp.json()
    randomcatpic = diction[0]['url'] 
    img_data = requests.get(randomcatpic).content

    #Create cat pic file
    with open('cat.jpg', 'wb') as handler:
        handler.write(img_data)
        randomcat = 'cat.jpg'
    return randomcat

    
def deleteFile():
    if(os.path.isfile("cat.jpg")):
    
        #os.remove() function to remove the file
        os.remove("cat.jpg")
    
        #Printing the confirmation message of deletion
        print("File Deleted successfully")
    elif(os.path.isfile("cat.gif")):
    
        #os.remove() function to remove the file
        os.remove("cat.gif")
    
        #Printing the confirmation message of deletion
        print("File Deleted successfully")
    else:
        print("File does not exist")

def main() :
    randomcat = createPic()
    submission(randomcat)
    deleteFile()

if __name__=="__main__":
    main()