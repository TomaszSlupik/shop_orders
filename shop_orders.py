# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:26:16 2022

@author: Admin
"""

import sys

class Shop ():
    
    def __init__ (self, products):
        self.products = products
     
        
    def product_basket (self):
        print ('W Twoim koszyku są produkty:')
        for food in self.products:
            print (food)
     
    def add (self):
        self.name_products = input ("Jaki produkt chcesz dodać do zamówienia? ")
        if self.name_products not in self.products:
            self.products.append(self.name_products)
        print ('Produkt został dodany do zamówienia.')
            
    def delete (self):
        self.name_products = input ("Jaki chcesz usunąć produkt? ")
        if self.name_products in self.products:
            self.products.remove(self.name_products)
            print ('Usunięto produkt z Twojego koszyka')
        else:
            print ('Podanego produktu nie ma w Twoim koszyku.')
            
            
    
basket = Shop([])

while True:
    print ("")
    print ('Wprowadź 1 aby sprawdzić swój koszyk z zamówieniem.')
    print ('Wprowadź 2 aby dodać produkt do zamówienia.')
    print ('Wprowadź 3 aby usunąć produkt z zamówienia')
    print ('Wprowadź 4 aby zakończyć zamówienie')
    user = int (input('Proszę wybrać opcję:'))
    if user is 1:
        basket.product_basket()
    elif user is 2:
        basket.add()
    elif user is 3:
        basket.delete()
    else:
        sys.exit()
        