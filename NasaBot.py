from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import win32con
import win32gui
import win32api
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")  


class NasaIOTDBot():
	def __init__(self):
		self.driver = webdriver.Chrome("YourPathToChromedriver.exe", options = chrome_options)
		self.img_path = "PathToYourBackgroundImage.jpg"

	def GetImage(self):
		self.driver.get("https://www.nasa.gov/multimedia/imagegallery/iotd.html")
		img = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[2]/div[2]/div[3]/section/section/div[2]/div/div/div/div[1]/div[1]/div/a/div/img")))
		img.click()
		images = self.driver.find_elements_by_tag_name('img')[0]
		source = images.get_attribute("src")
		daily_img = urllib.request.urlretrieve(source, self.img_path)

	def wallpaper(self):
	    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
	    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "0")
	    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
	    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.img_path, 1+2)

bot = NasaIOTDBot()
bot.GetImage()
bot.driver.quit()
bot.wallpaper()
