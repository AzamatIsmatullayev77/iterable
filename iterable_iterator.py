from typing import Optional


class MyRange:
    def __init__(self, stop, start: Optional[int] = None,
                 step: Optional[int] = None):
        self.start = start or 0
        self.stop = stop
        self.step = step or 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start < self.stop:
                current = self.start
                self.start += self.step
                return current
            else:
                print('stop must be greater then start')
                raise StopIteration

        elif self.step < 0:
            if self.start > self.stop:
                current = self.start
                self.start += self.step
                return current
            else:
                raise StopIteration
        else:
            print('error')

#
# my_range = MyRange(start=100, stop=0, step=-1)
# for number in my_range:
#     print(number)


class Fibonacci():
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return result
        else:
            raise StopIteration


my_fib = Fibonacci(10)
for fib in my_fib:
    print(fib)
