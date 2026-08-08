from utils.pdf_processor import process_pdf


# PDF location
pdf_path = "uploads/Python_Handwritten_Style_Notes.pdf"


print("=" * 60)
print("       AI CAMPUS ASSISTANT - PDF PROCESSOR")
print("=" * 60)


try:

    # Process PDF
    result = process_pdf(pdf_path)

    print("\nPDF PROCESSING SUCCESSFUL!")

    print("\n----------------------------------------")
    print("PDF INFORMATION")
    print("----------------------------------------")

    print("PDF:", pdf_path)

    print(
        "Total Characters:",
        result["total_characters"]
    )

    print(
        "Total Chunks:",
        result["total_chunks"]
    )


    # Display first 3 chunks
    print("\n========================================")
    print("FIRST 3 TEXT CHUNKS")
    print("========================================")


    for i, chunk in enumerate(
        result["chunks"][:3],
        start=1
    ):

        print("\n----------------------------------------")
        print(f"CHUNK {i}")
        print("----------------------------------------")

        print(chunk)


    print("\n========================================")
    print("PDF PROCESSING COMPLETED!")
    print("========================================")


except Exception as e:

    print("\nERROR OCCURRED!")
    print("----------------------------------------")
    print(str(e))