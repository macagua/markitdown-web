
# MarkItDown Web Converter

A MarkItDown-based web interface tool that provides convenient file to Markdown functionality.

## Functional Features

- 🚀 Easy-to-use web interface
- 📦 Support batch file upload and conversion
- 👀 Real-time preview of conversion results
- 💾 Download converted files with one click
- 🔌 Support multiple file format conversion

## Supported file formats

- Documentation
  - PDF files
  - Microsoft Word documents
  - PowerPoint presentations
  - Excel Forms

- Multimedia
  - Image files (EXIF metadata and OCR support)
  - Audio files (supports EXIF metadata and voice transcription)

- Other formats
  - HTML Web Page
  - CSV data files
  - JSON files
  - XML documents
  - ZIP archive (traversable content)

## Environmental requirements

- Python 3.x
- pip package manager

## 快速开始

1. Cloning projects to local:
```bash
git clone git@github.com:ccbsdu/markitdown-web.git
cd markitdown-web
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependency packages:
```bash
pip install -r requirements.txt
```

4. Launch the application:
```bash
streamlit run app.py
```

5. Access the application in a browser (default address: http://localhost:8501）

## Instructions for use

1. After opening the application, click the "Select Files to Convert" button or drag and drop the files directly to the upload area.
2. Support selecting multiple files at the same time for batch conversion.
3. The conversion will start automatically after uploading the files.
4. You can preview the conversion result on the interface after the conversion is finished.
5. Click "Download Markdown File" button to save the converted file.

## Project structure

```
markitdown-web/
├── app.py            # The main application
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## Caution

- It is recommended to use a virtual environment to run the application
- Conversion of large files may take a long time, please be patient.
- Temporary files will be cleaned up automatically after conversion
- Please make sure you have enough disk space.

## License

This project is open source under the MIT license.

## Acknowledgments

- Thanks to [MarkItDown](https://github.com/microsoft/markitdown) for providing the core conversion functionality.
- Thanks to [Streamlit](https://streamlit.io/) for the great web framework.
```
