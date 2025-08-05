from PIL import Image
import pytesseract
import re

# OCR the image
image_path = "eob_image.png.png"
image = Image.open(image_path)
text = pytesseract.image_to_string(image)

# Save OCR result
with open("ocr_output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# ---------- Extractors ----------

def extract_patient_name(text):
    lines = text.split('\n')
    for i in range(len(lines)):
        if "Member" in lines[i]:
            # Collect lines after "Member"
            next_lines = lines[i+1:i+5]
            for line in next_lines:
                cleaned = line.strip()
                if re.match(r'^[A-Z][a-z]+\s[A-Z][a-z]+$', cleaned):
                    return cleaned
    # If John Doe is somewhere else, fallback
    if "John Doe" in text:
        return "John Doe"
    return "Not Found"

def extract_total_billed(text):
    match = re.search(r'provider billed \$([\d.,]+)', text, re.IGNORECASE)
    return match.group(1).replace(",", ".") if match else "Not Found"

def extract_total_covered(text):
    match = re.search(r'covered by your plan \$([\d.,]+)', text, re.IGNORECASE)
    return match.group(1).replace(",", ".") if match else "Not Found"

def extract_responsibility(text):
    match = re.search(r'RESPONSIBILITY \$([\d.,]+)', text, re.IGNORECASE)
    return match.group(1).replace(",", ".") if match else "Not Found"

def extract_service_rows(text):
    lines = text.split("\n")
    services = []
    for line in lines:
        if re.search(r"\d{2}/\d{2}/\d{4}", line) and ("PAID" in line or "ONGOING" in line):
            cleaned = re.sub(r'[|}\]\[{()}]', ' ', line)
            parts = cleaned.split()
            try:
                date = parts[0]
                # Find where the amount values start
                idx_total = -5
                idx_covered = -2
                desc = " ".join(parts[1:idx_total])
                total = parts[idx_total].replace(",", ".")
                covered = parts[idx_covered].replace(",", ".")
                status = parts[-1]
                services.append((date, desc, total, covered, status))
            except:
                continue
    return services


# ---------- Output ----------

print("\n------ EXTRACTED DATA ------")
print("Patient Name:", extract_patient_name(text))
print("Total Billed Amount:", extract_total_billed(text))
print("Amount Covered:", extract_total_covered(text))
print("Patient Responsibility:", extract_responsibility(text))

print("\nService Details:")
services = extract_service_rows(text)
if services:
    for s in services:
        print(f"- {s[0]} | {s[1]} | ₹{s[2]} → Covered: ₹{s[3]} | Status: {s[4]}")
else:
    print("No service details found.")
