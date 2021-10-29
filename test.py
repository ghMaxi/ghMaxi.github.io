students = (
    (("Студент", "Отчествович", "Фамильный"), 4),
    (("Студентка", "Отчествовна", "Фамильная"), 5),
)
student_card = '''{0} {1} {2}: оценки: {3}'''
print(student_card.format(students[0][0][0], students[0][0][1], students[0][0][2],
                          " ".join(f"{subj}: {mark};" for subj, mark in students[0][1])))
