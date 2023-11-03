identity = {}

# dict[key] = value

identity['first_name'] = input("What`s your first name?\n")
identity['last_name'] = input("What`s your last name?\n")
identity['father`s_name'] = input("What`s your father`s name?\n")
identity['national_code'] = int(input("What`s your national_code?\n"))
identity['birth_date'] = int(input("What`s your birth_date?\n"))

print(identity.keys())

end = ""
while end != "end" :
    key = input("Please enter your key : \n")
    if key == 'end':
        end = "end"
    else :
        print(identity[key])

print('goodbye!\n See you later')
