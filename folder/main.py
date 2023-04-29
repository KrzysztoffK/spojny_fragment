file = open("pary.txt", "r")
words = []

#przygotowanie pliku przez ingorowanie liczb po lewej
for line in file:
    for char in line:
        if char == " ":
            index = line.index(char)
    newline = line[index+1:]
    words.append(newline)
file.close()

#zliczanie spojnych fragmentow
for elements in words:
    max_fragment= ""
    current_fragment = ""
    for i in range(len(elements)):
        if i == 0:
            current_fragment += elements[i]
        if elements[i] == elements[i-1]:
            current_fragment += elements[i]
        else:
            if len(current_fragment) > len(max_fragment):
                max_fragment = current_fragment
            current_fragment = elements[i]
    if len(current_fragment) > len(max_fragment):
        max_fragment = current_fragment
    print(max_fragment, len(max_fragment))
