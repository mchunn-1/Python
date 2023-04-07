

#def indicates that it is a function definition... rubiksouse(...) can be called later  
def  rubiksHouse(bedrooms, RoomHeight, bathrooms, familyRooms, kitchens, diningRooms):
    
    #average door size is 7 ft by 3 ft. Each room will have a door opening that must be subtracted from the number of cubes needed. 
    #each room has 6 surfaces to be accounded for. A ceiling, 4 walls, and a floor. All made of cubes. 
    bedroomsCalc = (bedrooms * 11 * 12 * RoomHeight * 6) - (7 * 3)
    bathroomsCalc = (bathrooms * 5 * 8 * RoomHeight * 6) - (7 * 3)
    familyRoomsCalc= (familyRooms * 16 * 20 * RoomHeight * 6) - (7 * 3)
    kitchensCalc = (kitchens * 12 * 15 * RoomHeight * 6) - (7 * 3)
    diningRoomsCalc = (diningRooms * 14 * 16 * RoomHeight * 6) - (7 * 3)
    totalSquareFeet = (bedroomsCalc + bathroomsCalc + familyRoomsCalc + kitchensCalc + diningRoomsCalc)
    #rubik's cubes are 2.25 inches and cost on average $10 a piece
    #rubik's cubes are .035156 square feet (2.25 * 2.25 / 144)
    numberOfCubes = int(totalSquareFeet / .03516) 
    #the price value is what needs to be return, so the variable is set 
    price = int(numberOfCubes * 10)
    return (price)


def BAContent(drinkNumber, weight, time, gender):

#the if statement sets up conditions... in this case different genders based on the users input  
    if gender == "1":
        gConstant = 0.68
                    
    elif gender == "2":
        gConstant = 0.55
           
    BAC = (((drinkNumber * .06 * 100 * 1.055) / (weight * gConstant)) - (.015 * time))    
    #the return statement will return a result from a funciton 
    return (BAC)


def coreTravel(speed, gasMPG, gasPPG):

    #int converts floating point numbers to integers, it doesn't round the number, it chops off the fraction
    timeHours = int((3959 / speed))
    gasPrice= int((3959 / gasMPG) * gasPPG)
    
    #the return statment will return both reults in this case 
    return(timeHours, gasPrice)


def squidGame(hours, bathroom):
  
    min = hours * 60
    minBathroom = min - bathroom
    squidDays = 485 / minBathroom
    
    return(squidDays)


def earthCDog(length_cm):

    length_m = length_cm * .01 
    earthDog = int(40075 / (length_m * .001)) 

    return (earthDog)

def BMICalc(height_ft, height_inch, weight):
    
    height= (height_ft*12) + height_inch
    h = height*2.54/100
    w = weight/2.2
    BMI = w / (h**2) 
    return (BMI)



def main():
    #the function is put into a loop 
    while 1:
        #try is used to test code for error
        try: 
            print("Hello and welcome to the calcualtion station! \nWe have some fun and useful options for you to choose from, so let us know what we can do for you!")
            #input gets input from the users keyboard and returns it as a string
            userChoice = input("Below are your options: \nEnter '1' to find out how much it would cost you to buid your dream house out of Rubik's cubes \nEnter '2' to calculate your blood alcohol content \nEnter '3' to find out how long it would take and how much it would cost you to travel to the center of the Earth \nEnter '4' to see how long it would take you personally to watch Squid Game \nEnter '5' to calculate how many clones of your own dog it would take to wrap them around the world if you lined them up from nose to tail. \nEnter '6' if you would like to calculate your BMI. \n" )
            
            if userChoice == '1':
                print("Let's find out how much it would cost to build your dream house out of 3x3 rubiks cubes!")
                #\n represents a new line 
                print("In our calculation we will use standard reported sizes for each room, but please choose to have as many rooms you like! \nLet's get building!")
                #float converts integers and strings to floating point numbers 
                RoomHeight = float(input("How tall would you like your rooms to be? Keep in mind the standard height is 10 feet. "))
                if RoomHeight <= 0:
                    #if user inputs a value less than or equal to 0, a ValueError will be raised 
                    raise ValueError
                bedrooms = float(input("How many bedrooms would you like to have? A standard bedroom is 11 ft x 12 ft. "))
                if bedrooms <= 0:
                    raise ValueError
                bathrooms = float(input("How many bathrooms would you like to have? A standard bathroom is 5 ft by 8 ft. "))
                if bathrooms <= 0:
                    #valueError is an error of the right type but incorrect value 
                    raise ValueError
                familyRooms = float(input("How many family rooms would you like to have? A standard family room is 16 ft by 20 ft. "))
                if familyRooms <= 0:
                    raise ValueError
                kitchens = float(input("How many kitchens would you like to have? A standard kitchen is 12 ft by 15 ft. "))
                if kitchens <= 0:
                    raise ValueError
                diningRooms = float(input("How many dining rooms would you like to have? A standard dining room is 14 ft by 16 ft. "))
                if diningRooms <= 0:
                    raise ValueError
                #the function rubiksHouse is converted and put equal to the variable x
                x = str(rubiksHouse(bedrooms, RoomHeight, bathrooms, familyRooms, kitchens, diningRooms))
                #the print statment will present the result of the calculation to the user 
                print("It would cost you around $" + x + " to build your dream house out of Rubik's cubes!")

            #if/elif is set up to account for the choice the user makes  
            elif userChoice == '2':
                print("Lets calculate your blood alcohol content!")
                drinkNumber = float(input("One standard drink is considered 12 oz of beer, 5 oz of wine, or 1.5 oz of liquir. \nHow many drinks have you had? "))    
                #<= sets up a condition pertaining to if the input is less than or equal to a given number
                if drinkNumber <= 0:
                    raise ValueError  
                weight = float(input("How much do you weigh in pounds? "))
                if weight <= 0:
                    raise ValueError
                time = float(input("How many hours has it been since your last drink "))
                if time <= 0:
                    raise ValueError
                gender = input("Please enter '1' if you are a male, or '2' if you are a female. ")
            
                x = str(BAContent(drinkNumber, weight, time, gender))
                
                print("Your blood alcohol level is " + x + ".")

            elif userChoice == '3':
            #== compares if values are equal 
                answer = input("Would you like to know how long it would take you to drive to the center of the earth and how much it would cost you in gas? Please enter '1' for yes or '2' for no.\n")
                if answer == '1':
                    #= assigns values to equal something 
                    speed = float(input("How fast would you drive? Please enter your miles per hour and remember, there's no speed limit when traveling to earth's core! ")) 
                    if speed <= 0:
                        raise ValueError
                    gasMPG = float(input("How many miles of gas does your car get per gallon? "))
                    if gasMPG <= 0:
                        raise ValueError
                    gasPPG = float(input("How much is one gallon of gas costing right now where you live? "))
                    if gasPPG <= 0:
                        raise ValueError
                #sort for "else if". Similar to if statement in that one branch will be executed. Can have multiple elif
                elif answer == '2': 
                    print("That's ok, come back if you change your mind! Bye!")
                #the else clause is ran last if the input is false 
                else:
                    #TyperError is raised if someting is of inappropriate type 
                    raise TypeError

                x = str(coreTravel(speed, gasMPG, gasPPG))
                print("Below tells you how long it would take (hours) and how much it would cost you ($) to travel to the center of the earth. Format = (time, cost)\n" + x ) 
                            
            elif userChoice == '4':
                answer = input("Do you feel left out and want to know how fast you can watch the whole Netflix original series Squid Game? \nPlease enter '1' for yes or '2' for no.\n")
                if answer == '1':
                    hours = float(input("How many hours a day can you commit to watching Squid Game? \n"))
                    if hours <= 0:
                        raise ValueError
                    print("You'll probably need a batroom break in there somewhere, so let's account for one bathroom run per day during the time you watch the show.")
                    bathroom = float(input("How many minutes would you guess it takes you for a bathroom break? \n"))
                    if bathroom <= 0:
                        raise ValueError
                elif answer == '2':
                    print("I guess you must have already seen the show, bye friend!")
                else:
                    raise TypeError
                #sets the function equal to a variable so the value from the function calcualtion can be returned
                x = str(squidGame(hours, bathroom))
                print("It would take you " + str(x) + " days to watch the whole series if you watched " + str(hours) + " hours per day with one bathroom break lasting " + str(bathroom) + " minutes per day.")
                print("Happy watching! Bye!")
                
            elif userChoice == '5':
                dog = input("Do you have a dog? \nPlease enter '1' for yes or '2' for no.\n")
                if dog == '1':
                    print("Great, dog people are the best. Please go measure the length of your pup from nose to tail, we need the measurment in centimeters!")
                    input("Press enter to continue")
                    dogName= str(input("What is your dog's name? \n"))
                    length_cm =float(input("How many centermeters long was " + dogName + ". Please enter the numerical value. \n"))
                    if length_cm <= 0:
                        raise ValueError
                elif dog == '2':
                    print("Sorry to hear that! Looks like this calculation won't do you any good, bye!")
                else:
                    raise TypeError
                x = str(earthCDog(length_cm))
                print("Wow! It would take around " + str(x) + " clones of " + dogName + " to wrap them around the earth's circumference!")

            elif userChoice == '6':
                print("Welcome to the BMI calculator!")
                height_ft = float(input("Please input your height measurment in feet only: "))
                if height_ft <= 0:
                    raise ValueError
                height_inch= float(input("Please input the remainder of your height measurment in inches: "))
                if height_inch <= 0:
                    raise ValueError
                weight = float(input("Please input weight (pounds): "))
                x = str(BMICalc(height_ft, height_inch, weight))
                print("Your BMI is " + x)

            else:
                raise ValueError
        #if an error is found in the try block, the except block is ran 
        except ValueError:
            print("Please follow the prompt! Only enter a numerical value when asked for a number, and make sure it is greater than 0!")
        except TypeError: 
            print("Your imput cannot be read! Please follow the prompt!")
        except:
            print("Please try again!")


#set to __main__ because the module is being run is the main program
if __name__ == '__main__':
    main()         
