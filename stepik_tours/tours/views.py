from django.shortcuts import render
from django.views import View

shapka = {
    'title': 'Stepik Travel',
    'subtitle': 'Качественный отдых только с Stepik Travel',
    'description': """Лучшие направления на любой бюджет,
    индивидуальный подход к каждому клиенту. """
}

departures = [
    {"title": "Из Москвы", 'url_name': 'msk'},
    {"title": "Из Петербурга", 'url_name': 'spb'},
    {"title": "Из Новосибирска", 'url_name': 'nsk'},
    {"title": "Из Екатеринбурга", 'url_name': 'ekb'},
    {"title": "Из Казани", 'url_name': 'kazan'}
]

tours = {
    1:
        {
            "title": "Marina Lake Hotel & Spa",
            "description": "Отель выглядит уютно. Он был построен из красного "
                           "соснового дерева и украшен синими камнями.  "
                           "Высокие округлые окна добавляют "
                           "общий стиль дома и были добавлены в дом "
                           "в довольно симметричном "
                           "образце.",
            "departure": "nsk",
            "picture": "https://images.unsplash.com/photo-"
                       "1551882547-ff40c63fe5fa"
                       "?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto="
                       "format&fit=crop&w=800&q=60",
            "price": 62000,
            "stars": "4",
            "country": "Куба",
            "nights": 6,
            "date": "2 марта",
        },
    2:
        {
            "title": "Baroque Hotel",
            "description": "Здание отеля имеет форму короткой буквы U. "
                           "Два расширения связаны стеклянными "
                           "нависающими панелями. Второй этаж такого"
                           " же размера, как и первый, который был"
                           " построен точно над полом под ним. "
                           "Этот этаж имеет "
                           "совершенно другой стиль, чем этаж ниже.",
            "departure": "ekb",
            "picture": "https://images.unsplash.com/photo-"
                       "1445019980597-"
                       "93fa8acb246c?ixlib=rb-1.2.1&ixid="
                       "eyJhcHBfaWQiOjEyMDd9&auto"
                       "=format&fit=crop&w=800&q=60",
            "price": 85000,
            "stars": "5",
            "country": "Вьетнам",
            "nights": 8,
            "date": "12 января",
        },
    3:
        {
            "title": "Voyager Resort",
            "description": "Снаружи отель выглядит красиво"
                           " и традиционно. Он был построен "
                           "с белыми камнями и имеет еловые "
                           "деревянные украшения. Высокие, "
                           "большие окна добавляют "
                           "к общему стилю дома и были добавлены"
                           " в дом в основном "
                           "симметричным способом.",
            "departure": "nsk",
            "picture": "https://images.unsplash.com/photo-"
                       "1569660072562-"
                       "48a035e65c30?ixlib=rb-1.2.1&ixid="
                       "eyJhcHBfaWQiOjEyMDd9&auto"
                       "=format&fit=crop&w=800&q=60",
            "price": 63000,
            "stars": "3",
            "country": "Пакистан",
            "nights": 11,
            "date": "7 февраля",
        },
    4:
        {
            "title": "Orbit Hotel",
            "description": "Каждый домик оборудован средней кухней "
                           "и одной небольшой ванной комнатой, "
                           "в нем также есть уютная гостиная, "
                           "две спальни, скромная столовая и большой "
                           "подвал.  Небольшие треугольные "
                           "окна добавляют к общему стилю дома"
                           " и были добавлены в дом в основном "
                           "симметричным способом.",
            "departure": "msk",
            "picture": "https://images.unsplash.com/photo-"
                       "1520250497591"
                       "-112f2f40a3f4?ixlib=rb-1.2.1&ixid="
                       "eyJhcHBfaWQiOjEyMDd9&auto"
                       "=format&fit=crop&w=800&q=60",
            "price": 62000,
            "stars": "4",
            "country": "Индия",
            "nights": 9,
            "date": "22 января",
        },
    5:
        {
            "title": "Atlantis Cabin Hotel",
            "description": "Этот дом среднего размера имеет "
                           "футуристический вид и находится в среднем"
                           " состоянии. Интерьер выполнен в "
                           "насыщенных тонах. Двор небольшой и "
                           "выглядит очень формально. Кроме того,"
                           " странные огни были замечены "
                           "движущимися в доме ночью.",
            "departure": "msk",
            "picture": "https://images.unsplash.com/photo-"
                       "1566073771259-"
                       "6a8506099945?ixlib=rb-1.2.1&ixid="
                       "eyJhcHBfaWQiOjEyMDd9&auto\n"
                       "=format&fit=crop&w=800&q=60",
            "price": 68000,
            "stars": "4",
            "country": "Доминикана",
            "nights": 8,
            "date": "18 января",
        },
    6:
        {
            "title": "Light Renaissance Hotel",
            "description": "Этот крошечный дом выглядит довольно "
                           "современно и находится в ужасном "
                           "состоянии. Интерьер выполнен в "
                           "цветах, которые напоминают вам "
                           "о тропическом лесу. "
                           "Двор небольшой и заросший дикими "
                           "растениями. Кроме того, "
                           "это было однажды показано в "
                           "телесериале, демонстрирующем "
                           "необычно украшенные дома.",
            "departure": "spb",
            "picture": "https://images.unsplash.com/photo-"
                       "1571896349842-"
                       "33c89424de2d?ixlib=rb-1.2.1&ixid="
                       "eyJhcHBfaWQiOjEyMDd9&auto"
                       "=format&fit=crop&w=800&q=60",
            "price": 53000,
            "stars": "3",
            "country": "Пакистан",
            "nights": 13,
            "date": "15 февраля",
        },
    7: {
        "title": "King's Majesty Hotel",
        "description": "Этот дом средних размеров "
                       "выглядит немного старомодно и "
                       "находится в среднем состоянии. "
                       "Интерьер выполнен в цветах, "
                       "которые напоминают о весеннем "
                       "цветнике. Двор среднего "
                       "размера и напоминает луг. "
                       "Кроме того, он был построен "
                       "над остатками дома, который "
                       "был разрушен в результате пожара.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-"
                   "1468824357306-"
                   "a439d58ccb1c?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto="
                   "format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "5",
        "country": "Мексика",
        "nights": 9,
        "date": "22 января",
        },
    8: {
        "title": "Crown Hotel",
        "description": "Этот огромный дом почти "
                       "выглядит инопланетянином и "
                       "находится в среднем состоянии. "
                       "Интерьер выполнен в цветах, "
                       "напоминающих апельсиновое дерево. "
                       "Двор среднего размера и "
                       "напоминает луг. Кроме того, "
                       "это место печально известного убийства.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-"
                   "1549109786-"
                   "eb80da56e693?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto="
                   "format&fit=crop&w=800&q=60",
        "price": 44000,
        "stars": "4",
        "country": "Тайланд",
        "nights": 7,
        "date": "3 февраля",
        },
    9: {
        "title": "Seascape Resort",
        "description": "Этот большой дом имеет сказочный "
                       "вид и находится в "
                       "отличном состоянии. Интерьер выполнен"
                       " в ярких цветах. "
                       "Двор маленький и аккуратно подстрижен."
                       " На заднем дворе "
                       "есть большой участок недавно созданной"
                       " земли, а дом имеет "
                       "большой решетчатый забор через него. "
                       "На заднем дворе живут "
                       "различные животные. Многие владельцы"
                       " приложили согласованные "
                       "усилия для поддержания этой собственности.",
        "departure": "nsk",
        "picture": "https://images.unsplash.com/photo-"
                   "1570214476695-"
                   "19bd467e6f7a?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto"
                   "=format&fit=crop&w=800&q=60",
        "price": 39000,
        "stars": "3",
        "country": "Индия",
        "nights": 10,
        "date": "1 февраля",
        },
    10: {
        "title": "Rose Sanctum Hotel",
        "description": "Снаружи этот дом выглядит старым, "
                       "но чудесным. Он был построен "
                       "из желтого соснового дерева и украшен "
                       "белым кирпичом. Короткие, "
                       "широкие окна пропускают много "
                       "света и были добавлены в дом "
                       "очень симметричным способом.",
        "departure": "msk",
        "picture": "https://images.unsplash.com/photo-"
                   "1560200353-ce0a76b1d438?ixlib"
                   "=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto"
                   "=format&fit=crop&w="
                   "800&q=60",
        "price": 52000,
        "stars": "4",
        "country": "Куба",
        "nights": 10,
        "date": "30 января",
        },
    11: {
        "title": "Viridian Obelisk Hotel & Spa",
        "description": "В доме очень хороший двор "
                       "с большими камнями, "
                       "похожими на озеро. В задней части "
                       "дома окна просторные, "
                       "с большими окнами, они светлее, "
                       "чтобы улучшить впечатление. "
                       "Снаружи есть пять маленьких деревьев. "
                       "Двор в очень хорошем "
                       "состоянии и очень живописный. "
                       "Есть пруд для развлечения",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-"
                   "1477120128765-"
                   "a0528148fed2?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto"
                   "=format&fit=crop&w=800&q=60",
        "price": 68000,
        "stars": "5",
        "country": "Индия",
        "nights": 9,
        "date": "1 марта",
        },
    12: {
        "title": "Saffron Tundra Hotel & Spa",
        "description": "Дом оборудован огромной кухней "
                       "и одной современной ванной "
                       "комнатой, а также имеет огромную "
                       "гостиную, две спальни, "
                       "небольшую столовую, гостиную "
                       "и скромную кладовую.  "
                       "Дом чистый, хорошо построенный "
                       "и в хорошем состоянии, "
                       "но, к сожалению, кровати сгорели "
                       "в мае этого года и, "
                       "к сожалению, все еще нуждаются "
                       "в ремонте. Возможно, "
                       "понадобится целая команда, "
                       "чтобы заменить старую "
                       "медную топку.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-"
                   "1440151050977-"
                   "247552660a3b?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto"
                   "=format&fit=crop&w=800&q=60",
        "price": 72000,
        "stars": "4",
        "country": "Мексика",
        "nights": 12,
        "date": "17 февраля",
        },
    13: {
        "title": "Traveller Resort",
        "description": "Снаружи этот дом выглядит "
                       "очень элегантно. "
                       "Он был построен из коричневого "
                       "кирпича и имеет коричневые "
                       "кирпичные украшения. Высокие, "
                       "большие окна добавляют к "
                       "общему стилю дома и были добавлены "
                       "к дому в довольно "
                       "асимметричном образце. Крыша "
                       "высокая и наклонена в одну "
                       "сторону и покрыта коричневой черепицей. "
                       "Один большой дымоход высовывает "
                       "центр крыши. На крыше нет окон. "
                       "Сам дом окружен великолепным садом "
                       "с виноградными лозами, "
                       "пагодой, прудом и множеством разных цветов.",
        "departure": "ekb",
        "picture": "https://images.unsplash.com/photo-"
                   "1553653924-"
                   "39b70295f8da?ixlib=rb-1.2.1&auto="
                   "format&fit=crop&w=800&q=60",
        "price": 49000,
        "stars": "3",
        "country": "Куба",
        "nights": 8,
        "date": "26 января"
        },
    14: {
        "title": "History Hotel & Spa",
        "description": "Крыша высокая, треугольная, многослойная, "
                       "покрыта пшеничной "
                       "соломой. Две большие трубы находятся "
                       "по обе стороны от дома. "
                       "Многие меньшие окна пропускают много "
                       "света в комнаты под "
                       "крышей.Сам дом окружен асфальтированной "
                       "землей, с местом "
                       "для еды и отдыха на открытом воздухе "
                       "и различными горшечными "
                       "растениями.",
        "departure": "kazan",
        "picture": "https://images.unsplash.com/photo-"
                   "1509600110300-21b9d5fedeb7?ixlib="
                   "rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto=format&fit="
                   "crop&w=800&q=60",
        "price": 91000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 9,
        "date": "3 февраля",
        },
    15: {
        "title": "Riverside Lagoon Hotel & Spa",
        "description": "Здание имеет форму круга. Дом частично "
                       "окружен деревянными "
                       "нависающими панелями с двух сторон. "
                       "Второй этаж "
                       "меньше первого, что позволило создать "
                       "несколько балконов "
                       "по бокам дома. Этот этаж следует тому "
                       "же стилю, что и этаж "
                       "ниже.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-"
                   "1568084680786-"
                   "a84f91d1153c?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto="
                   "format&fit=crop&w=800&q=60",
        "price": 82000,
        "stars": "4",
        "country": "Доминикана",
        "nights": 8,
        "date": "5 февраля",
        },
    16: {
        "title": "History Hotel & Spa",
        "description": "Это высокое здание из старого кирпича. "
                       "Крыша высокая, "
                       "треугольная, многослойная, покрыта "
                       "пшеничной соломой. "
                       "В тесной квадратной спальне "
                       "установлена деревянная и "
                       "стеклянная мебель. Пол деревянный, "
                       "а стены текстурированы "
                       "и окрашены.Настенные и напольные "
                       "светильники обеспечивают "
                       "свет. Комната оформлена в цветах, "
                       "напоминающих облачное "
                       "небо, и в целом выглядит очень "
                       "старомодно. Первое, что вы "
                       "заметите, это тщеславие.",
        "departure": "spb",
        "picture": "https://images.unsplash.com/photo-"
                   "1564056095795-"
                   "4d63b6463dbf?ixlib=rb-1.2.1&ixid="
                   "eyJhcHBfaWQiOjEyMDd9&auto"
                   "=format&fit=crop&w=800&q=60",
        "price": 74000,
        "stars": "5",
        "country": "Вьетнам",
        "nights": 12,
        "date": "24 января",
        }
}

count_msk = {
    'count_msk': 0,
    'price_msk': [],
    'nights_msk': [],
    'min_price_msk': [],
    'max_price_msk': [],
    'min_nights_msk': [],
    'max_nights_msk': []
}

count_spb = {
    'count_spb': 0,
    'price_spb': [],
    'nights_spb': [],
    'min_price_spb': [],
    'max_price_spb': [],
    'min_nights_spb': [],
    'max_nights_spb': []
}

count_nsk = {
    'count_nsk': 0,
    'price_nsk': [],
    'nights_nsk': [],
    'min_price_nsk': [],
    'max_price_nsk': [],
    'min_nights_nsk': [],
    'max_nights_nsk': []
}

count_ekb = {
    'count_ekb': 0,
    'price_ekb': [],
    'nights_ekb': [],
    'min_price_ekb': [],
    'max_price_ekb': [],
    'min_nights_ekb': [],
    'max_nights_ekb': []
}

count_kazan = {
    'count_kazan': 0,
    'price_kazan': [],
    'nights_kazan': [],
    'min_price_kazan': [],
    'max_price_kazan': [],
    'min_nights_kazan': [],
    'max_nights_kazan': []
}

for i in range(1, 17):
    if tours[i]['departure'] == 'msk':
        count_msk['count_msk'] += 1
        count_msk['price_msk'].append(tours[i]['price'])
        count_msk['min_price_msk'] = min(count_msk['price_msk'])
        count_msk['max_price_msk'] = max(count_msk['price_msk'])
        count_msk['nights_msk'].append(tours[i]['nights'])
        count_msk['min_nights_msk'] = min(count_msk['nights_msk'])
        count_msk['max_nights_msk'] = max(count_msk['nights_msk'])

    if tours[i]['departure'] == 'spb':
        count_spb['count_spb'] += 1
        count_spb['price_spb'].append(tours[i]['price'])
        count_spb['min_price_spb'] = min(count_spb['price_spb'])
        count_spb['max_price_spb'] = max(count_spb['price_spb'])
        count_spb['nights_spb'].append(tours[i]['nights'])
        count_spb['min_nights_spb'] = min(count_spb['nights_spb'])
        count_spb['max_nights_spb'] = max(count_spb['nights_spb'])

    if tours[i]['departure'] == 'nsk':
        count_nsk['count_nsk'] += 1
        count_nsk['price_nsk'].append(tours[i]['price'])
        count_nsk['min_price_nsk'] = min(count_nsk['price_nsk'])
        count_nsk['max_price_nsk'] = max(count_nsk['price_nsk'])
        count_nsk['nights_nsk'].append(tours[i]['nights'])
        count_nsk['min_nights_nsk'] = min(count_nsk['nights_nsk'])
        count_nsk['max_nights_nsk'] = max(count_nsk['nights_nsk'])

    if tours[i]['departure'] == 'ekb':
        count_ekb['count_ekb'] += 1
        count_ekb['price_ekb'].append(tours[i]['price'])
        count_ekb['min_price_ekb'] = min(count_ekb['price_ekb'])
        count_ekb['max_price_ekb'] = max(count_ekb['price_ekb'])
        count_ekb['nights_ekb'].append(tours[i]['nights'])
        count_ekb['min_nights_ekb'] = min(count_ekb['nights_ekb'])
        count_ekb['max_nights_ekb'] = max(count_ekb['nights_ekb'])

    if tours[i]['departure'] == 'kazan':
        count_kazan['count_kazan'] += 1
        count_kazan['price_kazan'].append(tours[i]['price'])
        count_kazan['min_price_kazan'] = min(count_kazan['price_kazan'])
        count_kazan['max_price_kazan'] = max(count_kazan['price_kazan'])
        count_kazan['nights_kazan'].append(tours[i]['nights'])
        count_kazan['min_nights_kazan'] = min(count_kazan['nights_kazan'])
        count_kazan['max_nights_kazan'] = max(count_kazan['nights_kazan'])

context = {
    'shapka': shapka,
    'departures': departures,
    'tours': tours,
    'count_msk': count_msk,
    'count_spb': count_spb,
    'count_nsk': count_nsk,
    'count_ekb': count_ekb,
    'count_kazan': count_kazan
}


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/base.html', context=context)


class MskView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/msk.html', context=context)


class TourView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/tour.html', context=context)


class SpbView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/spb.html', context=context)


class NskView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/nsk.html', context=context)


class EkbView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/ekb.html', context=context)


class KazanView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tours/kazan.html', context=context)
