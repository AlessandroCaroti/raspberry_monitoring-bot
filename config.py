import logging

# Telegram Web API Token
TOKEN: str = '5471117147:AAE6Po0_Z4IDhUlGiM8HKZnxkmQUeRiGOAM'

# Location to store the saved machines
MACHINES_STORAGE_PATH: str = '/mnt/c/Users/carot/Documents/GitHub/shepherd-bot/config/machines.csv'

# Location to store the saved commands
COMMANDS_STORAGE_PATH: str = '/mnt/c/Users/carot/Documents/GitHub/shepherd-bot/config/commands.csv'

# Location to store the saved users
USERS_STORAGE_PATH: str = '/mnt/c/Users/carot/Documents/GitHub/shepherd-bot/config/users.csv'

# The Regex used to find the IP in the webservice response
IP_REGEX: str = '([0-9]{1,3}\.){3}[0-9]{1,3}'

# Logger format for whole application
LOG_FORMAT: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# General log level to use in the application
LOG_LEVEL: int = logging.INFO

# Turn verification of host keys off or on.
# Not advisable, only turn off in private networks and for testing purposes, if ever
VERIFY_HOST_KEYS: bool = True
