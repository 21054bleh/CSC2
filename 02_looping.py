# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3

# loop to see tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("Please enter your name or 'xxx, to quit: ")

    tickets_sold += 1

    if name == 'xxx':
        break

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("congratulations you have sold all the tickets")

else:
    print("you have sole {} ticket/s.  There is {} ticket/s ramaining").format(tickets_sold, MAX_TICKETS - tickets_sold)