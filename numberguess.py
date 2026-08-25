import random

def _numberguess_in():
    attemps=0
    numbrs=random.randint(1,100)
    print("guess random number in between 1 to 100")
    while True:
        guess=int (input("your guess"))
        attemps=attemps+1
        if guess>numbrs:
            print("to large")
            
        elif guess<numbrs:
            print("to small")
        else :
            print(f"correct guess {attemps} attempts is !")
            break
_numberguess_in()

            
    
    
    
    