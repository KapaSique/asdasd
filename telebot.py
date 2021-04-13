import telebot
import datetime
from datetime import datetime, date, time
from telebot import types

bot = telebot.TeleBot('1713006046:AAFlbNuIwIZnkRCcyyREv58sqeDyT94xI0U')

date = datetime.isoweekday()

@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("11 класс")
    item2 = types.KeyboardButton("10 класс")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Здравствуйте!\nЯ - бот, рассылающий расписание\nПожалуйста, укажите свой класс",  reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '11 класс':

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Физмат", callback_data='fm11')
        item2 = types.InlineKeyboardButton("Инж", callback_data='eng11')
        item3 = types.InlineKeyboardButton("Тех", callback_data='tech11')
        item4 = types.InlineKeyboardButton("Политех", callback_data='ptch11')
        item5 = types.InlineKeyboardButton("Биохим", callback_data='bch11')
        item6 = types.InlineKeyboardButton("Гум", callback_data='hum11')

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Какой ваш профиль?', reply_markup=markup)
    elif message.text.lower() == '10 класс':

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Физмат", callback_data='fm10')
        item2 = types.InlineKeyboardButton("Инж", callback_data='eng10')
        item3 = types.InlineKeyboardButton("Тех", callback_data='tech10')
        item4 = types.InlineKeyboardButton("Политех", callback_data='ptch10')
        item5 = types.InlineKeyboardButton("Биохим", callback_data='bch10')
        item6 = types.InlineKeyboardButton("Гум", callback_data='hum10')

        markup.add(item1, item2, item3, item4, item5, item6)

        bot.send_message(message.chat.id, 'Какой ваш профиль?', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'fm11':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Русский язык ВМГ / с.к. Русский язык ВМГ\nЛитература ФИС\nФизкультура ВЕЕ РНР\n\nФизика ПВФ')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Информатика УМИ (2 эт)\nОбществознание САА\nАнглийский ПТВ(ПВА2)\n\nМатематика КИГ')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Математика КИГ\nМатан ШИИ / Биология ЯИВ\nГеография ЗНИ /\n\nс.к. Математика КИГ |')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Физкультура ВЕЕ РНР / Литература ФИС\nМатан ШИИ\nФизика ПВФ\n\nЛинейная алгебра НПИ /')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Математика КИГ\nИнформатика УМИ (2 эт)\nЯкутская литература ИСИ\n\nАнглийский ПТВ (ПВА2) / ОБЖ ЯИВ')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Информатика УМИ (2 эт)\nЭкономика КЕЕ  / Ист Якутии СНА	| Теория колеб НПИ / Ист Якутии СНА\nИстория СНА')
            elif call.data == 'fm10':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Английский СРЮ\nФизика ПВФ\nМатематика КИГ\n\nФизкультура ВЕЕ РНР')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Информатика ПНН\nИнформатика ПНН (3 эт) / Физика ПВФ\nМатематика КИГ\n\nЛитература ФИС\n| Физпрактикум ПРИ в 16:20')
                if date == 3:
                    bot.send_message(call.message.chat.id, '/ Матан ШИИ\nИнформатика ПНН (2 эт) / Химия ГАА\nБиология ЯИВ / Физкультура ВЕЕ РНР')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Русский язык ВМГ / Анализ текста ВМГ\nЛитература ФИС / Линейная алгебра НПИ\nМатан ШИИ\n\nс.к. Математика КИГ | Механика ПВФ')
                if date == 5:
                    bot.send_message(call.message.chat.id, '/ История Якутии СНА\nМатематика КИГ\nФизика ПВФ\n\nЭкономика КЕЕ / | Математика для физиков ПВФ /')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Як лит ИСИ\nОБЖ ЯИВ / Английский СРЮ\nИстория ГНИ')
            elif call.data == 'eng11':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Начер геом ДАА / Информатика УМИ (2 эт)\nМатематика ПАН\nРусский язык ЗЮН / с.к. Русский язык ЗЮН\n\n / Биология МАЕ')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Химия ГАА / Физика БГВ\nИнформатика УМИ (2 эт)\nЛитература ЗЮН\n\nс.к. математика ПАН')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Информатика УМИ (2 эт)\nМатематика ПАН\nМатан ШИИ\n\nОбществознание ФЧМ')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'География ЗНИ / Физкультура ВЕЕ РНР\nЯкутская литература НИД\nИнформатика УМИ (2 эт)\n\nс.к. Информатика УМИ (2 эт) / Экономика КЕЕ')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Физкультура ВЕЕ РНР\nИстория СНА\nАнглийский ПВА / ОБЖ ЯИВ\n\nМатематика ПАН')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Физика БГВ\nИстория Якутии СНА / Литература ЗЮН\nАнглийский ПВА\n\nс.к. Информатика УМИ (2 эт) /')
            elif call.data == 'eng10':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Матан ССВ\nРусский язык ЗЮН / Анализ текста ЗЮН\nНачер геом ДАА / Информатика УМИ (2 эт)\n\nБиология МАЕ /')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Математика ПАН\nАнглийский ПТВ(ПВА2)\nОБЖ ЯИВ/ Физкультура ВЕЕ РНР\n\nФизика ЯВГ /')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Математика ПАН\nИнформатика УМИ (2 эт)\nИстория ГНИ')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Математика ПАН\nИнформатика УМИ (2 эт)\nЛитература ЗЮН\n\nАнглийский ПТВ (ПВА2)/ с.к. Информатика УМИ (2 эт) ')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'История Якутии СНА / Глоб. мир ЗНИ\nОАК и ТР ФДС / с.к. Физика НПИ\nФизкультура ВЕЕ РНР\n\nЯкутская литература НИД')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Физика ЯВГ Информатика УМИ (2 эт)\nЛитература ЗЮН\nс.к. Информатика УМИ (2 эт)/')
            elif call.data == 'tech11':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Математика ПАН\nОБЖ ЯИВ / Экономика КЕЕ\nИстория НВВ\n\nЛитература ФИС')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Английский ПВА\nМатематика ПАН\nТеор механика АГП / Информатика ДМН(3 эт)\n\nФизкультура ВЕЕ РНР / Русский язык ВМГ')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Информатика ДМН (3 эт) / Начертательная геометрия ДАА\nОбществознание ФЧМ\nФизика ТПП\n\nМатан ПАН')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Физика ТПП\nМатематика ПАН\nИстория Якутии СНА / \n\nХимия НВВ // Физика ТПП (НПИ)')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Литература ФИС / с.к. по химии НВВ\nс.к. Русский язык ВМГ\nс.к. Математика ПАН / Английский ПВА\n\nЯк лит ИСИ')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Информатика ДМН (3 эт)\nФизкультура ВЕЕ РНР\nГеография ЗНИ / Биология ЯИВ\n')
            elif call.data == 'tech10':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Физика ТПП\nИнформатика УМИ (2 эт) / Химия НВВ\nИстория Якутии СНА / Биология ЯИВ')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Физкультура ВЕЕ РНР / Астрономия НПИ\nМатематика ИЭД\nЛитература ФИС\n\nФизика ТПП')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Як лит ИСИ\nФизика ТПП / Начер геом ДАА\nМатан ИЭД')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'История ГНИ\nОБЖ ЗНИ / Литература ФИС\nРусский язык ВМГ / Анализ текста ВМГ\n\nМатан ИЭД')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Информатика УМИ (2 эт)\nАнглийский ПВА\nИнформатика УМИ (2 эт)\n\nФизкультура ВЕЕ РНР')
                if date == 6:
                    bot.send_message(call.message.chat.id, '/ Английский ПВА\nМатематика ИЭД\nГеология РЕВ /')
            elif call.data == 'ptch11':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Физика БГВ\nИнформатика ДМН(3 эт)\nЭкономика КЕЕ\n\nИстория НВВ')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Математика ССВ\nЯк лит НИД\nс.к. по химии ГАА / Начер геом ДАА\n\nИнформатика ДМН  (3 эт) // Химия ГАА')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'с.к. Русский язык ХЗП (Через ZOOM)\nАнглийский ПВА\nМатан ССВ / География ЗНИ\n\nФизика БГВ')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'ОБЖ АММ / Физкультура ВЕЕ РНР\nс.к. Математика ЕАА\nМатематика ССВ\n\nЛитература ХЗП 15:00-16:40')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Физкультура ВЕЕ РНР\nФизика БГВ / Информатика ДМН (3 эт)\nЛитература ХЗП (через ZOOM) / \n\nОбществознание НВВ')
                if date == 6:
                    bot.send_message(call.message.chat.id, '/ История Якутии СНА\nАнглийский ПВА / Биология МАЕ\nМатематика ССВ')
            elif call.data == 'ptch10':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Глоб. мир ЗНИ  / Анализ текста ХЗП (Через ZOOM)\nФизика ТПП\nМатематика ССВ\n\nЛитература ХЗП 15:00-16:40')
                if date == 2:
                    bot.send_message(call.message.chat.id, '-\nМатематика ССВ\nИстория Якутии СНА / Физкультура ВЕЕ РНР\n\nПрактикум по матем ЕАА')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Физика ТПП\nОБЖ АММ / Биология МАЕ\nАнглийский ПТВ (ПВА2)')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Як лит НИД\nИнформатика КНН (3 эт)\nФизика ТПП / Информатика КНН (3 эт)\n\nМатан ЕАА / РКДЗ ГАА')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Русский язык ХЗП / Английский ПТВ (ПВА2)\nМатематика ССВ\nФизкультура ВЕЕ РНР\n\nЛитература ХЗП (Через ZOOM)/Экономика КЕЕ')
                if date == 6:
                    bot.send_message(call.message.chat.id, '-\nИстория ГНИ\nИнформатика КНН (3 эт)')
            elif call.data == 'bch11':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'с.к. по экологии МАЕ\nМатематика ПТГ\nИнформатика ДМН(3 эт) / Химия НВВ\n\n	с.к. по биологии ЯИВ')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Обществознание НВВ\nЯк лит ИСИ\nГеография ЗНИ / ОБЖ ЯИВ\n\nФизкультура ВЕЕ РНР / История Якутии СНА')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Русский язык ФИС / с.к. Русский язык ФИС\nФизика ФЛД / с.к. по химии НВВ\nс.к. Математика ПТГ / реш слож задач по мат ПТГ\n\nБиология ЯИВ')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Английский ПТВ (Через ZOOM)\nМатематика ПТГ\nХимия НВВ\n\nЛитература ФИС')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Английский ПТВ (ПВА2) / Литература ФИС\nс.к. по химии НВВ / физика ФЛД\nМатематика ПТГ\n\nс.к. Биохимия КСС')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'История НВВ\nФизкультура ВЕЕ РНР\nБиология ЯИВ /')
            elif call.data == 'bch10':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Анализ текста ХЗП (через ZOOM) / Эколог. статистика и моделирование ЗНИ\nЭкология МАЕ / Эксперим. экология АЕА\nМатематика ПТГ\n\nПрактикум хим. осн. матер. НВВ / Информатика ДМН (3 эт)')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Физкультура ВЕЕ РНР / Биология ЯИВ\nРусский язык ФИС / Литература ФИС\nЯк лит ИСИ\n\nАнглийский ПТВ (ПВА2)')
                if date == 3:
                    bot.send_message(call.message.chat.id, '/ Основы матана ПТГ\nЛитература ФИС\nХимия НВВ')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Физика ФЛД / Химия НВВ\nИстория Якутии СНА / Английский ПТВ (ПВА2)\nМатематика ПТГ\n\nс.к. Биохимия КСС')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Математика ПТГ\nБиология ЯИВ\nФизика ФЛД / Практикум хим. осн. матер. НВВ\n\nФизкультура ВЕЕ РНР')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Практикум по биологии в медицине ЯИВ\nГеография ЗНИ / ОБЖ ЯИВ\nИстория НВВ')
            elif call.data == 'hum11':
                if date == 1:
                    bot.send_message(call.message.chat.id, 'Право САА\nФизика БГВ / Химия ГАА\nФизкультура ВЕЕ РНР')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Обществознание САА\nЛитература ХЗП (Через ZOOM)\nОбществознание САА / Русский язык ХЗП (Через ZOOM)\n\nИстория як лит КСЕ / с.к. Рус яз ХЗП (Через ZOOM) | История Древнего Рима и Др. Греции БАА / с.к. Рус яз ХЗП (Через ZOOM)')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Введен в литер НАП / Английский СРЮ	| / Английский СРЮ\nМатематика СДА\nМХК ХЗП (через ZOOM) / Биология ЯИВ\n\nЛитература ХЗП / с.к. Литература ХЗП 15:00-16:40')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Физкультура ВЕЕ РНР / География ЗНИ\nСовр як яз СИН | с.к. по истории ГНИ\nс.к. Математика ЕАА\n\nИстория ГНИ')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Английский язык СРЮ\nМатематика СДА\nИстория ГНИ\n\n| Этнология СНА')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'История Якутии СНА /ОБЖ ЗНИ\nФизика БГВ / Информатика ДМН (3 эт)\nЯкутская лит КСЕ\n')
            elif call.data == 'hum10':
                if date == 1:
                    bot.send_message(call.message.chat.id, ' История ГНИ\nЛитература ХЗП (Через ZOOM)\nБиология ЯИВ / История Якутии СНА\nФизкультура ВЕЕ РНР')
                if date == 2:
                    bot.send_message(call.message.chat.id, 'Английский СРЮ\nДоп методы по матем ЕАА\nФизика БГВ / Як. Уст. Твор. ИВВ | Физика БГВ / \n\nс.к. Литер ХЗП (Через ZOOM) / Ист якут лит КСE | с.к. Литература ХЗП (Через ZOOM) /')
                if date == 3:
                    bot.send_message(call.message.chat.id, 'Математика ССВ\nОбществознание ГНИ\nХимия ГАА / Физкультура ВЕЕ РНР')
                if date == 4:
                    bot.send_message(call.message.chat.id, 'Английский СРЮ / Якут яз СИН\nРусский язык ХЗП (Через ZOOM)\nСовр. Як. Яз СИН/ МХК ХЗП (Через ZOOM) | История в лицах ГНИ / МХК ХЗП (Через ZOOM)\n\nДревнетюрский язык СНА / История Якутии СНА')
                if date == 5:
                    bot.send_message(call.message.chat.id, 'Информатика ДМН (3 эт)/\nИстория ГНИ\nМатематика ССВ\n\nиндив проект ДИА  /Литература ХЗП (Через ZOOM) | Кейс техн. общ наук ГНИ / Литература ХЗП (Через ZOOM)')
                if date == 6:
                    bot.send_message(call.message.chat.id, 'Право ГНИ\nЯкутская лит КСЕ\nЯНК ПАН (ZOOM) / География ЗНИ	')
            if date == 7:
                bot.send_message(call.message.chat.id, 'сегодня выходной эрэбээтэ)')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вот ваше расписание на сегодня:", reply_markup=None)
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
