# currency-converter-telegram-bot

## Overview

`currency-converter-telegram-bot` is a Telegram bot that allows users to quickly convert currencies using real-time exchange rates. The bot is designed to be simple, fast, and user-friendly.

## Features

- Real-time currency conversion.
- Supports a wide range of currencies.
- Easy-to-use Telegram interface.
- Lightweight and efficient.

## Prerequisites

- Docker application on host machine.
- A Telegram account.
- A Telegram bot token (can be obtained from [BotFather](https://core.telegram.org/bots#botfather)).
- An API key for a currency exchange rate provider (e.g., [ExchangeRate](https://exchangerate.host/)).

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dzibab/currency-converter-telegram-bot.git
    cd currency-converter-telegram-bot
    ```

2. Set up environment variables:
    Create a `.env` file in the project root and add the following:
    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    EXCHANGE_API_KEY=your_exchange_api_key
    ```

## Usage

1. Start the bot:
    ```bash
    docker compose up -d
    ```

2. Open Telegram and search for your bot.

3. Send a message in the format:
    ```
    <amount> <from_currency> <to_currency>
    ```
    Example:
    ```
    100 USD EUR
    ```

4. The bot will reply with the converted amount.

## Acknowledgments

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [ExchangeRate API](https://exchangerate.host/)