from datetime import datetime

def log_event(event_type: str, **kwargs) -> None:
    print(f"Event type: {event_type}")
    timestamp = datetime.now().isoformat()
    print(f"Timestamp: {timestamp}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main():
    log_event("UserLogin", user="JohnDoe", status="Success", ip="192.168.1.1")
    print("---------------------------------")
    log_event("FileUpload", user="JohnDoe", status="Failure", filename="report.pdf", reason="File too large")

if __name__ == "__main__":
    main()