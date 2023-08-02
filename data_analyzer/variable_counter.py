import re


#não conta arrays mas resultado não bate com num de variaveis de HowtocheckiftwogivenlinesegmentsintersectGeeksforGeeks-1.java dos crawled
def count_variables(content):
    pattern = r'\b(?!int|long|float|double|char|boolean|byte|short)\w+\b(?:\s*,\s*\w+\s*)*;'
    matches = re.findall(pattern, content)

    count = 0
    for match in matches:
        if not any(variable.endswith('[]') for variable in match.split(',')):
            count += 1

    return count
