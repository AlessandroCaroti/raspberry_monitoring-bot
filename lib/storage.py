import os.path
import logging
from typing import List, Union, Callable

import config.config as config
from lib.types import Command, SSHCommand, Machine, User

# Compatible machine file version with this code
from lib.utils import is_not_blank

MACHINE_FILE_VERSION: str = '3.0'
# Compatible command file version with this code
COMMAND_FILE_VERSION: str = '2.0'
# Compatible user file version with this code
USER_FILE_VERSION: str = '1.0'

logging.basicConfig(
    format=config.LOG_FORMAT,
    level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)


def read_users_file(path: str) -> List[User]:
    return __read_storage_file(path, __line_to_user, USER_FILE_VERSION)


def __read_storage_file(path: str, line_converter: Callable[[str], Union[User, Machine, Command]],
                        filespec_version: str) -> Union[List[Union[User, Machine, Command]], None]:
    objects = []
    logger.info('Reading stored entries from "{p}"'.format(p=path))
    # Warning: file contents will not be validated
    if not os.path.isfile(path):
        logger.error('No file found in {p}'.format(p=path))
        return
    with open(path, 'r') as f:
        for i, line in enumerate(f):
            # Remove all whitespaces
            line = line.strip()
            # Handle Settings
            if line.startswith('$VERSION'):
                _, value = line.split('=', 1)
                if not value.strip() == filespec_version:
                    raise ValueError('Incompatible storage file version')
            elif is_not_blank(line):
                objects.append(line_converter(line))
            else:
                continue

    return objects


def __line_to_user(line: str) -> User:
    line = "".join(line.split())
    uid, name, telegram_id, permissions = line.split(';', 3)
    permission_list = __get_permissions_for_stringlist(permissions)
    return User(int(uid), name, telegram_id, permission_list)


def __get_permissions_for_stringlist(value: str) -> List[str]:
    permissions = value.split(',')
    return permissions
