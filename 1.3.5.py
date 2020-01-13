def grading(sentence):
    grade = 0
    if ',' in sentence:
        grade += 1
    if '"' in sentence:
        grade += 1
    if '?' in sentence:
        grade += 1
    if '!' in sentence:
        grade += 1
    print (grade)