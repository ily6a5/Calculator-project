class Calculator():

    def plus(self, operand1, operand2):
        result = operand1 + operand2
        return result

    def minus(self, operand1, operand2):
        result = operand1 - operand2
        return result

    def multiply(self,operand1, operand2):
        result = operand1 * operand2
        return result

    def divide(self, operand1 ,operand2):
        result = operand1 /operand2
        return result

    def sec_divide(self,operand1,operand2):
        result = operand1 % operand2
        return result

    def power(self,operand1,operand2):
        result = operand1 ** operand2
        return result


calculator = Calculator()
calculator.plus(5, 0)
calculator.minus(4,3)
calculator.multiply(2,4)
calculator.divide(4,2)
print(calculator.sec_divide(3,2))
