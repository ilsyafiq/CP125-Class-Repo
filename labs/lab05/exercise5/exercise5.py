
def clean_sessions(pool, sessions, dead_servers):
    remove_later = []
    for server in pool:
        if server in dead_servers:
            remove_later.append(server)
    
    i = 0
    for session in sessions[:]:
        if session[0] in remove_later:
            sessions.remove(session)
    
    sessions.sort()
    return sessions

# Test
pool = ("srv-A", "srv-B", "srv-C", "srv-D")
sessions = [("srv-B", "cli-1"), ("srv-A", "cli-2"), ("srv-C", "cli-3"),
            ("srv-B", "cli-4"), ("srv-D", "cli-5")]
dead = []

result = clean_sessions(pool, sessions, dead)
print(f"Cleaned Sessions: {result}")
# Expected: [('srv-A', 'cli-2'), ('srv-C', 'cli-3')]
