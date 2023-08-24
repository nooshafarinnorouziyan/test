class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"
        
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

date = Date(1, 5, 2022)
print(date) 
print(date.is_leap_year())

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return self.show()
        
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def show(self):
        return f"{self.day}/{self.month}/{self.year}"
        
date = Date(1, 5, 2022)
print(date)  
print(date.is_leap_year()) 

import datetime

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return self.show()
        
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def show(self):
        return f"{self.day}/{self.month}/{self.year}"
        
    def add(self, other):
        date1 = datetime.date(self.year, self.month, self.day)
        date2 = datetime.date(other.year, other.month, other.day)
        delta = date2 - date1
        new_year = self.year + int(delta.days/365)
        new_month = self.month
        new_day = self.day + (delta.days%365)
        if (self.is_leap_year() and (self.month >= 3)) or (other.is_leap_year() and (other.month < 3)):
            new_day += 1
        while new_day > 365:
            if self.is_leap_year():
                new_day -= 366
                new_year += 1
            else:
                new_day -= 365
                new_year += 1
        new_date = Date(new_day, new_month, new_year)
        return new_date

date1 = Date(1, 5, 2022)
date2 = Date(30, 6, 2022)
new_date = date1.add(date2)
print(new_date) 


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return self.show()
        
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
        
    def show(self):
        return f"{self.day}/{self.month}/{self.year}"
        
    def add(self, other):
        date1 = datetime.date(self.year, self.month, self.day)
        date2 = datetime.date(other.year, other.month, other.day)
        delta = date2 - date1
        new_year = self.year + int(delta.days/365)
        new_month = self.month
        new_day = self.day + (delta.days%365)
        if (self.is_leap_year() and (self.month >= 3)) or (other.is_leap_year() and (other.month < 3)):
            new_day += 1
        while new_day > 365:
            if self.is_leap_year():
                new_day -= 366
                new_year += 1
            else:
                new_day -= 365
                new_year += 1
        new_date = Date(new_day, new_month, new_year)
        return new_date
    
    def sub(self, other):
        date1 = datetime.date(self.year, self.month, self.day)
        date2 = datetime.date(other.year, other.month, other.day)
        delta = date2 - date1
        return delta.days

date1 = Date(1, 5, 2022)
date2 = Date(30, 6, 2022)
diff = date2.sub(date1)
print(diff)