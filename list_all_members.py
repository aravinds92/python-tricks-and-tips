from atlassian import Confluence

confluence = Confluence(
    url='https://confluence.solaredge.com',
    username=user_name
    password=password )


#Prints all members in the confluence object
d = dir(confluence)
for data in d:
    print(data)
