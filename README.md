# EOB Parser using OCR and Python 🧾🤖

This project extracts structured information from scanned Explanation of Benefits (EOB) documents using Python, Tesseract OCR, and regular expressions. It's designed to assist in automating healthcare claim analysis workflows.

---

## 📂 Repository Name
`eob-ocr-parser`

---

## 📜 Project Description

**EOB Parser** is a Python-based tool to:
- OCR scanned EOB images using `pytesseract`
- Parse patient information, billing amounts, and service details
- Format and display extracted data in a clean format
- Modularize the logic using `config.py` for maintainability

---

## ⚙️ Technologies Used

- Python 3.10+
- Tesseract OCR
- Pillow (PIL)
- Regular Expressions
- VS Code / CLI

---

## 🏗️ Project Structure

```
eob-ocr-parser/
├── ocr_and_parse.py      # Main script to run OCR and extraction
├── config.py             # Extraction logic and helper functions
├── eob_image.png.png     # Input scanned EOB image
├── ocr_output.txt        # Raw OCR text from Tesseract
├── cleaned_output.txt    # Cleaned and formatted results
└── README.md             # Documentation
```

---

## 🚀 How to Run

1. **Install Dependencies**  
   Make sure `pytesseract` and `Pillow` are installed:
   ```bash
   pip install pytesseract pillow
   ```

2. **Install Tesseract OCR**  
   [Download here](https://github.com/tesseract-ocr/tesseract) and make sure the path is set correctly.

3. **Place your EOB image**  
   Place your EOB image in the project folder as `eob_image.png.png`.

4. **Run the script**
   ```bash
   python ocr_and_parse.py
   ```

---

## ✅ Output Example

```bash
------ EXTRACTED DATA ------
Patient Name: John Doe
Total Billed Amount: 5.600.00
Amount Covered: 4.480.00
Patient Responsibility: 1.120.00

Service Details:
- 12/20/2023 | HOSPITAL SERVICES | ₹5000.00 → Covered: ₹4000.00 | Status: ONGOING
...
```

---

## 🙌 Contributions

Feel free to fork, improve, and submit PRs.

---

## 📄 License

MIT License

---

Built with ❤️ for automating healthcare claim processing.
