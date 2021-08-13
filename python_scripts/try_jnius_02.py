import os
from pathlib import Path


# before importing jnius we need to set some environment variables

java_server_path = r"C:\Program Files\Java\jre1.8.0_221\bin\server"
java_home_path = r"C:\Program Files\Java\jdk1.8.0_221\bin"
jar_file_path = r"..\src\Human.jar"


def _assert_paths_exist(*paths):
    for path in paths:
        assert Path(path).exists(), f"Path '{path}' does not exist."


_assert_paths_exist(java_server_path, java_home_path, jar_file_path)

os.environ["PATH"] += ";" + java_server_path
os.environ['JAVA_HOME'] = java_home_path
os.environ["CLASSPATH"] = jar_file_path

from jnius import autoclass


# now load a class from the jar file and use it
Human = autoclass("Human")
human = Human(100, "Fero")
human.print()
