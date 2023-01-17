# MAX_CANDIDATES = 9
# nCandidates = int(input("How many candidates for this election:"))
candidates = {'John': 0, 'Martha': 0, 'Luca': 0}  # dictionary with candidates and vote count
list_of_the_candidates = list(candidates.keys())
nVoters = int(input("How many voters for this election: "))
print(f"Number of voter: {nVoters}")


def vote(candidate):
    candidates[candidate] += 1
    print(f"It's done. You've voted for {candidate}!")


def print_winner():
    winner = max(candidates, key=candidates.get)
    maxValue = max(candidates.items(), key=lambda x: x[1])
    listOfKeys = list()
    # Iterate over all the items in dictionary to find keys with max value
    for key, value in candidates.items():
        if value == maxValue[1]:
            listOfKeys.append(key)

    if len(listOfKeys) != 1:
        print("\nThe voting is over.\nIt's a tie between candidates: ", str(listOfKeys).strip('[]'))
        print(f"Each one received {candidates[winner]} vote(s).")

    else:
        print(f'\nThe voting is over.\n{winner} is the winner with {candidates[winner]} votes')


while nVoters > 0:

    name = input("\nIn which candidate would you like to vote for? ")
    if name in candidates:
        nVoters = nVoters - 1
        vote(name)

    else:
        print(f'\nThis candidate does not exist.\nCheck the candidates list:')
        print(f'{list_of_the_candidates}\n')

print_winner()
