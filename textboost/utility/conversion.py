import subprocess
import re
import os


def modify_markdown_file(file_path: str) -> None:
    """Removes the first and last line of Markdown file"""

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    pattern = r'<a\s+name="br\d+"></a>'
    lines = [line for line in lines if not re.search(pattern, line)]

    # Write the updated content back to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(lines)


def modify_content(
    file_path: str,
    name: str,
    folder: str,
) -> None:
    """Modifies the content for bionic reading"""

    modify_markdown_file(file_path)

    lines_to_extract = []

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
        lines = re.findall(r".+?(?=\n|$)", text, re.DOTALL)
        lines_to_extract.extend(lines)

    # Skip pattern to not add **** around them
    skip_pattern = (
        r"^(1\.|2\.|[3-9]\d?|100\.[0-9]?[0-9]?|[1-4]\d\d\.|500\.|-|#|##|###|####)"
    )

    for i in range(len(lines_to_extract)):
        line = lines_to_extract[i]
        bolded_line = []
        for word in line.split():
            # If word already has ** or exists within the skip pattern, simply append the word into the line
            if (
                re.match(skip_pattern, word)
                or "**" in word
                or "." in word[:2]
                or ":" in word[:2]
            ):
                bolded_line.append(word)
            else:
                bolded_line.append("**" + word[:2] + "**" + word[2:])

        lines_to_extract[i] = bolded_line

        if i < len(lines_to_extract) - 1:
            lines_to_extract[i].append("\n")

    for i in range(len(lines_to_extract)):
        print(lines_to_extract[i])
        lines_to_extract[i] = " ".join(lines_to_extract[i])

    text = "".join(lines_to_extract)

    with open(f"{folder}/{name}.md", "w", encoding="utf-8") as file:
        file.write(text)


def md_to_pdf(name: str, folder: str) -> None:
    """Converts markdown file to PDF file"""

    try:
        subprocess.run(
            [
                "mdpdf",
                "-o",
                f"{folder}/{name}.pdf",
                f"{folder}/{name}.md",
            ]
        )
    except subprocess.CalledProcessError:
        print("Issue calling subprocess 'mdpdf' command.")
    except FileNotFoundError:
        print(f"File path '{folder}/{name}.md' not found.")

    os.remove(f"{folder}/{name}.md")  # Remove the MD file after conversion
