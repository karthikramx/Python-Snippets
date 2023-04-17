from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('text.txt', mode='r') as f:
        text = f.read()
        translation = translator.translate(text=text)
        with open('text-japnese.txt',mode='w') as f2:
            f2.write(translation)
except FileNotFoundError as e:
    print(e)

