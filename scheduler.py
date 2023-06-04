from taskset import TaskSet



class Scheduler(object):
    def __init__(self, data):
        """constructor

        Args:
            data (json): json object of tasks data
        """
        self.taskSet = TaskSet(data)
        
        self.resources = {}
    
    def size(self):
        """return the size of task set

        Returns:
            int: len of tasks
        """
        return len(self.taskSet)
    
    def run(self, limit):
        """execute scheduler in an amount of time

        Args:
            limit (int): timeline

        Returns:
            dict: time and jobs
        """
        jobsList = {}
        
        for time in range(limit):
            currentJob = None
            
            jobs = [job for job in self.taskSet.getJobs() if job.isActive(time)] # get all active jobs
            jobs.sort(key=lambda x: x.getFP(), reverse=True) # sort jobs by deadline monothonic
            
            if len(jobs) > 0: # schedule when we have jobs
                currentJob = jobs[0]
                
            if currentJob != None: # do the job
                currentJob.doJob()

            jobsList[time] = currentJob
        
        return jobsList
