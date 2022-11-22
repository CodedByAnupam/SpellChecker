# write your solution here


def words_to_list(file):
    with open(file) as new_file:
        lst = []
        for line in new_file:
            line = line.replace("\n", "")
            lst.append(line)
    return lst


sent = input("Write text: ")
parts = sent.split(" ")
words_list = words_to_list("wordlist.txt")

for i in range(len(words_list)):
    words_list[i] = words_list[i].lower()

output = ""

for word in parts:
    # word = word.lower()
    if word.lower() in words_list:
        output = output + word + " "
    else:
        output = output + "*" + word + "*" + " "
    # output += " "
print(output)

# with open("wordlist.txt") as new_file:
#     for part in parts:
#         count = 0
#         for line in new_file:
#             line = line.replace("\n", "")
#             if part in line:
#                 count += 1

# sent = input("Write text: ")
# line = line.replace("\n", "")
# parts = sent.split(" ")
# for part in parts:
#     if part not
