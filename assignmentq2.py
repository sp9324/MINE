income=float(input("enter your income: "))
tax_rate=0.2
standard_deduction=10000
number_of_dep=int(input("enter number of deoendents: "))
additional_deduction=number_of_dep*3000
income_tax=income-standard_deduction-additional_deduction
print("income tax is: ", income_tax)