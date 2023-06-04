import sys
import json

from display import Display
from scheduler import Scheduler



if __name__ == "__main__":
    # get file path and time
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        time = int(sys.argv[2])
    else:
        file_path = "taskset.json"
        time = 50

    with open(file_path) as json_data:
        data = json.load(json_data)
    
    # create scheduler
    s = Scheduler(data=data)
    jobs = s.run(time)
    
    for t, j in jobs.items():
        if j != None:
            print(f'{t:02d} | {j}')
    
    # show diagram
    Display(jobs, time, s.size())
