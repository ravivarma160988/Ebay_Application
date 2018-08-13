from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import yaml,time

class Testcase001():

    def __init__(self):
        logger.info("Testcase Initialization section")
        robot_env = BuiltIn()
        self.userName = robot_env.get_variable_value("${Testcase001.Username}")
        self.password = robot_env.get_variable_value("${Testcase001.Password}")
        self.electronics = '//*[@id="container"]/div/header/div[3]/ul/li[1]/span'
        #self.electronics1 = '//*[@id="container"]/div/header/div[3]/ul/li[1]/span/svg'
        self.mi = '//*[@id="container"]/div/header/div[3]/ul/li[1]/ul/li/ul/li[1]/ul/li[2]/a '
        self.close = '/html/body/div[2]/div/div/button'
        pass

    def setup(self):
        logger.info("Testcase setup section")
        logger.info("Username : {0}".format(self.userName))
        logger.info("Password : {0}".format(self.password))
        driver = webdriver.Chrome()
        driver.get("https://www.flipkart.com/")
        driver.maximize_window()
        time.sleep(5)
        self.close_elem = driver.find_element_by_xpath(self.close)
        self.close_elem.click()
        time.sleep(5)
        element_to_hover_over = driver.find_element_by_xpath(self.electronics)
        hover = ActionChains(driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(2)
        element_to_click = driver.find_element_by_xpath(self.mi)
        element_to_click.click()
        time.sleep(10)
        pass

    def test(self):
        pass

    def cleanup(self):
        pass