import win32serviceutil
import win32service
import win32event
import servicemanager
import time
import datetime
import sys

import 

sys.exit()


def log_write(self, sstr: str):
        with open("c:\\ultralog\\jacky_python_service.log", "+a") as f:
            dt = datetime.datetime.now().strftime("%H:%M:%S")
            f.write(f"{dt} {sstr}\n")

class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'jacky_python_service'
    _svc_display_name_ = 'jacky Python Service'
    _svc_description_ = 'A sample Python service that runs a Python script.'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.stop_requested = False

    def SvcStop(self):
        self.stop_requested = True
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.main()
    
    
    def main(self):
        # Your main loop, which will run as a service
        while not self.stop_requested:
            # Here, insert your script logic
            log_write("Service is running...")
            time.sleep(5)  # Sleep for 1 minute

    
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)
