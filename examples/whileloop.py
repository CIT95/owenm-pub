stopped = False
while not stopped:
    print("Something")  # You can put anything here
    continue_running = input('Would you like to continue? (y/n)')
    if continue_running == 'n':
        stopped = True
