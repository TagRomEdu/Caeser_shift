ALPHABET = ('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
lang = int(input('Выбери язык алфавита: \n0 - Русский \n1 - Английский: \n'))
step = int(direction + input('Веди число, шаг сдвига (со сдвигом вправо): '))
text = input('Введите текст для обработки:\n')


def main():
    for i in text:
        if i.isalpha():
            char = ALPHABET[lang][(ALPHABET[lang].index(i.upper()) + step) % len(ALPHABET[lang])]
            print(char if i.isupper() else char.lower(), end='')
        else:
            print(i, end='')


if __name__ == '__main__':
    main()
