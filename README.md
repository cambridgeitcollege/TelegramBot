# Telegram Bot Message Sender

This Python script allows you to send a message to a personal chat or channel using a Telegram bot. It utilizes the `python-telegram-bot` library to interact with Telegram's API asynchronously.

## Features

- Sends custom messages to a personal chat or Telegram channel
- Uses the Telegram Bot API to interact with Telegram
- Scheduled message sending capabilities

## Requirements

- Python 3.7+
- Telegram Bot Token
- Python Libraries: 
  - `python-telegram-bot`
  - `python-dotenv`
  - `asyncio`

## GitHub Actions Workflows

This repository includes several automated workflows:

### 📅 Scheduled Message Sender (`scheduled-message.yml`)
- **Triggers**: Daily at 9:00 AM UTC (configurable), Manual dispatch
- **Features**:
  - Automated daily message sending
  - Custom message input via workflow dispatch
  - Secure environment variable handling
  - Execution logging


## Setup and Usage

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/cambridgeitcollege/TelegramBot
   cd TelegramBotCode
   ```

2. **Set up a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**
   - Create a .env file in the root of the project:
   ```bash
   cp .env.example .env
   ```
   - Edit the `.env` file and add your credentials:
     - `BOTAPIKEY`: Get this by creating a bot via [@BotFather](https://t.me/botfather) on Telegram
     - `CHATID`: Your personal chat ID or channel ID

5. **Run the Script:**
   ```bash
   python3 main.py
   ```

### GitHub Actions Setup

To use the automated workflows, you need to set up repository secrets:

1. **Rename the Folder:**
   - Rename the folder `.github.example/workflows` to `.github/workflows`

2. **Go to your GitHub repository → Settings → Secrets and variables → Actions**

3. **Add the following secrets:**
   - `BOTAPIKEY`: Your Telegram bot API key
   - `CHATID`: Your chat or channel ID

4. **Available Workflows:**
   - **Manual Message Sending**: Go to Actions → "Scheduled Message Sender" → "Run workflow"
   - **Automated Daily Messages**: Runs automatically at 9:00 AM UTC

### Customizing Messages

You can customize the message by:

1. **Direct code modification:**
   Edit the `message` variable in `main.py`

2. **GitHub Actions manual trigger:**
   Use the workflow dispatch feature to send custom messages

3. **Scheduled messages:**
   Modify the cron schedule in `.github/workflows/scheduled-message.yml`

## Project Structure

```
TelegramBotCode/
├── .github/
│   └── workflows/
│       ├── scheduled-message.yml     # Scheduled Message Sender
├── .env.example                     # Environment variables template
├── .gitignore                       # Git ignore file
├── main.py                          # Main bot script
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
├── LICENSE                          # MIT License
├── CodeOfConduct.md                 # Code of conduct
├── Contribution.md                  # Contribution guidelines
```

## Contributing

We welcome contributions! If you'd like to contribute to this Telegram Bot project, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct

Please review our [Code of Conduct](CodeOfConduct.md) before participating in this project.

## License

This project is licensed under the MIT [License](LICENSE).

## Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - Python wrapper for Telegram Bot API
- [GitHub Actions](https://github.com/features/actions) - For automation and CI/CD