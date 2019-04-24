import fbchat
import sys
import re

myfile = open("./log.log", 'w')

def write(string):
    global myfile
    myfile.write(string + "\n")
    myfile.flush()

write("hallo")
client = None
messageObj = None

# login string: login:[username],[password]
def login(string):
    write('login\n')
    global client
    args = re.split(r'#|,', string)
    client = fbchat.Client(args[1], args[2])
    write("here")
    print("#Ok")
    sys.stdout.flush()

def msg(string):
    global messageObj
    messageObj = fbchat.models.Message(string[1:])
    write("msg")
    print("#ok")
    sys.stdout.flush()

def start():
    write("starting")
    if not (client and messageObj):
        print("#Please log in and set message")
        sys.stdout.flush()
        return

    for friend in client.fetchAllUsers():
        print("#" + friend.name)
        sys.stdout.flush()
        input = sys.stdin.readline()[:-1]
        if input == "y":
            sent = client.send(messageObj, friend.uid)
            if sent:
                print("!Message sent successfully!")
                sys.stdout.flush()
        elif input == "n":
            print("!Message not sent")
            sys.stdout.flush()
        else:
            act(input)
    print("#Done")
    sys.stdout.flush()

def act(line):
    index = line[0]
    write(line)
    if index == "l":
        login(line)
    if index == "m":
        msg(line)
    if index == "s":
        start()

while True:
    write("next")
    line = sys.stdin.readline()[:-1]
    act(line)
    write("done")