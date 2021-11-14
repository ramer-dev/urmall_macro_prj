from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time, datetime
import json


class Macro:
    def __init__(self):
        # self.driver = Chrome()
        # self.driver.implicitly_wait(3)
        self.day = time.strftime('%d', time.localtime(time.time()))
        with open('settings.json', "r", encoding='utf-8') as f:
            self.settings = json.load(f)
            self.members = self.settings['members']
            self.update = self.settings['update']


    def siteDB(self, site):
        if site == '관제통신소':
            return '44'
        elif site == '항공통신소':
            return '45'
        elif site == '종합통신소':
            return '46'

    def MemberDB(self, site, team):
        return self.members[site][team]

    def SetTime(self):
        self.day = time.strftime('%d', time.localtime(time.time()))

    def readSettings(self):
        with open('settings.json', "r", encoding='utf-8') as f:
            self.settings = json.load(f)
        print(self.settings)

    def InputAll(self, daynight, site, name):
        self.SetTime()

        if daynight == 'D':
            daynight = '주간'
        elif daynight == 'N':
            daynight = '야간'
        self.driver.get('http://urmall.iptime.org/bbs/board.php?bo_table=calendar_1')
        link = self.driver.find_elements(By.PARTIAL_LINK_TEXT, daynight)

        self.driver.get(link[int(self.day) - 1].get_attribute('href'))

        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CLASS_NAME, 'ca_incheon').click()

        self.driver.find_element(By.NAME, 'input_val_' + site + '_0').clear()
        self.driver.find_element(By.NAME, 'input_val_' + site + '_1').clear()
        self.driver.find_element(By.NAME, 'input_val_' + site + '_3').clear()

        self.driver.find_element(By.NAME, 'input_val_' + site + '_0').send_keys(name)
        self.driver.find_element(By.NAME, 'input_val_' + site + '_1').send_keys('1')
        self.driver.find_element(By.NAME, 'input_val_' + site + '_3').send_keys('특이사항 없음')
        self.driver.find_element(By.NAME, 'input_val_' + site + '_ck').click()
        self.driver.find_element(By.ID, 'btn_submit').click()

    def InputOnlyStatus(self, daynight, site):
        if daynight == 'D':
            daynight = '주간'
        elif daynight == 'N':
            daynight = '야간'
        self.driver.get('http://urmall.iptime.org/bbs/board.php?bo_table=calendar_1')
        link = self.driver.find_elements(By.PARTIAL_LINK_TEXT, daynight)

        self.driver.get(link[int(self.day) - 1].get_attribute('href'))

        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CLASS_NAME, 'ca_incheon').click()

        self.driver.find_element(By.NAME, 'input_val_' + site + '_3').clear()
        self.driver.find_element(By.NAME, 'input_val_' + site + '_3').send_keys('특이사항 없음')
        self.driver.find_element(By.NAME, 'input_val_' + site + '_ck').click()
        self.driver.find_element(By.ID, 'btn_submit').click()

    def InputOnlyMember(self, daynight, site, name):
        if daynight == 'D':
            daynight = '주간'
        elif daynight == 'N':
            daynight = '야간'
        self.driver.get('http://urmall.iptime.org/bbs/board.php?bo_table=calendar_1')
        link = self.driver.find_elements(By.PARTIAL_LINK_TEXT, daynight)

        self.driver.get(link[int(self.day) - 1].get_attribute('href'))

        self.driver.implicitly_wait(1)
        self.driver.find_element(By.CLASS_NAME, 'ca_incheon').click()

        self.driver.find_element(By.NAME, 'input_val_' + site + '_0').clear()
        self.driver.find_element(By.NAME, 'input_val_' + site + '_1').clear()

        self.driver.find_element(By.NAME, 'input_val_' + site + '_0').send_keys(name)
        self.driver.find_element(By.NAME, 'input_val_' + site + '_1').send_keys('1')
        self.driver.find_element(By.NAME, 'input_val_' + site + '_ck').click()
        self.driver.find_element(By.ID, 'btn_submit').click()

    def TeamMacro(self, daynight):
        self.SetTime()
        self.InputAll(daynight, self.siteDB('관제통신소'))
        self.InputAll(daynight, self.siteDB('항공통신소'))
        self.InputAll(daynight, self.siteDB('종합통신소'))

    def getTeam(self):
        self.SetTime()




test = Macro()
print(test.MemberDB('관제통신소','B'))
print(test.readSettings())

day = time.strftime('20%y,%m,%d', time.localtime(time.time()))
[year, month, day] = day.split(',')
[year, month, day] = [int(year), int(month), int(day)]





