import logging
from services.some_service import SomeService

logger = logging.getLogger('cron_jobs_test')

def invoke():
    x = SomeService('JOB B')
    print('###### JOB B ######')
    logger.debug(f'%%%%%%%   {x.name}   %%%%%%%')