def format_contact(name, phone):
    return f"{name}, {phone}\n"

def parse_contact(line):
    name, phone = line.strip().split(",")
    return name, phone