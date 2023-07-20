from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from utility import utils as ut
from textual.validation import Validator, Function
import time


# https://textual.textualize.io/widgets/progress_bar/


class Message(Static):
    """"""

    user_input = reactive("")


class InputField(Static):
    """An input field widget"""

    message = reactive("")
    user_input = reactive("")

    def on_input_changed(self, event: Input.Changed) -> str:
        self.user_input = event.input.value

    def compose(self) -> ComposeResult:
        with Container(id="background-panel"):
            with Vertical(id="input-area"):
                yield Input(placeholder="Place your command...")
                with Horizontal(id="buttons"):
                    yield Button("Add Files📃", id="add", variant="default")
                    yield Button("Process Files📨", id="process", variant="primary")
                    yield Button("View Files📤", id="view", variant="warning")
                    yield Button("Delete File📭", id="delete", variant="error")
                    yield Button("Find File📬", id="find", variant="success")

        # Static(
        #     "Made with 💖 by @boushrabettir[https://github.com/boushrabettir]."
        # ),


class TextBoost(App):
    """TextBoost App"""

    BINDINGS = [("e", "exit_application", "Exit Application")]
    CSS_PATH = "main.css"

    def on_input_changed(self, event: Input.Changed) -> str:
        self.query_one(Message).user_input = event.input.value

    def on_button_pressed(self, event: Button.Pressed) -> None:
        message = self.query_one(Message).user_input

        if event.button.id == "add":
            splitted = ut.splitted_value(message)
            ut.cli_command_utilizer(splitted, event.button.id)
        elif event.button.id == "process":
            splitted = ut.splitted_value(message)
            ut.cli_command_utilizer(splitted, event.button.id)
        elif event.button.id == "view":
            ut.access_unprocessed_list()
        elif event.button.id == "delete":
            ut.cli_command_utilizer(message, event.button.id)
        elif event.button.id == "find":
            ut.cli_command_utilizer(message, event.button.id)

    def action_exit_application(self) -> None:
        """An action to toggle dark mode."""

        self.exit()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="background-panel"):
            with Vertical(id="input-area"):
                yield Input(placeholder="Place your command...")
                with Horizontal(id="buttons"):
                    yield Button("Add Files📃", id="add", variant="default")
                    yield Button("Process Files📨", id="process", variant="primary")
                    yield Button("View Files📤", id="view", variant="warning")
                    yield Button("Delete File📭", id="delete", variant="error")
                    yield Button("Find File📬", id="find", variant="success")
        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
