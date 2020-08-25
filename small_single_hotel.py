# the goal of the small excercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

hotel = {
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
}

def is_vacant(hotel, room):
    if 'guest' in hotel[room]:
        return 'Room is occupied'
    else:
        return 'Room is empty'


def check_in(desired_room, guest_info_dictionary, dictionary):
    for room in dictionary:
        if room == desired_room:
            dictionary[room]['guest'] = guest_info_dictionary
    
    return dictionary

def checkout():
    checking_out = []
    y = "y"
    while y == 'y':
        takes_a_key = input("What room number is checking out? ")
        if takes_a_key in hotel:
            checking_out.append(hotel[takes_a_key])
            hotel[takes_a_key] = {}
            print(f"Our current roster is\n\n{hotel}\n\nGuests currently checking out are \n\n{checking_out}\n")
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