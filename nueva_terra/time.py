from datetime import UTC, datetime, timedelta

from nextcord.utils import utcnow

ANP = datetime(year=2023, month=1, day=1, tzinfo=UTC)
ZERO = datetime(year=1, month=1, day=1, tzinfo=UTC)


def time_since_anp() -> timedelta:
    return utcnow() - ANP


def current() -> datetime:
    since_anp = time_since_anp().total_seconds()

    return ZERO + (timedelta(seconds=since_anp) * 8)


def current_format() -> str:
    datetime = current()
    date = datetime.strftime("%d %b %Y ANP")

    time = datetime.strftime("%H:%M")
    time = time.rjust(len(date))

    return f"{date}\n\n{time}"
