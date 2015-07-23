from apscheduler.schedulers.blocking import BlockingScheduler
from scraper.googleplay.tasks import googleplay_freeapps_crawler_job
from settings import logger

__author__ = 'can'

import argparse
import sys
import traceback

from apscheduler.events import EVENT_JOB_EXECUTED
from apscheduler.events import EVENT_JOB_ERROR
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.jobstores.mongodb import MongoDBJobStore

from pytz import utc


def default_job_listener(event):
    if event.exception:
        logger.error("Job %s failed at %s" % (event.job_id, event.scheduled_run_time))
        logger.error(event.exception)
        logger.error(event.traceback)
    else:
        logger.info("Job %s completed successfully at %s" % (event.job_id, event.scheduled_run_time))


def clear_jobs():
    scheduler.remove_all_jobs()

def init_jobs():
    clear_jobs()
    scheduler.add_job(googleplay_freeapps_crawler_job, 'cron', hour='*', id='hourly_googleplay_freeapps_crawler_job')



jobstores = {
    'mongo': MongoDBJobStore(),
    'default': MongoDBJobStore()
}
executors = {
    'default': ThreadPoolExecutor(20),
    'processpool': ProcessPoolExecutor(5)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 3,
    'trigger': 'cron'
}

scheduler = BlockingScheduler(jobstores=jobstores, executors=executors, job_defaults=job_defaults, timezone=utc)
scheduler.add_listener(default_job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Manage scheduled jobs..')

    parser.add_argument('--init', '-i', action="store_true")
    parser.add_argument('--clear', '-c', action='store_true')


    args = parser.parse_args()

    if args.init:
        init_jobs()
    if args.clear:
        clear_jobs()


    try:
        scheduler.start()
    except Exception as e:
        logger.error("Exiting")
        logger.error(e)
        logger.error(traceback.format_exc())
        logger.error(sys.exc_info())






