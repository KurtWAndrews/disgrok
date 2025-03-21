# Custom Discord Bot with Grok Integration

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg) ![Discord.py](https://img.shields.io/badge/Discord.py-2.0+-green.svg) ![xAI](https://img.shields.io/badge/xAI-Grok_API-orange.svg) ![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

A custom Discord bot built with Python, utilizing the `discord.py` library and integrating the Grok API from xAI for advanced AI-powered responses.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features

- Seamless integration with Discord using `discord.py`.
- AI-powered responses via the Grok API from xAI.
- Customizable commands for interacting with Grok.
- Error handling for robust bot operation.
- Environment variable support for secure API key management.

---

## Prerequisites

Before you begin, ensure you have the following:

- **Python 3.9+**: Installed on your system ([Download Python](https://www.python.org/downloads/)).
- **Discord Bot Token**: Obtainable from the [Discord Developer Portal](https://discord.com/developers/applications)).
- **Grok API Key**: Provided by xAI (sign up at [xAI's website](https://x.ai/) if available).
- **Git**: For cloning the repository (optional).

---

## Installation

1. **Clone the Repository** (or download the source code):

   ```bash
   git clone https://github.com/yourusername/your-bot-repo.git
   cd your-bot-repo
   ```

1. **Set Up a Virtual Environment** (recommended):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 - # Installs Poetry globally so you can use it (alternate to pip install poetry for chromeos linux container).
   poetry init # Creates the pyproject.toml configuration file.
   poetry add "aiohttp>=3.10,<3.10.11" # poetry won't add discord.py without aiohttp 3.10.10 or lower
   poetry add discord.py # Declares discord.py as a dependency in pyproject.toml.
   poetry install # Installs aiohttp and discord.py (and creates the virtual environment and lock file).
   poetry run python bot.py # Runs your bot in the virtual environment with all dependencies available.

   poetry self add poetry-plugin-export # add the export plugin to poetry
   poetry export --without-hashes --format=requirements.txt --output=requirements.txt # create a requirements.txt for pip just in case
   ```
