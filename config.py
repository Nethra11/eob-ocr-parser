import re

def extract_patient_name(text):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if "Member" in line:
            for j in range(i + 1, len(lines)):
                candidate = lines[j].strip()
                if candidate and not candidate.lower().startswith("january"):
                    return candidate
    return "Not Found"

def extract_total_billed(text):
    match = re.search(r'provider billed \$([\d,.]+)', text, re.IGNORECASE)
    return match.group(1).replace(",", ".") if match else "Not Found"

def extract_total_covered(text):
    match = re.search(r'covered by your plan \$([\d,.]+)', text, re.IGNORECASE)
    return match.group(1).replace(",", ".") if match else "Not Found"

def extract_responsibility(text):
    match = re.search(r'RESPONSIBILITY \$([\d,.]+)', text, re.IGNORECASE)
    return match.group(1).replace(",", ".") if match else "Not Found"

def extract_service_rows(text):
    lines = text.split("\n")
    services = []
    combined = ""
    for line in lines:
        if re.search(r"\d{2}/\d{2}/\d{4}", line):
            combined = line
        elif "PAID" in line or "ONGOING" in line:
            combined += " " + line
            cleaned = re.sub(r'[|}\\]]', '', combined)
            parts = cleaned.split()
            try:
                date = parts[0]
                desc = " ".join(parts[1:-4])
                total = parts[-4].replace(",", ".")
                covered = parts[-2].replace(",", ".")
                status = parts[-1]
                services.append((date, desc, total, covered, status))
            except:
                pass
            combined = ""
    return services
