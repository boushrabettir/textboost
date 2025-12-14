import subprocess
import re
import os
import math
from ml.summarize import create_summarization


def modify_markdown_file(file_path: str) -> None:
    """Removes the first and last line of Markdown file"""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Pattern with exists throughout the PDF
    pattern = r'<a\s+name="br\d+"></a>'

    # Remove those unnecessary lines from that pattern
    lines = [line for line in lines if not re.search(pattern, line)]

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def modify_content(file_path: str, name: str, folder: str, summarize: str) -> None:
    """Modifies the content for bionic reading"""

    modify_markdown_file(file_path)

    # Read lines from markdown
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()

    skip_pattern = (
        r"^(1\.|2\.|[3-9]\d?|100\.[0-9]?[0-9]?|[1-4]\d\d\.|500\.|-|#|##|###|####)"
    )

    modified_lines = []

    for line in lines:
        words = []
        for word in line.split():
            bolding = math.ceil(len(word) / 2)
            if (
                re.match(skip_pattern, word)
                or "**" in word
                or any(c in word[:bolding] for c in ".:-")
            ):
                words.append(word)
            else:
                words.append("**" + word[:bolding] + "**" + word[bolding:])
        modified_lines.append(" ".join(words))

    text = "\n".join(modified_lines)

    # Add summarization
    if summarize.lower() == "true":
        summarization = create_summarization(file_path)
        text += f"\n\n\n**Summarization**:\n\n{summarization}\n"

    # Debug log for PDF generation
    with open("step3finalstep.txt", "a", encoding="utf-8") as f:
        f.write(f"Writing modified markdown to: {folder}/{name}.md\n")
        f.write(f"Modified text length: {len(text)}\n")

    # Write markdown
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/{name}.md", "w", encoding="utf-8") as f:
        f.write(text)


def md_to_pdf(name: str, folder: str) -> None:
    """Converts markdown file to PDF file"""

    md_path = f"{folder}/{name}.md"
    pdf_path = f"{folder}/{name}.pdf"

    # Check if file exists
    if not os.path.exists(md_path):
        print(f"ERROR: Markdown file '{md_path}' does not exist!")
        return

    try:
        # Run mdpdf and show errors
        subprocess.run(
            ["mdpdf", "-o", pdf_path, md_path],
            check=True,  # raises CalledProcessError on failure
        )
    except subprocess.CalledProcessError as e:
        print("mdpdf failed with error:", e)
    except FileNotFoundError:
        print("mdpdf executable not found! Make sure it is installed and in your PATH.")

    # Only remove markdown if PDF exists
    if os.path.exists(pdf_path):
        os.remove(md_path)
