import logging
from services.some_service import SomeService

logger = logging.getLogger('cron_jobs_test')

def invoke():
    x = SomeService('JOB A')
    print('###### JOB A ######')
    logger.debug(f'%%%%%%%   {x.name}   %%%%%%%')