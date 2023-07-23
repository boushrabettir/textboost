from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from utility import utils as ut
from dataclasses import dataclass

# TODO - Figure out message


@dataclass
class Message:
    message: str


message_holder = Message("")
MESSAGE = message_holder.message
# END-TODO


class Instructions(Static):
    """Instructions text widget"""

    def compose(self) -> ComposeResult:
        yield Static("INSTRUCTIONS", id="bolded")
        yield Static("\n1. Add Files - [FILE_PATH] [NEW_FILE_NAME]\n")
        yield Static("2. Process Files - [TRUE/FALSE] (Text summarization)\n")
        yield Static("3. View Files - [FILE_PATH]\n")
        yield Static(
            "4. Delete Files -[FILE_PATH]\nAdd a file path, or place nothing \nto delete the most recent file.\n"
        )
        yield Static("5. Find Files - [FILE_PATH]")


class InputField(Static):
    """Input field widget"""

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
        """Proceeds with functionality when a button is pressed"""

        user_input = self.query_one(InputField).user_input
        splitted = ut.splitted_value(user_input)
        action_type = event.button.id

        if event.button.id == "add":
            message_holder.message = ut.cli_command_utilizer(splitted, action_type)
        if event.button.id == "process":
            message_holder.message = ut.cli_command_utilizer(splitted, action_type)
        if event.button.id == "view":
            message_holder.message = ut.access_unprocessed_list()
        if event.button.id == "delete":
            message_holder.message = ut.cli_command_utilizer(splitted, action_type)
        if event.button.id == "find":
            message_holder.message = ut.cli_command_utilizer(splitted, action_type)

    def action_exit_application(self) -> None:
        """An action to toggle dark mode."""
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
                yield Static(MESSAGE)
                yield Static("Made with 💖 by @boushrabettir.")
        with Container(id="background-text-panel"):
            yield Instructions()

        yield Footer()


if __name__ == "__main__":
    app = TextBoost()
    app.run()
