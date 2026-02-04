def get_unique_attendees(attendance_logs):
    attendee_id = set()
    for log in attendance_logs:
        attendee_id.add(log[0])
    return attendee_id

def count_unique_events(attendance_logs, attendee_id):
    for attendee in attendee_id:
        if attendee_id

def filter_by_threshold(attendees, attendance_logs, min_events):
    """Return sorted list of attendees who attended >= min_events."""
    pass

def find_frequent_attendees(attendance_logs, min_events):
    """Find attendees who attended at least min_events unique events."""
    pass


attendance_logs = [
    ("A1", "Workshop_Python"),
    ("A1", "Workshop_Data"),
    ("A2", "Workshop_Python"),
    ("A1", "Workshop_Python"),  # duplicate
    ("A3", "Workshop_Data"),
    ("A2", "Workshop_Data"),
    ("A2", "Workshop_Web")
]
