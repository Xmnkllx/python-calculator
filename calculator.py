class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b          # FIX #1: original was b - a

    def _neg(self, x):
        return self.subtract(0, x)

    def _abs(self, x):
        return x if x >= 0 else self._neg(x)

    def multiply(self, a, b):

        # FIX #2: original did not handle negative b
        abs_b = self._abs(b)
        result = 0
        for _ in range(abs_b):
            result = self.add(result, a)
        return self._neg(result) if b < 0 else result

    def _divmod_abs(self, a, b):
        """quotient & remainder of |a| / |b| using only + and -."""
        x, y = self._abs(a), self._abs(b)
        q = 0
        while x >= y:
            x = self.subtract(x, y)
            q = self.add(q, 1)
        return q, x

    def divide(self, a, b):

        # FIX #3: original had no zero check and broke on negatives
        if b == 0:
            raise ZeroDivisionError("division by zero")
        q, r = self._divmod_abs(a, b)
        if (a < 0) != (b < 0):          
            if r != 0:                  
                q = self.add(q, 1)
            return self._neg(q)
        return q

    def modulo(self, a, b):

        # FIX #4: original looped forever / wrong for negatives and b == 0
        if b == 0:
            raise ZeroDivisionError("modulo by zero")
        _, r = self._divmod_abs(a, b)
        if r == 0:
            return 0
        if b > 0:
            return r if a > 0 else self.subtract(b, r)
        # b < 0
        return self._neg(r) if a < 0 else self.add(b, r)



if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))