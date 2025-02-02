class getString:
    def __init__(self, string):
        self.string = str(input("Enter a string: "))

class printString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

input_string = getString("").string
string_printer = printString(input_string)
print(string_printer)