#Log File Analyzer

def get_file():
    """
    Prompts user for a file name, opens it, and returns the lines
    parameters: none
    returns: file
    """
    file_name = input("Which log file would you like to check? (Do not include .txt) ")
    file = open(f"{file_name}.txt", 'r')
    lines = file.readlines()
    file.close()
    return lines


def parse_line(line):
    """
    Takes a line and splits it into seperate parts to make for easier counting and organzing
    parameters: single line from log file
    returns: line parts
    """
    line = line.strip()
    parts = line.split()
    message = " ".join(parts[4:])
    parts = parts[:4]
    parts.append(message)
    return parts


def count_severities(file):
    """
    Counts the number of each severity type
    Parameters: file
    Returns: dictionary consisting of how many times each severity type appeared
    """
    
    sev_count = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0,
    "CRITICAL": 0,
    }
    
    lines = file
    for line in lines:
        parts = parse_line(line)
        if parts[2] == "INFO":
            sev_count["INFO"] += 1
        elif parts[2] == "WARNING":
            sev_count["WARNING"] += 1
        elif parts[2] == "ERROR":
            sev_count["ERROR"] += 1
        elif parts[2] == "CRITICAL":
            sev_count["CRITICAL"] += 1

    return sev_count


def count_services(file):
    """
    Counts the number of each service type
    Parameters: file
    Returns: dictionary consisting of how many times each service type appeared
    """
    
    serv_count = {
    }

    lines = file
    for line in lines:
        parts = parse_line(line)
        if parts[2] == "ERROR" or parts[2] == "CRITICAL":
            if parts[3] not in serv_count:
                serv_count[parts[3]] = 0
                serv_count[parts[3]] += 1
            else:
                serv_count[parts[3]] += 1
    return serv_count
        

def get_criticals(file):
    """
    Determins which lines of the log wre critical so that the user can review those lines
    Parameters: file
    Returns: List of critical severities
    """
    criticals = []
    lines = file
    for line in lines:
        parts = parse_line(line)
        if parts[2] == "CRITICAL":
            criticals.append(line)
    return criticals


def print_summary(service_count, sev_count, criticals, file_length):
    """
    Neatly displays all important information from the log
    Parameters: service dictionary, severity dictionary, critical alerts, and number of entries
    Returns: none
    """

    print("=== LOG SUMMARY ===")
    print(f"Total entries: {file_length}")
    print(f"INFO: {sev_count['INFO']}")
    print(f"WARNING: {sev_count['WARNING']}")
    print(f"ERROR: {sev_count['ERROR']}")
    print(f"CRITICAL: {sev_count['CRITICAL']}")
    print()

    print("=== CRITICAL ALERTS ===")
    for crit in criticals:
        print(crit)
    print()

    print("=== TOP ERRORS BY SERVICE ===")
    for service in service_count:
        print(f"{service} - {service_count[service]} occurrence(s)")


def main():
    """
    Gathers all the important information to easily pass to print_summary() for results
    Parameters: none
    Returns: none
    """
    file = get_file()
    service_count = count_services(file)
    sev_count = count_severities(file)
    criticals = get_criticals(file)
    file_length = 0
    for line in file:
        file_length += 1

    print_summary(service_count, sev_count, criticals, file_length)
    
main()
    
