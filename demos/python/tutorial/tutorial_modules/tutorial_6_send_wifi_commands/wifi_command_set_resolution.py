# wifi_command_set_resolution.py/Open GoPro, Version 2.0 (C) Copyright 2021 GoPro, Inc. (http://gopro.com/OpenGoPro).
# This copyright was auto-generated on Wed, Sep  1, 2021  5:06:04 PM

import json
import logging
import argparse

import requests

from tutorial_modules import GOPRO_BASE_URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def main():
    # Note!! The endpoint below changed between Open GoPro version 1.0 and 2.0
    # This endpoint supports >= 2.0

    # Build the HTTP GET request
    url = GOPRO_BASE_URL + f"/gopro/camera/setting?setting=2&option=9"
    logger.info(f"Setting the video resolution to 1080: sending {url}")

    # Send the GET request and retrieve the response
    response = requests.get(url)
    # Check for errors (if an error is found, an exception will be raised)
    response.raise_for_status()
    logger.info("Command sent successfully")
    # Log response as json
    logger.info(f"Response: {json.dumps(response.json(), indent=4)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set the video resolution to 1080.")
    parser.parse_args()
    main()
