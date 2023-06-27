# Textboost

## About Textboost

TextBoost is an innovative tool that leverages the power of AI and machine learning to enhance the reading experience, particularly for individuals with ADHD.

## How TextBoost Harnesses Machine Learning

Powered by advanced machine learning algorithms, TextBoost offers additional data science-driven features that further enrich the user experience:

- **Folder Management within "Downloads"**: TextBoost provides the capability to organize files within the "Downloads" directory. The model can create subsections such as `Downloads/food`, `Downloads/space`, `Downloads/politics`, and more and store the respected pdf within their folder.

## Usage

- Git clone this repository by running the command `https://github.com/boushrabettir/textboost.git`
- Move to the `textboost` folder by running `cd ./textboost`
- Pip install all the requirements by running `pip install -r requirements.txt`
- Run the script by typing `python ./textboost.py`
- In the input bar type `--help` and to get started

> **PLEASE NOTE THE FOLLOWING**<br/>
> The updated PDF will be automatically placed in their respective folders dependent on the context of the text. The model will place your file in a folder similar to `textboost/history/your_file.py`<br/>
> Make sure to take a look in the current directory you are in to find your outputted file

## Key Features

- Selective bold formatting to emphasize specific letters within words.
- Customization options to adjust the level of bold formatting.
- Export modified files while preserving the original content.

## Demo

- Video goes here

---

Made with 🐱💛 by Boushra Bettir

---

Delete below this line when completed with this branch

## To Do in Current Branch:

- [x] Get basic functionality working
- [x] Possibility of getting a folder on their downloads, and look in that folder and there can be subsections like `Downloads/food` or `Downloads/makeup` or `Downloads/clothing` etc. And dependent on the context of the outputted pdf, the machine learning algorithm will place the pdf in their respected folder
- [ ] Fix the model (inconsistent in placing pdfs in their respective folders)
- [ ] Make UI a prettier
- [ ] Add all the other CLI commands that I have to do in `utils.py`
- [ ] Add font size change capabilites as well as how many letters per word to be bolded

## To Do in Next Branch:

- [ ] Use machine learning techniques to translate to other languages (This is an optinal feature dependent if the user wants it)
- [ ] Grammar/Quality Assessment (This is an optional feature users can disable)
