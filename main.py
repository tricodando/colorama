from colorama import Fore, init

init()

color = {
  'yellow': Fore.YELLOW,
  'blue': Fore.BLUE,
  'magenta': Fore.MAGENTA,
  'reset': Fore.RESET,
}

menu = [
  {'cod': 1, 'name': 'Calabresa', 'price': 'R$ 19,70'},
  {'cod': 2, 'name': 'Muçarela', 'price': 'R$ 22,70'},
  {'cod': 3, 'name': 'Frango', 'price': 'R$ 20,50'},
  {'cod': 4, 'name': 'Catupiry', 'price': 'R$ 21,90'},
]

while True:
  print(f"{color['blue']}PIZZARIA LA SABOR{color['reset']}")
  print(f"\n[CARDAPIO]")
  for item in menu:
      trace = '-'*10
      print(f"{item['cod']}. {item['name']:10} {trace} {color['yellow']} {item['price']} {color['reset']}")
  choose = input(f"\n{color['magenta']}Escolha um sabor: ")