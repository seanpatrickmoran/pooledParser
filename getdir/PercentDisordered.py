#! /usr/bin/env python3


def PCN_disordered(LEN,dARRAY=list()):
    PCNDRD = 0
    # LEN = ast.literal_eval(LEN)
    for y in dARRAY:
        PCNDRD += y[1]-y[0]    
    return (PCNDRD/LEN)

