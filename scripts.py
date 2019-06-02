import os
import urllib.request

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


def track():
    os.system('cls')
    if len(url) == "0":
        print("There is no URL to track! Go back and add more.")
        return
    get_contents()  # Get current contents of URLs
    cont = True
    while cont:
        print("Now tracking the URLs. They will be checked every 5 seconds.\n")
        for i in range(len(url)):
            compare_contents()
            print(str(i + 1) + ". " + name[i] + status[i])


def get_contents():
    for i in range(len(url)):
        print(url)
        print(name)
        print(i)
        current_cont[i] = urllib.request.urlopen(url[i]).read()


def compare_contents():
    # Get new contents
    for i in range(len(url)):
        # TODO Fix the damn IndexError list assignment index out of range
        new_cont[i] = urllib.request.urlopen(url[i]).read()

    # Compare them and return status
    for i in range(len(url)):
        if current_cont[i] == new_cont[i]:
            status[i] = "No change!"
        else:
            status[i] = "Changed!"
