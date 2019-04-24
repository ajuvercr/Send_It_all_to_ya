import fbchat
import sys
import re

client = None
messageObj = None
# login string: login:[username],[password]
def login(string):
    global client
    args = re.split(r'#|,', string)
    client = fbchat.Client(args[1], args[2])

def msg(string):
    global messageObj
    messageObj = fbchat.models.Message(string[1:])

def start():
    if not (client and messageObj):
        print("!Please log in and set message")
        return
    for friend in client.fetchAllUsers():
        print("#" + friend.name)
        input = sys.stdin.readline()[:-1]
        if input == "y":
            sent = client.send(messageObj, friend.uid)
            if sent:
                print("!Message sent successfully!")
        elif input == "n":
            print("!Message not sent")
        else:
            print("!Not valid: stopping, valid are y and n")
            return

if __name__ == "__main__":
    while True:
        line = sys.stdin.readline()[:-1]
        index = line[0]
        if index == "l":
            login(line)
        if index == "m":
            msg(line)
        if index == "s":
            start()