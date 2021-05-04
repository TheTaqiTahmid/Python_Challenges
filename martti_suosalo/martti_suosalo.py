# Python version 3.9.0
import unittest

# Input and error handling
while True:
    player = input("Insert the total number of players: ")
    try:
        player == int(player)
        if int(player) >= 1:
            player = int(player)
            break
        else:
            print("The number of player must me 1 or higher")
    except: 
        print("Number of players must be an integer")
        
while True:
    no_of_round = input("Insert the number of rounds: ")
    try: 
        no_of_round == int(no_of_round)
        if int(no_of_round) >= 1:
            no_of_round = int(no_of_round)
            break
        else:
            print("Number of rounds must be 1 or higher")
    except:
        print("Number of rounds must be an integer")

# Function definition
def sum_of_digits(number):
    ''' This function returns the sum of all the digits in a numer'''
    summ = sum(int(digit) for digit in str(number))
    return summ

def check_digits(value):
    ''' This function checks if all the digits in a number are equal'''
    string  = str(value)
    if len(string) > 1:
        if len(set(string)) == 1:
            return True
    return False

# Logic
def drinking_game(no_of_player, no_of_rounds):
    j = 1
    k = True
    for i in range(1, no_of_round + 1):
        if j > player:
            j = 1
        elif j < 1:
            j = player
        if sum_of_digits(i) == 7 or i % 7 == 0 or "7" in str(i):
            print(f"Player: {j:<4} Martti Suosalo")
        else:
            print(f"Player: {j:<4} \"{i}\"")
        if check_digits(i):
            if k == True:
                k = False
            elif k == False:
                k = True
        if k == True:
            j += 1
        else:
            j -= 1

drinking_game(player, no_of_round)


 # Unit Tests       
class TestGame(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum_of_digits(35), 8)
        self.assertEqual(sum_of_digits(10), 1)
        self.assertEqual(sum_of_digits(43), 7)

    def test_check_similar_digits(self):
        self.assertEqual(check_digits(33), True)
        self.assertEqual(check_digits(121), False)
        self.assertEqual(check_digits(111), True)

if __name__ == '__main__':
    unittest.main()