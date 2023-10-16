"""This module is for the purpose of manipulating data so that we can provide useful
information for the collaborative algorithm"""

"""This Function is to get all user data based off of the users id"""
def GetUserData(id):
    result = []  # A list to store the tuples

    with open('hetrec2011-lastfm-2k/user_artists.dat', 'r') as file:
        first_line = True 
        for line in file:
            if first_line:
                first_line = False
                continue 

            numbers = line.strip().split()

            if len(numbers) != 3:
                continue

            num1, num2, num3 = map(int, numbers) 

            if id == num1:
                result.append((num2, num3))

    return result

"""This Function gets the artists name based off of its artist id"""
def GetArtistName(id):
    with open('hetrec2011-lastfm-2k/artists.dat', 'r') as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                continue

            data = line.strip().split()
            name = data[1]

            if id == int(data[0]):
                for word in data[2:]:
                    if "http" in word:
                        return name

                    name = name + " " + word

                return name

    return "Name not in database"

"""This Function gets the artists id based off of the artists name"""
def GetArtistId(name):
    with open('hetrec2011-lastfm-2k/artists.dat', 'r') as file:
        first_line = True
        for line in file:
            if first_line:
                first_line = False
                continue

            data = line.strip().split()
            temp_name = ""
            for word in data[1:]:
                if "http" not in word: 
                    if temp_name == "":
                        temp_name = temp_name + word
                    else:
                        temp_name = temp_name + " " + word

            if name == temp_name:
                return data[0]

    return "Name not in database"


print(GetUserData(3))
print(GetArtistName(1))
print(GetArtistId("MALICE MIZER"))
