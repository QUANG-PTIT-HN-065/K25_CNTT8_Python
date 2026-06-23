def calculate_average(scores):
    valid_scores = [x for x in scores if isinstance(x, (int, float))]
    if len(valid_scores) == 0:
        return 0
    return sum(valid_scores) / len(valid_scores)


def classify_student(avg):
    if avg >= 8:
        return "Giỏi"
    elif avg >= 6.5:
        return "Khá"
    elif avg >= 5:
        return "Trung bình"
    return "Yếu"
