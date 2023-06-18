import argparse
from rich.console import RenderableType
from textual import events
from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input, Label
from textual.widget import Widget
from textual.containers import ScrollableContainer, Container
from textual.reactive import reactive
import utils as ut
from textual.app import App
from textual import events

"""

Design Steps:

User Input Widget:

Create a widget that allows users to enter input.
Track the user input, possibly using the query_one function.

Input Processing:

Upon pressing the Enter key, capture the entered value.
Call the utility function with the captured input as an argument.

Input Validation:

Utilize a Validator built-in widget to validate the user input.
Ensure that the user input includes the "--command-type {args}" format.

Utility Function Execution:

Split the validated user input into a list of command and arguments.
Example: User input "--add-file potato 3 4 chicken" should be split into ["--add-file", "potato 3 4 chicken"].
Call the utility function, passing the command and arguments as parameters.
Example: " ".join([x for x in arguments.{ARGUMENT}])
All types of commands are in utils.py

Message Prompting:

Include a message prompt in the middle of executing each function, similar to the prompts in utils.py.
This message should provide feedback or instructions during the execution process.

argparse Integration:

Consider using the argparse library for command-line parsing.
Implement argparse to handle the command-line arguments passed to the utility function.
This will enable a structured and robust way to parse arguments and handle errors.

Error Handling and Validation:

Ensure that the widget includes proper error handling.
Display error messages when the user input is not in the required format or if any issues occur during execution.

Additional Ideas:

Explore other functionalities that can be integrated into the utility function.
Consider additional widgets or user interface elements to enhance the user experience.
Implement error logging to capture and record any errors encountered during execution.
Design an interactive help system to provide guidance on available commands and their usage.
"""


class ActionsApp(App):
    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_key(self, event: events.Key) -> None:
        if event.key == "d":
            self.action_set_background("red")


if __name__ == "__main__":
    app = ActionsApp()
    app.run()
