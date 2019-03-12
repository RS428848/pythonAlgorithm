from random import randrange
cards = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac","2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad","2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As","2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]

#Player 1
playerOne_cards = []

playerOne_index1 = randrange(len(cards)-1)
playerOne_cards.append(cards[playerOne_index1])
cards.pop(playerOne_index1)

playerOne_index2 = randrange(len(cards)-1)
playerOne_cards.append(cards[playerOne_index2])
cards.pop(playerOne_index2)

print("Player 1 Card: ",playerOne_cards)

#Interlude
done = str(input("Type done after knowing your cards: "))
while done != "done":
    done = str(input("Please type done when you are finsihed viewing yoru cards: "))
print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*")

#Player 2
playerTwo_cards = []

playerTwo_index1 = randrange(len(cards)-1)
cards.pop(playerTwo_index1)

playerTwo_index2 = randrange(len(cards)-1)
cards.pop(playerTwo_index2)

playerTwo_cards.append(cards[playerTwo_index1])
playerTwo_cards.append(cards[playerTwo_index2])
print("PLayer 2 Card: ", playerTwo_cards)

#Interlude
done = str(input("Type done after knowing your cards: "))
while done != "done":
    done = str(input("Please type done when you are finsihed viewing yoru cards: "))
print("*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*")

#Flop
flop = []
flop_one = randrange(len(cards)-1)
flop.append(cards[flop_one])
cards.pop(flop_one)

flop_two = randrange(len(cards)-1)
flop.append(cards[flop_two])
cards.pop(flop_two)

flop_three = randrange(len(cards)-1)
flop.append(cards[flop_three])
cards.pop(flop_three)

print("Flop: ", flop)

#Pre-flop bet
amount = int(input("First player: please enter the amount of money you would like to bet: "))
print(amount)
if amount == 0:
    response = str(input("Type \"check\" to bet 0, type \"bet\" to bet chips or type \"fold\" to forfeit the round: "))
if amount > 0:
    response = str(input("Type \"call\" to bet the same amount,type \"raise\" to bet more chips or type \"fold\" to forfeit the round: ))

if response == ("bet" or "raise"):
    value = int(input("How much money are you betting: "))
if response == ("check" or "call"):
    pot = 2*amount
if response == "fold"
    pot = amount
print(value)
            
