import os
import subprocess
import humanize


def main():
    completed_process = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True
    )
    files = []
    total_size = 0
    for path in completed_process.stdout.strip().split("\n"):
        size = os.path.getsize(path)
        files.append((size, path))
        total_size += size
    files.sort(key=lambda size_and_path: size_and_path[0], reverse=True)

    def format_size(size):
        return "{:>6} {:<5}".format(*humanize.naturalsize(size, binary=True).split())

    for (size, path) in files:
        print("{} | {:4.0%} | {}".format(format_size(size), size / total_size, path))
    print("{}".format(format_size(total_size)))


if __name__ == "__main__":
    main()
