# Initial version of less frequent reports--no need to upload every 5 minutes

import time
from weewx.engine import StdReport

class Reports(StdReport):

    # Override launch_report_thread:
    def launch_report_thread(self, event):
	# TODO force hourly alignment
        # Launch only every "report_interval" seconds
	report_interval = self.config_dict['StdArchive']['Reporst'].as_int('report_interval')
        if not self.launch_time or (time.time() - self.launch_time >= report_interval):
            StdReport.launch_report_thread(self,event)
