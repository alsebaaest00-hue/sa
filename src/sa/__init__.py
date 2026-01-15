"""sa package"""

__version__ = "0.1.0"
__author__ = "alsebaaest00"
__description__ = "منصة تحويل النصوص إلى صور وفيديوهات مع إضافة الصوت"

from .generators import ImageGenerator, VideoGenerator, AudioGenerator
from .utils import config, Config, SuggestionEngine

__all__ = [
    "ImageGenerator",
    "VideoGenerator",
    "AudioGenerator",
    "SuggestionEngine",
    "config",
    "Config",
]
