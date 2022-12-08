
class CountFromBy:
	def __init__(self, v: int=0, i: int=1) -> None:
		self.val = v
		self.incr = i
	def increase(self) -> None:
		self.val += self.incr

a = CountFromBy()
a.increase()
a.increase()
a.increase()
print(a.val)
print(a)

print()

b = CountFromBy(100, 10)
b.increase()
b.increase()
b.increase()
print(b.val)
print(b)

