# import mechanicalsoup
# import pytesseract
# import urllib
import os
import scripts


cont = True
while cont:
    os.system('cls')
    print("Welcome to website change checker by servingfish!\n[1]Enter a new URL\n[2]Start tracking!\n[0]Exit")
    selec = input("Enter a selection: ")

    if selec == "1":
        scripts.newurl()
    elif selec == "2":
        scripts.track()
    elif selec == "0":
        cont = False


# browser = mechanicalsoup.StatefulBrowser()
# browser.open(url)
#
# browser.launch_browser()
