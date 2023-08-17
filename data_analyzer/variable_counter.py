import re

import javalang
from javalang import tree


#LocalVariableDeclaration + VariableDeclaration
def count_variables(content):
    tokens = list(javalang.tokenizer.tokenize(content))#a declaração de variável não é captada pelo token eu acho
    count = 0
    aux = tokens
    
    return count 
