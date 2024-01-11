from params import ALPHABET


def encode_decode_text(text: str, lang: int, step: int) -> str:
    """
    Function for translating text with Caeser shift.
    """
    phrase = ""
    for i in text:
        if i.isalpha():
            char = ALPHABET[lang][(ALPHABET[lang].index(i.upper()) + step) % len(ALPHABET[lang])]
            phrase += char if i.isupper() else char.lower()
        else:
            phrase += i
    return phrase
