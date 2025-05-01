# Slack Calendar Reminder Bot for Raspberry Pi

A simple Python script, `calendar_reminder.py`, that runs on a Raspberry Pi, fetches today's events from Google Calendar using a service account, and sends a morning reminder to Slack via an Incoming Webhook.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Cron Job](#cron-job)
- [Author](#author)
- [License](#license)

## Prerequisites
1. **Python 3.6+** installed on your Raspberry Pi.
2. **Google Calendar API** service account JSON key file.
3. **Slack Incoming Webhook URL**.
4. Internet access on the Raspberry Pi.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/slack-calendar-reminder-bot.git
   cd slack-calendar-reminder-bot
   ```
2. Install required Python packages:
   ```bash
   pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib requests
   ```

## Configuration
1. Place your service account key JSON file in the project directory:
   ```bash
   mv /path/to/your-key.json ./your-service-account.json
   ```
2. Update the path in `calendar_reminder.py` to point to the actual location of your service account JSON file. Update the directory path as needed:
   ```python
   SERVICE_ACCOUNT_FILE = '/home/pi/path/to/your-service-account.json'  # update the path to your JSON file as needed
   ```
3. Export your Slack Webhook URL as an environment variable:
   ```bash
   echo 'export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXXX/YYYY/ZZZZ"' >> ~/.bashrc
   source ~/.bashrc
   ```

## Usage
Run the script manually to test:
```bash
python3 calendar_reminder.py
```
On success, you should see a Slack notification with today’s events.

## Cron Job
To automate daily reminders at 08:00 AM, add a cron entry. Update the script and log file paths as needed.

```bash
crontab -e
```
Add the following line (replace paths as appropriate):
```cron
0 8 * * * /usr/bin/python3 /home/pi/path/to/calendar_reminder.py >> /home/pi/path/to/calendar_reminder.log 2>&1
```
Save and exit.

## Author
- **Murasan** (https://murasan-net.com/)

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
