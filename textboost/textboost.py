from textual.app import App, ComposeResult
from textual.widgets import Button, Header, Footer, Static
from textual.containers import ScrollableContainer


class IntroLargeText(Static):
    """A widget to display the main larger texts"""


class Introduction(Static):
    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield IntroLargeText("TEXTBOOST")
        yield Button("Help", id="")


class TextBoost(App):
    # CSS_PATH = "main.css"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        # yield ScrollableContainer(Testing())

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark


if __name__ == "__main__":
    app = TextBoost()
    app.run()
