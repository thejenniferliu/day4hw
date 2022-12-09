# Steps
# Create a function that will ask user for name and addresses and stores them in a dictionary
# Define an empty dictionary with which to work (global or local variable?)
# Begin a loop that will continue to ask a user for information until the user "quits"
# If the user does not quit, ask for a name and address and store the variables into variables
# Add information to the dictionary with name as the key and address as the value
# If the user does quit, end the loop
# Print out the information from the dictionary in a formatted way
# Execute/Call the function
def return_name_and_address():
    loaded_dictionary={}
    ans = 'yes'
    while ans != 'no':
        name = input("what is your name?")
        address = input("what is your address?")
        ans = input("would you like to continue? yes/no?")
        loaded_dictionary[name] = address
    for entries, entry in dict.items(loaded_dictionary):
        print(f"I'm {entries}, and i live at {entry}")
return_name_and_address()


person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']

def meet_time(this_list, *another_list):
    return list(set(this_list).intersection(*another_list))
print(meet_time(person1, person2, person3))


