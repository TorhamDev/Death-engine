from rich.console import Console
from rich.markdown import Markdown

def print_readme() -> None:

    MARKDOWN = open("./README.md").read()
    console = Console()
    md = Markdown(MARKDOWN)
    console.print(md)