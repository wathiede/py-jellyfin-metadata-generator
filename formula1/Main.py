# Copyright (C) 2025 eHonnef <contact@honnef.net>
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
import argparse
from Generator import Generator, generator_logger
import Fetchnator
import logging

LOG_LEVEL = logging.INFO
logging.basicConfig(level=LOG_LEVEL, format='%(levelname)-8s :: %(message)s')


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("basefolder",
                        help="The base folder where the Formula 1 seasons are saved.")
    parser.add_argument("-m", "--mapped-folder",
                        help="In case you are using a docker container. "
                             "Pass the docker internal path to the Formula 1 season folder. "
                             "Default will be the base folder.")
    parser.add_argument("-c", "--convert-to-jpg",
                        action="store_true",
                        help="Converts the webp images to jpg format. Needs Pillow to work")
    parser.add_argument("-l", "--log-level",
                        default="INFO",
                        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                        help="Set the log level")

    args = parser.parse_args()

    # Set logging
    LOG_LEVEL = getattr(logging, args.log_level)
    Fetchnator.fetchnator_logger.setLevel(LOG_LEVEL)
    generator_logger.setLevel(LOG_LEVEL)

    if args.mapped_folder is None:
        args.mapped_folder = args.basefolder

    conversion = Fetchnator.ImageConvertor.DONT
    if args.convert_to_jpg:
        conversion = Fetchnator.ImageConvertor.JPG

    return Generator(args.basefolder, args.mapped_folder, conversion)


if __name__ == '__main__':
    # Set to false if you want to debug stuff
    DEPLOY = True

    if DEPLOY:
        gen = parse_arguments()
    else:
        from Testing import GenerateTests

        GenerateTests.create_tests()

        LOG_LEVEL = logging.DEBUG
        Fetchnator.fetchnator_logger.setLevel(LOG_LEVEL)
        generator_logger.setLevel(LOG_LEVEL)
        gen = Generator("./Formula 1", "Test", Fetchnator.ImageConvertor.JPG)
    gen.run()
