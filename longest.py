string1 = 'this_somting_we try'
string2 = 'thisSomting'

longest_common = ''
smallest_string = ''

if len(string1) <= len(string2):
    smallest_string = string1
else:
    smallest_string = string2

for index in range(len(smallest_string)):
    if string1[index] == string2[index]:
        longest_common += smallest_string[index]

print(longest_common)