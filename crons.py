import datetime as dt
from jobs.a import job_a
from jobs.b import job_b

def logger(msg):
    print(f"""<<====={dt.datetime.now().ctime().split(" ")[3:-1][0]}====>>>>> {msg}""")

def run_job_a():
    ret = job_a()
    logger(ret)

def run_job_b():
    ret = job_b()
    logger(ret)

# if __name__ == '__main__':

#     run_job_a()
