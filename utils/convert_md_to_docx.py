import pypandoc
import sys
import os

def convert_md_to_docx(input_file, output_file=None):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"Error: {input_file} does not exist.")
        return
    
    # If output_file is not provided, use the same name as input with .docx extension
    if output_file is None:
        output_file = os.path.splitext(input_file)[0] + '.docx'

    # Convert the Markdown file to Word document
    try:
        pypandoc.convert_file(input_file, 'docx', outputfile=output_file)
        print(f"Conversion successful! {input_file} has been converted to {output_file}")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_md_to_docx.py <input_file.md> [output_file.docx]")
    else:
        input_md_file = sys.argv[1]
        output_docx_file = sys.argv[2] if len(sys.argv) > 2 else None
        convert_md_to_docx(input_md_file, output_docx_file)
