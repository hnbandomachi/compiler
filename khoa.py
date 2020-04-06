import sys
from pathlib import Path

# [instructions spec]
# specific instructions' compiler, as a function return a tuple of:
# (code_section_str, variable_name_list)
def ADD(param_list):
    a, b, res = param_list
    return ('{} = {} + {};\n'.format(res, a, b), param_list)

def SUB(param_list):
    a, b, res = param_list
    return ('{} = {} - {};\n'.format(res, a, b), param_list)
    
def MUL(param_list):
    a, b, res = param_list
    return ('{} = {} * {};\n'.format(res, a, b), param_list)

def DIV(param_list):
    a, b, res = param_list
    return ('{} = {} / {};\n'.format(res, a, b), param_list)

def prompt(varname):
    return 'printf("Enter {} = ");  scanf("%d", &{});\n'.format(varname, varname)

def INPUT(param_list):
    prompt_stmts = list(map(prompt, param_list))
    stmt_section = ''.join(prompt_stmts)
    return (stmt_section, param_list)

def report(varname):
    return 'printf("Result {} = %d\\n", {});\n'.format(varname, varname)
#                                  ^ escape the backslash here

def OUTPUT(param_list):
    report_stmts = list(map(report, param_list))
    stmt_section = ''.join(report_stmts)
    return (stmt_section, param_list)

instruction_dict = dict(
    ADD = ADD,
    SUB = SUB,
    MUL = MUL,
    DIV = DIV,
    INPUT = INPUT,
    OUTPUT = OUTPUT
)
# [/instructions spec]

def lexing(instructionStr):
    # return syntax representation structure for given instruction string
    # for simplicity, here is not proper syntax tree, just a list of tokens
    return instructionStr.rstrip('\n').split(' ')

def main():
    # open file given the name from commandline argument
    if len(sys.argv) < 2:
        print('Please provide source filename. Abort.')
        return 1

    source_filename = sys.argv[-1]
    source_file = open(source_filename)

    # list of "body" statements that actually do computation and I/O
    working_stmts = []

    # set of variable name to declare
    varnames = set()

    for line in source_file:
        # for each line in source, compile it into corresponding C statement section
        token_list = lexing(line)
        instruction_type = token_list[0] # first token
        param_list = token_list[1:]      # rest tokens
        instruction = instruction_dict[instruction_type]
        (stmt_section, new_varnames) = instruction(param_list)
        working_stmts.append(stmt_section)
        for varname in new_varnames:
            varnames.add(varname)
            
    # build one declare statement from accumulated set of variable name
    declare_stmt = 'int ' + ', '.join(sorted(varnames)) + ';\n'
    
    leading_boilerplate = '''
#include <stdio.h>

int main() {
'''

    trailing_boilerplate = '''
return 0;
}
'''

    # write target C file with the same basename as source file
    target_filename = Path(source_filename).stem + '.c'
    target_file = open(target_filename, 'w')

    target_file.write(leading_boilerplate)
    target_file.write(declare_stmt)
    for stmt in working_stmts:
        target_file.write(stmt)
    target_file.write(trailing_boilerplate)

    target_file.close()

if __name__ == '__main__':
    main()
