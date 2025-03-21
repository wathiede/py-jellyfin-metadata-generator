# Copyright (C) 2025 eHonnef <contact@honnef.net>
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import os
import pathlib
import random
import string
from string import Template

base_dir = "./Formula 1"

def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_files(season_folder, season, n_round, string_list):
    video_ext_list = [".avi", ".mp4", ".mkv"]
    for item in string_list:
        filename = item.substitute(season=season, episode=n_round, rand_string=random_string(20), extension=random.choice(video_ext_list))
        pathlib.Path(f"{season_folder}/{filename}").touch()

def create_season_folder(season):
    season_folder = f"{base_dir}/{str(season)}"
    os.makedirs(season_folder, exist_ok=True)
    return season_folder

def create_tests():
    if os.path.exists(base_dir):
        print("Cleaning up .nfo and .jpg")
        directory_path = pathlib.Path(base_dir)
        extensions = [".nfo", ".jpg"]
        for ext in extensions:
            for file in directory_path.rglob(f"*{ext}"):
                try:
                    file.unlink()
                    print(f"Deleted: {file}")
                except Exception as e:
                    pass
    else:
        print("Creating test files")
        race_template = Template("Formula 1 - s${season}e${episode} - Race ${rand_string}${extension}")
        race_template_2 = Template("Formula 1 - s${season}e${episode} - ${rand_string}${extension}")
        fp_template = Template("Formula 1 - s${season}e${episode} - Free practice ${rand_string}${extension}")
        fp1_template = Template("Formula 1 - s${season}e${episode} - FP1 ${rand_string}${extension}")
        fp2_template = Template("Formula 1 - s${season}e${episode} - FP2 ${rand_string}${extension}")
        fp3_template = Template("Formula 1 - s${season}e${episode} - FP3 ${rand_string}${extension}")
        quali_template = Template("Formula 1 - s${season}e${episode} - QUALI ${rand_string}${extension}")
        sprint_quali_template = Template("Formula 1 - s${season}e${episode} - SprintQuali ${rand_string}${extension}")
        sprint_template = Template("Formula 1 - s${season}e${episode} - Sprint ${rand_string}${extension}")

        # Sprint without sprint qualification
        season_folder = create_season_folder(2021)
        create_files(season_folder, 2021, 1, [race_template_2, fp_template])
        create_files(season_folder, 2021, 9, [race_template, fp2_template, quali_template])
        create_files(season_folder, 2021, 10, [race_template_2, sprint_template])
        create_files(season_folder, 2021, 14, [fp1_template, fp2_template, fp3_template, quali_template, sprint_template, race_template])

        # Sprint with sprint qualification
        season_folder = create_season_folder(2024)
        create_files(season_folder, 2024, 1, [race_template, fp2_template, quali_template])
        create_files(season_folder, 2024, 5, [race_template_2, sprint_quali_template, sprint_template])
        create_files(season_folder, 2024, 21, [fp1_template, quali_template, sprint_quali_template, sprint_template, race_template])
        create_files(season_folder, 2024, 23, [sprint_template, race_template])


if __name__ == '__main__':
    create_tests()
