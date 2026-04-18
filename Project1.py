import random

print("🎮 ROCK PAPER SCISSORS GAME 🎮")
choices = ["rock", "paper", "scissors"]

user = input("Choose rock / paper / scissors: ").lower()
computer = random.choice(choices)

print("Computer chose:", computer)

if user == computer:
    print("😐 Draw!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("✅ You Win 🎉")
else:
    print("❌ You Lose 😭")
