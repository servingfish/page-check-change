import os

url = []


def newurl():
    os.system('cls')
    print("New URL Screen\nHere are the current URLs")
    for i in range(len(url)):
        print(str(i + 1) + ". " + url[i])
    inputurl = input("Enter a new URL: ")
    url.append(inputurl)
