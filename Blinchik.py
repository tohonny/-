import vk_api
import random
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType

TOKEN = "b24e5b10bb881b1eb586d1b193544ab6d03bbdde8a2b3bb9333601196ae97fe2be2e191f443f58691c2a9"
vk_session = vk_api.VkApi(token=TOKEN)

vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session,"187554722")

tic_tac_toe = False

for event in longpoll.listen():
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.obj.text != '':
            if event.from_user:
                text = event.obj.text
                text = text.lower()
                if text == 'блинчики':
                    reply = 'Для питона'
                elif text == 'кабачок':
                    reply = 'Это наш всеми любимый котик'
                elif text == 'меня интересует':
                    reply = 'Варианты: "Блинчики", "Кабачок", "Драма", "Фантастика", "Спорт", (любой цвет), (камень, ножницы, бумага), "крестики-нолики" "Обед", "Анекдот"'
                elif text == 'фантастический фильм' or text == 'фантастика':
                    reply = random.choice(['Гарри Поттер','Мстители','Аватар','Назад в будущее','Пятый элемент'])
                elif text == 'мелодрама' or text == 'драма':
                    reply = 'Настоящая мелодрама лишь одна - "Хатико"'
                elif text == 'спорт':
                    reply = random.choice(['Попробуйте сыграть в футбол','Ни разу не играли в хоккей?','Получали мячом по лицу во время игры в волейбол?','Лично я плохо играю в шахматы','Баскетбол - не моё, так как я лишь кусочек кода, но, может, у тебя получится'])
                elif text == 'красный' or text == 'оранжевый' or text == 'жёлтый' or text == 'зелёный' or text == 'голубой' or text == 'синий' or text == 'фиолетовый' or text == 'чёрный' or text == 'белый' or text == 'розовый' or text == 'коричневый':
                    reply = random.choice(['И красный','И оранжевый','И жёлтый','И зелёный','И голубой','И синий','И фиолетовый','И чёрный','И белый','И коричневый','И розовый'])
                elif text == 'камень' or text == 'ножницы' or text == 'бумага':
                    reply = random.choice(['камень','ножницы','бумага'])
                    if text == reply:
                        reply = reply + '. Ничья'
                    elif (text == 'камень' and reply == 'бумага') or (text == 'ножницы' and reply == 'камень') or (text == 'бумага' and reply == 'ножницы'):
                        reply = reply + '. Вы проиграли'
                    else: reply = reply + '. Вы выиграли'
                elif text == 'обед':
                    reply = 'Почему-то без омлета'
                elif text == 'анекдот':
                    reply = random.choice(['Будьте, как хороший парфюм. Привлекайте внимание без шума','- Я вчера целый вечер смотрел телевизор \n- А я - холодильник','Спящий ребенок - это не только мило, но и наконец-то','- Не в деньгах счастье, но если другого нет - берите деньгами...','Каждому может быть послан знак свыше, и хорошо если этот знак не кирпич','Терапевт - это 1024 гигапевта...','Завел в квартире кота. Теперь это его квартира','Ну просто грех открыть йогурт и не облизать фольгу!'])
                elif text == 'привет' or text == 'здравствуй' or text == 'ку' or text == 'хай':
                    reply = 'Приветствуем вас в блинчиках для питона! \nЧто вас интересует?'
                elif text == 'крестики-нолики':
                    tic_tac_toe=['_','_','_','_','_','_','_','_','_']
                    flag = True
                    reply = 'Начинаем игру \n', tic_tac_toe[0], ' ', tic_tac_toe[1], ' ', tic_tac_toe[2], '\n', tic_tac_toe[3], ' ', tic_tac_toe[4], ' ', tic_tac_toe[5], '\n', tic_tac_toe[6], ' ', tic_tac_toe[7], ' ', tic_tac_toe[8], '\nВы ходите первым. Чтобы поставить "X", напишите цифру, соответствующую клетке'
                elif (text != '1' and text != '2' and text != '3' and text != '4' and text != '5' and text != '6' and text != '7' and text != '8' and text != '9') or tic_tac_toe == False:
                    reply = 'Ничего не понял'
                if (text == '1' or text == '2' or text == '3' or text == '4' or text == '5' or text == '6' or text == '7' or text == '8' or text == '9') and tic_tac_toe != False:
                    flag = True
                    if text == '1' and tic_tac_toe != False and tic_tac_toe[0] == '_': tic_tac_toe[0] = 'x'
                    elif text == '2' and tic_tac_toe != False and tic_tac_toe[1] == '_': tic_tac_toe[1] = 'x'
                    elif text == '3' and tic_tac_toe != False and tic_tac_toe[2] == '_': tic_tac_toe[2] = 'x'
                    elif text == '4' and tic_tac_toe != False and tic_tac_toe[3] == '_': tic_tac_toe[3] = 'x'
                    elif text == '5' and tic_tac_toe != False and tic_tac_toe[4] == '_': tic_tac_toe[4] = 'x'
                    elif text == '6' and tic_tac_toe != False and tic_tac_toe[5] == '_': tic_tac_toe[5] = 'x'
                    elif text == '7' and tic_tac_toe != False and tic_tac_toe[6] == '_': tic_tac_toe[6] = 'x'
                    elif text == '8' and tic_tac_toe != False and tic_tac_toe[7] == '_': tic_tac_toe[7] = 'x'
                    elif text == '9' and tic_tac_toe != False and tic_tac_toe[8] == '_': tic_tac_toe[8] = 'x'
                    else: flag = False
                    if flag == True:
                        rand = -1
                        if tic_tac_toe[0] == '_' or tic_tac_toe[1] == '_' or tic_tac_toe[2] == '_' or tic_tac_toe[3] == '_' or tic_tac_toe[4] == '_' or tic_tac_toe[5] == '_' or tic_tac_toe[6] == '_' or tic_tac_toe[7] == '_' or tic_tac_toe[8] == '_':
                            while tic_tac_toe[rand] != '_':
                                rand = random.randint(0,8)
                            tic_tac_toe[rand] = 'o'
                        reply = '', tic_tac_toe[0], ' ', tic_tac_toe[1], ' ', tic_tac_toe[2], '\n', tic_tac_toe[3], ' ', tic_tac_toe[4], ' ', tic_tac_toe[5], '\n', tic_tac_toe[6], ' ', tic_tac_toe[7], ' ', tic_tac_toe[8], ''
                        if (((tic_tac_toe[0] == tic_tac_toe[1] == tic_tac_toe[2] == 'x') or (tic_tac_toe[0] == tic_tac_toe[1] == tic_tac_toe[2] == 'o') or
                            (tic_tac_toe[3] == tic_tac_toe[4] == tic_tac_toe[5] == 'x') or (tic_tac_toe[3] == tic_tac_toe[4] == tic_tac_toe[5] == 'o') or
                            (tic_tac_toe[6] == tic_tac_toe[7] == tic_tac_toe[8] == 'x') or (tic_tac_toe[6] == tic_tac_toe[7] == tic_tac_toe[8] == 'o') or
                            (tic_tac_toe[0] == tic_tac_toe[3] == tic_tac_toe[6] == 'x') or (tic_tac_toe[0] == tic_tac_toe[3] == tic_tac_toe[6] == 'o') or
                            (tic_tac_toe[1] == tic_tac_toe[4] == tic_tac_toe[7] == 'x') or (tic_tac_toe[1] == tic_tac_toe[4] == tic_tac_toe[7] == 'o') or
                            (tic_tac_toe[2] == tic_tac_toe[5] == tic_tac_toe[8] == 'x') or (tic_tac_toe[2] == tic_tac_toe[5] == tic_tac_toe[8] == 'o') or
                            (tic_tac_toe[0] == tic_tac_toe[4] == tic_tac_toe[8] == 'x') or (tic_tac_toe[0] == tic_tac_toe[4] == tic_tac_toe[8] == 'o') or
                            (tic_tac_toe[2] == tic_tac_toe[4] == tic_tac_toe[6] == 'x') or (tic_tac_toe[2] == tic_tac_toe[4] == tic_tac_toe[6] == 'o')) or
                            (tic_tac_toe[0] != '_' and tic_tac_toe[1] != '_' and tic_tac_toe[2] != '_' and tic_tac_toe[3] != '_' and tic_tac_toe[4] != '_' and tic_tac_toe[5] != '_' and tic_tac_toe[6] != '_' and tic_tac_toe[7] != '_' and tic_tac_toe[8] != '_')):
                            reply = '', tic_tac_toe[0], ' ', tic_tac_toe[1], ' ', tic_tac_toe[2], '\n', tic_tac_toe[3], ' ', tic_tac_toe[4], ' ', tic_tac_toe[5], '\n', tic_tac_toe[6], ' ', tic_tac_toe[7], ' ', tic_tac_toe[8], '\nИгра закончена'
                            tic_tac_toe = False
                    else: reply = 'Там уже стоит знак, выберите другую клетку'
                vk.messages.send(
                    user_id=event.obj.from_id,
                    random_id=get_random_id(),
                    message=reply)