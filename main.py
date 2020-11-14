#Sends emails from gmail
#By Abhishek Shahane at 11:39PM
#REQUIRED: YOUR EMAIL HAS TO HAVE LESS SECURE APPS ENABLED FOR THIS TO WORK AND IT HAS TO BE A GMAIL ACCOUNT
#Find the link for toggling that here: https://myaccount.google.com/lesssecureapps
#pip install selenium for this to work
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from getpass import getpass
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
web = webdriver.Chrome('./chromedriver.exe', chrome_options = chrome_options)
get_1 = input("Enter your email: ")
get_2 = getpass()
#Was going to use the gmail api, but found a workaround
web.get('https://www.gmail.com')
web.implicitly_wait(20)
email = web.find_element_by_css_selector("#identifierId")
email.click()
email.send_keys("{}".format(get_1))
submit = web.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
submit.click()
web.implicitly_wait(20)
#Making the page has loaded before we continue
password3 = web.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
password3.click()
password3.send_keys('{}'.format(get_2))
finalbutton = web.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
finalbutton.click()
web.implicitly_wait(20) #gives an implicit wait for 20 seconds
compose = web.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
compose.click()
#Enter recipients here, separated by multiple lines
recipients = """

"""
#TODO: Subject
subject="""

"""
#TODO: message
message="""

"""
web.implicitly_wait(20)
f = web.find_element_by_name("to")
f.send_keys("{}".format(recipients))
web.implicitly_wait(4)
j = web.find_element_by_name("subjectbox")
j.send_keys("{}".format(subject))
web.implicitly_wait(4)
#Ids are dynamically generated and hence they can change(ie: we can't get a definite id)
u = web.find_element_by_xpath("//*[@class='Am Al editable LW-avf tS-tW']") 
u.send_keys("{}".format(message))
web.implicitly_wait(4)
p = web.find_element_by_xpath("//*[@class='Am Al editable LW-avf tS-tW']") 
p.send_keys(Keys.CONTROL, Keys.ENTER)
#Prevent sys path is none error
sleep(9)
web.quit()
print("MESSAGE SENT!")
sleep(6)
print("Quitting",end="")
for j in range(10):
    print(".",end="")
    sleep(1)
#All done! Everything ran sucessfully.
print()
