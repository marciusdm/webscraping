

def split_detail_summary(json_data):
    detail_data = []
    summary_data = []
    for line in json_data:
        if line["type"] == "summary":
            summary_data.append(line)
        elif line["type"] == "detail":
            detail_data.append(line)
    return summary_data, detail_data
