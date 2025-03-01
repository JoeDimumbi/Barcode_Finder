# Extracting Barcodes from PDF Files

This guide provides step-by-step instructions to install the required dependencies and run the Python script to extract barcodes from PDF files.

## Prerequisites

- Python 3.6 or higher installed on your system

## Description

The script processes PDF files in a specified directory, extracts barcodes from images within the PDFs, and saves the extracted barcode data to a CSV file. It handles each page of the PDFs, identifies images, decodes any barcodes found in these images, and then compiles all the barcodes into a single output file for easy access and review.

## Dependencies

You need to install the following Python libraries to run the script:

- `PyMuPDF` (also known as `fitz`)
- `pyzbar`
- `Pillow`
- `glob2`

### Installing Dependencies

You can install the required libraries using `pip`. Run the following command in your terminal or command prompt:

```bash
pip install pymupdf pyzbar pillow glob2
