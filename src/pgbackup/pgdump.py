import subprocess
import sys

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSEerror as err:
        print(f"Error: {err}")
        sys.exit(1)


