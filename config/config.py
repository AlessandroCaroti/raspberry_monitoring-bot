import logging

# Telegram Web API Token
TOKEN: str = '123456789:abcxdefghijklmnopqrs-tuvwxyzabcdefg'

# Location to store the saved users
USERS_STORAGE_PATH: str = '/opt/monitoring-bot/config/users.csv'

# The Regex used to find the IP in the webservice response
IP_REGEX: str = '([0-9]{1,3}\.){3}[0-9]{1,3}'

# Logger format for whole application
LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# General log level to use in the application
LOG_LEVEL: int = logging.INFO

# Turn verification of host keys off or on.
# Not advisable, only turn off in private networks and for testing purposes, if ever
VERIFY_HOST_KEYS: bool = True