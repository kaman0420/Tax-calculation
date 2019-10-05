# Question 1
print("***Tax Calculator***")
print()

# RESIDENTS TAX RATES 2019-20
# Taxable income: 0 – $18,200; Tax on this income: Nil
# Taxable income: $18,201 – $37,000; Tax on this income: 19c for each $1 over $18,200
# Taxable income: $37,001 – $90,000; Tax on this income: $3,572 plus 32.5c for each $1 over $37,000   
# Taxable income: $90,001 – $180,000; Tax on this income: $20,797 plus 37c for each $1 over $90,000
# Taxable income: $180,001 and over; Tax on this income: $54,097 plus 45c for each $1 over $180,000

# NON-RESIDENTS TAX RATES 2019-20
# Taxable income: 0 – $90,000; Tax on this income: 32.5c for each $1
# Taxable income: $90,001 – $180,000; Tax on this income: $29,250 plus 37c for each $1 over $90,000
# Taxable income: $180,001 and over; Tax on this income: $62,550 plus 45c for each $1 over $180,000

# ask whether the user is a resident or not
input_taxpayer = input ("Are you resident for tax purposes (Y/N)?: ") #user input for input_taxpayer = "N"

# ask the user the taxable income
input_taxable_income = input ("Enter your total taxable income (in AUD): ") # user input for input_taxable_income = 90000.50​
taxable_income = float (input_taxable_income) # convert input_taxable_income into decimal number

if ((input_taxpayer == "Y") or (input_taxpayer == "y")): 
# calcute the income tax amount for RESIDENTS
    if (taxable_income >= 180001):
        income_tax = 54097 + 0.45 * (taxable_income - 180000)
      
    elif (taxable_income >= 90001):
        income_tax = 20797 + 0.37 * (taxable_income - 90000)
      
    elif (taxable_income >= 37001):
        income_tax = 3572 + 0.325 * (taxable_income - 37000)
      
    elif (taxable_income >= 18201):
        income_tax = 0.19 * (taxable_income - 18200)

    else:
        income_tax = "Nil"

else: 
# calcute the income tax amount for NON-RESIDENTS
    if (taxable_income >= 180001):
        income_tax = 62550  + 0.45 * (taxable_income - 180000)

    elif (taxable_income >= 90001):
        income_tax = 29250 + 0.37 * (taxable_income - 90000)

    else:
        income_tax = taxable_income * 0.325

after_tax_income = taxable_income - income_tax
after_tax_income_per_week = after_tax_income/12

# user output for income_tax
print("Your tax is: ${0}".format(income_tax))

print("Your after-tax income is: ${0}".format(after_tax_income))
print("Your after-tax income per week is:{0}".format(round(after_tax_income_per_week,2)))
