# imports the class LogLine
from display_log import LogLine


# user input log line
log_line_input = input("Enter log line: ")


# sanitise access_log and create the LogLine object
def parse(access_log: str):
    # splits access_log from a string into a list by using space delimiter
    split_log = remove_quotes(access_log.split(' '))
    # variables containing strings from split_log list for defined index
    timestamp = remove_square_bracket(split_log[0])
    req_method = split_log[1]
    req_path = split_log[2]
    protocol = split_log[3]
    response_code = split_log[4]
    response_flag = split_log[5]
    response_code_details = split_log[6]
    connection_term_details = split_log[7]
    transport_failure_reason = split_log[8]
    bytes_received = split_log[9]
    bytes_sent = split_log[10]
    duration = split_log[11]
    upstream_service_time = split_log[12]
    req_forwarded_for = split_log[13]
    req_user_agent = split_log[14]
    req_request_id = split_log[15]
    req_authority = split_log[16]
    upstream_host = split_log[17]
    upstream_cluster = split_log[18]
    upstream_local_address = split_log[19]
    downstream_local_address = split_log[20]
    downstream_remote_address = split_log[21]
    requested_server_name = split_log[22]
    route_name = split_log[23]
    return LogLine(timestamp, req_method, req_path, protocol, response_code, response_flag, response_code_details,
                   connection_term_details, transport_failure_reason, bytes_received, bytes_sent, duration,
                   upstream_service_time, req_forwarded_for, req_user_agent, req_request_id, req_authority,
                   upstream_host, upstream_cluster, upstream_local_address, downstream_local_address,
                   downstream_remote_address, requested_server_name, route_name)


# removes square brackets from a string
def remove_square_bracket(raw_string: str):
    return raw_string.strip("[]")


# removes quotes from items in a list
def remove_quotes(raw_list: list):
    return [x.strip('"') for x in raw_list]


# LogLine object is stored in a variable
log_line_object = parse(log_line_input)
# calls the function in the object to display table with enriched log data
log_line_object.display_enriched_log()