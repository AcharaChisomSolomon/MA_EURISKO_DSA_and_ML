def check_if_symmetric(string):
    middle_id = len(string) // 2
    for i in range(middle_id):
        if string[i].lower() != string[-1*(i+1)].lower():
            return False
    return True