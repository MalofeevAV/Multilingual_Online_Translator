def welcome_message(available_languages):
    print("Hello, welcome to the translator. Translator supports:")
    [print(f"{indx}. {lang}") for indx, lang in enumerate(available_languages[1:], 1)]

    message_1 = "Type the number of your language:\n"
    your_language = int(input(message_1))

    message_2 = "Type the number of a language you want to translate to or '0' to translate to all languages:\n"
    language_to_translate_to = int(input(message_2))

    message_3 = "Type the word you want to translate:\n"
    word = input(message_3).lower()
    print()

    return available_languages, available_languages[your_language], available_languages[language_to_translate_to], word


def request(your_language, language_to_translate_to, word):
    url = f"https://context.reverso.net/translation/{your_language.lower()}-{language_to_translate_to.lower()}/{word}"
    headers = {'User-Agent': 'Mozilla/5.0'}

    r = requests.get(url, headers=headers)

    if r:
        soup = BeautifulSoup(r.content, 'html.parser')
        translations = soup.find_all("span", {"class": "display-term"})
        examples = soup.find("section", {"id": "examples-content"}).find_all("span", {"class": "text"})
        return translations, examples
    else:
        print("Poor connection")


def translate(available_languages, your_language, language_to_translate_to, word):
    if language_to_translate_to == "All":
        for language in available_languages[1:]:
            if language != your_language:
                write_to_the_file(word, result(language, *request(your_language, language, word)))
    else:
        write_to_the_file(word, result(language_to_translate_to, *request(your_language, language_to_translate_to, word)))
        # print_result(*result(language_to_translate_to, *request(your_language, language_to_translate_to, word)))
    read_data_from_file(f"{word}.txt")

def result(language_to_translate_to, translations, examples):
    result_translations = [f"{language_to_translate_to} Translations:"]
    result_translations.extend([el.text.strip() for el in translations])

    result_examples = [f"{language_to_translate_to} Examples:"]
    result_examples.extend([el.text.strip() for el in examples])

    return result_translations, result_examples


def print_result(result_translations, result_examples):
    print(*result_translations[:2], sep="\n")
    print(*result_examples[:3], sep="\n")


def write_to_the_file(word, content):
    with open(f"{word}.txt", "a", encoding="utf-8") as f:
        [f.write("\n".join(el) + "\n\n") for el in content]

def read_data_from_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    import requests
    from bs4 import BeautifulSoup

    available_languages = ('All', 'Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch',
                           'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish')

    translate(*welcome_message(available_languages))
