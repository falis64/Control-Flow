# if, elif and else

# age = 16

# if age >= 18:
#    print("You are the correct age to buy a ticket for this movie")
# elif age < 18:
#    print("Sorry, you are not old enough to buy a ticket for this movie")
# elif and else

film_rating = "falis"

if film_rating.lower() == "Universal":
    print("All ages can watch this movie")
elif film_rating.lower() == "pg":
    print("Parental guidance recommended")
elif film_rating.lower() == "12":
    print("You must be at least 12 years old to watch this movie")
elif film_rating.lower() == "15":
    print("You must be at least 15 years old to watch this movie")
elif film_rating.lower() == "18":
    print("You must be at least 18 to watch this movie")
else:
    print("This is not a correct rating, please use universal pg 12/15/18")

# THERE ARE NO SWITCH OR CASE STATEMENTS IN PYTHON


years = input("how old are you?")
age = int(years)
if age > 117:
    print("This is not a valid age")
elif age <= 1:
    print("This is not a valid age")
elif age >= 18:
    print("The movie rating that are available to you are pg, 12, 15, 18")
elif age >= 15:
    print("The movie ratings that are available to you are pg, 12 and 15")
elif age >= 12:
    print("The movie ratings that are available to you are pg and 12")

