import ast
import re

import javalang

# def count_minMax(content):
    
#     first_recursive_call = 1 #makes sure that when eliminating the recursive we don't eliminate the original one
    
#     min_calls = len(re.findall(r'\bmin\([^)]*\)', content))
#     max_calls = len(re.findall(r'\bmax\([^)]*\)', content))

#     min_recursive_calls = len(re.findall(r'\bmin(?!\()', content))
#     max_recursive_calls = len(re.findall(r'\bmax(?!\()', content))
    
#     if(min_recursive_calls > 0):
#         min_calls = min_calls + first_recursive_call
#     if(max_recursive_calls > 0):
#         max_calls = max_calls + first_recursive_call

#     return min_calls - min_recursive_calls + max_calls - max_recursive_calls




def count_minMax(content):
    # Parse the Java code
    tree = javalang.parse.parse(content)

    # Initialize counters
    min_calls = 0
    max_calls = 0

    # Traverse the syntax tree to count calls to min() and max()
    for path, node in tree:
        if isinstance(node, javalang.tree.MethodInvocation):
            method_name = node.member
            if method_name == "min":
                min_calls += 1
            elif method_name == "max":
                max_calls += 1

    return min_calls + max_calls