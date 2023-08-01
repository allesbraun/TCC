from data.data_analyzer.break_counter import count_breaks
from data.data_analyzer.else_counter import count_elses
from data.data_analyzer.if_counter import count_ifs
from data.data_analyzer.loop_counter import count_loops
from data.data_analyzer.switch_counter import count_switches


def data_response(content, file):
    response_data = {
        'filename': file.name,
        'if_count': count_ifs(content),
        'else_count': count_elses(content), 
        'break_count': count_breaks(content), 
        'switch_count': count_switches(content),
        'loop_count': count_loops(content),
    }
    return response_data