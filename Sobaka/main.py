import play

play.set_backdrop('light blue')



@play.when_program_starts # Функція для початку програми
def start():
    text1 = play.new_text(words = "П - Привітатися, О - Обняти, Ж - Жарт, С - Спати, Ф - Фокус, Ї - Їсти", x=0, y=250, font_size = 30)
    text2 = play.new_text(words = "Пробіл - Піти", x=0, y=200, font_size = 30)
    img = play.new_image(image='hello.jpg', x=0, y=0)

@play.repeat_forever # Повторювати завжди (ігровий цикл)
def do():
    pass


play.start_program() # Запуск програми