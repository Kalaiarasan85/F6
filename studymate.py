# studymate.py
# Simple AI-powered PDF Q&A system (College Mini Project)
# Author: Kalaiarasan

import PyPDF2

def extract_text_from_pdf(pdf_path):
    '''Extract all text from a given PDF file'''
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text()
        return text
    except Exception as e:
        print("Error reading PDF:", e)
        return ""

def answer_question(pdf_text, question):
    '''Find simple keyword-based answer'''
    lines = pdf_text.split("\n")
    question_words = question.lower().split()
    best_line = ""
    best_score = 0

    for line in lines:
        line_lower = line.lower()
        score = sum(word in line_lower for word in question_words)
        if score > best_score:
            best_score = score
            best_line = line.strip()

    if best_score == 0:
        return "Sorry, I couldn’t find an answer in the PDF."
    else:
        return f"Answer (best match): {best_line}"

def main():
    print("📘 Welcome to StudyMate - AI PDF Q&A System")
    pdf_path = input("Enter your PDF file name (with .pdf): ")
    pdf_text = extract_text_from_pdf(pdf_path)

    if not pdf_text:
        print("Failed to extract text. Please check your PDF.")
        return

    while True:
        question = input("\nAsk a question (or type 'exit' to quit): ")
        if question.lower() == "exit":
            print("Goodbye 👋")
            break
        answer = answer_question(pdf_text, question)
        print(answer)

if __name__ == "__main__":
    main()
