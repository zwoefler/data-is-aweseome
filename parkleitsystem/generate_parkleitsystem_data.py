def add_new_data(existing_data, new_data):
    final_data = existing_data
    message = ""

    timestamp = new_data["timestamp"]

    if new_data not in existing_data:
        final_data.append(new_data)
        message = f"Added {timestamp}"
    else:
        message = f"Skipped {timestamp}, it already exists in the dataset"

    return final_data, message