import time

# prints a message with a delay and blank lines
def delayed_print(message="", delay=1.5, blank_lines=1):
    print(message)
    time.sleep(delay)
    if blank_lines > 0:
        print("\n" * blank_lines, end="")