import unittest
import number_string

class NumberStringTestCase(unittest.TestCase):

    # test number factory method returns correct implementation
    def test_number_factory_1(self):
        num = number_string.NumberString(1)
        self.assertEqual(num.factory_implementation(),number_string.NumberTens)
    
    def test_number_factory_99(self):
        num = number_string.NumberString(99)
        self.assertEqual(num.factory_implementation(),number_string.NumberTens)
    
    def test_number_factory_100(self):
        num = number_string.NumberString(100)
        self.assertEqual(num.factory_implementation(),number_string.NumberHundreds)
    
    def test_number_factory_999(self):
        num = number_string.NumberString(999)
        self.assertEqual(num.factory_implementation(),number_string.NumberHundreds)
    
    def test_number_factory_1000(self):
        num = number_string.NumberString(1000)
        self.assertEqual(num.factory_implementation(),number_string.NumberThousands)
    
    def test_number_factory_999999(self):
        num = number_string.NumberString(999999)
        self.assertEqual(num.factory_implementation(),number_string.NumberThousands)
    
    def test_number_factory_1000000(self):
        num = number_string.NumberString(1000000)
        self.assertEqual(num.factory_implementation(),number_string.NumberMillions)
    
    def test_number_factory_999999999(self):
        num = number_string.NumberString(999999999)
        self.assertEqual(num.factory_implementation(),number_string.NumberMillions)
    
    def test_number_factory_1000000000(self):
        num = number_string.NumberString(1000000000)
        self.assertEqual(num.factory_implementation(),number_string.NumberBillions)
    
    def test_number_factory_999999999999(self):
        num = number_string.NumberString(999999999999)
        self.assertEqual(num.factory_implementation(),number_string.NumberBillions)

    # test NumberTens implementation works
    def test_numberTens_1(self):
        num = number_string.NumberString(1)
        self.assertEqual(num.string,'One')

    def test_numberTens_10(self):
        num = number_string.NumberString(10)
        self.assertEqual(num.string,'Ten')

    def test_numberTens_19(self):
        num = number_string.NumberString(19)
        self.assertEqual(num.string,'Nineteen')

    def test_numberTens_20(self):
        num = number_string.NumberString(20)
        self.assertEqual(num.string,'Twenty')

    # test NumberHundreds implementation works
    def test_numberHundreds_100(self):
        num = number_string.NumberString(100)
        self.assertEqual(num.string,'One Hundred')
    
    def test_numberHundreds_500(self):
        num = number_string.NumberString(500)
        self.assertEqual(num.string,'Five Hundred')

    def test_numberHundreds_203(self):
        num = number_string.NumberString(203)
        self.assertEqual(num.string,'Two Hundred and Three')
    
    def test_numberHundreds_220(self):
        num = number_string.NumberString(220)
        self.assertEqual(num.string,'Two Hundred and Twenty')

    def test_numberHundreds_999(self):
        num = number_string.NumberString(999)
        self.assertEqual(num.string,'Nine Hundred and Ninety Nine')

    #test NumberThousands implementation works
    def test_numberThousands_1000(self):
        num = number_string.NumberString(1000)
        self.assertEqual(num.string,'One Thousand')

    def test_numberThousands_1001(self):
        num = number_string.NumberString(1001)
        self.assertEqual(num.string,'One Thousand and One')

    def test_numberThousands_1100(self):
        num = number_string.NumberString(1100)
        self.assertEqual(num.string,'One Thousand One Hundred')

    def test_numberThousands_1101(self):
        num = number_string.NumberString(1101)
        self.assertEqual(num.string,'One Thousand One Hundred and One')
    
    def test_numberThousands_1111(self):
        num = number_string.NumberString(1111)
        self.assertEqual(num.string,'One Thousand One Hundred and Eleven')
    
    def test_numberThousands_9999(self):
        num = number_string.NumberString(9999)
        self.assertEqual(num.string,'Nine Thousand Nine Hundred and Ninety Nine')

    def test_numberThousands_100000(self):
        num = number_string.NumberString(100000)
        self.assertEqual(num.string,'One Hundred Thousand')
    
    def test_numberThousands_100001(self):
        num = number_string.NumberString(100001)
        self.assertEqual(num.string,'One Hundred Thousand and One')

    def test_numberThousands_101001(self):
        num = number_string.NumberString(101001)
        self.assertEqual(num.string,'One Hundred and One Thousand and One')

    def test_numberThousands_100100(self):
        num = number_string.NumberString(100100)
        self.assertEqual(num.string,'One Hundred Thousand One Hundred')
    
    def test_numberThousands_101100(self):
        num = number_string.NumberString(101100)
        self.assertEqual(num.string,'One Hundred and One Thousand One Hundred')
    
    def test_numberThousands_110100(self):
        num = number_string.NumberString(110100)
        self.assertEqual(num.string,'One Hundred and Ten Thousand One Hundred')

    def test_numberThousands_999999(self):
        num = number_string.NumberString(999999)
        self.assertEqual(num.string,'Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')
    
    #test NumberMillions implementation works
    def test_numberMillions_1000000(self):
        num = number_string.NumberString(1000000)
        self.assertEqual(num.string,'One Million')
    
    def test_numberMillions_1000001(self):
        num = number_string.NumberString(1000001)
        self.assertEqual(num.string,'One Million and One')
    
    def test_numberMillions_1000100(self):
        num = number_string.NumberString(1000100)
        self.assertEqual(num.string,'One Million One Hundred')

    def test_numberMillions_1001000(self):
        num = number_string.NumberString(1001000)
        self.assertEqual(num.string,'One Million One Thousand')
    
    def test_numberMillions_1010000(self):
        num = number_string.NumberString(1010000)
        self.assertEqual(num.string,'One Million Ten Thousand')
    
    def test_numberMillions_1100000(self):
        num = number_string.NumberString(1100000)
        self.assertEqual(num.string,'One Million One Hundred Thousand')
    
    def test_numberMillions_10000000(self):
        num = number_string.NumberString(10000000)
        self.assertEqual(num.string,'Ten Million')
    
    def test_numberMillions_55555555(self):
        num = number_string.NumberString(55555555)
        self.assertEqual(num.string,'Fifty Five Million Five Hundred and Fifty Five Thousand Five Hundred and Fifty Five')
    
    def test_numberMillions_100000001(self):
        num = number_string.NumberString(100000001)
        self.assertEqual(num.string,'One Hundred Million and One')

    def test_numberMillions_900000000(self):
        num = number_string.NumberString(900000000)
        self.assertEqual(num.string,'Nine Hundred Million')

    def test_numberMillions_999999999(self):
        num = number_string.NumberString(999999999)
        self.assertEqual(num.string,'Nine Hundred and Ninety Nine Million Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')

    #test number billions implemntation works
    def test_numberBillions_1000000000(self):
        num = number_string.NumberString(1000000000)
        self.assertEqual(num.string,'One Billion')
    
    def test_numberBillions_1000000001(self):
        num = number_string.NumberString(1000000001)
        self.assertEqual(num.string,'One Billion and One')
    
    def test_numberBillions_1000000022(self):
        num = number_string.NumberString(1000000022)
        self.assertEqual(num.string,'One Billion and Twenty Two')

    def test_numberBillions_1000000100(self):
        num = number_string.NumberString(1000000100)
        self.assertEqual(num.string,'One Billion One Hundred')

    def test_numberBillions_1000000101(self):
        num = number_string.NumberString(1000000101)
        self.assertEqual(num.string,'One Billion One Hundred and One')

    def test_numberBillions_1000001000(self):
        num = number_string.NumberString(1000001000)
        self.assertEqual(num.string,'One Billion One Thousand')
    
    def test_numberBillions_1000001111(self):
        num = number_string.NumberString(1000001111)
        self.assertEqual(num.string,'One Billion One Thousand One Hundred and Eleven')
    
    def test_numberBillions_1000010000(self):
        num = number_string.NumberString(1000010000)
        self.assertEqual(num.string,'One Billion Ten Thousand')

    def test_numberBillions_1000022522(self):
        num = number_string.NumberString(1000022522)
        self.assertEqual(num.string,'One Billion Twenty Two Thousand Five Hundred and Twenty Two')

    def test_numberBillions_1000100000(self):
        num = number_string.NumberString(1000100000)
        self.assertEqual(num.string,'One Billion One Hundred Thousand')

    def test_numberBillions_1000152345(self):
        num = number_string.NumberString(1000152345)
        self.assertEqual(num.string,'One Billion One Hundred and Fifty Two Thousand Three Hundred and Fourty Five')

    def test_numberBillions_1001000000(self):
        num = number_string.NumberString(1001000000)
        self.assertEqual(num.string,'One Billion One Million')
    
    def test_numberBillions_1001542345(self):
        num = number_string.NumberString(1001542345)
        self.assertEqual(num.string,'One Billion One Million Five Hundred and Fourty Two Thousand Three Hundred and Fourty Five')

    def test_numberBillions_1010000000(self):
        num = number_string.NumberString(1010000000)
        self.assertEqual(num.string,'One Billion Ten Million')
    
    def test_numberBillions_1010345260(self):
        num = number_string.NumberString(1010345260)
        self.assertEqual(num.string,'One Billion Ten Million Three Hundred and Fourty Five Thousand Two Hundred and Sixty')

    def test_numberBillions_1100000000(self):
        num = number_string.NumberString(1100000000)
        self.assertEqual(num.string,'One Billion One Hundred Million')

    def test_numberBillions_1100000001(self):
        num = number_string.NumberString(1100000001)
        self.assertEqual(num.string,'One Billion One Hundred Million and One')

    def test_numberBillions_999999999999(self):
        num = number_string.NumberString(999999999999)
        self.assertEqual(num.string,'Nine Hundred and Ninety Nine Billion Nine Hundred and Ninety Nine Million Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')