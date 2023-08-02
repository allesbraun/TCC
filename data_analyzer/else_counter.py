import javalang


def count_elses(content):
    tokens = javalang.tokenizer.tokenize(content)
    count = 0
    for token in tokens:
        if isinstance(token, javalang.tokenizer.Keyword) and token.value == 'else':
            count += 1
    return count

# import javalang


# def count_elses(content):
#     tokens = list(javalang.tokenizer.tokenize(content))
#     count = 0
#     stack = []

#     for token in tokens:
#         if isinstance(token, javalang.tokenizer.Keyword):
#             if token.value == 'if':
#                 stack.append('if')
#             elif token.value == 'else':
#                 if len(stack) == 0 or stack[-1] != 'if':
#                     count += 1
#                 else:
#                     stack.pop()

#     return count



