import random

p1_deck = []
p2_deck = []
table_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
p1_score = sum(p1_deck)
p2_score = sum(p2_deck)
score_dict = {"Player 1": p1_score, "Player 2": p2_score}

print("Let's play some 21! First cards rolling:\n")

p1_deck.append(random.choice(table_deck))
p1_score = sum(p1_deck)
p2_deck.append(random.choice(table_deck))
p2_score = sum(p2_deck)

print(f"Player 1: {p1_deck} | Total:{p1_score} \nPlayer 2: {p2_deck} | Total:{p2_score}\n")

while p1_score <= 21 and p2_score <= 21:

    prompt_card = input("Player 1 pick a card (y/n)? ")
    if prompt_card == "y":
        p1_deck.append(random.choice(table_deck))
        p1_score = sum(p1_deck)
        score_dict.update({"Player 1": p1_score})
        print(f"\nPlayer 1: {p1_deck} | Total:{p1_score} \nPlayer 2: {p2_deck} | Total:{p2_score}\n")

    elif prompt_card == "n":
        print("All right, Player 1 ain't buying!\n")

    if p1_score <= 21 and p2_score <= 21:

        prompt_card = input("Player 2 pick a card (y/n)? ")
        if prompt_card == "y":
            p2_deck.append(random.choice(table_deck))
            p2_score = sum(p2_deck)
            score_dict.update({"Player 2": p2_score})
            print(f"\nPlayer 1: {p1_deck} | Total:{p1_score} \nPlayer 2: {p2_deck} | Total:{p2_score}\n")

        elif prompt_card == "n":
            print("All right, Player 2 ain't buying!\n")
    else:
        pass

else:
    print(f"Game over! Winner is {min(score_dict, key=score_dict.get)}!")
