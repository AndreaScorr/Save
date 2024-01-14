#!/usr/bin/env python

class Person:
	
	def __init__(self,pets,address):
		
		self.pets=pets
		self.address=address
	
	def printData(self):
		print(self.pets)
		print(self.address)
	
	


def main():
	pets=["Dog","Cat"]
	address="via capramozza"
	
	person1=Person(pets,address)
	
	person1.printData()
	
	
	
main()
