import logging


def yes_no_input() -> bool:
  # raw_input returns the empty string for "enter"
  yes = {'yes', 'y', 'ye', ''}
  no = {'no', 'n'}

  choice = input().lower()
  if choice in yes:
    return True
  elif choice in no:
    return False
  else:
    logging.error("Please respond with 'yes' or 'no'")
    return False
