import json

def parse_line(line):
    parts = line.split()
    level = line.count('.')
    name = ''.join(parts[:-1]).strip()
    page = int(parts[-1])
    return level, name, page

def add_to_dict(d, levels, name, page):
    current_level = 0
    current_dict = d
    for level in levels:
        if level not in current_dict:
            current_dict[level] = {} if current_level < levels[-1] else page
        current_dict = current_dict[level]
        current_level += 1
    if current_level == levels[-1]:
        current_dict[name] = page


toc_dict = {}
for line in toc.strip().split('\n'):
    level, name, page = parse_line(line)
    levels = [int(l) for l in name.split('.') if l.isdigit()]
    name = ''.join([l for l in name if not l.isdigit() and l != '.']).strip()
    add_to_dict(toc_dict, levels, name, page)

json_output = json.dumps(toc_dict, indent=2)
print(json_output)
