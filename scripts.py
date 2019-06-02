import os
import urllib.request
import time

url = []
name = []
current_cont = []
new_cont = []
status = []

def newurl():
    os.system('cls')
    print("New URL Screen\nHere are the current URLs")
    for i in range(len(url)):  # Print the current url list
        print(str(i + 1) + ". " + name[i] + "  " + url[i])  # "{Number}. {url}"
    inputurl = input("Enter a new URL: ")
    inputname = input("Enter a name for this URL: ")
    url.append(inputurl)
    name.append(inputname)
    print(url[0])
    print(name[0])


def get_contents():
    for i in range(len(url)):
        print("Loading...")
        current_cont.append(urllib.request.urlopen(url[i]).read())
        status.append("x")


def compare_contents():
    # Get new contents
    for i in range(len(url)):
        new_cont.append(urllib.request.urlopen(url[i]).read())

    # Compare them and return status
    for i in range(len(url)):
        if current_cont[i] == new_cont[i]:
            status[i] = "\t\tNo change!"
        else:
            status[i] = "\t\tChanged!"


def track():
    # TODO make output better
    os.system('cls')
    if len(url) == "0":
        print("There is no URL to track! Go back and add more.")
        return
    get_contents()  # Get current contents of URLs
    cont = True
    while cont:
        os.system('cls')
        print("Now tracking the URLs. They will be checked every 5 seconds.\n")
        for i in range(len(url)):
            if status[i] == "\t\tChanged!":
                print(str(i + 1) + ". " + name[i] + status[i])
            else:
                continue
        for i in range(len(url)):
            compare_contents()
            if status[i] == "\t\tNo change!":
                print(str(i + 1) + ". " + name[i] + status[i])
            else:
                continue
            time.sleep(5)
