from textual.app import ComposeResult
from textual.widgets import Static, Input
from textual.reactive import reactive
from datetime import datetime


class InputField(Static):
    """Input field widget"""

    user_input = reactive("")

    def on_input_changed(self, event: Input.Changed) -> str:
        self.user_input = event.input.value

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Place your command...")


class Instructions(Static):
    """Instructions text widget"""

    def compose(self) -> ComposeResult:
        yield Static("👾 INSTRUCTIONS 📑", id="bolded")
        yield Static("\n1. Add Files - [FILE_PATH] [NEW_FILE_NAME]\n")
        yield Static("2. Process Files - [TRUE/FALSE] (Text summarization)\n")
        yield Static("3. View Files - [FILE_PATH]\n")
        yield Static(
            "4. Delete Files -[FILE_PATH]\nAdd a file path, or place nothing \nto delete the most recent file.\n"
        )
        yield Static("5. Find Files - [FILE_PATH]")


class LeftWidget(Static):
    """Left most widget"""

    def compose(self) -> ComposeResult:
        yield Static(
            f"🔅💫 WELCOME TO TEXTBOOST 💫🔅\n Date: {datetime.now().strftime('%m/%d/%Y')},",
        )
