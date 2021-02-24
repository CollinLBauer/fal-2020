class Date:
    """Represents a date composed of a day, month, and year."""
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def is_leap_day(self):
        """Returns whether or not this date represents a leap day."""
        return self.month == 2 and self.day == 29

    def is_before(self, other):
        """Returns whether or not this date occurs before a specified date."""
        same_month = self.month == other.month and self.day < other.day
        same_year = self.year == other.year and (self.month < other.month or same_month)
        return self.year < other.year or same_year

    def __str__(self):
        return "{:02}/{:02}/{}".format(self.month, self.day, self.year)


def main():
    pass


main()