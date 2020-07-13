tekst = input()
new_tekst = ""
new_list =[]
for char in tekst:
    if char.isalpha():
        new_tekst += char
    else:
        new_tekst += "."

list_split = new_tekst.split(".")
#print(list_split)
for item in list_split:
    new_list.append(item.capitalize())
print("".join(new_list))