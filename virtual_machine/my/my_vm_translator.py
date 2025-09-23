from my.my_asm_codes import (
    PUSH_COMMAND,
    CONSTANT_SEGMENT,
    ADD_COMMAND,
    EQ_COMMAND,
    LT_COMMAND,
    GT_COMMAND,
    SUB_COMMAND,
    NEG_COMMAND,
    AND_COMMAND,
    OR_COMMAND,
    NOT_COMMAND,
    POP_LOCAL_COMMAND,
    POP_ARGUMENT_COMMAND,
    POP_THIS_COMMAND,
    POP_THAT_COMMAND,
    POP_TEMP_COMMAND,
    POP_STATIC_COMMAND,
    POP_POINTER_COMMAND,
    PUSH_LOCAL_COMMAND,
    PUSH_POINTER_COMMAND,
    PUSH_TEMP_COMMAND,
    PUSH_STATIC_COMMAND,
    PUSH_ARGUMENT_COMMAND,
    PUSH_THIS_COMMAND,
    PUSH_THAT_COMMAND
)

#vm_code arrays
vm_code = []
vm_code_keys = []

asm_code = []

index = 0

def get_vm_code_from_file():
    f = open("./code.vm")
    for line in f:
        vm_code.append(line.replace("\n", ""))
    f.close()


def split_by_keys():
    for line in vm_code:
        vm_code_keys.append(line.split(" "))


def copy_code(asm_commands, value):
    global index
    for line in asm_commands:
        if value != None:
            asm_code.append(line.replace(":n", value))
        elif ':i' in line:
            asm_code.append(line.replace(":i", str(index)))
        else:
            asm_code.append(line)

def create_asm_file():
    f = open("./asm_code.asm", "+w")
    for line in asm_code:
        f.write(line + "\n")
    f.close()

def analysis_and_generate_code():
    global index

    for vm_command in vm_code_keys:
        if len(vm_command) == 3:
            if vm_command[0] == 'push':
                # push constant n
                if vm_command[1] == 'constant':
                    copy_code(CONSTANT_SEGMENT, vm_command[2])
                    copy_code(PUSH_COMMAND, None)
                if vm_command[1] == 'local':
                    copy_code(PUSH_LOCAL_COMMAND, vm_command[2])
                if vm_command[1] == 'argument':
                    copy_code(PUSH_ARGUMENT_COMMAND, vm_command[2])
                if vm_command[1] == 'this':
                    copy_code(PUSH_THIS_COMMAND, vm_command[2])
                if vm_command[1] == 'that':
                    copy_code(PUSH_THAT_COMMAND, vm_command[2])
                if vm_command[1] == 'pointer':
                    copy_code(PUSH_POINTER_COMMAND, vm_command[2])
                if vm_command[1] == 'temp':
                    copy_code(PUSH_TEMP_COMMAND, vm_command[2])
                if vm_command[1] == 'static':
                    copy_code(PUSH_STATIC_COMMAND, 'BasicTest.' + str(vm_command[2]))

            if vm_command[0] == 'pop':
                if vm_command[1] == 'local':
                    copy_code(POP_LOCAL_COMMAND, vm_command[2])
                if vm_command[1] == 'argument':
                    copy_code(POP_ARGUMENT_COMMAND, vm_command[2])
                if vm_command[1] == 'this':
                    copy_code(POP_THIS_COMMAND, vm_command[2])
                if vm_command[1] == 'that':
                    copy_code(POP_THAT_COMMAND, vm_command[2])
                if vm_command[1] == 'temp':
                    copy_code(POP_TEMP_COMMAND, vm_command[2])
                if vm_command[1] == 'static':
                    copy_code(POP_STATIC_COMMAND, 'BasicTest.' + str(vm_command[2]))
                if vm_command[1] == 'pointer':
                    copy_code(POP_POINTER_COMMAND, str(3) if int(vm_command[2]) == 0 else str(4))


        if len(vm_command) == 1:
            if vm_command[0] == 'add':
                copy_code(ADD_COMMAND, None)
            if vm_command[0] == 'eq':
                copy_code(EQ_COMMAND, None)
                index+=1
            if vm_command[0] == 'lt':
                copy_code(LT_COMMAND, None)
                index+=1
            if vm_command[0] == 'gt':
                copy_code(GT_COMMAND, None)
                index+=1
            if vm_command[0] == 'sub':
                copy_code(SUB_COMMAND, None)
                index+=1
            if vm_command[0] == 'neg':
                copy_code(NEG_COMMAND, None)
                index+=1
            if vm_command[0] == 'and':
                copy_code(AND_COMMAND, None)
                index+=1
            if vm_command[0] == 'or':
                copy_code(OR_COMMAND, None)
                index+=1
            if vm_command[0] == 'not':
                copy_code(NOT_COMMAND, None)
                index+=1


def main():
    get_vm_code_from_file()
    split_by_keys()
    analysis_and_generate_code()
    create_asm_file()

    print(asm_code)


if __name__ == "__main__":
    main()