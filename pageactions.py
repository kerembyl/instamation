from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import functionparameters_defh as FP
import sqlite3

#PROXY = "62.91.90.130:8080"
#webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
#    "httpProxy": PROXY,
#    "ftpProxy": PROXY,
#    "sslProxy": PROXY,
#    "proxyType": "MANUAL",
#}

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
#browser = webdriver.Firefox(firefox_options=fireFoxOptions)
browser = webdriver.Firefox()

class LoginPageActions():
    @staticmethod
    def enterUsername(my_username):
        username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        username.clear()
        username.send_keys(my_username)
    @staticmethod
    def enterPassword(my_password):
        password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        password.clear()
        password.send_keys(my_password)
    @staticmethod
    def clickLoginButton():
        login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        login_button.click()

class PostPageActions():
    @staticmethod
    def writeComment(commentList):
        try:
            locate_comment_textbox = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
            locate_comment_textbox.clear()
            randomComment = random.choice(commentList)
            locate_comment_textbox.send_keys(randomComment + Keys.ENTER)
        except:
            print('Uyarı: Yorum atma işlemi tekrar deneniyor...')
            locate_comment_textbox = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
            locate_comment_textbox.clear()
            randomComment = random.choice(commentList)
            locate_comment_textbox.send_keys(randomComment + Keys.ENTER)
            print('Yorum eklendi:', randomComment)
    @staticmethod
    def locateLikeStatus():
        locate_like_status = browser.find_element_by_css_selector("#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg")
        like_status = locate_like_status.get_attribute('aria-label')
        return like_status
    @staticmethod
    def clickLikeButton():
        locate_like_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
        locate_like_button.click()
        print ('Post begenildi!')
    @staticmethod
    def clickFollowButton():
        locate_follow_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[2]/button")
        locate_follow_button.click()
        print('Kullanici takip edildi')
    @staticmethod
    def getPostOwner():
        locate_post_beholderid = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a")
        post_beholderid = locate_post_beholderid.get_attribute('href')
        return post_beholderid
        

class TagPageActions():
    @staticmethod
    def goToPost(post_loc_sub1=int, post_loc_sub2=int):
        locate_post_permalink = browser.find_element_by_xpath(f"/html/body/div[1]/section/main/article/div[2]/div/div[{str(post_loc_sub2)}]/div[{str(post_loc_sub1)}]/a")
        post_permalink = locate_post_permalink.get_attribute('href')
        print('=====================================')
        print(f'{post_permalink} Adresine gidiliyor...')
        browser.get(post_permalink)

class UserPageActions():
    @staticmethod
    def getFollowerCount():
        locate_user_followers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span")
        follower_count = locate_user_followers.get_attribute('innerHTML')
        conn = sqlite3.connect('instadb.sqlite')
        cur = conn.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            count INTEGER,
            date TEXT
        )''')

        cur.execute('''
        INSERT INTO Users (count, date) VALUES (?, datetime('now', 'localtime'))''', (follower_count, )
        )

        conn.commit()
        print(f'Mevcut takipçi sayısı {follower_count} olup, deger veritabanına işlenmiştir.')
