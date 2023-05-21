import play

play.set_backdrop('light blue')

@play.when_program_starts # Функція для початку програми
def start():
    global player, speech
    text1 = play.new_text(words = "П - Привітатися, О - Обняти, Ж - Жарт, С - Спати, Ф - Фокус, Ї - Їсти", x=0, y=250, font_size = 30)
    text2 = play.new_text(words = "Пробіл - Піти", x=0, y=200, font_size = 30)


    player = play.new_image(image='start.jpg', x=0, y = 0, size = 100)
    speech = play.new_text(words='Що я тут роблю?', x=0, y=-250)
@play.repeat_forever # Повторювати завжди (ігровий цикл)
async def do():
    if play.key_is_pressed("п") or play.key_is_pressed("П"):
        player.image = 'hello.jpg'
        speech.words = 'Здоров був!'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'І що ти вилупився?'
        await play.timer(2.0)
        player.image = 'NO2.jpg'
        speech.words = 'Може я краще піду!?'
    if play.key_is_pressed("о") or play.key_is_pressed("О"):
        player.image = 'obnimashki.jpg'
        speech.words = 'Задушиш..'
        await play.timer(3.0) 
        player.image = 'NO.jpg'   
        speech.words = 'Зупинись >:('
        await play.timer(2.0)
        player.image = 'NO2.jpg'   
        speech.words = "Ти занадто нав'язливий"      
    if play.key_is_pressed("ж") or play.key_is_pressed("Ж"):
        player.image = 'Laugh.jpg'
        speech.words = 'лол, ахахх..'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'Ще буде жарт?'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Мені стає нудно...'
    if play.key_is_pressed("с") or play.key_is_pressed("С"):
        player.image = 'sleep.jpg'
        speech.words = 'ZzZz..'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'Я прокинувся'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Дай встати! Свободу мишам!'
    if play.key_is_pressed("ф") or play.key_is_pressed("Ф"):
        player.image = 'Focus.jpg'
        speech.words = 'Ти що чаклун?'
        await play.timer(3.0)
        player.image = 'NO.jpg'    
        speech.words = 'Давай ще!'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Та ти не чаклун.'
    if play.key_is_pressed("і") or play.key_is_pressed("І"):
        player.image = 'Food.jpg'
        speech.words = 'Дякую, дуже смачно!'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'Я вже наївся'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Мене зараз стошнить'
    if play.key_is_pressed("space"):
        player.image = 'Bye.jpg'
        speech.words = "Бувай, приходь ще!"
        await play.timer(10.0)
        player.image = 'NO.jpg'   
        speech.words = 'Давай вже йди, не мозоль очі.'
        quit()
    pass


play.start_program() # Запуск програми