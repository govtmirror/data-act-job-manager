from dataactcore.models.jobTrackerInterface import JobTrackerInterface

class JobManager(JobTrackerInterface):
    def startReady(self):
        """ Look for jobs with a ready status and assign them to any available instances

        """

    def checkPrereq(self):
        """ Check dependencies to see if any waiting jobs should be moved to ready

        :return:
        """

    def checkFailed(self):
        """ Check for failed jobs, possibly restart them?

        :return:
        """

    def chooseInstance(self):
        """ Get an available instance off the resources table, what to do if none are available?  Interact with Ec2Manager in some way?

        :return:
        """