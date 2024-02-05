############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


game_end = False
import random
from replit import clear
from art import logo
  

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)


def calculate_score(list_of_cards):
  return sum(list_of_cards)
  if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
    return 0
  if 11 in list_of_cards and sum(list_of_cards) > 21:
    list_of_cards.remove(11)
    list_of_cards.append(1)
    
def compare(user_score, computer_score):
  if computer_score == 0:
    print("You lose, computer got a blackjack")
  elif user_score == 0:
    print("You win! You got a Blackjack")
  elif computer_score == user_score:
    print("Draw.")
  elif user_score > 21:
    print("Busted! You lose.")
  elif computer_score > 21:
    print("Computer got Busted! You win.")
  elif user_score > computer_score:
    print("You win.")
  elif user_score < computer_score:
    print("You lose.")

game_continues = True

while game_continues:
  user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if user == "n":
    game_continues = False
    print("Good bye.")
  elif user == "y":
    clear()
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    calculate_score(user_cards)
    calculate_score(computer_cards)
    while not game_end:
      computer_score = calculate_score(computer_cards)
      user_score = calculate_score(user_cards)
      if computer_score == 0:
        game_end = True
      if user_score == 0:
        game_end = True
      elif user_score > 21:
        game_end = True
      print(f"Your cards: {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")
      if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        user_cards.append(deal_card())
      else:
        game_end = True
        print(f"Your final hand: {user_cards}. Final score: {user_score}.")
    
    while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
      computer_cards.append(deal_card())
      print(f"Computer's final hand: {computer_cards}. Final score: {calculate_score(computer_cards)}.")
      compare(user_score, computer_score)