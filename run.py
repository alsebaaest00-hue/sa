#!/usr/bin/env python
"""Main entry point for the SA application"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from sa.ui.app import main

if __name__ == "__main__":
    main()
