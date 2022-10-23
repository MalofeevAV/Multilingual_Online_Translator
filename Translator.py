def welcome_message():
	available_languages = ('Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish')
	print("Hello, welcome to the translator. Translator supports:")
	[print(f"{indx}. {lang}") for indx, lang in enumerate(available_languages, 1)]

	message_1 = "Type the number of your language:\n"
	your_language = int(input(message_1)) - 1

	message_2 = "Type the number of language you want to translate to:\n"
	language_to_translate_to = int(input(message_2)) - 1

	message_3 = "Type the word you want to translate:\n"
	word = input(message_3).lower()
	print()

	return available_languages[your_language], available_languages[language_to_translate_to], word


def request(your_language, language_to_translate_to, word):
	url = f"https://context.reverso.net/translation/{your_language.lower()}-{language_to_translate_to.lower()}/{word}"
	headers = {'User-Agent': 'Mozilla/5.0'}

	r = requests.get(url, headers=headers)

	if r:
		soup = BeautifulSoup(r.content, 'html.parser')

		translations = soup.find_all("span", {"class":"display-term"})
		print(f"{language_to_translate_to} Translations:")
		[print(el.text.strip()) for el in translations]
		print()

		examples = soup.find("section", {"id":"examples-content"}).find_all("span", {"class":"text"})
		print(f"{language_to_translate_to} Examples:")
		# [print(el.text.strip(), end=("\n\n", "\n")[count%2]) for count, el in enumerate(examples, 1)]
		[print(el.text.strip()) for el in examples]

	else:
		print("Poor connection")


if __name__ == "__main__":
	import requests
	from bs4 import BeautifulSoup

	request(*welcome_message())ы
