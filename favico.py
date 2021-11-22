import requests
import codecs
import mmh3                     # pip install mmh3
import favicon                  # pip install favicon

# Barvicky
CRED = '\033[91m'
CGREEN = '\033[92m'
CFINALE = '\33[4m'
CEND = '\033[0m'

# Ziskani seznamu FAVIONEK z webu
# Zajimaji nas pouze ty, ktere maji koncovku .ico
FiltrICO = "ico"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
headers = {'User-Agent': user_agent}
GetFavicons = favicon.get('https://www.alza.cz/', headers=headers, timeout=2)

# Print radku, ktere obsahuji hledanou koncovku
pouze_ICO = [line.url for line in GetFavicons if FiltrICO in line]
print(CGREEN + "Nalezené ICO podporované favikonky" + CEND)
for icoline in pouze_ICO:
    print(icoline)

print()

# Kdyby nahodou nebyly, tak jen pro info seznam nepodporovanych koncovek
print(CRED + "Další nepodporované favikonky" + CEND)
pouze_NE_ICO = [line.url for line in GetFavicons if FiltrICO not in line]
for nonicoline in pouze_NE_ICO:
    print(nonicoline)

print()

# Spocitani hashe
print(CFINALE + " --- Hash pro podposovane ikonky ---" + CEND)
for radek in pouze_ICO:
    response = requests.get(radek)
    favicon = codecs.encode(response.content, "base64")
    hash = mmh3.hash(favicon)
    print(radek + '\t\t' + str(hash))
