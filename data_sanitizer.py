data_entries: ["100", "200", "three", "400", "Sive"] # type: ignore
parsed_data = []

for entry in data_entries:
    try:
        parsed_data.append(int(entry))
    except ValueError:
        print(f"Warning: '{entry}' is not a valid integer and will be skipped.")

print(f"Parsed Data: {parsed_data}")