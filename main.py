from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

limit = int(input("Enter Crawl Limit: "))
findomain = input("Enter Starting URL ")
enddomain = input("Enter Root Domain ")
enddomain = 'https://www.'+enddomain

Options = Options()
Options.headless = True
driver = webdriver.Firefox(options=Options)
driver.get(findomain)

elems = driver.find_elements_by_xpath("//a[@href]")
for elem in elems:
    i = 1
    while(i<=limit):
        elemst = driver.find_elements_by_xpath("//a[@href]")
        for elemt in elemst:
            if enddomain in elemt.get_attribute("href"):
                print(elemt.get_attribute("href"))
        i+=1