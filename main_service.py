import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import traceback

# Import your custom modules if needed
# from automatic_start import add_startup_registry_entry, remove_from_startup
# from thread_for_folder import monitor



import sys
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'monitoring_symlink'
    _svc_display_name_ = 'Monitoring Symlink Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_running = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def main(self):
        try:
            # Uncomment and modify the following lines to include your desired logic
            test=1

            while self.is_running and win32event.WaitForSingleObject(self.hWaitStop, 0) != win32event.WAIT_OBJECT_0:
                folder = r"C:\Users\O-c-O\OneDrive\up"  # Path to the folder to monitor for file changes
                # monitor(folder)  # Start monitoring file changes in the specified folder
                # Run your background tasks or keep the service active
                pass
        except Exception as e:
            print(traceback.print_exc())  # Output exception information to the console


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(MyService)
            servicemanager.StartServiceCtrlDispatcher()
        else:
            win32serviceutil.HandleCommandLine(MyService)
    except UnicodeEncodeError as e:
        print("Error starting service:", repr(e).encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding))
