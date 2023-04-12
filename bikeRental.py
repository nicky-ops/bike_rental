import datetime

class BikeRental:
  def __init__(self, stock):
    self.stock = stock

  def displaystock(self):
    print(f"We currently have {self.stock} in stock")
    return self.stock

  def rentBikeOnHourlyBasis(self, n):
    if (n <= 0):
      print("Invalid number, the number of bikes should be positive!")
      return None
    elif n > self.stock:
      print(f"Sorry We currently do not have {self.stock } bikes available to rent.")
      return None
    else:
      now = datetime.datetime.now();
      print(f"You have rented {n} bike(s) on an hourly basis at {now.hour} hours")
      print("YOu will be charged $5 per hour per bike")
      print("We hope you will return our bikes in good condition. Thank you")
      self.stock -= n
      return now

  def rentBikeOnDailyBasis(self, n):
    if (n <= 0):
      print("Invalid number, the number of bikes should be positive!")
      return None
    elif n > self.stock:
      print(f"Sorry We currently do not have {self.stock } bikes available to rent.")
      return None
    else:
      now = datetime.datetime.now();
      print(f"You have rented {n} bike(s) on a daily basis at {now.hour} day")
      print("You will be charged $20 per day per bike")
      print("We hope you will return our bikes in good condition. Thank you")
      self.stock -= n
      return now

  def rentBikeOnWeeklyBasis(self, n):
    if (n <= 0):
      print("Invalid number, the number of bikes should be positive!")
      return None
    elif n > self.stock:
      print(f"Sorry We currently do not have {self.stock } bikes available to rent.")
      return None
    else:
      now = datetime.datetime.now()
      print(f"You have rented {n} bike(s) on a weekly basis at {now.hour} hours")
      print("You will be charged $40 per week per bike")
      print("We hope you will return our bikes in good condition. Thank you")
      self.stock -= n
      return now

  def returnBike(self, request):
    rentalTime, rentalBasis, numOfBikes = request
    bill = 0

    if rentalBasis and numOfBikes and rentalTime:
      self.stock += numOfBikes
      now = datetime.now();
      rentalPeriod = now - rentalTime

    if rentalBasis == 1:
      bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes

    elif rentalBasis == 2:
      bill = round(rentalPeriod.days) * 20 * numOfBikes

    elif rentalBasis == 3:
      bill = round(rentalPeriod.days / 7) * 60 * numOfBikes

    if (3 <= numOfBikes <= 5):
      print("You are eligible for a 30% family discount")
      bill *= 0.7
      
      print("Thank you for returning our bikes! Hope you had a great time")
      print(f"That would be {bill}")
    else:
      print("Are you sure you rented with us?")
      return None


class Customer:

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestBike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0