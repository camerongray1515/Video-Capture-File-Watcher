#!/usr/bin/env python3
import os
import time
import subprocess
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("capture_dir", help="Directory that captured files are "
                    "written to")
parser.add_argument("output_dir", help="Directory to write convered files to")

try:
    args = parser.parse_args()
except:
    sys.exit(0)


capture_dir = args.capture_dir
output_dir = args.output_dir

def wait_for_file():
    while True:
        files = os.listdir(capture_dir)
        if files:
            print("File found! Converting...")
            return files[0]
        else:
            print("Waiting for file...")
            time.sleep(1)

def process_file(filename):
    print("Processing file: " + filename)
    infile = os.path.join(capture_dir, filename)
    outfile = os.path.join(output_dir, filename.replace(".avi", ".mov"))

    # Parameters below may be changed to change output format.
    # "-re" must be supplied to ensure ffmpeg converts at the file's framerate.
    # Without this it will run the conversion as quickly as possible and will
    # reach the end of the file while the capture is still running, stopping the
    # conversion process.
    process = subprocess.Popen(["ffmpeg", "-re", "-i", infile, "-c:v", "prores",
                               "-profile:v", "3", "-c:a", "pcm_s24le", outfile])
    process.wait()
    print("Done, Deleting original captured file!")
    os.remove(infile)

def main():
    if (os.listdir(capture_dir)):
        print("Capture directory is not empty, quitting!")
        return

    while True:
        filename = wait_for_file()
        process_file(filename)


if __name__ == "__main__":
    main()
