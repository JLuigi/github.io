print("Welcome to the tip calculator\n")
total = float(input("What was the total bill? £"))
percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))

result = total * (percent/100 + 1) / split

end_result = round(result,2)
end_result = "{:.2f}".format(end_result)
print(f"Each person should pay: £{end_result}")
print("\nThanks for using this tip calculator")
input("\nPress enter to close")