# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from dataclasses import dataclass
from typing import Any

from omegaconf import OmegaConf

import hydra
from hydra.core.config_store import ConfigStore


@dataclass
class MySQLConfig:
    driver: str = "mysql"
    host: str = "localhost"
    port: int = 3306


@dataclass
class PostGreSQLConfig:
    driver: str = "postgresql"
    host: str = "localhost"
    port: int = 5432
    timeout: int = 10


@dataclass
class Config:
    # We will populate db using composition.
    db: Any


cs = ConfigStore.instance()
cs.store(name="config", node=Config)
cs.store(group="db", name="mysql", node=MySQLConfig)
cs.store(group="db", name="postgresql", node=PostGreSQLConfig)


@hydra.main(config_path=None, config_name="config")
def my_app(cfg: Config) -> None:
    print(60 * "#")
    print(OmegaConf.to_yaml(cfg))
    print(60 * "#")
    print(OmegaConf.to_container(cfg))
    print(60 * "#")



if __name__ == "__main__":
    my_app()
