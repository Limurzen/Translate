import googletrans
from googletrans import Translator

# Создаем экземпляр класса Translator
translator = Translator()

# Функция для перевода текста
def translate(text, dest_language):
    translated_text = translator.translate(text, dest=dest_language)
    return translated_text.text

# Пример использования функции
text_to_translate = "Hello, World!"
translated_text = translate(text_to_translate, "es")
print(translated_text)  # вывод: "¡Hola, mundo!"
