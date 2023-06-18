import play
from play.play import Sprite, text


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
    if play.key_is_pressed("п") or play.key_is_pressed("П") or play.key_is_pressed("g") or play.key_is_pressed("G"):
        player.image = 'hello.jpg'
        speech.words = 'Здоров був!'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'І що ти вилупився?'
        await play.timer(2.0)
        player.image = 'NO2.jpg'
        speech.words = 'Може я краще піду!?'
    if play.key_is_pressed("о") or play.key_is_pressed("О") or play.key_is_pressed("j") or play.key_is_pressed("J"):
        player.image = 'obnimashki.jpg'
        speech.words = 'Задушиш..'
        await play.timer(3.0) 
        player.image = 'NO.jpg'   
        speech.words = 'Зупинись >:('
        await play.timer(2.0)
        player.image = 'NO2.jpg'   
        speech.words = "Ти занадто нав'язливий"      
    if play.key_is_pressed("ж") or play.key_is_pressed("Ж") or play.key_is_pressed(";") or play.key_is_pressed(":"):
        player.image = 'Laugh.jpg'
        speech.words = 'лол, ахахх..'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'Ще буде жарт?'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Мені стає нудно...'
    if play.key_is_pressed("с") or play.key_is_pressed("С") or play.key_is_pressed("c") or play.key_is_pressed("C"):
        player.image = 'sleep.jpg'
        speech.words = 'ZzZz..'
        await play.timer(3.0)
        player.image = 'NO.jpg'   
        speech.words = 'Я прокинувся'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Дай встати!'
    if play.key_is_pressed("ф") or play.key_is_pressed("Ф") or play.key_is_pressed("a") or play.key_is_pressed("A"):
        player.image = 'Focus.jpg'
        speech.words = 'Ти що чаклун?'
        await play.timer(3.0)
        player.image = 'NO.jpg'    
        speech.words = 'Давай ще!'
        await play.timer(5.0)
        player.image = 'NO2.jpg'   
        speech.words = 'Та ти не чаклун.'
    if play.key_is_pressed("і") or play.key_is_pressed("І") or play.key_is_pressed("s") or play.key_is_pressed("S"):
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
        await play.timer(5.0)
        player.image = 'NO.jpg'   
        speech.words = 'Давай вже йди, не мозоль очі.'
        await play.timer (2.0)
        quit()
    if play.key_is_pressed("з") or play.key_is_pressed("З") or play.key_is_pressed("p") or play.key_is_pressed("P"):
        play.set_backdrop('dark red')
        player.image = 'pashalka.jpg'
        speech.words = '!??*"!(№?('
        await play.timer (2.0)
        quit()
    pass

play.start_program() # Запуск програми