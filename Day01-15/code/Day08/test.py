# from math import sqrt

# class Triangle(object):

# 	def __init__(self,a,b,c):
# 		self._a = a
# 		self._b = b
# 		self._c = c

# 	@staticmethod
# 	def is_valid(a,b,c):
# 		return a + b > c and b + c > a and a + c > b

# 	def perimeter(self):
# 		return self._a + self._b + self._c

# 	def area(self):
# 		half = self.perimeter() / 2
# 		return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

# def main():
# 	a,b,c = 3,4,5
# 	if Triangle.is_valid(a,b,c):
# 		t = Triangle(a,b,c)
# 		print(t.perimeter())
# 	else:
# 		print('无法构成三角形')

# if __name__ == '__main__':

# class Person(object):
# 	def __init__(self,name,age):
# 		self._name = name
# 		self._age = age

# 	@property
# 	def name(self):
# 		return self._name
	
# 	@property
# 	def age(self):
# 		return self._age
	
# 	@age.setter
# 	def age(self,age)
# 		self._age = age

# 	def play(self):
# 		print('%s正在愉快的玩耍.' % self._name)

# 	def watch_av(self):
# 		if self._age >= 18:
# 			print('%s正在观看爱情动作片。' % self._name)
# 		else:
# 			print('%s正在观看熊出没' % self._name)

# class Student(Person):
# 	def __init__(self,name,age,grade):
# 		super().__init__(name,age)
# 		self._grade = grade

# 	@property
# 	def grade(self):
# 		return self._grade
	
# 	@grade.setter
# 	def grade(self,grade)
# 	self._grade = grade

# 	def study(self,course):
# 		print('....')


# class Teacher(Person):
# 	def __init__(self,name,age,title):
# 		super.__init__(name,age)
# 		self._title = title

# 	@property
# 	def title(self):
# 		return self._title

# 	@title.setter
# 	def title(self,title):
# 		self._title = title

# 	def teach(self,course):
# 		print('======')

import pygame

def main():
	pygame.init()
	screen = pyname.display.set_mode(800,600)
	pyname.display.set_caption('大球吃小球')
	running = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

if __name__ == '__main__':
	main()		



