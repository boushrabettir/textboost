from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static
from textual.containers import Container, Horizontal, Vertical
from utility import utils as ut
from components.widgets import InputField, Instructions
from datetime import datetime


class TextBoost(App):
    """TextBoost App"""

    BINDINGS = [("e", "exit_application", "Exit Application")]
    CSS_PATH = "main.css"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Proceeds with functionality when a button is pressed"""

        user_input = self.query_one(InputField).user_input
        splitted = ut.splitted_value(user_input)
        action_type = event.button.id

        if event.button.id == "add":
            ut.cli_command_utilizer(splitted, action_type)
        if event.button.id == "process":
            ut.cli_command_utilizer(splitted, action_type)
        if event.button.id == "view":
            ut.access_unprocessed_list()
        if event.button.id == "delete":
            ut.cli_command_utilizer(splitted, action_type)
        if event.button.id == "find":
            ut.cli_command_utilizer(splitted, action_type)

    def action_exit_application(self) -> None:
        """An action to toggle dark mode."""
        self.exit()

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="background-text-panel_2"):
            yield Static(
                f"WELCOME TO TEXTBOOST\nDate: {datetime.now().strftime('%m/%d/%Y')}"
            )
        with Container(id="background-panel"):
            with Vertical(id="input-area"):
                yield InputField()
                with Horizontal(id="buttons"):
                    yield Button("Add Files📃", id="add", variant="default")
                    yield Button("Process Files📨", id="process", variant="primary")
                with Horizontal(id="buttons2"):
                    yield Button("View Files📤", id="view", variant="warning")
                    yield Button("Delete File📭", id="delete", variant="error")
                    yield Button("Find File📬", id="find", variant="success")
                yield Static("Made with 💖 by @boushrabettir.")
        with Container(id="background-text-panel"):
            yield Instructions()
        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
