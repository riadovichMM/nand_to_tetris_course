
#arithmetic and logic command
ADD_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'D=D+M',
    'M=D'
]

SUB_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'D=M-D',
    'M=D',
]

NEG_COMMAND = [
    '@SP',
    'A=M-1',
    'M=-M',
]

#stack


EQ_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'D=M-D',
    '@EQ_:i',
    'D;JEQ',
    '@SP',
    'A=M-1',
    'M=0',
    '@END_:i',
    '0;JMP',
    '(EQ_:i)',
    '@SP',
    'A=M-1',
    'M=-1',
    '(END_:i)',
]

# if (x > y) then true else false
GT_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'D=M-D',
    '@GT_:i',
    'D;JGT',
    '@SP',
    'A=M-1',
    'M=0',
    '@END_:i',
    '0;JMP',
    '(GT_:i)',
    '@SP',
    'A=M-1',
    'M=-1',
    '(END_:i)',
]

# if (x < y) then true else false
LT_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'D=M-D',
    '@LT_:i',
    'D;JLT',
    '@SP',
    'A=M-1',
    'M=0',
    '@END_:i',
    '0;JMP',
    '(LT_:i)',
    '@SP',
    'A=M-1',
    'M=-1',
    '(END_:i)',
]


AND_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'M=D&M',
]

OR_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',
    'A=A-1',
    'M=D|M',
]


NOT_COMMAND = [
    '@SP',
    'A=M-1',
    'M=!M',
]


# pop command

POP_LOCAL_COMMAND = [
    '@:n',
    'D=A',
    '@R13',
    'M=D',

    '@LCL',
    'D=M',
    '@R13',
    'M=D+M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@R13',
    'A=M',
    'M=D',
    '@R13',
    'M=0',
]


POP_ARGUMENT_COMMAND = [
    '@:n',
    'D=A',
    '@R13',
    'M=D',

    '@ARG',
    'D=M',
    '@R13',
    'M=D+M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@R13',
    'A=M',
    'M=D',
    '@R13',
    'M=0',
]



POP_THIS_COMMAND = [
    '@:n',
    'D=A',
    '@R13',
    'M=D',

    '@THIS',
    'D=M',
    '@R13',
    'M=D+M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@R13',
    'A=M',
    'M=D',
    '@R13',
    'M=0',
]


POP_THAT_COMMAND = [
    '@:n',
    'D=A',
    '@R13',
    'M=D',

    '@THAT',
    'D=M',
    '@R13',
    'M=D+M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@R13',
    'A=M',
    'M=D',
    '@R13',
    'M=0',
]

POP_TEMP_COMMAND = [
    '@:n',
    'D=A',
    '@R13',
    'M=D',

    '@5',
    'D=A',
    '@R13',
    'M=D+M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@R13',
    'A=M',
    'M=D',
    '@R13',
    'M=0',
]


POP_STATIC_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@:n',
    'M=D'
]


POP_POINTER_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@:n',
    'M=D',
]




# push command
PUSH_CONSTANT_COMMAND = [
    '@:n',
    'D=A',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]


PUSH_LOCAL_COMMAND = [
    '@LCL',
    'D=M',
    '@:n',
    'D=D+A',
    'A=D',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]

PUSH_ARGUMENT_COMMAND = [
    '@ARG',
    'D=M',
    '@:n',
    'D=D+A',
    'A=D',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]

PUSH_THIS_COMMAND = [
    '@THIS',
    'D=M',
    '@:n',
    'D=D+A',
    'A=D',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]


PUSH_THAT_COMMAND = [
    '@THAT',
    'D=M',
    '@:n',
    'D=D+A',
    'A=D',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]



PUSH_POINTER_COMMAND = [
    '@3',
    'D=A',
    '@:n',
    'D=D+A',
    'A=D',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]


PUSH_TEMP_COMMAND = [
    '@5',
    'D=A',
    '@:n',
    'D=D+A',
    'A=D',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]


PUSH_STATIC_COMMAND = [
    '@:n',
    'D=M',
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]
