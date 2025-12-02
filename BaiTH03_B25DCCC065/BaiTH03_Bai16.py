students_scores = {
    'An': 85,
    'Binh': 92,
    'Chi': 78,
    'Dung': 90,
    'Duong': 88
}
sorted_students = sorted(students_scores.items(), key=lambda item: item[1], reverse=True)
print("Danh sách sinh viên sắp xếp theo điểm giảm dần:")
for name, score in sorted_students:
    print(f"{name}: {score}")