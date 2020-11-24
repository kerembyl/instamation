import time
import pageactions as PA
import functionparameters_defh as FP
import random

#Login
PA.browser.get('https://www.instagram.com')
if 'Instagram' in PA.browser.title:
    print ('Site basligi dogru gorunuyor, devam edelim...')
time.sleep(4)
print ('Kullanıcı adı giriliyor...')
PA.LoginPageActions.enterUsername(FP.myusername)
print ('Sifre giriliyor...')
PA.LoginPageActions.enterPassword(FP.mypassword)
PA.LoginPageActions.clickLoginButton()
time.sleep(4)
print ('Giris yapildi!')
time.sleep(4)

#Gather follower count from profile page
PA.browser.get(f'https://www.instagram.com/{FP.myusername}')
PA.UserPageActions.getFollowerCount()

#Like By Tags
while True:
    for tag in FP.tagList:
        tagurl = f"https://www.instagram.com/tags/{tag}"
        PA.browser.get(tagurl)
        print('Bilgi:', tagurl, 'Adresine gidilerek ', tag, 'etiketindeki postlar gosteriliyor')

        for post_loc_sub1 in range (1, 4):
            for post_loc_sub2 in range (1, 4):
                time.sleep(6)
                PA.TagPageActions.goToPost(post_loc_sub1, post_loc_sub2)

                try:
                    postowner = PA.PostPageActions.getPostOwner()
                    print('Bilgi: Post sahibi -> ', postowner)             
                except:
                    print('Uyarı: Post sahibi tespit edilemedi, geri dönüp başka bir post deniyorum...')
                    PA.browser.get(tagurl)
                    time.sleep(6)

                if PA.PostPageActions.locateLikeStatus() == "Like":
                    if random.randint(0, 100) < FP.likePercent:
                        PA.PostPageActions.clickLikeButton()
                        PA.PostPageActions.clickFollowButton()
                        time.sleep(6)
                        if FP.commentAdd==True:
                            try:
                                PA.PostPageActions.writeComment(FP.commentList)
                                time.sleep(6)
                            except:
                                print('Uyarı: Post yorumlara kapalı, geri gidiyorum.')   
                                PA.browser.get(tagurl)                     
                        else: pass
                    else:
                        print('Bilgi: Bu postu pas geçiyorum.')
                elif PA.PostPageActions.locateLikeStatus() == "Unlike":
                    print('Bilgi: Post zaten begenilmis, bunu atliyorum.')
                PA.browser.get(tagurl)
                time.sleep(6)
        print('Bilgi: Bir sonraki tage gitmek icin 30 dakika bekliyorum.')
        time.sleep(1100)

