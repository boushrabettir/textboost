from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from utility import utils as ut
from textual.validation import Validator, Function
import time


class InputField(Static):
    """"""

    user_input = reactive("")

    def on_input_changed(self, event: Input.Changed) -> str:
        self.user_input = event.input.value

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Place your command...")


class TextBoost(App):
    """TextBoost App"""

    BINDINGS = [("e", "exit_application", "Exit Application")]
    CSS_PATH = "main.css"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Debugger
        # with open("debug.txt", "w", encoding="utf-8") as f:
        #     f.write(self.query_one(InputField).user_input + " " + event.button.id)

        user_input = self.query_one(InputField).user_input

        # TODO - Update utils
        if event.button.id == "add":
            splitted = ut.splitted_value(user_input)
            ut.add_file_utilizer(splitted)
        if event.button.id == "process":
            ut.process_file_utilizer(user_input)
        if event.button.id == "view":
            ut.access_unprocessed_list()
        if event.button.id == "delete":
            ut.delete_file(user_input)
        if event.button.id == "find":
            ut.find_file(user_input)

    def action_exit_application(self) -> None:
        """An action to toggle dark mode."""
        print(self.query_one(InputField).user_input)
        self.exit()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="background-panel"):
            with Vertical(id="input-area"):
                yield InputField()
                with Horizontal(id="buttons"):
                    yield Button("Add Files📃", id="add", variant="default")
                    yield Button("Process Files📨", id="process", variant="primary")
                    yield Button("View Files📤", id="view", variant="warning")
                    yield Button("Delete File📭", id="delete", variant="error")
                    yield Button("Find File📬", id="find", variant="success")

                yield Static(
                    "Made with 💖 by @boushrabettir[https://github.com/boushrabettir]."
                )

        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
