import csv
import random
from datetime import datetime, timedelta, date
from pathlib import Path


def generate_fake_logs(num_rows: int, output_path: str, log_date: date) -> None:
    """
    Generate a CSV file with synthetic web log data.

    Columns:
    - event_time (timestamp)
    - user_id (e.g. user_001)
    - endpoint (/home, /products, /cart, /login)
    - status_code (200, 201, 400, 404, 500)
    - response_ms (integer milliseconds)
    - user_agent (desktop, mobile, tablet)
    """
    endpoints = ["/", "/home", "/products", "/product/123", "/cart", "/login", "/search"]
    status_codes = [200, 200, 200, 201, 400, 404, 500]  # more 200s (success rate) than errors
    user_agents = ["desktop", "mobile", "tablet"]

    # Use log_date as base
    day_start = datetime(log_date.year, log_date.month, log_date.day, 0, 0, 0)
    day_end = day_start + timedelta(days=1)

    # Make sure parent directory exists
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header row
        writer.writerow(
            ["event_time", "user_id", "endpoint", "status_code", "response_ms", "user_agent"]
        )

        for i in range(num_rows):
            # Random timestamp within the day
            random_seconds = random.randint(0, 24 * 60 * 60 - 1)
            event_time = day_start + timedelta(seconds=random_seconds)

            user_id = f"user_{random.randint(1, 500):03d}"
            endpoint = random.choice(endpoints)
            status_code = random.choice(status_codes)
            response_ms = random.randint(50, 2000)
            user_agent = random.choice(user_agents)

            writer.writerow(
                [
                    event_time.isoformat(timespec="seconds"),
                    user_id,
                    endpoint,
                    status_code,
                    response_ms,
                    user_agent,
                ]
            )

    print(f"Generated {num_rows} log rows at: {output_file.resolve()}")


if __name__ == "__main__":
   # Configuration: how many days and rows per day
    days_back = 10         # generate logs for today and 6 previous days
    rows_per_day = 2000   

    today = date.today()

    for offset in range(days_back):
        log_date = today - timedelta(days=offset)
        date_str = log_date.strftime("%Y%m%d")  # e.g. 20260126
        output_path = f"date/logs_{date_str}.csv"

        generate_fake_logs(
            num_rows=rows_per_day,
            output_path=output_path,
            log_date=log_date
        )
