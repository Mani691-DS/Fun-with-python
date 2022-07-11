import random

str_inp = input("Enter the customer names with commas separated between them:- ")
str_spl = str_inp.split(",")
str_ran = random.choice(str_spl)
print(f"{str_ran} is going to pay today's bill")

#random bill generator with the names given with a comma 
