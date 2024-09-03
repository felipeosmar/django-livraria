from enum import Enum


class Actions(Enum):
    LIST = "list"
    RETRIEVE = "retrieve"
    MANAGE = "manage"


class DRFAction:
    @staticmethod
    def is_list(action):
        return action in [Actions.LIST.value, Actions.RETRIEVE.value]

    @staticmethod
    def is_manage(action):
        return action in [Actions.MANAGE.value]
