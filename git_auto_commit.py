import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Timer, Lock

IGNORE_DIRS = {".git", "__pycache__", ".venv", "venv", "node_modules"}
BATCH_INTERVAL = 60

class GitAutoCommitHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.changed_files = set()
        self.lock = Lock()
        self.timer = None

    def on_any_event(self, event):
        if event.is_directory:
            return
        for ignored in IGNORE_DIRS:
            if ignored in event.src_path:
                return
        with self.lock:
            self.changed_files.add(event.src_path)
        self.schedule_commit()

    def schedule_commit(self):
        with self.lock:
            if self.timer is None:
                self.timer = Timer(BATCH_INTERVAL, self.commit_changes)
                self.timer.start()

    def commit_changes(self):
        with self.lock:
            files = list(self.changed_files)
            self.changed_files.clear()
            self.timer = None
        if files:
            print(f"Detected changes in {len(files)} files.")
            try:
                subprocess.run(["git", "add", "."], check=True)
                message = f"Auto commit: changes in {len(files)} files"
                subprocess.run(["git", "commit", "-m", message], check=True)
                print("Committed successfully.")
                confirm = input("Push to remote? (y/n): ").strip().lower()
                if confirm == "y":
                    subprocess.run(["git", "push"], check=True)
                    print("Pushed to remote.")
                else:
                    print("Push skipped.")
            except subprocess.CalledProcessError as e:
                print(f"Git error: {e}")

if __name__ == "__main__":
    path = "."
    event_handler = GitAutoCommitHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print("Watching for changes... Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Stopped watching.")
    observer.join()
