# sinch-sdk-python-snippets

Sinch Python SDK Code Snippets Repository

This repository contains code snippets demonstrating usage of the
[Sinch Python SDK](https://github.com/sinch/sinch-sdk-python).

## Requirements
- Python 3.9 or later
- [Poetry](https://python-poetry.org/) for dependency management
- [Sinch account](https://dashboard.sinch.com)
- [Sinch package](https://pypi.org/project/sinch/)


## Snippets execution settings
When executing a snippet, you will need to provide some information about your Sinch account (credentials, Sinch virtual phone number, ...)

This setting can be placed directly in the snippet source, or you can use an [environment file](.env), in which case the settings will be shared and used automatically by every snippet.

Install dependencies using Poetry:

```bash
poetry install
```


## Running snippets

All available code snippets are located in the `snippets/` directory, structured by feature and corresponding actions.

To execute a specific snippet, navigate to the appropriate subdirectory and run:

```shell
python run python snippet.py
```