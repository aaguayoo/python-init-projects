
with open(r'semblanza.txt', 'r') as file:
        # read all content from a file using read()
        content = file.read()
        # check if string present or not
        if 'Line 8' in content:
            print('string exist')
        else:
            print('string does not exist')