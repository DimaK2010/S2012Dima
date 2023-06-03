[9:55] Андрій Применко

class Checker:
    def Check(self, function):
        def check(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
            except Exception as ex:
                print(ex)
            else:
                print("No exceptions")
        return check
    def Calculate(self, expression):
        return eval(expression)

[9:56] Андрій Применко

#4 - decorator
from decorator import Checker
checker = Checker()
calculate = checker.Check(checker.Calculate)
calculate("2+2")
#4 - decorator
from decorator import Checker
checker = Checker()
#calculate = checker.Check(checker.Calculate)
digit1 = input("Enter digit1: ")
digit2 = input("Enter digit2: ")
operation = input("Operation: ")
checker.Calculate(f"{digit1}{operation}{digit2}")
class Checker:
    def Check(self, *exc_types):
        def Check(function):

            def Check(*args, **kwargs):
                try:
                    print(function(*args, **kwargs))
                except (exc_types) as ex:
                    print(ex)
                else:
                    print("No exceptions")
            return Check
        return Check
    @Check(NameError, TypeError, SyntaxError, ZeroDivisionError)
    def Calculate(self, expression):
        return eval(expression)