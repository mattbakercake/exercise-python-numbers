from abc import ABC,abstractmethod

class NumberString:
    '''Entry point - factory method determines stringify class required for specfic number'''
    def __init__(self, number):
        self.number = number
        self.validate_number()
    
    # factory method to determine number class to implement
    def factory_method(self):
        length = len(str(self.number))
        if length == 1:
            return NumStringifySingle
        if length == 2:
            return NumStringifyTens
        if length == 3:
            return NumStringifyHundreds
        if length == 4:
            return NumStringifyThousands
        if length == 5:
            return NumStringifyTensThousands
        if length == 6:
            return NumStringifyHundredsThousands
        if length == 7:
            return NumStringifyMillions
        if length == 8:
            return NumStringifyTensMillions
        if length == 9:
            return NumStringifyHundredsMillions
        if length == 10:
            return NumStringifyBillions
        if length == 11:
            return NumStringifyTensBillions
        if length == 12:
            return NumStringifyHundredsBillions
    
    #check number falls within spec for conversion
    def validate_number(self):
        if self.number < 0 or self.number > 999999999999:
            raise Exception("Number must be between 0 and 999999999999") 
        
    
    #return object from class determined by factory method
    def stringifier(self):
        stringifier = self.factory_method()
        return stringifier(self.number)


class NumStringify(ABC):
    '''Abstract stringify class specifies attributes and methods needed'''

    #unique numbers needed to build strings
    unique_nums = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five",
        6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve",
        13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen",
        18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Fourty", 
        50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"
    }

    #required property - base 10 exponent/power e.g. 10^x
    @property
    @abstractmethod
    def class_exponent(self):
        return
    
    #string representation of numerical group e.g. Hundred/Thousand etc.
    @property
    @abstractmethod
    def numerical_name(self):
        return
    
    #constructor
    def __init__(self,number):
        #initialise object variables
        self.string = None
        self.first_digit_string = None
        self.remainder_string = None
        self.number = number # number passed to object
        self.remainder = self.number%pow(10,self.class_exponent) #remainder of number after number group e.g 2 for 102
        self.stringify() #convert number passed in to string
    
    #extract first part of number e.g. 1 for 100/300 for 325000
    def get_first_digit(self):
        if self.class_exponent == 0:
            return self.number
         
        #slice n digits from end of number (n = exponent) 
        return int(str(self.number)[:-self.class_exponent])
    
    #return number of digits in number
    def num_length(self,number):
        return len(str(number))
    
    #fetches and sets string for first part of number e.g. 'One Hundred' for 102
    def set_first_digit(self):
        #get stringifier object from factory and first digit string
        stringifier = (NumberString(self.get_first_digit()).stringifier())
        #e.g. 1000 = 'One Thousand'
        if self.remainder == 0:
            self.first_digit_string = ' '.join([stringifier.string, self.numerical_name]).strip()
            return bool(False)#don't fetch remainder
        #e.g. 1100 = 'One Thousand' (set_remainder adds 'One Hundred')
        if self.remainder%100 == 0:
            self.first_digit_string = ' '.join([stringifier.string, self.numerical_name]).strip()
            return bool(True)#fetch remainder
        #e.g. 1001 = 'One' (set_remainder adds 'Thousand and One')
        if self.remainder > 0 and self.remainder < 100:
            self.first_digit_string = ' '.join([stringifier.string]).strip()
            return bool(True)#fetch remainder
        #e.g. 1101 = 'One Thousand' (set_remainder adds 'One Hundred and One')
        if self.remainder >= 100:
            self.first_digit_string = ' '.join([stringifier.string,self.numerical_name]).strip()
            return bool(True)#fetch remainder

    #fetches and sets string for the second part of number e.g. 'and Two' for 102
    def set_remainder(self):
        stringifier = (NumberString(self.remainder).stringifier())
        if self.remainder == 0:
            self.remainder_string = ''
            return
        if self.num_length(self.remainder) == 1 or self.num_length(self.remainder) == 2:
            self.remainder_string = ' '.join([self.numerical_name,'and',stringifier.string]).strip()  
            return
        if self.num_length(self.remainder) >= 3:
            self.remainder_string = ' '.join([stringifier.string]).strip() 
            return

    #builds and returns string for number passed in
    def stringify(self):
        remainder = self.set_first_digit()
        if (bool(remainder)):
            self.set_remainder()
            
        self.string =  ' '.join([self.first_digit_string, self.remainder_string or '']).strip()

class NumStringifyTensOfX(NumStringify):
    '''Extends abstract Numstringify for classes implementing e.g. tens of thousands'''

    def set_first_digit(self):
        #get stringifier object from factory and first digit string
        stringifier = (NumberString(self.get_first_digit()).stringifier())
        #e.g. 10000000 = 'Ten Million'
        if bool(self.remainder == 0):
            self.first_digit_string = ' '.join([stringifier.string, self.numerical_name]).strip()
            return bool(False)#don't fetch remainder
        #e.g. 10000100 = 'Ten Million' (set_remainder adds 'One Hundred'
        if self.remainder%100 == 0:
            self.first_digit_string = ' '.join([stringifier.string, self.numerical_name]).strip()
            return bool(True)#fetch remainder
        #e.g. 10000001 = 'Ten' (set_remainder adds 'Million and One')
        if self.remainder > 0 and self.remainder < 100 :
            self.first_digit_string = ' '.join([stringifier.string]).strip()
            return bool(True)#fetch remainder
        #e.g. 10000100 = 'Ten Million' (set_remainder adds 'One Hundred')
        if self.remainder >= 100:
            self.first_digit_string = ' '.join([stringifier.string, self.numerical_name]).strip()
            return bool(True)#fetch remainder
        
class NumStringifyHundredsX(NumStringify):
    '''Extends abstract Numstringify for classes implementing e.g. hundreds of thousands'''

    def set_first_digit(self):
        #get stringifier object from factory and first digit string
        stringifier = (NumberString(self.get_first_digit()).stringifier())
        #e.g. 100000000 = 'One Hundred Million'
        if bool(self.remainder == 0):
            self.first_digit_string = ' '.join([stringifier.string, self.numerical_name]).strip()
            return bool(False)#don't fetch remainder
        #e.g. 100000100 = 'One Hundred Million' (set_remainder adds 'One Hundred')
        if self.remainder%pow(10,self.class_exponent) == 0:
            self.first_digit_string = ' '.join([stringifier.string]).strip()
            return bool(True)#fetch remainder
        #e.g. 100000001 = 'One Hundred' (set_remainder adds 'Million and One')
        if self.remainder > 0 and self.remainder < 100:
            self.first_digit_string = ' '.join([stringifier.string]).strip()
            return bool(True)#fetch remainder
        if self.remainder >= 100 and self.remainder < (pow(10,self.class_exponent)*0.01):
            self.first_digit_string = ' '.join([stringifier.string,self.numerical_name]).strip()
            return bool(True)#fetch remainder
        #e.g. 101000000 = 'One Hundred and' (set_remainder adds 'One Million')
        if self.remainder >= (pow(10,self.class_exponent)*0.01):
            self.first_digit_string = ' '.join([stringifier.string,'and']).strip()
            return bool(True)#fetch remainder

#       
#child classes implement abstract stringify class directly or via NumStringifyTensOfX/NumStringifyHundredsOfX
#

class NumStringifySingle(NumStringify):
    '''Single digit numbers'''

    class_exponent = 0
    numerical_name = ''

    #overload super stringify method
    def stringify(self):
        self.string =  self.unique_nums[self.number]

class NumStringifyTens(NumStringify):
    '''Double digit numbers'''

    class_exponent = 1
    numerical_name = ''

    #overload super stringify method
    def stringify(self):
        #unique numbers (10-19 + round)
        if self.number <=19 or self.remainder == 0:
            self.string =  self.unique_nums[self.number]

        #compound numbers (above 19) are built from two strings
        if self.number > 19 and self.remainder != 0:
            self.first_digit_string = self.unique_nums[self.number-self.remainder]
            self.remainder_string = self.unique_nums[self.remainder]
            

            self.string =   ' '.join([self.first_digit_string, self.remainder_string]).strip()

class NumStringifyHundreds(NumStringify):
    '''Hundreds (extends NumStringify)'''

    class_exponent = 2
    numerical_name = 'Hundred'   

class NumStringifyThousands(NumStringify):
    '''Thousands (extends NumStringify)'''

    class_exponent = 3
    numerical_name = 'Thousand'

class NumStringifyTensThousands(NumStringifyTensOfX):
    '''Tens of Thousands (extends NumStringifyTensOfX)'''

    class_exponent = 4
    numerical_name = 'Thousand'

    #overload super get_first_digit method
    def get_first_digit(self):
        return int(str(self.number)[:-3])
        
    #overload super set_remainder method
    def set_remainder(self):
        #set self.remainder to last three digits and call super method
        self.remainder = int(str(self.remainder)[-3:])
        super().set_remainder()

class NumStringifyHundredsThousands(NumStringifyHundredsX):
    '''Tens of Thousands (extends NumStringifyHundredsOfX)'''

    class_exponent = 5
    numerical_name = 'Thousand'

    #overload super get_first_digit method
    def get_first_digit(self):
        return int(str(self.number)[:-5] + '00') #e.g. 100 for 110000

class NumStringifyMillions(NumStringify):
    '''Millions (extends NumStringify)'''

    class_exponent = 6
    numerical_name = 'Million'
        
class NumStringifyTensMillions(NumStringifyTensOfX):
    '''Tens of Millions (extends NumStringifyTensOfX)'''

    class_exponent = 7
    numerical_name = 'Million'
    
    #overload super get_first_digit method
    def get_first_digit(self):
        return int(str(self.number)[:-6]) #e.g. 10 for 10000000
    
    #overload super set_remainder method
    def set_remainder(self):
        #set self.remainder to last six digits and call super method
        self.remainder = int(str(self.remainder)[-6:])
        super().set_remainder()

class NumStringifyHundredsMillions(NumStringifyHundredsX):
    '''Hundreds of Millions (extends NumStringifyHundredsOfX)'''
    class_exponent = 8
    numerical_name = 'Million'
    
    #overload super get_first_digit method
    def get_first_digit(self):
        return int(str(self.number)[:-8] + '00') #e.g. 100 for 101000000
    
class NumStringifyBillions(NumStringify):
    '''Billions (extends NumStringify)'''

    class_exponent = 9
    numerical_name = 'Billion'

class NumStringifyTensBillions(NumStringify):
    '''Tens of Billions (extends NumStringifyTensOfX)'''

    class_exponent = 10
    numerical_name = 'Billion'

    #overload super get_first_digit method
    def get_first_digit(self):
        return int(str(self.number)[:-9])
    
    def set_remainder(self):
        #set self.remainder to last three digits and call super method
        self.remainder = int(str(self.remainder)[-9:])
        super().set_remainder()

class NumStringifyHundredsBillions(NumStringifyHundredsX):
    '''Hundreds of Billions (extends NumStringifyHundredsOfX)'''

    class_exponent = 11
    numerical_name = 'Billion'

    #overload super get_first_digit method
    def get_first_digit(self):
        return int(str(self.number)[:-11] + '00') #e.g. 100 for 102000000000