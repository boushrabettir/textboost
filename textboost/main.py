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


class InputField(Static):
    """An input field widget"""

    message = reactive("")
    user_input = reactive("")

    def on_input_changed(self, event: Input.Changed) -> str:
        self.user_input = event.input.value

    def compose(self) -> ComposeResult:
        yield Container(
            Vertical(
                Input(placeholder="Place your command..."),
                Horizontal(
                    Button("Add Files📃", id="add", variant="default"),
                    Button("Process Files📨", id="process", variant="primary"),
                    Button("View Files📤", id="view", variant="warning"),
                    Button("Delete File📭", id="delete", variant="error"),
                    Button("Find File📬", id="find", variant="success"),
                ),
            ),
            classes="container",
        )

        # Static(
        #     "Made with 💖 by @boushrabettir[https://github.com/boushrabettir]."
        # ),


class TextBoost(App):
    """TextBoost App"""

    CSS_PATH = "main.css"
    BINDINGS = [("e", "exit_application", "Exit Application")]

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.user_input = self.query_one(InputField).user_input
        self.message = self.query_one(InputField).message

        if event.button.id == "add":
            splitted = ut.splitted_value(self.user_input)
            self.message = ut.cli_command_utilizer(splitted, event.button.id)
        elif event.button.id == "process":
            splitted = ut.splitted_value(self.user_input)
            self.message = ut.cli_command_utilizer(splitted, event.button.id)
        elif event.button.id == "view":
            self.message = ut.access_unprocessed_list()
        elif event.button.id == "delete":
            self.message = ut.cli_command_utilizer(self.user_input, event.button.id)
        elif event.button.id == "find":
            self.message = ut.cli_command_utilizer(self.user_input, event.button.id)

        self.query_one(InputField).user_input = ""

    def action_exit_application(self) -> None:
        """An action to toggle dark mode."""

        self.exit()

    def compose(self) -> ComposeResult:
        yield Header()
        yield InputField()
        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
