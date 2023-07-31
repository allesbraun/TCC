from data.data_analyzer.else_counter import count_else_statements
from data.data_analyzer.if_counter import count_if_statements


def data_response(content, file):
    response_data = {
        'filename': file.name,
        'if_count': count_if_statements(content),
        'else_count': count_else_statements(content), 
    }
    return response_data