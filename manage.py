#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")

    from django.core.management import execute_from_command_line
    port = os.environ.get("PORT", 5000)
    
    try:
        int(sys.argv[2][-4:])
        sys.argv[2] = sys.argv[2][:-4] + str(port)
    except:
        pass
    execute_from_command_line(sys.argv)
