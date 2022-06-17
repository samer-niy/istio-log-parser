from tabulate import tabulate  # Imports a module into this file


class LogLine:
    # using self in class to access methods and attributes
    def __init__(self, timestamp, req_method, req_path, protocol, response_code, response_flag, response_code_details,
                 connection_term_details, transport_failure_reason, bytes_received, bytes_sent, duration,
                 upstream_service_time, req_forwarded_for, req_user_agent, req_request_id, req_authority, upstream_host,
                 upstream_cluster, upstream_local_address, downstream_local_address, downstream_remote_address,
                 requested_server_name, route_name):
        self.timestamp = timestamp
        self.req_method = req_method
        self.req_path = req_path
        self.protocol = protocol
        self.response_code = response_code
        self.response_flag = response_flag
        self.response_code_details = response_code_details
        self.connection_term_details = connection_term_details
        self.transport_failure_reason = transport_failure_reason
        self.bytes_received = bytes_received
        self.bytes_sent = bytes_sent
        self.duration = duration
        self.upstream_service_time = upstream_service_time
        self.req_forwarded_for = req_forwarded_for
        self.req_user_agent = req_user_agent
        self.req_request_id = req_request_id
        self.req_authority = req_authority
        self.upstream_host = upstream_host
        self.upstream_cluster = upstream_cluster
        self.upstream_local_address = upstream_local_address
        self.downstream_local_address = downstream_local_address
        self.downstream_remote_address = downstream_remote_address
        self.requested_server_name = requested_server_name
        self.route_name = route_name

    # other is the argument expected from class not from method
    def __eq__(self, other): # Creating a function that compares two objects
        return self.timestamp == other.timestamp, \
               self.req_method == other.req_method, \
               self.req_path == other.req_path, \
               self.protocol == other.protocol, \
               self.response_code == other.response_code, \
               self.response_flag == other.response_flag, \
               self.response_code_details == other.response_code_details, \
               self.connection_term_details == other.connection_term_details, \
               self.transport_failure_reason == other.transport_failure_reason, \
               self.bytes_received == other.bytes_received, \
               self.bytes_sent == other.bytes_sent, \
               self.duration == other.duration, \
               self.upstream_service_time == other.upstream_service_time, \
               self.req_forwarded_for == other.req_forwarded_for, \
               self.req_user_agent == other.req_user_agent, \
               self.req_request_id == other.req_request_id, \
               self.req_authority == other.req_authority, \
               self.upstream_host == other.upstream_host, \
               self.upstream_cluster == other.upstream_cluster, \
               self.upstream_local_address == other.upstream_local_address, \
               self.downstream_local_address == other.downstream_local_address, \
               self.downstream_remote_address == other.downstream_remote_address, \
               self.requested_server_name == other.requested_server_name, \
               self.route_name == other.route_name

    # prints the table with values from log data
    def display_enriched_log(self):
        table = [           # Create a list for tabulate
            ['Format Type', 'Log Value'],
            ['START_TIME', self.timestamp],
            ['REQUEST_METHOD', self.req_method],
            ['REQUEST_ORIGINAL_PATH', self.req_path],
            ['PROTOCOL', self.protocol],
            ['RESPONSE_CODE', self.response_code],
            ['RESPONSE_FLAG', self.response_flag],
            ['RESPONSE_CODE_DETAILS', self.response_code_details],
            ['CONNECTION_TERMINATION_DETAILS', self.connection_term_details],
            ['UPSTREAM_TRANSPORT_FAILURE_REASON', self.transport_failure_reason],
            ['BYTES_RECEIVED', self.bytes_received],
            ['BYTES_SENT', self.bytes_sent],
            ['DURATION', self.duration],
            ['RESP_UPSTREAM_SERVICE_TIME', self.upstream_service_time],
            ['REQUEST_FORWARDED_FOR', self.req_forwarded_for],
            ['REQUEST_USER_AGENT', self.req_user_agent],
            ['REQUEST_REQUEST ID', self.req_request_id],
            ['REQUEST_AUTHORITY', self.req_authority],
            ['UPSTREAM_HOST', self.upstream_host],
            ['UPSTREAM_CLUSTER', self.upstream_cluster],
            ['UPSTREAM_LOCAL_ADDRESS', self.upstream_local_address],
            ['DOWNSTREAM_LOCAL_ADDRESS', self.downstream_local_address],
            ['DOWNSTREAM_REMOTE_ADDRESS', self.downstream_remote_address],
            ['REQUESTED_SERVER_NAME', self.requested_server_name],
            ['ROUTE_NAME', self.route_name],
        ]
        print(tabulate(table)) # displays the table using tabulate module
