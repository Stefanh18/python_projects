# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, type):
    while True:
        inp_t = input(prompt)
        try:
            type(inp_t)
            return inp_t
            break
        except ValueError:
            a_type = type
            print("Error: please enter a value of ", a_type)

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

