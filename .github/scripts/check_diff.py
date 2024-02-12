import json
import sys
import os

LANGCHAIN_DIRS = {
    "libs/genai",
    "libs/vertexai",
}

if __name__ == "__main__":
    files = sys.argv[1:]
    dirs_to_run = set()

    if len(files) == 300:
        # max diff length is 300 files - there are likely files missing
        raise ValueError("Max diff reached. Please manually run CI on changed libs.")

    for file in files:
        if any(
            file.startswith(dir_)
            for dir_ in (
                ".github/workflows",
                ".github/tools",
                ".github/actions",
                "libs/core",
                ".github/scripts/check_diff.py",
            )
        ):
            dirs_to_run.update(LANGCHAIN_DIRS)
        elif file.startswith("libs/"):
            dirs_to_run.update(LANGCHAIN_DIRS)
        else:
            pass
    json_output = json.dumps(list(dirs_to_run))
    print(f"dirs-to-run={json_output}")