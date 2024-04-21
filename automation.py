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




