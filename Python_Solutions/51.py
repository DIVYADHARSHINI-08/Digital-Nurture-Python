import hashlib


class URLShortener:

    def __init__(self):
        self.url_database = {}

    def shorten_url(self, original_url):

        short_code = hashlib.md5(
            original_url.encode()
        ).hexdigest()[:6]

        self.url_database[short_code] = original_url

        return short_code

    def retrieve_url(self, short_code):

        if short_code in self.url_database:
            return self.url_database[short_code]

        return "URL not found"


shortener = URLShortener()

url1 = "https://www.google.com"
url2 = "https://www.python.org"

short1 = shortener.shorten_url(url1)
short2 = shortener.shorten_url(url2)

print("----- Shortened URLs -----")
print(f"{url1} -> {short1}")
print(f"{url2} -> {short2}")

print("\n----- Redirect Simulation -----")

print(f"{short1} redirects to:")
print(shortener.retrieve_url(short1))

print(f"\n{short2} redirects to:")
print(shortener.retrieve_url(short2))