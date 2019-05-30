# import mechanicalsoup
# import pytesseract
# import urllib
import os
import scripts

cont = True
while cont:
    os.system('cls')
    print("Welcome to website change checker by servingfish!\n[1]Enter a new URL")
    selec = input("Enter a selection: ")

    if selec == "1":
        scripts.newurl()

# browser = mechanicalsoup.StatefulBrowser()
# browser.open(url)
#
# browser.launch_browser()
