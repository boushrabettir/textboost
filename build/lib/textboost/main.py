from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Label
from textual.containers import Container, Horizontal, Vertical
from utility import utils as ut
from components.widgets import InputField, Instructions, LeftWidget
from textual.reactive import reactive
from textual.widget import Widget


class Message(Widget):
    """Message widget for specific file functions"""

    message = reactive("")

    def render(self) -> str:
        return self.message


class TextBoost(App):
    """TextBoost App"""

    BINDINGS = [("e", "exit_application", "Exit Application")]
    CSS_PATH = "main.css"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Proceeds with functionality when a button is pressed"""

        user_input = self.query_one(InputField).user_input

        splitted = ut.splitted_value(user_input)
        action_type = event.button.id

        if event.button.id == "view":
            self.query_one(Message).message = ut.access_unprocessed_list()
        else:
            self.query_one(Message).message = ut.cli_command_utilizer(
                splitted, action_type
            )

    def action_exit_application(self) -> None:
        """An action to toggle dark mode."""
        self.exit()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="background-text-panel-2"):
            yield Message()
        with Container(id="background-panel"):
            with Vertical(id="input-area"):
                yield LeftWidget()
                yield InputField()
                with Horizontal(id="buttons"):
                    yield Button("Add Files📃", id="add", variant="default")
                    yield Button("Process Files📨", id="process", variant="primary")
                with Horizontal(id="buttons2"):
                    yield Button("View Files🔎", id="view", variant="warning")
                    yield Button("Delete File📭", id="delete", variant="error")
                    yield Button("Find File📬", id="find", variant="success")
                yield Static("Made with 🐱💖 by @boushrabettir.")
        with Container(id="background-text-panel"):
            yield Instructions()
        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
