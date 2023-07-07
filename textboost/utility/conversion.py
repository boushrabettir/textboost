import subprocess
import re


def modify_markdown_file(file_path: str) -> None:
    """"""

    with open(file_path, "r") as file:
        lines = file.readlines()

    # Remove the first and last lines
    lines = lines[1:-1]

    # Write the updated content back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)


def modify_content(file_path: str) -> None:
    """"""
    modify_markdown_file(file_path)

    lines_to_extract = []

    with open(file_path, "r") as file:
        text = file.read()
        lines = re.findall(r".+?(?=\n|$)", text, re.DOTALL)
        lines_to_extract.extend(lines)

    skip_pattern = (
        r"^(1\.|2\.|[3-9]\d?|100\.[0-9]?[0-9]?|[1-4]\d\d\.|500\.|-|#|##|###|####)"
    )

    for i in range(len(lines_to_extract)):
        line = lines_to_extract[i]
        bolded_line = []
        for word in line.split():
            if re.match(skip_pattern, word):
                bolded_line.append(word)
            elif "**" in word:
                bolded_line.append(word)
            else:
                bolded_line.append("**" + word[:2] + "**" + word[2:])

        lines_to_extract[i] = bolded_line

        if i < len(lines_to_extract) - 1:
            lines_to_extract[i].append("\n")

    for i in range(len(lines_to_extract)):
        lines_to_extract[i] = " ".join(lines_to_extract[i])

    text = "".join(lines_to_extract)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)


def md_to_pdf(name: str, folder: str, file_path) -> None:
    """Converts markdown file to PDF file"""

    try:
        subprocess.run(
            [
                "mdpdf",
                "-o",
                f"{folder}/{name}.pdf",
                f"{file_path}",
            ]
        )
    except subprocess.CalledProcessError:
        print("Issue calling subprocess 'mdpdf' command.")
    except FileNotFoundError:
        print(f"File path '{file_path}' not found.")
