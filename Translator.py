def welcome_message(DEBUG):
	if DEBUG:
		language = "french"
		word = "hello"
	else:
		message_1 = "Type \"en\" if you want to translate from French into English, or \"fr\" if you want to translate from English into French:\n"
		language = input(message_1)

		message_2 = "Type the word you want to translate:\n"
		word = input(message_2)

	print(f"You chose \"{language}\" as the language to translate \"{word}\" to.")

	return language, word


def request(language, word):
	languages = ("english-french", "french-english")[language == "en"]
	lang = languages.split("-")[1]

	url = f"https://context.reverso.net/translation/{languages}/{word}"
	headers = {'User-Agent': 'Mozilla/5.0'}

	r = requests.get(url, headers=headers)

	if r:
		print(f"200 OK\n")
		soup = BeautifulSoup(r.content, 'html.parser')

		translations = soup.find_all("span", {"class":"display-term"})
		print(f"{lang.capitalize()} Translations:")
		[print(el.text.strip()) for el in translations[:5]]
		print()

		examples = soup.find("section", {"id":"examples-content"}).find_all("span", {"class":"text"})
		print(f"{lang.capitalize()} Examples:")
		[print(el.text.strip(), end="\n\n") if count%2 == 0 else print(el.text.strip()) for count, el in enumerate(examples[:10], 1)]

	else:
		print("Poor connection")


if __name__ == "__main__":
	import requests
	from bs4 import BeautifulSoup

	DEBUG = False

	request(*welcome_message(DEBUG))
