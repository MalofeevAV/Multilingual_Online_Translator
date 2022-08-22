def welcome_message(DEBUG):
	if DEBUG:
		language = "french"
		word = "hello"
	else:
		message_1 = "Type \"en\" if you want to translate from French into English, or \"fr\" if you want to translate from English into French:"
		language = input(message_1)

		message_2 = "Type the word you want to translate:"
		word = input(message_2)

	print(f"You chose \"{language}\" as the language to translate \"{word}\" to.")

	return language, word


def request(language_1, word):

	language_2 = ("en", "fr")[language_1 != "en"]
	url = f"https://context.reverso.net/translation/{language_1}-english/{word}"
	headers = {'User-Agent': 'Mozilla/5.0'}

	r = requests.get(url, headers=headers)

	if r:
		print("200 OK", "Translations", sep="\n")
		soup = BeautifulSoup(r.content, 'html.parser')
		result = soup.find_all("a", {"class":"translation ltr dict n"})
		print(result, url)
	else:
		pass


if __name__ == "__main__":
	import requests
	from bs4 import BeautifulSoup

	DEBUG = True

	request(*welcome_message(DEBUG))
