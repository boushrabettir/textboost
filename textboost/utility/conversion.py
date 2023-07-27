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

    # Holds lines from the markdown file
    lines_to_extract = []

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        lines = re.findall(r".+?(?=\n|$)", text, re.DOTALL)
        lines_to_extract.extend(lines)

    # Skip pattern to not add bolding around specific special characters
    skip_pattern = (
        r"^(1\.|2\.|[3-9]\d?|100\.[0-9]?[0-9]?|[1-4]\d\d\.|500\.|-|#|##|###|####)"
    )

    for i in range(len(lines_to_extract)):
        # Current line from the list
        line = lines_to_extract[i]

        # Holds the modified bolded line
        bolded_line = []
        for word in line.split():
            # Calculate the amount of letters to bold per word
            bolding_per_word = math.ceil(len(word) / 2)

            # If word already has ** or exists within the skip pattern, simply append the word into the line
            if (
                re.match(skip_pattern, word)
                or "**" in word
                or "." in word[:bolding_per_word]
                or ":" in word[:bolding_per_word]
                or "-" in word[:bolding_per_word]
            ):
                bolded_line.append(word)
            else:
                bolded_line.append(
                    "**" + word[:bolding_per_word] + "**" + word[bolding_per_word:]
                )

        # Modify the value to the bolded line
        lines_to_extract[i] = bolded_line

        if i < len(lines_to_extract) - 1:
            lines_to_extract[i].append("\n")

    # Join each line together
    for i in range(len(lines_to_extract)):
        lines_to_extract[i] = " ".join(lines_to_extract[i])

    # Join each sentence to one big text
    text = "".join(lines_to_extract)

    # Add summarized text if the user wants text summarization
    if summarize.lower() == "true":
        # Create summary through pretrained model
        summarization = create_summarization(file_path)
        text += f"\n\n\n**Summarization**:\n\n{summarization}\n"

    with open(f"{folder}/{name}.md", "w", encoding="utf-8") as file:
        file.write(text)


def md_to_pdf(name: str, folder: str) -> None:
    """Converts markdown file to PDF file"""

    # Try to convert MD to PDF
    try:
        with open(os.devnull, "w") as null_file:
            subprocess.run(
                [
                    "mdpdf",
                    "-o",
                    f"{folder}/{name}.pdf",
                    f"{folder}/{name}.md",
                ],
                stdout=null_file,
                stderr=null_file,
            )
    except subprocess.CalledProcessError:
        print("Issue calling subprocess 'mdpdf' command.")
    except FileNotFoundError:
        print(f"File path '{folder}/{name}.md' not found.")
