import os
import csv
import glob
import fitz  # PyMuPDF
from pyzbar.pyzbar import decode
from PIL import Image, UnidentifiedImageError
from io import BytesIO

def extract_barcodes_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    barcodes = []
    for page_num in range(doc.page_count):
        page = doc[page_num]
        img_list = page.get_images(full=True)
        for img_info in img_list:
            img = doc.extract_image(img_info[0])
            img_bytes = img["image"]
            img = Image.open(BytesIO(img_bytes))
            img.save(f"page_{page_num+1}_image_{img_info[0]}.png")  # Save for debugging
            decoded_barcodes = decode(img)
            barcodes.extend([barcode.data.decode('utf-8') for barcode in decoded_barcodes])
    doc.close()
    return barcodes


def save_barcodes_to_csv(output_path, barcode_data):
    """
    Save barcode data to a CSV file.
    Args:
        output_path (str): Path to the output CSV file.
        barcode_data (list of tuples): List of (file_name, barcode) tuples.
    """
    try:
        with open(output_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['File Name', 'Barcode'])
            csv_writer.writerows(barcode_data)
        print(f"Barcodes successfully saved to {output_path}.")
    except Exception as e:
        print(f"Error writing to CSV file {output_path}: {e}")

def main():
    """
    Main function to process PDFs and extract barcodes.
    """
    folder_path = os.path.dirname(os.path.abspath(__file__))
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))

    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    print("PDF Files Found:", pdf_files)

    barcode_data = []

    for pdf_file in pdf_files:
        print(f"Processing {pdf_file}...")
        barcodes = extract_barcodes_from_pdf(pdf_file)
        if barcodes:
            barcode_data.extend([(os.path.basename(pdf_file), barcode) for barcode in barcodes])
        else:
            print(f"No barcodes found in {pdf_file}.")

    output_csv_path = os.path.join(folder_path, 'output.csv')
    save_barcodes_to_csv(output_csv_path, barcode_data)

if __name__ == "__main__":
    main()
