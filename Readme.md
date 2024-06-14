# Integer to String Converter

Dusting off Python knowledge and delving a little bit into OOP within the language and in general.

Script takes an integer between 0-999999999999 converts it to a string representation e.g. 'One Hundred and One'

This approach attempts to leverage OOP practices to emulate a solution that would be maintainable and extendable.

Solution uses:
* Abstract class to provide base methods and enforce required child parameters
* Polymorphism - inheritance of abstract class for child stringify classes that generate strings(tens/hundreds/thousands etc) and method overloading.
* factory method pattern - NumberString class determines which stringify class object to instantiate.

To run tests:
* from same directory as test_numbers.py run `python3 -m unittest discover`

To convert a string from the terminal:
* from the same directory as number_string.py end the interactive python console `python3`
* include the module: `import number_string`
* call the NumberString class: e.g. `number_string.NumberString(1001).stringifier().string` will output 'One Thousand and One'