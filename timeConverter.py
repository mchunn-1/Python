#this code will covert seconds to other units of time (days, hrs, etc...) 

#store value of seconds as a number
seconds=(float(input("Please input seconds: ")))

#divide seconds into whole number of minutes less than 1 hr
min=seconds//60%60
#divide seconds into whole number of hours less than 1 day
hrs=seconds//60//60%24
#divide seconds into whole number of days 
days=seconds//60//60//24
#grab remaining number of seconds less than 1 minute
remainder=seconds%60

#convert all onto strings
min=str(min)
hrs=str(hrs)
days=str(days)
remainder=str(remainder)

#print output in descending order of size
print(days+" days")
print(hrs+" hours")
print(min+" minutes")
print("and "+ remainder+" seconds.")
