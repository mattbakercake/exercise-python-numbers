from abc import ABC,abstractmethod
import math

class NumberString:

    # constructor
    def __init__(self,number):
        self.number = number #number supplied for conversion
        self.string_converter = self.factory_implementation()#instantiate number converter and create string
        self.string = self.string_converter(self.number).string

    # factory method to determine number class to implement
    def factory_implementation(self):
        
        length = len(str(self.number))
        if length < 3:
            return NumberTens
        if length == 3:
            return NumberHundreds
        if length >= 4 and length < 7:
            return NumberThousands
        if length >= 7 and length < 10:
            return NumberMillions
        if length >= 10 and length <= 12:
            return NumberBillions


class Number(ABC):
    unique_nums = {
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        10:"Ten",
        11:"Eleven",
        12:"Twelve",
        13:"Thirteen",
        14:"Fourteen",
        15:"Fifteen",
        16:"Sixteen",
        17:"Seventeen",
        18:"Eighteen",
        19:"Nineteen",
        20:"Twenty",
        30:"Thirty",
        40:"Fourty",
        50:"Fifty",
        60:"Sixty",
        70:"Seventy",
        80:"Eighty",
        90:"Ninety"
    }

    @property
    @abstractmethod
    def class_exponent(self):
        return
    
    # constructor
    def __init__(self,number):
        self.number = number
        self.remainder = self.number%pow(10,self.class_exponent)
        self.string = self.build_string()
    
    def first_digit(self):
        return (self.number-self.remainder)/pow(10,self.class_exponent)
    
    def num_length(self,number):
        return len(str(number))

    @abstractmethod
    def build_string(self):
        return

class NumberTens(Number):
    class_exponent = 1

    def build_string(self):
        #compound numbers (above 19)
        if self.number > 19 and self.remainder != 0:
            second_num = self.unique_nums[self.remainder]
            first_num = self.unique_nums[self.number-self.remainder]

            return first_num + ' ' + second_num
        
        #unique numbers (0-19 + round)
        return self.unique_nums[self.number]

class NumberHundreds(Number):
    class_exponent = 2

    def build_string(self):
        #first digit
        num_str = NumberTens(self.first_digit()).string + ' Hundred'

        #for numbers NOT round hundreds
        if self.remainder != 0:
            num_str = num_str + ' and ' + NumberTens(self.remainder).string

        return num_str

class NumberThousands(Number):
    class_exponent = 3

    def build_string(self):
        #text for first digit
        if self.num_length(self.number) <= 5:
            num_str = NumberTens(self.first_digit()).string #(one to tens thousands)
        else:
            num_str = NumberHundreds(self.first_digit()).string #(hundreds thousands)
            
        #round thousands
        if self.remainder == 0:
            num_str = num_str + ' Thousand'

        #for numbers NOT round thousands
        if self.remainder != 0:
            #remainder is tens
            if self.num_length(self.remainder) < 3:
                num_str = num_str + ' Thousand and ' + NumberTens(self.remainder).string
            
            #remainder is hundreds
            if self.num_length(self.remainder) == 3:
                num_str = num_str + ' Thousand ' + NumberHundreds(self.remainder).string

        return num_str

class NumberMillions(Number):
    class_exponent = 6

    def build_string(self):
        #first digit
        if self.num_length(self.number) < 9:
            num_str = NumberTens(self.first_digit()).string #(one to tens millions)
        else:
            num_str = NumberHundreds(self.first_digit()).string #(hundreds millions)

        #round millions
        if self.remainder == 0:
            num_str = num_str + ' Million'
        
        #for numbers NOT round millions
        if self.remainder != 0:
            #remainder is tens
            if self.num_length(self.remainder) < 3:
                num_str = num_str + ' Million and ' + NumberTens(self.remainder).string
            
            #remainder is hundreds
            if self.num_length(self.remainder) == 3:
                num_str = num_str + ' Million ' + NumberHundreds(self.remainder).string
            
            #remainder is thousands
            if self.num_length(self.remainder) >= 4:
                num_str = num_str + ' Million ' + NumberThousands(self.remainder).string

        return num_str

class NumberBillions(Number):
    class_exponent = 9

    def build_string(self):
        #first digit
        if self.num_length(self.number) < 12:
            num_str = NumberTens(self.first_digit()).string #(one to tens of billions)
        else:
            num_str = NumberHundreds(self.first_digit()).string #(hundreds of billions)

        #round billions
        if self.remainder == 0:
            num_str = num_str + ' Billion'
        
        # #for numbers NOT round billions
        if self.remainder != 0:
            #remainder is tens
            if self.num_length(self.remainder) < 3:
                num_str = num_str + ' Billion and ' + NumberTens(self.remainder).string
            
            #remainder is hundreds
            if self.num_length(self.remainder) == 3:
                num_str = num_str + ' Billion ' + NumberHundreds(self.remainder).string
            
            #remainder is thousands
            if self.num_length(self.remainder) >= 4 and self.num_length(self.remainder) <= 6:
                num_str = num_str + ' Billion ' + NumberThousands(self.remainder).string

            #remainder is millions
            if self.num_length(self.remainder) >= 7:
                num_str = num_str + ' Billion ' + NumberMillions(self.remainder).string

        return num_str