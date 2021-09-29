organization_name = input("Enter your favorite organization name to get its acronym: ")
the_acronym = ""
def acronym(word):
    the_acronym = ""
    splited_organization_name = organization_name.split()
    for i in splited_organization_name:
        the_acronym += i[0]
    return the_acronym.upper()     
print(acronym(organization_name))