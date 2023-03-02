import os
import requests
from bs4 import BeautifulSoup
os.system("clear")

url = "https://www.iban.com/currency-codes"
countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)

def menu():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Escolha um país da lista:")
      menu()
    else:
      country = countries[choice]
      print(f"Você escolheu {country['name']}\nO código da moeda é {country['code']}")
  except ValueError:
    print("Isso não é um número!")
    menu()

print("Bem-vindo ao Negociador de Moedas!\nEscolha pelo número da lista o país que desja consultar o código da moeda.\n")

for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")
  
menu()
