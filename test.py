REPUTATION = 0
CALIBRATED = False
print('>†<---------WARHAMMER 40,000: ANATHEMA--------->†<')
choice = input('''
\t1. Начать игру 
\t2. Справочник 
\t3. Выйти\n''')

if '1' in choice:
    print('Вы просыпаетесь в жилом отсеке легкого крейсера имперского флота класса \"Неустрашимый\".',
          'Вот уже 3 месяца ваш корабль пересекает Имматериум с единственной целью - доставить вас к поверхности мира-улья Гринда.',
          'Сквозь иллюминатор пробивается смешение розового, фиолетового и красного цветов свет, а бесконечные волны энергии потрясают корабль.',
          'Кроме этого в комнате есть лишь массивный кейс с вашим снаряжением и цифровой дисплей, с информацией о миссии.',
          'Он то и привлек ваше внимание - на экране мерцал рапорт о предстоящей задаче, который так или иначе вы уже заучили наизусть.', sep='\n')
    report = input('''
    1. Прочитать рапорт
    2. Оставить без внимания\n''')
    if '1' in report:
        print('''
    ◹☠◸------------------------------------------------------------------◹☠◸
     |   Цель: Планетарный губернатор мира-улья Гринда, Келл ван Хеллсинг   | 
     |   Фото:                                                              |
     |                    ^!!^                                              |
     |                 ^?B&@@&GJ^                                           |
     |               ~P&@@@@@@@@&G!                                         |
     |             :5@@@@@@@@@@@@@@5.                                       |
     |           .J#@@BB#B&@@#GBBG&@G^                                      |
     |           P@@@#!...:~!: ..:B@@&!                                     |
     |           !@@@@&P:  :.     ?&&&@#:                                   |
     |           Y@&&&&@Y^:7^:::.7@@&&&@?                                   |
     |           ?@&&&&@&Y7!!!??7#@&&&&@Y                                   |
     |           :#@&&&@&7 .:777G@&&&&&&~                                   |
     |           !&@&&&@&5JJY5#@&&&&&@Y                                     | 
     |            !#@&@@@@@@@@@&&&&@@5.                                     | 
     |             :B@&&&@@@&@&@&&&#7                                       |
     |            .J&&&&&&&&&&&&&&@Y                                        |
     |                                                                      |
     |   Обвинение: Предательство Империума, распространение ереси          |
     |   Приговор: Казнь                                                    |
     |   Исполнитель: Каин Целес, клада Виндикар                            |
     |                                                                      |
     |   Доп. сведения: Тиран, в тоже время тщеславен и горделив. Часто     |
     |   устраивает показательные казни неугодных, остальное время проводит |
     |   в своем дворце. На публике всегда окружен охраной, также возможно  | 
     |   наличие двойника.                                                  |
    ◹☠◸------------------------------------------------------------------◹☠◸\n''')
        print('Закончив изучать рапорт, вы отходите от дисплея и направляетесь к оружейному ящику.')
    elif '2' in report:
        print('~Келл ван Хеллсинг~ - проговариваете вы и переводите взгляд на оружейный ящик, покрытый светящимися рунами.')
    print('Подойдя к нему, вы отщелкиваете тяжелые зажимы и поднимаете крышку.',
          'Внутри, на черной бархатной ткани с узорами имперской аквилы, аккуратно уложены винтовка и пистолет \"Экзетус\".',
          'Винтовка создается индивидуально для каждого владельца, потому становится словно естественным продолжением тела ассасина, '
          'a пистолет является лишь дополнением, использующимся лишь в крайне безвыходных ситуациях.', sep='\n')
    check_in = input('''
    1. Проверить снаряжение
    2. Закончить экипирование\n''')
    if '1' in check_in:
        print('Вы берете винтовку на руки и быстро понимаете, что она сохранила идеальную балансировку.',
              'Затем вы наводите прицел на иллюминатор и вглядываетесь. Постояв так пару секунд вы замечаете, что прицел сбит на пару градусов.',
              'Хорошо, что заметили вы это именно сейчас, ведь на проведение всей операции выделили 1 день, что значит времени на полевую подготовку почти не будет.',
              'Закончив с калибровкой, вы также забираете пистолет и проверяете свой визор, а затем покидаете отсек.\n', sep='\n')
        REPUTATION += 1
        CALIBRATED = True
    elif '2' in check_in:
        print('Окинув взглядом свой арсенал, вы быстро экипируетесь и направляетесь к выходу из отсека.\n')
    print('Спустя пару часов ожидания, ваш корабль наконец выполняет варп-сдвиг и оказывается прямо рядом с планетой, на поверхность которой вас скрытно доставляют на челноке.')
    print('Высадка прошла успешно - вы оказываетесь в двух часах ходьбы от столицы')