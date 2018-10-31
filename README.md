# weewx-reports

This extension is no longer needed. As of weewx 3.6, there is a "report_timing"
option in the "[StdReport]" section of weewx.conf.

This is a weewx extension to upload reports less frequently than the archive
interval. For various reasons, I do not care about seeing the weather
data every archive interval but I do want it in the weewx databases.

This is a shamelss packaging of a suggestion from tkeffer in the
weewx-user Google group. You can view the original thread at
```
https://groups.google.com/forum/#!searchin/weewx-user/ftp/weewx-user/paclaK5NCsg/AnLxcjZq8AgJ
```

## Setup

Clone this repo to your weewx extensions directory; for example

```
git clone git@github.com:wmadill/weewx-reports /home/weewx/extensions/weewx-reports
```

## Installation instuctions

1. run the installer

  ```
  cd /home/weewx
  setup.py install --extension extensions/weewx-reports
  ```

  This adds an additional report service at the botoom of
  `weewx.conf`. Look for the line beginning `report_services`
  in the `[[Services]]` stanze. It will look something like
  ```
  report_services = weewx.engine.StdPrint, weewx.engine.StdReport, user.reports.Reports
  ```

  Remove the `weewx.engine.StdReport` so that line now looks
  like
  ```
  report_services = weewx.engine.StdPrint, user.reports.Reports
  ```

  You may want to make a copy of the original line (commented out!) 
  because if you later remove this extension, you'll wonder why
  you are no longer getting reports! You will need to manually add
  the `weewx.engine.StdReport` service back in.

2. The default report interval is "1800" (30 minutes). You can change
it to any value that is at least as large as the `archive_interval` in
the `StdArchive` stanza.  The `report_interval` is also set in the
same stanza.

3. restart weewx:

  ```
  sudo /etc/init.d/weewx stop
  sudo /etc/init.d/weewx start
  ```

## Manual installation instructions:

1. copy the file to the weewx user directory:

  ```
  cp -rp bin/user/S3upload /home/weewx/bin/user
  ```

2. add the following to weewx.con

  ```
  [StdArchive]
      ...
      [[Reports]]
          report_interval = 1800 # Change as needed
  ```

3. start weewx

  ```
  sudo /etc/init.d/weewx start
  ```
