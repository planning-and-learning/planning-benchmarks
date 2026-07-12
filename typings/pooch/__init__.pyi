"""Minimal local stubs for pooch (no upstream py.typed), covering what we use."""

from collections.abc import Callable
from pathlib import Path

def os_cache(project: str) -> Path: ...

class Untar:
    def __init__(self, members: list[str] | None = None, extract_dir: str | None = None) -> None: ...
    def __call__(self, fname: str, action: str, pooch: Pooch) -> list[str]: ...

Downloader = Callable[[str, str, "Pooch"], object]

class Pooch:
    path: Path
    abspath: Path
    registry: dict[str, str]
    def fetch(
        self,
        fname: str,
        processor: Untar | None = None,
        downloader: Downloader | None = None,
        progressbar: bool = False,
    ) -> str | list[str]: ...
    def load_registry(self, fname: str | Path) -> None: ...

def create(
    path: str | Path,
    base_url: str,
    version: str | None = None,
    version_dev: str = "master",
    env: str | None = None,
    registry: dict[str, str] | None = None,
    urls: dict[str, str] | None = None,
    retry_if_failed: int = 0,
    allow_updates: bool | str = True,
) -> Pooch: ...
