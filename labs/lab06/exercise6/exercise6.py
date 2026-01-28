def manage_roster(enrolled, drop_requests, waitlist):
    for student in drop_requests:
        enrolled.discard(student)

    if len(enrolled) < 5:
        add = 7 - len(enrolled)
        for student in list(waitlist)[:add]:
            enrolled.add(student)
            waitlist.remove(student)

    return len(enrolled)
