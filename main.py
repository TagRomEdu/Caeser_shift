from utils import encode_decode_text


def main():
    while True:
        try:
            lang = int(input('Выбери язык алфавита (Choose the language): \n0 - Русский \n1 - English: \n'))
            if lang in range(2):
                break
            else:
                print("Выбирай 0. Как раз про тебя. (0 or 1 friend.)")
        except ValueError:
            print("Зачем же так? Это сейчас цифра по-твоему была? Малюй 1 или 0 (Try to enter a number 0 or 1 please.)")

    if lang:
        direction = input('Choose the direction: \n(+) - Encoding \n(-) - Decoding:\n ')
        step = int(direction + input('Write the number, step: '))
        text = input('Give me the phrase:\n')
    else:
        direction = input('Выбери направление: \n(+) - Шифрование \n(-) - Дешифрование:\n ')
        step = int(direction + input('Веди число, шаг сдвига: '))
        text = input('Введите текст для обработки:\n')

    print(encode_decode_text(text, lang, step))


if __name__ == '__main__':
    main()
