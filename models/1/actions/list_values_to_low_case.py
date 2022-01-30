def list_value_to_low_case(list_in):

    # list to be returned
    return_list = []

    # go through passed list and convert all characters to lowercase
    for entity in list_in:
        return_list.append(entity.lower())
    return return_list
