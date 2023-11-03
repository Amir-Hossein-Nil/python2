def grades():
    data = {}

    data_check = False
    while not data_check:
        data['first name'] = input('Enter your first name:\n')
        if not (data['first name'].isalpha()):
            print("Invalid entry!\n enter only letters")
            print("______________________________________")
            continue


        data['last name'] = input('Enter your last name:\n')

        if not (data['last name'].isalpha()):
            print("Invalid entry!\n enter only letters")
            print("______________________________________")
        else:
            data_check = True

    data_check_age = False
    while not data_check_age:
        try:
            data['age'] = int(input('Enter your age:\n'))
            if data['age'] > 100:
                print("Please enter your real age !!")
                continue
            data_check_age = True
        except ValueError:
            print("Please enter a valid value")

    data_check_math = False
    while not data_check_math:
        try:
            data['math grade'] = float(input('Enter your math grade:\n'))
            if data['math grade'] > 20:
                print("enter your grade as 20")
                continue
            data_check_math = True
        except ValueError:
            print("Please enter a valid value")

    data_check_physic = False
    while not data_check_physic:
        try:
            data['physic grade'] = float(input('Enter your physic grade:\n'))
            if data['physic grade'] > 20:
                print("enter your grade as 20")
                continue
            data_check_physic = True
        except ValueError:
            print("Please enter a valid value")

    data_check_chemistry = False
    while not data_check_chemistry:
        try:
            data['chemistry grade'] = float(input('Enter your chemistry grade:\n'))
            if data['chemistry grade'] > 20:
                print("enter your grade as 20")
                continue
            data_check_chemistry = True
        except ValueError:
            print("Please enter a valid value")

    return data
