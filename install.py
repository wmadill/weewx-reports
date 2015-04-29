# installer for reports extensions

from setup import ExtensionInstaller

def loader():
    return ReportsInstaller()

class ReportsInstaller(ExtensionInstaller):
    def __init__(self):
        super(ReportsInstaller, self).__init__(
            version="0.1",
            name='reports',
            description='Run reports less frequently than archive interval',
            author='Bill Madill',
            author_email='bill@jamimi.com',
            report_services='user.reports.Reports',
            config={
                'StdArchive': {
                    'Reports': {
                        'report_intreval': 1800,}}},

            files=[('bin/user', ['bin/user/reports.py'])]
            )
