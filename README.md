# OCR-Based Mobile Number Extractor  

This project is an OCR (Optical Character Recognition) model designed to extract mobile numbers from various file types, including images, PDFs, and documents. The model leverages EasyOCR for text recognition and processing. It is optimized for typed numbers and includes improvements for recognizing handwritten numbers.

---

 Features  
✅ Extracts mobile numbers from:  
- Images (JPG, PNG, BMP)  
- PDFs  
- Text Documents (DOC, DOCX)  

✅ Handles different number formats and patterns  
✅ High accuracy for typed numbers  
✅ Basic support for handwritten numbers  
✅ Fast and efficient processing  

---

 Technologies Used  
- Python – Core programming language  
- EasyOCR – Optical character recognition  
- OpenCV – Image processing  
- PyMuPDF – PDF parsing  
- Docx – Document parsing  

---

 Installation  
# Step 1: Clone the Repository  
```bash
git clone https://github.com/ayushsharma/OCR-Mobile-Extractor.git
```

# Step 2: Navigate to the Project Directory  
```bash
cd OCR-Mobile-Extractor
```

# Step 3: Create a Virtual Environment (Optional)  
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

# Step 4: Install Dependencies  
```bash
pip install -r requirements.txt
```

---

 Usage  
# 1. Run the Script  
```bash
python main.py
```

# 2. Input File  
- Provide the file path when prompted  
- Supports file types: `.jpg`, `.png`, `.bmp`, `.pdf`, `.doc`, `.docx`  

# 3. Output  
- Extracted mobile numbers are displayed in the console  
- Optionally, save the results to a text file  

---

 Sample Output  
```bash
Extracting mobile numbers from input.pdf...
Found Numbers:
+91 9899006757
+91 9999988888
```

---

 Project Structure  
```
├── data/                   # Sample input files  
├── src/                    # Core source code  
│   ├── extractor.py        # Extraction logic  
│   ├── utils.py            # Utility functions  
├── requirements.txt        # Python dependencies  
├── main.py                 # Entry point  
├── README.md               # Project documentation  
└── .gitignore              # Git ignore file  
```

---

 Dependencies  
- `python >= 3.8`  
- `EasyOCR`  
- `OpenCV`  
- `PyMuPDF`  
- `python-docx`  

---

 Challenges and Improvements  
✅ High accuracy with typed numbers  
🚧 Improving recognition accuracy for handwritten numbers  
🚧 Adding multi-language support  

---

 Future Work  
- Enhance recognition of handwritten numbers  
- Improve multi-language support  
- Add GUI for better user experience  

---

 Contributing  
Contributions, issues, and feature requests are welcome!  
1. Fork the repository  
2. Create a new branch (`git checkout -b feature-branch`)  
3. Commit changes (`git commit -m 'Add feature'`)  
4. Push to branch (`git push origin feature-branch`)  
5. Create a Pull Request  

---

 License  
This project is licensed under the MIT License.

---
