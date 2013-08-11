#!/usr/bin/env python
# encoding: utf-8

import traceback
from jenkinsapi import api
from jenkinsapi import exceptions

class Jenkins(object):
        def __init__(self, jenkinsurl):
                self.jenkinsurl =jenkinsurl
        def check(self, jobnames):
                try:
                    jenkins = api.Jenkins(self.jenkinsurl)
                    for jobname in jobnames:
                            awesome_job = jenkins.get_job(jobname)
                            awesome_build = awesome_job.get_last_build()
                            if not awesome_build.is_good():
                                if awesome_build.get_status():
                                    print jobname + ' is ' + awesome_build.get_status()
                                return jobname
                    return ''
                except (exceptions.UnknownJob, exceptions.NoBuildData) as e:
                    traceback.print_exc()
                    return ''


