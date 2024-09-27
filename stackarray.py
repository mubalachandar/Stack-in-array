class StringReverser:
    def _init_(self, input_string):
        self.input_string = input_string
        self.stack = [None] * len(input_string)
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == len(self.stack) - 1

    def push(self):
        for char in self.input_string:
            if self.is_full():
                print("Stack Overflow")
            else:
                self.top += 1
                self.stack[self.top] = char

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
        else:
            reversed_string = ""
            while self.top >= 0:
                reversed_string += self.stack[self.top]
                self.top -= 1
            return reversed_string


input_string = input("Enter a string: ")
reverser = StringReverser(input_string)

reverser.push()
result= reverser.pop()

print("Reversed string:", result)