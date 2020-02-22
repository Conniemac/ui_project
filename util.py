from datetime import timedelta


def build_now_string(now) -> str:

    month = now.month
    month = "0" + str(month) if month < 10 else str(month)

    day = now.day
    day = "0" + str(day) if day < 10 else str(day)

    year = str(now.year)

    hour = now.hour
    hour = "0" + str(hour) if hour < 10 else str(hour)

    minute = now.minute
    minute = "0" + str(minute) if minute < 10 else str(minute)

    second = now.second
    second = "0" + str(second) if second < 10 else str(second)

    return f"{month}/{day}/{year} {hour}:{minute}:{second}"


def build_past_string(now, interval):

    return build_now_string(now - timedelta(hours=interval))