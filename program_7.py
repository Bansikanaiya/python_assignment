#7 to read a card as input and output if the card is lucky or not

print("-----------Find a card is lucky or not---------")

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# all suits  Hearts, Diamonds, Clubs, Spades

card = input("Enter a card (e.g. 5 of Hearts): ")

if values == '7' or values=='5' or values=='3':
    print(f"{card} is a lucky card!")
else:
    print(f"{card} is not a lucky card.")       