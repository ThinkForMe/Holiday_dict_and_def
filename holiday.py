"""
Calculate the user's holiday total cost;
Get input of plane, hotel and car cost;
Calculate with user defined functions;
Print out
"""
print("Hello and welcome to Off The Grid,the cheapest holidays to Nowhere.\n\
According to https://www.thetravel.com/most-remote-cities-in-the-world/\n\
These are the most secluded cities...")

# A dictionary to list the available destinations
dest ={
    '1' : "Socotra in Yemen",
    '2' : "Supai in Arizona",
    '3' : "Iqaluit in Canada",
    '4' : "Ittoqqortoormiit in Greenland",
    '5' : "La Rinconada in Peru",
    '6' : "Coober Pedy in Australia"
}

# A dictionary for the flight costs
flight_cost ={
    '1' : 2458,
    '2' : 3410,
    '3' : 4120,
    '4' : 1899,
    '5' : 4819,
    '6' : 6520
}

# A dictionary for the hotel night cost per location
hotel_loc = {
    '1' : 52,
    '2' : 89.99,
    '3' : 75.50,
    '4' : 109.99,
    '5' : 42.55,
    '6' : 33.99
}

# An empty dictionary for our trip
trip = {}

# A function to calculate flight costs
def plane_cost(choice):
    trip[choice] = price
    return print(f"It will cost you {"{:,}".format(round(price, 2))} GBP to fly there.")

# A function to calculate hotel stay
def hotel_cost(city_flight):
    global cost
    cost = hotel_loc[city_flight] * num_nights
    trip[num_nights] = cost
    return print(f"\
{num_nights} nights in {choice} will cost you {"{:,}".format(round(cost))} GBP.")

# A function to calculate car rental cost
def car_rental():
    global rental
    rental = rental_days * 35.99
    trip[rental_days] = rental
    return print(f"\
Car rental for {rental_days} days will cost you {"{:,}".format(rental)} GBP")

# A function to calculate the total cost of the holiday
def holiday_cost():
    total = sum(trip.values())
    return print(f"\
Your total cost will be\t{"{:,}".format(total)} GBP:\n\
- Plane ticket is:\t{"{:,}".format(price)} GBP\n\
- Hotel stay is:\t{"{:,}".format(round(cost))} GBP for {num_nights} nights.\n\
- Car rental is:\t{"{:,}".format(round(rental, 2))} GBP for {rental_days} days\n\
Off The Grid wishes you a great trip!")

# We ask the user for his destination choice
while True:
    global city_flight
    global choice
    global price
    for key, value in dest.items():
        print(key, ". ", value)
    city_flight = input("So where are we taking you to (choose a number): ")
    try:      
        choice = dest[city_flight]
        price = flight_cost[city_flight]
        print(f"\
You are flying to {choice}, exciting!")
        plane_cost(choice)
        break
    except (KeyError, ValueError):
        print("Invalid choice, try again!")

#We ask for the trip duration
while True:
    global num_nights
    try:
        num_nights = int(input(\
"How many nights would you like to spend there? "))
        break
    except ValueError:
        print("Please enter a round number...")
print(f"you are about to spend {num_nights} nights in {choice}...Nice trip!")
hotel_cost(city_flight)

#We ask for the car rental
while True:
    global rental_days
    try:
        rental_days = int(input(\
"For how many days would you like to rent a car? "))
        break
    except ValueError:
        print("Please enter a round number...")
print(f"\
You will spend {num_nights} nights & drive {rental_days} days. Adventurous!")
car_rental()

# Here we output the total and the detail of the trip
holiday_cost()