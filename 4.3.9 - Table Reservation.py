"""
This program ask user for their name (cannot print floats or interger),
then check if the user's input matches with the reservation_name. If it does
it would print "Right this way!", if not it would print something else.
"""
userName = str(input('Name: '))
reservation_name = "Kolton"
if userName == reservation_name:
    print ("Right this way!")
else:
    print ("Sorry, we don't have a reservation under that name.")
