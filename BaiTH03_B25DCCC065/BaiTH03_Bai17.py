data = [
    {"name": "A", "score": 7},
    {"name": "B", "score": 9},
    {"name": "A", "score": 8},
]
def aggregate_scores(data):
    result = {}
    for entry in data:
        name = entry["name"]
        score = entry["score"]
        if name in result:
            result[name].append(score)
        else:
            result[name] = [score]
    return result
aggregated_dict = aggregate_scores(data)
print("Dictionary tổng hợp điểm theo tên:", aggregated_dict)