#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import requests
from google.oauth2 import service_account
from googleapiclient.discovery import build

# ——————————————
# 設定
# ——————————————
SERVICE_ACCOUNT_FILE = ''    # サービスアカウントキーのパス
CALENDAR_ID = 'primary'                                   # 共有したカレンダーID（通常 'primary'）
SLACK_WEBHOOK_URL = os.environ.get('SLACK_WEBHOOK_URL')   # 環境変数に設定推奨
TIMEZONE = 'Asia/Tokyo'
# ——————————————

def get_calendar_service():
    """サービスアカウント認証で Google Calendar API クライアントを返す"""
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=['https://www.googleapis.com/auth/calendar.readonly']
    )
    return build('calendar', 'v3', credentials=creds)

def fetch_todays_events(service):
    """当日のイベントを取得してリストで返す"""
    tz = ZoneInfo(TIMEZONE)
    today = datetime.now(tz)
    start_of_day = today.replace(hour=0, minute=0, second=0, microsecond=0)
    end_of_day = start_of_day + timedelta(days=1)

    events_result = service.events().list(
        calendarId=CALENDAR_ID,
        timeMin=start_of_day.isoformat(),
        timeMax=end_of_day.isoformat(),
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    return events_result.get('items', [])

def format_slack_message(events):
    """Slack に送るメッセージ文字列を生成"""
    if not events:
        return "📅 *今日の予定はありません*"

    lines = ["📅 *今日の予定一覧*"]
    for evt in events:
        start = evt['start'].get('dateTime', evt['start'].get('date'))
        # ISO フォーマット → 日本時間表示
        dt = datetime.fromisoformat(start).astimezone(ZoneInfo(TIMEZONE))
        time_str = dt.strftime('%H:%M')
        lines.append(f"- {time_str} ｜ {evt.get('summary','(タイトルなし)')}")
    return "\n".join(lines)

def send_slack_notification(message):
    """Slack Webhook へ通知を送信"""
    if not SLACK_WEBHOOK_URL:
        print("Error: SLACK_WEBHOOK_URL が設定されていません。", file=sys.stderr)
        sys.exit(1)
    payload = {"text": message}
    resp = requests.post(SLACK_WEBHOOK_URL, json=payload)
    resp.raise_for_status()

def main():
    service = get_calendar_service()
    events = fetch_todays_events(service)
    msg = format_slack_message(events)
    send_slack_notification(msg)
    print("Slack に通知しました。")

if __name__ == '__main__':
    main()
