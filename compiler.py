def notExit(word):
    for i in range(len(declareCode)):
        if word == declareCode[i]:
            return False
    return True

lines = []
codeC = "#include<stdio.h>\nint main() {\n"
declareCode = []
with open('add.txt') as my_file:
    for line in my_file:
        lines.append(line)

numLines = len(lines)
for i in range(numLines):
    words = lines[i].replace('\n', '').split(" ")

    for j in range(1, len(words)):
        if notExit(words[j]):
            codeC = codeC + 'int ' + words[j] + ';\n'
            declareCode.append(words[j])

for i in range(len(lines)):
    words = lines[i].replace('\n', '').split(" ")
    if words[0] == "INPUT":
        for j in range(1, len(words)):
            codeC = codeC + 'printf("Enter ' + words[j] + ' ="; scanf("%d", &' + words[j] + ');\n'

    if words[0] == "ADD":
            codeC = codeC + words[1] + ' = ' + words[2] + ' + ' + words[3] + ';\n'

    if words[0] == "SUB":
            codeC = codeC + words[1] + ' = ' + words[2] + ' - ' + words[3] + ';\n'

    if words[0] == "MUL":
            codeC = codeC + words[1] + ' = ' + words[2] + ' * ' + words[3] + ';\n'

    if words[0] == "DIV":
            codeC = codeC + words[1] + ' = ' + words[2] + ' / ' + words[3] + ';\n'

for i in range(1, len(lines) - 1):
    words = lines[i].replace('\n', '').split(" ")
    codeC = codeC + 'printf("Result ' + words[1] + ' = %d, ' + words[1] + ');\n'

codeC = codeC + 'return 0;' + '\n}'

print(codeC)