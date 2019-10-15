import requests
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType 
import random as r

vk_group = ('187626512','0de088ef455298040fa4f614469e8c41eeb9515d66f4220615ccf25ae35f2bf956ce140d045a4d6537024')
YaTrans_api_key ='trnsl.1.1.20191015T072253Z.770b09345199f98a.c6e3fd98c616b90c1308dc419fa21f392970ed6b'

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