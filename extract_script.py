import re

def parse_id_array_from_script(script_text, function_name):
    # Looks for something like: function dersSil() { ... var dids = [8,7,44,...]; ... }
    # We'll capture the numbers in the array
    # function_name in ["dersSil", "uniteSil", "kazanimSil"]
    pattern = rf"{function_name}\s*\(\)\s*{{.*?var dids\s*=\s*\[([^\]]*)\];.*?}}"

    match = re.search(pattern, script_text, re.DOTALL)
    print("Match:", match)
    if not match:
        return set()
    raw_ids = match.group(1)
    # raw_ids might look like: 8,7,44,6,46
    # We split on commas and parse them into integers
    ids = set()
    for x in raw_ids.split(","):
        x = x.strip()
        if x.isdigit():
            ids.add(int(x))
    return ids

def parse_ders_unite_kazanim_ids(html):
    # Extract sets of valid IDs from the script in Default.aspx
    scripts = re.findall(r"<script[^>]*>(.*?)</script>", html, re.DOTALL)
    target_script = scripts[-1]
    print("Number of scripts found:", len(scripts))
    ders_ids, unite_ids, kazanim_ids = set(), set(), set()
    
    if "function dersSil" in target_script:
        print("Found dersSil")
        ders_ids = parse_id_array_from_script(target_script, "dersSil")
    # parse for uniteSil
    if "function uniteSil" in target_script:
        print("Found unite")
        unite_ids = parse_id_array_from_script(target_script, "uniteSil")
    # parse for kazanimSil
    if "function kazanimSil" in target_script:
        print("Found kazanim")
        kazanim_ids = parse_id_array_from_script(target_script, "kazanimSil")

    return ders_ids, unite_ids, kazanim_ids


html = ''
with open('html.html', 'r') as f:
    html = f.read()

ders_ids, unite_ids, kazanim_ids = parse_ders_unite_kazanim_ids(html)
print("ders_ids:", ders_ids)
print("unite_ids:", unite_ids)
print("kazanim_ids:", kazanim_ids)
