import argparse
from datetime import datetime
from services.booking import check_availability, reserve_cabin

def main():
    parser = argparse.ArgumentParser(description="Система бронирования кабинетов")
    parser.add_argument("action", choices=["check", "reserve"])
    parser.add_argument("--cabin", type=int, required=True)
    parser.add_argument("--time", required=True, help="YYYY-MM-DD HH:MM")
    parser.add_argument("--user_name")
    parser.add_argument("--user_email")
    parser.add_argument("--user_phone")
    parser.add_argument("--duration", type=int)

    args = parser.parse_args()
    time = datetime.strptime(args.time, "%Y-%m-%d %H:%M")

    if args.action == "check":
        print(check_availability(args.cabin, time))
    elif args.action == "reserve":
        print(reserve_cabin(
            args.cabin,
            args.user_name,
            args.user_email,
            args.user_phone,
            time,
            args.duration
        ))


if __name__ == "__main__":
    main()
