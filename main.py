from main_class import Mainclass
if __name__ == '__main__':
    print("Дисклеймер.")
    print("Данная программа создана исключительно в учебных целях.")
    print("Она не несет цели оскорбить кого либо.")
    print("Все совпадения случайны.")

    t = True
    while t:
        otv = input('Если вы желаете продолжить введите 1 (0 - для выхода): ')
        if otv == '0' or otv == '1':
            otv = int(otv)
            t = False
    if not otv:
        exit(0)
    else:
        bot = Mainclass()
        print("Напишите что-нибудь на английском (для выхода введите 0)")
        while True:

            frase = input(': ')
            if frase == '0':
                exit(0)
            if len(frase) == 0:
                frase = 'hi'
            if frase.isdigit():
                frase = 'hi'
            # bot.get_vertex(frase)
            print(bot.censor(bot.response(frase)))

