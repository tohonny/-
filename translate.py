import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random as r
 
vk_group = ('187556970','71fa6a50dd64673ca6fa833bedaa62d73fc76fa627615a20e1f1a046f4270bf27706d28b07aadaa9fce25')
YaTrans_api_key ='trnsl.1.1.20191015T124414Z.d5eba00fc9a975a3.3e23c9466d0f149ae3972f4ebb85d17abde6864f'
 
vk = vk_api.VkApi(token = vk_group[1])
longpoll = VkBotLongPoll(vk,vk_group[0])
 
def Translate(text, lang):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key='+YaTrans_api_key+'&lang='+lang+'&text='+str(text)
    result = requests.post(url).json()
    return result
 
for event in longpoll.listen():
    msg = {}
    if event.type == VkBotEventType.MESSAGE_NEW:
        msg['text'] = event.obj.text 
        msg['user'] = str(event.obj.from_id)
        randomnum = r.randint(-2147483648,2147483647)
 
        try:
            answer = Translate(msg['text'], lang = 'ru')
           
            if answer['text'][0].lower() == msg['text'].lower():
                answer = Translate(msg['text'],lang='en')
                
 
            vk.method('messages.send', {'user_id': msg['user'],'random_id':randomnum ,'message': answer['text'][0]})
        except Exception as e:
            vk.method('messages.send', {'user_id': msg['user'],'random_id':randomnum ,'message': 'Houston, we have some problems...'}) 