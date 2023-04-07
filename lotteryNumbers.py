import random
#generates random numbers from range x to y 
def ranNumGen(x,y):
    return random.randint(x,y)

def main():
    #calls on the function to generate a random number between 1 and 100 and assigns it to a variable 
    first = ranNumGen(1,26)
    second = ranNumGen(1,26)
    third = ranNumGen(1,26)
    fourth = ranNumGen(1,26)
    fifth = ranNumGen(1,26)
    powerBall = ranNumGen(1,26)
    #puts the 6 random numbers together into one variable 
    lottery = (first, second, third, fourth, fifth, "powerball:" + str(powerBall))
    #prints out the lottery numbers 
    print (lottery)



if __name__ == "__main__":
	main()
