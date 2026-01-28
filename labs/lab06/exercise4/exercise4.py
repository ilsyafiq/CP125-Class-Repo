def synchronize_databases(legacy_list, modern_set, blacklist):
    passed = set()
    for user in legacy_list:
        if user[1] not in blacklist:
            passed.add(user[0])
    
    return passed - modern_set, modern_set - passed
