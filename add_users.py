import random
import decimal

def get_names():
    names = []
    with open('names.txt', 'r') as file:
        for line in file.readlines():
            tokens = line.split(' ')
            name = [tokens[0], tokens[1].rstrip()] #remove newline char from end
            names.append(name)
    return names

def user_info(name):
    email = name[0].lower() + name[1].lower() + "@gmail.com"
    username = name[0].lower() + name[1].lower() + "1"
    password = "password"
    out_name = name[0] + " " + name[1]
    latitude = float(decimal.Decimal(random.randrange(40116410, 40116430))/1000000)
    longitude = float(decimal.Decimal(random.randrange(-88243395, -88243375))/1000000)

    print("{")
    print("\"email\" : \"%s\"," % email)
    print("\"username\" : \"%s\"," % username)
    print("\"password\" : \"%s\"," % password)
    print("\"name\" : \"%s\"," % out_name)
    print("\"latitude\" : \"%s\"," % latitude)
    print("\"longitude\" : \"%s\"," % longitude)
    print("},")

if __name__ == '__main__':
    names = get_names()
    for name in names:
        user_info(name)
