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

### Calendar Sharing and Service Account Setup
1. Share your Google Calendar with your service account’s email (found under `client_email` in your JSON key) and grant “See all event details” permission.
2. Place your service account JSON key file in a secure location (e.g., the project root) and set the `GOOGLE_SERVICE_ACCOUNT_FILE` environment variable to its full path.
3. If you are using a calendar other than the primary one, set the `CALENDAR_ID` environment variable to your calendar’s ID (e.g., `your.email@gmail.com`).

### Environment Variables Examples
```bash
export GOOGLE_SERVICE_ACCOUNT_FILE="/path/to/your-key.json"
export CALENDAR_ID="your.email@gmail.com"  # optional, defaults to 'primary'
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/XXX/YYY/ZZZ"
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
