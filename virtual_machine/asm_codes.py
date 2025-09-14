CONSTANT_SEGMENT = [
    '@:n',
    'D=A',
]

PUSH_COMMAND = [
    '@SP',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1',
]

# result = x + y
ADD_COMMAND = [
    '@SP',
    'M=M-1',
    'M=M-1',
    'A=M',
    'D=M',
    '@SP',
    'M=M+1',
    'A=M',
    'D=D+M',
    '@SP',
    'M=M-1',
    'A=M',
    'M=D',
    '@SP',
    'M=M+1'
]

EQ_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=D-M',

    '@IF_ZERO_:i',
    'D;JEQ',
    
    '@ELSE_:i',
    '0;JMP',

    '(IF_ZERO_:i)',
    '@SP',
    'A=M',
    'M=-1',
    '@END_IF_:i',
    '0;JMP',

    '(ELSE_:i)',
    '@SP',
    'A=M',
    'M=0',
    '@END_IF_:i',
    '0;JMP',

    '(END_IF_:i)',
    '@SP',
    'M=M+1'
]

# if (x < y) then true else false
LT_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=D-M',

    '@IF_LESS_THAN_:i',
    'D;JGT',
    
    '@ELSE_:i',
    '0;JMP',

    '(IF_LESS_THAN_:i)',
    '@SP',
    'A=M',
    'M=-1',
    '@END_IF_:i',
    '0;JMP',

    '(ELSE_:i)',
    '@SP',
    'A=M',
    'M=0',
    '@END_IF_:i',
    '0;JMP',

    '(END_IF_:i)',
    '@SP',
    'M=M+1'
]

# if (x > y) then true else false
GT_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    '@SP',
    'M=M-1',
    'A=M',
    'D=D-M',

    '@IF_GREATE_THAN_:i',
    'D;JLT',
    
    '@ELSE_:i',
    '0;JMP',

    '(IF_GREATE_THAN_:i)',
    '@SP',
    'A=M',
    'M=-1',
    '@END_IF_:i',
    '0;JMP',

    '(ELSE_:i)',
    '@SP',
    'A=M',
    'M=0',
    '@END_IF_:i',
    '0;JMP',

    '(END_IF_:i)',
    '@SP',
    'M=M+1'
]


SUB_COMMAND = [
    '@SP',
    'M=M-1',
    'M=M-1',
    'A=M',
    'D=M',

    '@SP',
    'M=M+1',
    'A=M',
    'D=D-M',

    '@SP',
    'M=M-1',
    'A=M',
    'M=D',

    '@SP',
    'M=M+1',
]

NEG_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    'M=-D',

    '@SP',
    'M=M+1',
]


AND_COMMAND = [
    '@SP',
    'M=M-1',
    'M=M-1',
    'A=M',
    'D=M',

    '@SP',
    'M=M+1',
    'A=M',
    'D=D&M',

    '@SP',
    'M=M-1',
    'A=M',
    'M=D',

    '@SP',
    'M=M+1',
]

OR_COMMAND = [
    '@SP',
    'M=M-1',
    'M=M-1',
    'A=M',
    'D=M',

    '@SP',
    'M=M+1',
    'A=M',
    'D=D|M',

    '@SP',
    'M=M-1',
    'A=M',
    'M=D',

    '@SP',
    'M=M+1',
]


NOT_COMMAND = [
    '@SP',
    'M=M-1',
    'A=M',
    'D=M',

    'M=!D',

    '@SP',
    'M=M+1',
]


# pop 

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


# push

PUSH_LOCAL_COMMAND = [
    '@:n',
    'D=A',

    '@R13',
    'M=D',

    '@LCL',
    'D=M',

    '@R13',
    'M=D+M',

    '@R13',
    'A=M',
    'D=M',

    '',
]


