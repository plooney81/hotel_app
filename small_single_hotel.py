# the goal of the small excercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

hotel = [{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
},
{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
},
{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
         }
    },
    '105': {},
}] 



#function that checks to see if the room is vacant in the hotel
def is_vacant(hotel, room, hotel_numb):
    if 'guest' in hotel[hotel_numb][room]:
        return 'Room is occupied'
    else:
        return 'Room is empty'

# function that checks a guest in given the desired_room, the guest info (in dictionary format), and the dictionary itself
def check_in(desired_room, guest_info_dictionary, dictionary, hotel_numb):
    for room in dictionary[hotel_numb]:
        if room == desired_room:
            dictionary[room]['guest'] = guest_info_dictionary
    return dictionary

# function that checks out a guest
def checkout():
    checking_out = []
    y = "y"
    y2 = "y2"
    while y2 == 'y2':
        takes_a_index = int(input("Which hotel are they staying in? "))
        if takes_a_index < len(hotel):
            which_hotel = hotel[takes_a_index]
            y2 = ''
        else:
            print("I didn't catch that.")
    while y == 'y':
        takes_a_key = input("What room number is checking out? ")
        if takes_a_key in which_hotel:
            checking_out.append(which_hotel[takes_a_key])
            which_hotel[takes_a_key] = {}
            print(f"Our current roster in this hotel is\n\n{which_hotel}\n\nGuests currently checking out are \n\n{checking_out}\n")
            y = input("Is someone else checking out? [y/n]: ")
        else:
            print("I didn't catch that.")
    return checking_out


# example_dictionary_guest_info = {
#             'name': 'John Doe',
#             'phone': 8675309
#         }

# hotel = check_in("102", example_dictionary_guest_info, hotel)

# print(hotel)

# main menue
while True:
    user_input = input('What would you like to?\n1.Print hotel room status(print)\n2.Check in customer(check in)\n3.Check out customer(check out)\n4.Quit(quit)\n> ').lower()
    if user_input == 'print':
        y3 = "y2"
        while y3 == 'y2':
            takes_a_index = int(input("Which hotel are they staying in? "))
            if takes_a_index < len(hotel):
                which_hotel = hotel[takes_a_index]
                y3 = ''
            else:
                print("I didn't catch that.")
        room_number = input('What room number would you like check on?')
        print(is_vacant(hotel, room_number, takes_a_index))