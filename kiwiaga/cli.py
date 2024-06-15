from typing import Optional
from uuid import UUID

import typer
from rich.console import Console
from typing_extensions import Annotated

from kiwiaga import __app__, __version__
from kiwiaga.config import Config
from kiwiaga.manga import Manga

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

    manga = Manga(manga_uuid)
    if manga.exists():
        config = Config()

        if not config.path.exists():
            config.write(config.template)

        config.read()

        if str(manga_uuid) in config.yaml["mangas"]:
            console.print("Manga already exists in the list.")
            raise typer.Exit(1)

        config.yaml["mangas"].append(str(manga_uuid))
        config.write(config.yaml)

        console.print(
            f"Manga from UUID ({manga_uuid}) has been added to the list."
        )

        raise typer.Exit(0)

    console.print(f"Manga from UUID ({manga_uuid}) doesn't exist.")
    raise typer.Exit(1)


@app.command()
def show(lang: Annotated[Optional[str], typer.Argument(...)] = "en"):
    """Show latest chapter info from manga list."""
    print(lang)
