import os

print os.getcwd()

man = []
other = []

try:
    data = open('sketch.txt')
    # print data.readline()

    # with open

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split('said:', 1)
            print (role)
            print (' said: ')
            print (line_spoken)

            line_spoken = line_spoken.strip()
            if role == 'man':
                man.append(line_spoken)
            elif role == 'other man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()

except IOError:
    print ('The data file is missing!')

try:
    # man_file = open('man_data.txt', 'w')
    # other_file = open('other_data.txt', 'w')

    # print (man, man_file)
    # print (other, other_file)
    print(man, 'man_data.txt')
    print (other, 'other_data.txt')

    # man_file.close()
    # other_file.close()

except IOError:
    print ('file error.')
