import telegram
# my_token  chinh la cai api ma bot_father dua
my_token = "5967111725:AAEssCocj62KYx4ocOEf5cyEhH8GMOVI6lY"
#tao bot
bot = telegram.Bot(token=my_token)

# gui tin nhan tu bot qua nguoi dung
bot.sendMessage(chat_id="5172036139",text="Ban muon giup gi ko ? ^pycharm^")

# #gui tin nhan img tu Bot qua nguoi dung
# bot.sendPhoto(chat_id="5172036139",photo = open("E:\\backup\\pyhon_anacodan\\Bai_tap\\anh\\1.png","rb"),caption = "chup man hinh")
