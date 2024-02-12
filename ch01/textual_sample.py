from textual.app import App, ComposeResult
from textual.widgets import Label

class HelloWorld(App):
    CSS_PATH = "align.tcss"

    def compose(self) -> ComposeResult:
        yield Label("Hello World!", id="hello")
        yield Label("(Press CTRL+C to exit)")

    def on_mount(self) -> None:
        self.screen.styles.background = "darkblue"
        hello_label = self.query_one("#hello")
        hello_label.styles.color = "white"
        hello_label.styles.content_align = ("center", "middle")

if __name__ == "__main__":
    app = HelloWorld()
    app.run()
