class Calculator:

    @staticmethod
    def devide(a, b, visitor):
        visitor(a, b)
        print('Answer:', a/b)

class Visitor:

    def __call__(cls, a, b):
        if b == 0:
            raise ZeroDivisionError("Personalized error message")

Calculator.devide(10, 2, Visitor())
Calculator.devide(10, 0, Visitor())
