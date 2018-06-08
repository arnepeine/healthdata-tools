def read_csv(filename):
    import_file = open(filename, "r")
    text = import_file.read()
    string_list_temp = text.split("\n")
    string_list = string_list_temp[1:len(string_list_temp)]
    final_list = []
    
    for string in string_list:
        int_fields = []
        string_fields = string.split(",")
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
