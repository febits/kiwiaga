from typing import Optional
from uuid import UUID

import typer
from rich.console import Console
from typing_extensions import Annotated

from kiwiaga import __app__, __version__

app = typer.Typer(help="")
console = Console()


def version_cb(value: bool):
    """Callback that shows the current version."""

    if value:
        console.print(__app__, __version__)
        raise typer.Exit(0)


@app.callback()
def main(
    version: Annotated[
        Optional[bool],
        typer.Option(
            "--version",
            "-v",
            "-V",
            help="Show the current version.",
            is_flag=True,
            callback=version_cb,
        ),
    ] = False
):
    """Configure a callback to print version number."""


@app.command()
def add(manga_uuid: Annotated[UUID, typer.Argument(...)]):
    """Add a new manga to list from UUID."""
    print(manga_uuid)


@app.command()
def show(lang: Annotated[Optional[str], typer.Argument(...)] = "en"):
    """Show latest chapter info from manga list."""
    print(lang)
