from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input, Label
from textual.containers import ScrollableContainer, Container, Horizontal, Vertical
from textual.reactive import reactive
from utility import utils as ut
from textual.validation import Validator, Function

# """
# Input Validation:

# Utilize a Validator built-in widget to validate the user input.
# Ensure that the user input includes the "--command-type {args}" format.

# Message Prompting:

# Include a message prompt in the middle of executing each function, similar to the prompts in utils.py.
# This message should provide feedback or instructions during the execution process.
# Error Handling and Validation:

# Ensure that the widget includes proper error handling.
# Display error messages when the user input is not in the required format or if any issues occur during execution.

# Additional Ideas:

# Explore other functionalities that can be integrated into the utility function.
# Consider additional widgets or user interface elements to enhance the user experience.
# Implement error logging to capture and record any errors encountered during execution.
# Design an interactive help system to provide guidance on available commands and their usage.
# """

# # TODO - Grabbing input value from input widget


class Intro(Static):
    """An introduction text widget"""


class InputField(Static):
    """An input field widget"""

    user_input = reactive("")

    def on_input_changed(self, event: Input.Changed) -> str:
        self.user_input = event.input.value

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Place your command...", id="input")
        yield Button("Submit", id="submit", variant="primary")
        yield Label("First time? Write --help to get started!")


class TextBoost(App):
    """TextBoost App"""

    CSS_PATH = "main.css"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            self.user_input = self.query_one(InputField).user_input
            splitted = ut.splitted_value(self.user_input)
            with open("debug.txt", "w") as f:
                f.write(self.user_input)

            ut.cli_command_utilizer(splitted)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield InputField()


# if __name__ == "__main__":
#     app = TextBoost()
#     app.run()


testing = "--add-file ./pre-modified/test.md testing"
testing_process = "--process-file"

splitted_1 = ut.splitted_value(testing)
splitted_2 = ut.splitted_value(testing_process)
print(splitted_2, splitted_1)
ut.cli_command_utilizer(splitted_1)
ut.cli_command_utilizer(splitted_2)
ut.add_file_utilizer(splitted_1[1:])
ut.process_file_utilizer()
