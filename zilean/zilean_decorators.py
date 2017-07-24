#
from .zilean_jobs import incr_subjob, incr_job, get_job
from .zilean_pen import _add_element
from .zilean_rtype import ZileanOP
import time

def intern_fail_reporter():
    # Intern fail repoter
    pass

def _report_fail():
    pass

def op_fails_reporter(mode="", job=None):
    def wrap_func(func):
        def wrap_args(*args, **kwargs):
            if job == "subjob":
                incr_subjob()
            else:
                incr_job()
            job = get_job()
            res = func(*args, **kwargs)
            t = time.ctime()
            if isinstance(res, ZileanOP):
                if res.status != -9999:
                    _report_fail(func, job, t, res.status, res.out_put, args=args, kwargs=kwargs)
            return res
        return wrap_args
    return wrap_func


def zilean():
    pass

def unzilean():
    pass

def unzilean_ifempty():
    pass
