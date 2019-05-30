import mechanicalsoup
import pytesseract
import urllib

url = "https://stdportal.emu.edu.tr/"
ogr_no = "17330172"
passw = "2200270911"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

browser.select_form()
# browser.get_current_form().print_summary()

browser["txtOgR_no"] = ogr_no
browser["txtPassword"] = passw

browser.download_link("image.aspx")

browser.launch_browser()
