# Kiwiaga

Kiwiaga ([**Kiwi**](https://en.wikipedia.org/wiki/Kiwifruit) + Manga) is a CLI tool made for exhibit info about manga from [**Mangadex**](https://mangadex.org/).

> Currently, this tool is a personal need of mine and shows only "latest chapter" info

## Installation

You can get it from PyPi:

```bash
pip install kiwiaga
```

## Usage

```bash
kiwiaga --help
```

```
                                                                                                                                                         
 Usage: kiwiaga [OPTIONS] COMMAND [ARGS]...                                                                                                              
                                                                                                                                                         
╭─ Options ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --version             -v,-V        Show the current version.                                                                                          │
│ --install-completion               Install completion for the current shell.                                                                          │
│ --show-completion                  Show completion for the current shell, to copy it or customize the installation.                                   │
│ --help                             Show this message and exit.                                                                                        │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ add    Add a new manga to list from UUID.                                                                                                             │
│ show   Show latest chapter info from manga list.                                                                                                      │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

- `add`: receives a manga `UUID` from Mangadex

    Firstly, any manga from the Mangadex platform has a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). So, you can add a manga to the list following the steps below:

    ```bash
    kiwiaga add manga_uuid
    ```

- `show`: receives a language code from [ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes), default is `"en"`

    > Mangadex depends on the scans. Those scans came from various parts of the world. So, you need to specify which `language-code` you want to extract info for, and then the API responds with the info from a scan that corresponds to it.

    Basically, this command shows the info about latest chapter by a given `language-code` (the default value is "`en`"). The codes supported are all from [ISO 639](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes). Follow the below:

    ```bash
    kiwiaga show language-code
    ```

## TODO

- [ ] Show more interesting info about manga from the Mangadex API
- [ ] I don't know, it's totally 4fun
