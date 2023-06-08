from selenium.webdriver.common.by import By
from msedge.selenium_tools import Edge
from msedge.selenium_tools import EdgeOptions
import time
import warnings

"""
# Documentation 5th of November 2022.
# Program written by TKO 5th of November 2022 (Last updated 17th of November 2022)
# This program automates the Microsoft Rewards System by searching the web automagically
# Run this program once a day to guarantee 90+12 Points daily if Level 2 (30+3 if Level 1)
# Program requires installation of Selenium version 4.x.x (Install using pip)
# Program also requires installation of the Edge web driver (Chromium version)
# This web driver must be placed in the same file path as the .py file
# Disclaimer: If banned for using my program I humbly apologize (Just kidding bozo)
"""

r"""
Unused code:
# optionsformobile.add_extension(r"C:\Users\TamirOladejo\AppData\Local\Microsoft\Edge\User 
# Data\Default\Extensions\kfhpbcjoekokcapipficfgjadanhfmjb\1.2.0_0.crx")
# capabilities = DesiredCapabilities.EDGE
# driver = Edge(executable_path=r"C:\Users\TamirOladejo\IdeaProjects\AutoEdge Searches\msedgedriver.exe")
# optionsfordesktop.headless = True
# optionsfordesktop.add_argument("--headless")
# optionsfordesktop.add_argument("window-size=1400,600")
"""

print(r"Starting program please be patient...")

warnings.filterwarnings("ignore", category=DeprecationWarning)

optionsfordesktop = EdgeOptions()
optionsfordesktop.use_chromium = True
driver = Edge(options=optionsfordesktop)

print("AutoEdge for desktop is running...")

for i in range(40):
    driver.get('https://bing.com')
    time.sleep(0.4)
    if i == 0:
        time.sleep(5)
    if i < 10:
        element = driver.find_element(By.ID, 'sb_form_q')
        element.send_keys(f'Superbowl 200{i}')
        print(f"Currently doing search {i+1}")
        element.submit()
        if i == 0:
            time.sleep(2)
        else:
            time.sleep(0.7)
    else:
        element = driver.find_element(By.ID, 'sb_form_q')
        element.send_keys(f'Superbowl 20{i}')
        print(f"Currently doing search {i+1}")
        element.submit()
        time.sleep(0.7)

print("AutoEdge searches on desktop completed successfully!")
time.sleep(2)
print("Please wait for AutoEdge for desktop to shut down properly...")
driver.quit()

optionsformobile = EdgeOptions()
optionsformobile.use_chromium = True
optionsformobile.binary_location = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
optionsformobile.add_argument(r"--user-data-dir=C:\Users\$YourUser$\AppData\Local\Microsoft\Edge\User Data1") # User Data1 is completely an optional name for the file
driverpath = 'msedgedriver.exe'
driver = Edge(options=optionsformobile)

print("AutoEdge for mobile is running...")

for i in range(30):
    driver.get('https://bing.com')
    if i < 10:
        element = driver.find_element(By.ID, 'sb_form_q')
        element.send_keys(f'NBA Draft 200{i}')
        print(f"Currently doing search {i+1}")
        element.submit()
        if i == 0:
            time.sleep(2)
        else:
            time.sleep(0.7)
    else:
        element = driver.find_element(By.ID, 'sb_form_q')
        element.send_keys(f'NBA Draft 20{i}')
        print(f"Currently doing search {i+1}")
        element.submit()
        time.sleep(0.7)


print("AutoEdge searches on mobile completed successfully!")
time.sleep(2)
print("Please wait for AutoEdge for mobile to shut down properly...")
driver.quit()
