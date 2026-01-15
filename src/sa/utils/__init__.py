"""Utilities module"""

from .config import config, Config
from .suggestions import SuggestionEngine
from .database import db, Database
from .projects import project_manager, ProjectManager

__all__ = [
    "config",
    "Config",
    "SuggestionEngine",
    "db",
    "Database",
    "project_manager",
    "ProjectManager",
]
