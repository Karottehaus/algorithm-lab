from datetime import datetime, timedelta
from pathlib import Path
from textwrap import dedent
from uuid import uuid4
from settings import TIMEZONE

OUTPUT_FILE = Path("WG4_Meeting.ics")
ZOOM_URL = "https://maine.zoom.us/j/83399700188"


def format_ics_datetime(dt: datetime) -> str:
    return dt.strftime("%Y%m%dT%H%M%S")


def create_ics_content(
        title: str,
        start: datetime,
        end: datetime,
        description: str,
        location: str,
        url: str
) -> str:
    return dedent(f"""\
    BEGIN:VCALENDAR
    VERSION:2.0
    PRODID:-//Hanyu//WG4 Meeting//EN
    CALSCALE:GREGORIAN
    BEGIN:VEVENT
    UID:{uuid4()}
    DTSTAMP:{format_ics_datetime(datetime.now(TIMEZONE))}
    DTSTART;TZID=Europe/Zurich:{format_ics_datetime(start)}
    DTEND;TZID=Europe/Zurich:{format_ics_datetime(end)}
    SUMMARY:{title}
    DESCRIPTION:{description}
    LOCATION:{location}
    URL:{url}
    END:VEVENT
    END:VCALENDAR
    """)


def save_ics_file(content: str, output_path: Path) -> None:
    output_path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    start = datetime(2026, 7, 16, 14, 0, 0, tzinfo=TIMEZONE)
    end = start + timedelta(hours=1)

    description = (
        "July 16, 2026 2:00 PM (Zurich time)\\n\\n"
        f"Zoom: {ZOOM_URL}\\n\\n"
        "Looking forward to seeing you"
    )

    ics_content = create_ics_content(
        title="WG4 Meeting",
        start=start,
        end=end,
        description=description,
        location="Zoom",
        url=ZOOM_URL,
    )

    save_ics_file(ics_content, OUTPUT_FILE)
