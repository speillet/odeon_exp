# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from dataclasses import dataclass
from omegaconf import DictConfig, OmegaConf
import hydra
from hydra.core.config_store import ConfigStore


@dataclass
class MySQLConfig:
    host: str = "localhost"
    port: int = 3306


@dataclass
class UserInterface:
    title: str = "My app"
    width: int = 1024
    height: int = 768


@dataclass
class MyConfig:
    db: MySQLConfig = MySQLConfig()
    ui: UserInterface = UserInterface()


cs = ConfigStore.instance()
cs.store(name="config", node=MyConfig)


@hydra.main(config_path=None, config_name="config")
def my_app(cfg: MyConfig) -> None:
    print(f"Title={cfg.ui.title}, size={cfg.ui.width}x{cfg.ui.height} pixels")
    print(60 * "#")
    print(OmegaConf.to_yaml(cfg))
    print(60 * "#")
    print(OmegaConf.to_container(cfg))
    print(60 * "#")

if __name__ == "__main__":
    my_app()
