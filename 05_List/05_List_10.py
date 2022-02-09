def c(cards):
    new_cards = cards[len(cards)//2:]
    new_cards += cards[0:len(cards)//2]
    return (new_cards)

def s(cards):
    new_cards = cards[0::2]
    new_cards += cards[1::2]
    return (new_cards)

cards = input().split()
commands = input()

for command in commands:
    if command == 'C':
        cards = c(cards)
    elif command == 'S':
        cards = s(cards)
        
print(*cards)