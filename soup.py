import mechanicalsoup
import pytesseract
import urllib

url = "https://stdportal.emu.edu.tr/"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

browser.launch_browser()
