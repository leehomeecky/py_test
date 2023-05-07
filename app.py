from HTMLTableScraper import HTMLTableScraper, recursive_search, generate_binary_to_decimal, fibonacci_sum

#########################################################
############# colour test ###############################
#########################################################
scraper = HTMLTableScraper('https://drive.google.com/open?id=1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf')
mean = scraper.calculate_mean()
median = scraper.calculate_median()
mode = scraper.calculate_mode()
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")


#########################################################
############# recursive test ############################
#########################################################
# Prompt the user to enter a list of numbers and a target number
numbers = input("Enter a list of numbers, separated by commas: ").split(",")
numbers = [int(num) for num in numbers] # convert input to a list of integers
target = int(input("Enter the number you want to search for: "))

# Call the recursive_search function and print the result
result = recursive_search(numbers, target)
if result:
    print("The number {} was found in the list.".format(target))
else:
    print("The number {} was not found in the list.".format(target))
    

#########################################################
############# Binary to decimal test ####################
#########################################################
# Call the generate_binary_to_decimal function and print the results
binary, decimal = generate_binary_to_decimal()
print("Binary number: {}".format(binary))
print("Decimal equivalent: {}".format(decimal))


#########################################################
############# fibonacci test ############################
#########################################################
# Call the fibonacci_sum function and print the result
sum_50 = fibonacci_sum(50)
print("The sum of the first 50 Fibonacci numbers is:", sum_50)

