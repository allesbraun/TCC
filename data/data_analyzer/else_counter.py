import javalang


def count_else_statements(content):
    tokens = javalang.tokenizer.tokenize(content)
    count = 0
    for token in tokens:
        if isinstance(token, javalang.tokenizer.Keyword) and token.value == 'else':
            count += 1
    return count