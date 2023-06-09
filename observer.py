import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/DELL/Downloads'

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'{os.path.basename(event.src_path)} is created')
    def on_moved(self,event):
        print(f'{os.path.basename(event.src_path)} has been moved')

    def on_deleted(self, event):
        print(f'{os.path.basename(event.src_path)} has been deleted')

    def on_modified(self,event):
        print(f'{os.path.basename(event.src_path)} has been modified')
          
               
event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive= True)

observer.start()

try:
    while True:
        print('running', end='\r')
except KeyboardInterrupt:
    time.sleep(1)
    print('Stopped')