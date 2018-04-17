# Video Capture File Watcher

This is a pretty hacked together script built to solve a specific problem. I use
OBS to capture video from an HDMI camera using a Blackmagic Intensity Pro 4k
card for later editing in Blackmagic Davinci Resolve under Linux. I want to
capture to a compressed, lossless intermediate file to preserve quality while
also avoiding I/O related performance issues or running out of storage.  To do
this I'd ideally capture directly to Prores (which Davinci Resolve can import)
but there appears to be a bug with OBS/ffmpeg where capturing to Prores results
in serious screen tearing.  Therefore I need to capture to another codec (such
as utvideo) however this cannot be imported into resolve.

This simple script monitors a directory for files that are being written to by
OBS, when a file is found, it will start to convert it into prores in real time,
once the capture is completed, it will delete the utvideo file leaving just the
converted prores output.  The script performs the conversion in real time while
the capture is running which eliminates waiting after each capture to convert
the files.

## Usage
0. Create 2 directories, one to hold captured files, one to hold the converted
output
0. Configure OBS (or whatever capture software) to capture files to the capture
directory.
0. Run the "capture_watcher.py" script by supplying the two directories.

The script will now start printing "Waiting for file..." - Start capturing the
video at which point it will start converting the file.  When capture is stopped
the captured file will be deleted leaving the converted file in the specified
directory. The script will then go back to "Waiting for file..." at which point
a new capture can be started.

## Limitations/Things to fix
* Filenames in capture directory must not contain spaces
