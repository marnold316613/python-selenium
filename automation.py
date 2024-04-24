from selenium import webdriver
from selenium.webdriver.edge.service import Service


service = Service()

options = webdriver.EdgeOptions()

options.add_argument('--no-first-run')
options.add_argument('--no-default-browser-check')
options.add_argument('--disable-extensions')
options.add_argument('--disable-profile-management') 
options.add_argument("--enable-chrome-browser-cloud-management")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

edge_browser = webdriver.Edge(service=service,options=options)

edge_browser.get("www.google.com")

print("hello world")

# this still doesn't work, need to trouble shoot drivers and get the rigth versions

# no changes to commit for today

# no changes to commit for today




