import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox()


def login_action(my_username, my_password):
    browser.get('https://www.instagram.com')

    if 'Instagram' in browser.title:
        print ('Site basligi dogru gorunuyor, devam edelim...')

    time.sleep(2)
    print ('Kullanıcı adı giriliyor...')
    username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    username.clear()
    username.send_keys(my_username)

    print ('Sifre giriliyor...')
    password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    password.clear()
    password.send_keys(my_password)

    login_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
    login_button.click()
    print ('Giris yapildi!')

    pass

def like_by_tags(tagList, commentList, likePercent, commentAdd):
    
    time.sleep(2)
    for tag in tagList:
        tagurl = 'https://www.instagram.com/tags/' + tag
        browser.get(tagurl)
        time.sleep(2)
        print(tagurl, 'Adresine gidilerek ', tag, 'etiketindeki postlar gosteriliyor')
        tagurl = "clear"

        for post_loc_sub1 in range(1, 4):
            for post_loc_sub2 in range (1, 4):
                locate_post_permalink = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div["
                                 + str(post_loc_sub2) + "]/div[" + str(post_loc_sub1) + "]/a")
                post_permalink = locate_post_permalink.get_attribute('href')
                print(post_permalink, 'Adresine gidiliyor...')
                browser.get(post_permalink)

                locate_post_beholderid = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div[1]/span/a")
                post_beholderid = locate_post_beholderid.get_attribute('href')
                print('Post sahibi: ', post_beholderid)

                time.sleep(2)
                locate_like_status = browser.find_element_by_css_selector("#react-root > section > main > div > div.ltEKP > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg")
                get_like_status = locate_like_status.get_attribute('aria-label')
                
                if get_like_status == "Like":

                    if random.randint(0, 100) < likePercent:
                        locate_like_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                        locate_like_button.click()
                        print ('Post begenildi!')

                        if commentAdd==True:

                            try:
                                locate_comment_textbox = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                                locate_comment_textbox.clear()
                                randomComment = random.choice(commentList)
                                locate_comment_textbox.send_keys(randomComment + Keys.ENTER)  #Write some stuff from commentList and hit enter
                                print ("Post'a yorum eklendi: ", randomComment)
                                time.sleep(2)
                            except:
                                print('textarea bulunamadı, tekrar deniyorum')
                                locate_comment_textbox = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea")
                                locate_comment_textbox.clear()
                                randomComment = random.choice(commentList)
                                locate_comment_textbox.send_keys(randomComment + Keys.ENTER)  #Write some stuff from commentList and hit enter
                                print ("Post'a yorum eklendi: ", randomComment)
                                time.sleep(2)
                            
                        else: pass
                        
                    else:
                        print('Bu postu pas geçiyorum.')

                elif get_like_status == "Unlike":
                    print('Post zaten begenilmis, bunu atliyorum.')

                browser.back()
                post_permalink = "clear"
                time.sleep(2)
