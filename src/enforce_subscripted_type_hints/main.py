import logging
from src.enforce_subscripted_type_hints.config import Config
from src.enforce_subscripted_type_hints._logger import (
    get_dir_path,
    setup_logger,
)

Config().set_filepath(get_dir_path(__file__, 2, "configs/example_config.yaml"))

setup_logger(__file__, 2)
logger = logging.getLogger()
