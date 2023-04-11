from _typeshed import Incomplete

class LogManager:
    log_level: Incomplete
    console_handler: Incomplete
    formatter: Incomplete
    loggers: Incomplete
    def __init__(self) -> None: ...
    def get_logger(self, module_name): ...
    def set_level(self, level: int) -> None: ...

log_manager: Incomplete
