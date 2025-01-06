with open("names.txt",'a+') as f:
    # names = f.read()
    # names_occurances = {}
    # for name in names:
    #     name = name.split("\n")[0]
    #     if name in names_occurances:
    #         names_occurances[name] = 1
    #     else:
    #         names_occurances[name] += 1
    
    # print(names_occurances)
    names_list = f.readlines()
    skywalker_list = []
    for name in names_list:
        if name == 'Luke':
            skywalker_list.append('Luke Skywalker')
        else:
            skywalker_list.append(name)

    for name in skywalker_list:
        f.write(name)

# try:
#     f = open('names.txt','a+')
#     lines = f.readlines()
#     name_list = []
#     for name in lines:
#         if name == "Luke":
#             name_list.append("Luke Skywalker")
#         else:
#             name_list.append(name)
    
#     for name in name_list:
#         f.write(name)

# finally:
#     f.close()