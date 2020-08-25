import json

# the goal of the small excercise is to get practice with the syntax for querying and manipulating the data in a single, nested dictionary.

hotels = [{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309,
            'paid' : 'yes'
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890,
            'paid' : 'no'
         }
    },
    '105': {},
},
{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309,
            'paid' : 'yes'
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890,
            'paid' : 'no'
         }
    },
    '105': {},
},
{
     '101': {
        'guest': {
            'name': 'Elliot Alderson',
            'phone': 8675309,
            'paid' : 'yes'
        }
    },
    '102': {},
    '103': {},
    '104': {
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890,
            'paid' : 'no'
         }
    },
    '105': {},
}] 

# function that checks if the hotel# exists
def which_hotel_stayin_in(hotel):
        while True:
            try:
                takes_a_index = int(input("> "))
                if takes_a_index > len(hotel) - 1 or takes_a_index < 0:
                    raise ValueError
                else:
                    return takes_a_index
            except ValueError:
                print("I didn't catch that.")

def which_room_staying_in(hotel, hotel_numb):
    room_number = input('Whats the room number?\n> ')
    while True:
        if room_number in hotel[hotel_numb]:
            return room_number
        else:
            room_number = input(f'That room number doesn\'t exist in hotel {hotel_numb}. Please try again.\n> ')

#function that checks to see if the room is vacant in the hotel
def is_vacant(hotel, room, hotel_numb):
    if 'guest' in hotel[hotel_numb][room]:
        return 'Room is occupied'
    else:
        return 'Room is empty'

# function that checks a guest in given the desired_room, the guest info (in dictionary format), and the dictionary itself
def check_in(desired_room, guest_info_dictionary, dictionary, hotel_numb):
    while True:
        if is_vacant(dictionary, desired_room, hotel_numb) == 'Room is empty':
            break
        else:
            desired_room = input('That room is not vacant, please input another room\n> ')
    for room in dictionary[hotel_numb]:
        if room == desired_room:
            dictionary[hotel_numb][room]['guest'] = guest_info_dictionary
    return dictionary

# function that checks out a guest
def checkout():
    checking_out = []
    y = "y"
    y2 = "y2"
    while y2 == 'y2':
        takes_a_index = int(input("Which hotel are they staying in? "))
        if takes_a_index < len(hotels) - 1:
            which_hotel = hotels[takes_a_index]
            y2 = ''
        else:
            print("I didn't catch that.")
    while y == 'y':
        takes_a_key = input("What room number is checking out? ")
        if takes_a_key in which_hotel and (hotels[takes_a_index][takes_a_key]["guest"]["paid"] == 'yes'):
            checking_out.append(which_hotel[takes_a_key])
            which_hotel[takes_a_key] = {}
            print(f"Our current roster in this hotel is\n\n{which_hotel}\n\nGuests currently checking out are \n\n{checking_out}\n")
            y = input("Is someone else checking out? [y/n]: ")
        elif takes_a_key in which_hotel and (hotels[takes_a_index][takes_a_key]["guest"]["paid"] == 'no'):
            print('This guest still needs to pay!')
            y = input("Is someone else checking out? [y/n]: ")
        else:
            print("I didn't catch that.")
    return checking_out

# funciton for the main menu
def main_menu(hotels):
    # main menue
    while True:
        user_input = input('\nWhat would you like to?\n1.Print hotel room status(print)\n2.Check in customer(check in)\n3.Check out customer(check out)\n4.Quit(quit)\n> ').lower()
        if user_input == 'print':
            hotel_counter = 1
            # takes_a_index = which_hotel_stayin_in(hotel)
            # room_number = which_room_staying_in(hotel, takes_a_index)
            # print(is_vacant(hotel, room_number, takes_a_index))
            for hotel in hotels:
                guest_counter = 1
                for room in hotel.keys(): 
                    if 'guest' in hotel[room]:
                        print(f"hotel {hotel_counter} guest number {guest_counter}: {hotel[room]['guest']['name']} is staying in room number {room}\n")
                        guest_counter += 1
                hotel_counter += 1
        elif user_input == 'check in':
            print('\nFirst we need the guests name:')
            user_name = input('> ')
            print('\nWe also need the guests phone number')
            user_phone = input('> ')
            # create a dictionary for the guest information
            guest_info_dictionary = {
                'name' : user_name,
                'phone' : user_phone
            }
            print('What hotel are they staying in?')
            takes_a_index = which_hotel_stayin_in(hotels)
            room_number = which_room_staying_in(hotels, takes_a_index)
            hotels = check_in(room_number, guest_info_dictionary, hotels, takes_a_index)
        elif user_input == 'check out':
            # guest_who_went_away = checkout()
            # print(guest_who_went_away)
            checkout()
        elif user_input == 'add':
            add_hotel()
        elif user_input == 'delete':
            delete_hotel()
        elif user_input == 'quit':
            break
        else:
            print('Invalid input, please type either print, check in, check out, or quit')






# open a new hotel
def add_hotel():
    while True:
        user_hotel = input('Would you like to add a hotel? ')
        #could potentially ask for room numbers, will do this later
        if user_hotel == 'yes':
            hotels.append({})
            print(hotels)
            break
        else:
            break

# close a hotel
def delete_hotel():
    counter = 1
    while True: 
        for hotel in hotels:
            print(f'Hotel {counter} is the {hotel}')
            counter += 1         
        user_input = int(input(f'What hotel would you like to delete?  \n')) - 1
        del hotels[user_input]
        delete_again = input('Would you like to delete another hotel? \n')
        if delete_again == 'yes':
            pass
        else:
            break


# # save room info into a json file
# def export_hotel(hotel):
#     print('Which hotel info would you like to export to an external file?')
#     hotel_number = which_hotel_stayin_in(hotel)
#     with open(f'{hotel_number}.txt', 'w') as outfile:
#         json.dump(hotel[hotel_number], outfile)

# # load room info from a json file
# def load_hotel():
#     open_again = "y"
#     while open_again == "y":
#         with open(input("What would you like to read? ") as hotel_file:
#         hotel_json = json.load(hotel_file)
#         print(hotel_json)
#         open_again = input("Would you like to look at a new file? [y/n]: ")

# export_hotel(hotel)

main_menu(hotels)