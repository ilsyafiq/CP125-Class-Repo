def audit_zero_trust(baseline_set, current_log_list):
   current_log_list = set(current_log_list)
   authorized = baseline_set & current_log_list
   alert = current_log_list - baseline_set
   inactive = baseline_set - current_log_list

   return authorized, alert, inactive