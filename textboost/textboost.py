from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input, Label
from textual.containers import ScrollableContainer, Container
from textual.reactive import reactive
from .utility import utils as ut
from textual.app import App
from textual.validation import Validator, Function

"""
Input Validation:

Utilize a Validator built-in widget to validate the user input.
Ensure that the user input includes the "--command-type {args}" format.

Message Prompting:

Include a message prompt in the middle of executing each function, similar to the prompts in utils.py.
This message should provide feedback or instructions during the execution process.
Error Handling and Validation:

Ensure that the widget includes proper error handling.
Display error messages when the user input is not in the required format or if any issues occur during execution.

Additional Ideas:

Explore other functionalities that can be integrated into the utility function.
Consider additional widgets or user interface elements to enhance the user experience.
Implement error logging to capture and record any errors encountered during execution.
Design an interactive help system to provide guidance on available commands and their usage.
"""

# TODO - Grabbing input value from input widget


class InputField(Static):
    """An input field widget"""

    user_input = reactive("")

    def on_input_submitted(self, event: Input.Submitted) -> str:
        return event.input.value

    def compose(self) -> ComposeResult:
        """Child widgets for stopwatch"""

        yield Input(placeholder="Place your command...", id="input")
        yield Button("Submit", id="submit", variant="primary")
        yield Label("First time? Write --help to get started!")


class TextBoost(App):
    """TextBoost App"""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            input_field = self.query_one(InputField)  # How to grab input value?
            # Testing - will delete all of this (works)
            user_input = (
                "--add-file C:/Users/boush/Downloads/test.pdf testing_with_splited"
            )

            splitted_input = ut.splitted_value(user_input)
            ut.cli_command_utilizer(splitted_input)
            user_checkout = "--view-unprocessed-files"
            ut.cli_command_utilizer(user_checkout)

    def compose(self) -> ComposeResult:
        yield Header()
        yield InputField()
        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
