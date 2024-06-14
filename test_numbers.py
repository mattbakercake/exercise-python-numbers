import unittest
import number_string

class NumberStringTestCase(unittest.TestCase):

    # test number factory method returns correct implementation
    def test_number_factory_1(self):
        num = number_string.NumberString(1)
        self.assertEqual(num.factory_method(),number_string.NumStringifySingle)
    
    def test_number_factory_99(self):
        num = number_string.NumberString(99)
        self.assertEqual(num.factory_method(),number_string.NumStringifyTens)
    
    def test_number_factory_100(self):
        num = number_string.NumberString(100)
        self.assertEqual(num.factory_method(),number_string.NumStringifyHundreds)
    
    def test_number_factory_999(self):
        num = number_string.NumberString(999)
        self.assertEqual(num.factory_method(),number_string.NumStringifyHundreds)
    
    def test_number_factory_1000(self):
        num = number_string.NumberString(1000)
        self.assertEqual(num.factory_method(),number_string.NumStringifyThousands)
    
    def test_number_factory_99999(self):
        num = number_string.NumberString(99999)
        self.assertEqual(num.factory_method(),number_string.NumStringifyTensThousands)

    def test_number_factory_100000(self):
        num = number_string.NumberString(100000)
        self.assertEqual(num.factory_method(),number_string.NumStringifyHundredsThousands)
    
    def test_number_factory_1000000(self):
        num = number_string.NumberString(1000000)
        self.assertEqual(num.factory_method(),number_string.NumStringifyMillions)

    def test_number_factory_10000000(self):
        num = number_string.NumberString(10000000)
        self.assertEqual(num.factory_method(),number_string.NumStringifyTensMillions)
    
    def test_number_factory_999999999(self):
        num = number_string.NumberString(999999999)
        self.assertEqual(num.factory_method(),number_string.NumStringifyHundredsMillions)
    
    def test_number_factory_1000000000(self):
        num = number_string.NumberString(1000000000)
        self.assertEqual(num.factory_method(),number_string.NumStringifyBillions)

    def test_number_factory_10000000000(self):
        num = number_string.NumberString(10000000000)
        self.assertEqual(num.factory_method(),number_string.NumStringifyTensBillions)
    
    def test_number_factory_999999999999(self):
        num = number_string.NumberString(999999999999)
        self.assertEqual(num.factory_method(),number_string.NumStringifyHundredsBillions)

    #test NumStringifyTens implementation works
    def test_NumStringifyTens_1(self):
        self.assertEqual(number_string.NumberString(1).stringifier().string,'One')

    def test_NumStringifyTens_10(self):
        self.assertEqual(number_string.NumberString(10).stringifier().string,'Ten')

    def test_NumStringifyTens_19(self):
        self.assertEqual(number_string.NumberString(19).stringifier().string,'Nineteen')

    def test_NumStringifyTens_20(self):
        self.assertEqual(number_string.NumberString(20).stringifier().string,'Twenty')

    #test NumStringifyHundreds implementation works
    def test_NumStringifyHundreds_100(self):
        self.assertEqual(number_string.NumberString(100).stringifier().string,'One Hundred')
    
    def test_NumStringifyHundreds_500(self):
        self.assertEqual(number_string.NumberString(500).stringifier().string,'Five Hundred')

    def test_NumStringifyHundreds_203(self):
        self.assertEqual(number_string.NumberString(203).stringifier().string,'Two Hundred and Three')
    
    def test_NumStringifyHundreds_220(self):
        self.assertEqual(number_string.NumberString(220).stringifier().string,'Two Hundred and Twenty')

    def test_NumStringifyHundreds_999(self):
        self.assertEqual(number_string.NumberString(999).stringifier().string,'Nine Hundred and Ninety Nine')

    #test NumStringifyThousands implementation works
    def test_NumStringifyThousands_1000(self):
        self.assertEqual(number_string.NumberString(1000).stringifier().string,'One Thousand')

    def test_NumStringifyThousands_1001(self):
        self.assertEqual(number_string.NumberString(1001).stringifier().string,'One Thousand and One')

    def test_NumStringifyThousands_1100(self):
        self.assertEqual(number_string.NumberString(1100).stringifier().string,'One Thousand One Hundred')

    def test_NumStringifyThousands_1101(self):
        self.assertEqual(number_string.NumberString(1101).stringifier().string,'One Thousand One Hundred and One')
    
    def test_NumStringifyThousands_1111(self):
        self.assertEqual(number_string.NumberString(1111).stringifier().string,'One Thousand One Hundred and Eleven')
    
    def test_NumStringifyThousands_9999(self):
        self.assertEqual(number_string.NumberString(9999).stringifier().string,'Nine Thousand Nine Hundred and Ninety Nine')

    def test_NumStringifyThousands_100000(self):
        self.assertEqual(number_string.NumberString(100000).stringifier().string,'One Hundred Thousand')
    
    def test_NumStringifyThousands_100001(self):
        self.assertEqual(number_string.NumberString(100001).stringifier().string,'One Hundred Thousand and One')

    def test_NumStringifyThousands_101001(self):
        self.assertEqual(number_string.NumberString(101001).stringifier().string,'One Hundred and One Thousand and One')

    def test_NumStringifyThousands_100100(self):
        self.assertEqual(number_string.NumberString(100100).stringifier().string,'One Hundred Thousand One Hundred')
    
    def test_NumStringifyThousands_101100(self):
        self.assertEqual(number_string.NumberString(101100).stringifier().string,'One Hundred and One Thousand One Hundred')
    
    def test_NumStringifyThousands_110100(self):
        self.assertEqual(number_string.NumberString(110100).stringifier().string,'One Hundred and Ten Thousand One Hundred')

    def test_NumStringifyThousands_999999(self):
        self.assertEqual(number_string.NumberString(999999).stringifier().string,'Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')
    
    #test NumStringifyMillions implementation works
    def test_NumStringifyMillions_1000000(self):
        self.assertEqual(number_string.NumberString(1000000).stringifier().string,'One Million')
    
    def test_NumStringifyMillions_1000001(self):
        self.assertEqual(number_string.NumberString(1000001).stringifier().string,'One Million and One')
    
    def test_NumStringifyMillions_1000100(self):
        self.assertEqual(number_string.NumberString(1000100).stringifier().string,'One Million One Hundred')

    def test_NumStringifyMillions_1001000(self):
        self.assertEqual(number_string.NumberString(1001000).stringifier().string,'One Million One Thousand')
    
    def test_NumStringifyMillions_1010000(self):
        self.assertEqual(number_string.NumberString(1010000).stringifier().string,'One Million Ten Thousand')
    
    def test_NumStringifyMillions_1100000(self):
        self.assertEqual(number_string.NumberString(1100000).stringifier().string,'One Million One Hundred Thousand')
    
    def test_NumStringifyMillions_10000000(self):
        self.assertEqual(number_string.NumberString(10000000).stringifier().string,'Ten Million')
    
    def test_NumStringifyMillions_10000001(self):
        self.assertEqual(number_string.NumberString(10000001).stringifier().string,'Ten Million and One')

    def test_NumStringifyMillions_10000100(self):
        self.assertEqual(number_string.NumberString(10000100).stringifier().string,'Ten Million One Hundred')

    def test_NumStringifyMillions_10001000(self):
        self.assertEqual(number_string.NumberString(10001000).stringifier().string,'Ten Million One Thousand')

    def test_NumStringifyMillions_10010000(self):
        self.assertEqual(number_string.NumberString(10010000).stringifier().string,'Ten Million Ten Thousand')

    def test_NumStringifyMillions_10100000(self):
        self.assertEqual(number_string.NumberString(10100000).stringifier().string,'Ten Million One Hundred Thousand')
    
    def test_NumStringifyMillions_55555555(self):
        self.assertEqual(number_string.NumberString(55555555).stringifier().string,'Fifty Five Million Five Hundred and Fifty Five Thousand Five Hundred and Fifty Five')
    
    def test_NumStringifyMillions_100000000(self):
        self.assertEqual(number_string.NumberString(100000000).stringifier().string,'One Hundred Million')

    def test_NumStringifyMillions_100000001(self):
        self.assertEqual(number_string.NumberString(100000001).stringifier().string,'One Hundred Million and One')

    def test_NumStringifyMillions_100000100(self):
        self.assertEqual(number_string.NumberString(100000100).stringifier().string,'One Hundred Million One Hundred')
    
    def test_NumStringifyMillions_100001000(self):
        self.assertEqual(number_string.NumberString(100001000).stringifier().string,'One Hundred Million One Thousand')

    def test_NumStringifyMillions_100010000(self):
        self.assertEqual(number_string.NumberString(100010000).stringifier().string,'One Hundred Million Ten Thousand')
    
    def test_NumStringifyMillions_100100000(self):
        self.assertEqual(number_string.NumberString(100100000).stringifier().string,'One Hundred Million One Hundred Thousand')
    
    def test_NumStringifyMillions_101000000(self):
        self.assertEqual(number_string.NumberString(101000000).stringifier().string,'One Hundred and One Million')
    
    def test_NumStringifyMillions_110000000(self):
        self.assertEqual(number_string.NumberString(110000000).stringifier().string,'One Hundred and Ten Million')
    
    def test_NumStringifyMillions_1542345(self):
        self.assertEqual(number_string.NumberString(1542345).stringifier().string,'One Million Five Hundred and Fourty Two Thousand Three Hundred and Fourty Five')

    def test_NumStringifyMillions_999999999(self):
        self.assertEqual(number_string.NumberString(999999999).stringifier().string,'Nine Hundred and Ninety Nine Million Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')

    # #test number billions implemntation works
    def test_NumStringifyBillions_1000000000(self):
        self.assertEqual(number_string.NumberString(1000000000).stringifier().string,'One Billion')
    
    def test_NumStringifyBillions_1000000001(self):
        self.assertEqual(number_string.NumberString(1000000001).stringifier().string,'One Billion and One')
    
    def test_NumStringifyBillions_1000000022(self):
        self.assertEqual(number_string.NumberString(1000000022).stringifier().string,'One Billion and Twenty Two')

    def test_NumStringifyBillions_1000000100(self):
        self.assertEqual(number_string.NumberString(1000000100).stringifier().string,'One Billion One Hundred')

    def test_NumStringifyBillions_1000000101(self):
        self.assertEqual(number_string.NumberString(1000000101).stringifier().string,'One Billion One Hundred and One')

    def test_NumStringifyBillions_1000001000(self):
        self.assertEqual(number_string.NumberString(1000001000).stringifier().string,'One Billion One Thousand')
    
    def test_NumStringifyBillions_1000001111(self):
        self.assertEqual(number_string.NumberString(1000001111).stringifier().string,'One Billion One Thousand One Hundred and Eleven')
    
    def test_NumStringifyBillions_1000010000(self):
        self.assertEqual(number_string.NumberString(1000010000).stringifier().string,'One Billion Ten Thousand')

    def test_NumStringifyBillions_1000022522(self):
        self.assertEqual(number_string.NumberString(1000022522).stringifier().string,'One Billion Twenty Two Thousand Five Hundred and Twenty Two')

    def test_NumStringifyBillions_1000100000(self):
        self.assertEqual(number_string.NumberString(1000100000).stringifier().string,'One Billion One Hundred Thousand')

    def test_NumStringifyBillions_1000152345(self):
        self.assertEqual(number_string.NumberString(1000152345).stringifier().string,'One Billion One Hundred and Fifty Two Thousand Three Hundred and Fourty Five')

    def test_NumStringifyBillions_1001000000(self):
        self.assertEqual(number_string.NumberString(1001000000).stringifier().string,'One Billion One Million')
    
    def test_NumStringifyBillions_1001542345(self):
        self.assertEqual(number_string.NumberString(1001542345).stringifier().string,'One Billion One Million Five Hundred and Fourty Two Thousand Three Hundred and Fourty Five')

    def test_NumStringifyBillions_1010000000(self):
        self.assertEqual(number_string.NumberString(1010000000).stringifier().string,'One Billion Ten Million')
    
    def test_NumStringifyBillions_1010345260(self):
        self.assertEqual(number_string.NumberString(1010345260).stringifier().string,'One Billion Ten Million Three Hundred and Fourty Five Thousand Two Hundred and Sixty')

    def test_NumStringifyBillions_1100000000(self):
        self.assertEqual(number_string.NumberString(1100000000).stringifier().string,'One Billion One Hundred Million')

    def test_NumStringifyBillions_1100000001(self):
        self.assertEqual(number_string.NumberString(1100000001).stringifier().string,'One Billion One Hundred Million and One')

    def test_NumStringifyBillions_10000000000(self):
        self.assertEqual(number_string.NumberString(10000000000).stringifier().string,'Ten Billion')
    
    def test_NumStringifyBillions_10000000001(self):
        self.assertEqual(number_string.NumberString(10000000001).stringifier().string,'Ten Billion and One')
    
    def test_NumStringifyBillions_10000000100(self):
        self.assertEqual(number_string.NumberString(10000000100).stringifier().string,'Ten Billion One Hundred')
    
    def test_NumStringifyBillions_10000001000(self):
        self.assertEqual(number_string.NumberString(10000001000).stringifier().string,'Ten Billion One Thousand')

    def test_NumStringifyBillions_10000010000(self):
        self.assertEqual(number_string.NumberString(10000010000).stringifier().string,'Ten Billion Ten Thousand')

    def test_NumStringifyBillions_10000100000(self):
        self.assertEqual(number_string.NumberString(10000100000).stringifier().string,'Ten Billion One Hundred Thousand')

    def test_NumStringifyBillions_10001000000(self):
        self.assertEqual(number_string.NumberString(10001000000).stringifier().string,'Ten Billion One Million')

    def test_NumStringifyBillions_10010000000(self):
        self.assertEqual(number_string.NumberString(10010000000).stringifier().string,'Ten Billion Ten Million')

    def test_NumStringifyBillions_10100000000(self):
        self.assertEqual(number_string.NumberString(10100000000).stringifier().string,'Ten Billion One Hundred Million')

    def test_NumStringifyBillions_11000000000(self):
        self.assertEqual(number_string.NumberString(11000000000).stringifier().string,'Eleven Billion')

    def test_NumStringifyBillions_100000000000(self):
        self.assertEqual(number_string.NumberString(100000000000).stringifier().string,'One Hundred Billion')
    
    def test_NumStringifyBillions_100000000001(self):
        self.assertEqual(number_string.NumberString(100000000001).stringifier().string,'One Hundred Billion and One')

    def test_NumStringifyBillions_100000000100(self):
        self.assertEqual(number_string.NumberString(100000000100).stringifier().string,'One Hundred Billion One Hundred')
    
    def test_NumStringifyBillions_100000001000(self):
        self.assertEqual(number_string.NumberString(100000001000).stringifier().string,'One Hundred Billion One Thousand')
    
    def test_NumStringifyBillions_100000010000(self):
        self.assertEqual(number_string.NumberString(100000010000).stringifier().string,'One Hundred Billion Ten Thousand')

    def test_NumStringifyBillions_100000100000(self):
        self.assertEqual(number_string.NumberString(100000100000).stringifier().string,'One Hundred Billion One Hundred Thousand')
    
    def test_NumStringifyBillions_100001000000(self):
        self.assertEqual(number_string.NumberString(100001000000).stringifier().string,'One Hundred Billion One Million')

    def test_NumStringifyBillions_100010000000(self):
        self.assertEqual(number_string.NumberString(100010000000).stringifier().string,'One Hundred Billion Ten Million')

    def test_NumStringifyBillions_100100000000(self):
        self.assertEqual(number_string.NumberString(100100000000).stringifier().string,'One Hundred Billion One Hundred Million')

    def test_NumStringifyBillions_101000000000(self):
        self.assertEqual(number_string.NumberString(101000000000).stringifier().string,'One Hundred and One Billion')

    def test_NumStringifyBillions_110000000000(self):
        self.assertEqual(number_string.NumberString(110000000000).stringifier().string,'One Hundred and Ten Billion')

    def test_NumStringifyBillions_111000000000(self):
        self.assertEqual(number_string.NumberString(111000000000).stringifier().string,'One Hundred and Eleven Billion')

    def test_NumStringifyBillions_999999999999(self):
        self.assertEqual(number_string.NumberString(999999999999).stringifier().string,'Nine Hundred and Ninety Nine Billion Nine Hundred and Ninety Nine Million Nine Hundred and Ninety Nine Thousand Nine Hundred and Ninety Nine')