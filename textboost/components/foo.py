from textual.app import ComposeResult
from textual.widgets import Button, Header, Footer, Static, Input, Label
from textual.containers import Container
from textual.reactive import reactive
from textual.validation import Validator, Function


class InputField(Static):
    """An input field widget"""

    user_input = reactive("")
    user_splitted = reactive([])

    def on_input_changed(self, event: Input.Changed) -> str:
        self.user_input = event.input.value
        # self.user_splitted = ut.splitted_value(self.user_inputs)

    def compose(self) -> ComposeResult:
        """Child widgets for stopwatch"""

        yield Input(placeholder="Place your command...", id="input")
        yield Button("Submit", id="submit", variant="primary")
        yield Label("First time? Write --help to get started!")
