from selenium import webdriver
from time import sleep
from sys import argv
import random

nycDistricts = open('nycDistricts.txt', 'w+')
nycNeighbourhoods = open('nycNeighbourhoods.txt', 'w+')

profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference('useAutomationExtension', False)
profile.set_preference('privacy.trackingprotection.enabled', True)
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)
profile.update_preferences()
driver = webdriver.Firefox(profile)
driver.implicitly_wait(20)

driver.get("https://communityprofiles.planning.nyc.gov/")
driver.find_element_by_css_selector('.ember-power-select-placeholder').click()
districtClass = driver.find_elements_by_css_selector('.district')
neighbourhoodClass = driver.find_elements_by_css_selector('.neighborhoods')

for district in districtClass:
    nycDistricts.write(district.text + '\n')

for neighbourhood in neighbourhoodClass:
    nycNeighbourhoods.write(neighbourhood.text + '\n')

nycDistricts.close()
nycNeighbourhoods.close()
driver.quit()
