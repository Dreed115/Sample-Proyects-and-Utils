from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json

class MyHandeler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(track_folder):
            i = 1
            if filename != "Test1":
                new_file = filename
                file_exist = os.path.isfile(destination_folder + '\\' + new_file)
                while file_exist:
                    i += 1
                    new_file = os.path.splitext(track_folder + '\\' + filename)[0] + str(i) + os.path.splitext(track_folder + '\\' + new_file)[1]
                    new_file = new_file.split("\\")[6]
                    file_exist = os.path.isfile(destination_folder + '\\' + new_file)
            
                src = track_folder + "\\" + filename
                new_file = destination_folder + "\\" + new_file
                os.rename(src, new_file)


track_folder = "C:\\Users\\diego\\OneDrive\\Escritorio\\Test"
destination_folder = "C:\\Users\\diego\\OneDrive\\Escritorio\\Test\\Test1"
event_handeler = MyHandeler()
observer = Observer()
observer.schedule(event_handeler, track_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()