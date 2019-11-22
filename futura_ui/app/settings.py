# -*- coding: utf-8 -*-
import json
import os
import shutil
from typing import Optional

import appdirs
import brightway2 as bw

from futura_ui.app.signals import signals
from .. import PACKAGE_DIRECTORY


class BaseSettings(object):
    """ Base Class for handling JSON settings files.
    """
    def __init__(self, directory: str, filename: str = None):
        self.data_dir = directory
        self.filename = filename or "default_settings.json"
        self.settings_file = os.path.join(self.data_dir, self.filename)
        self.settings: Optional[dict] = None
        self.initialize_settings()

    @classmethod
    def get_default_settings(cls) -> dict:
        """ Returns dictionary containing the default settings for the file
        """
        raise NotImplementedError

    def restore_default_settings(self) -> None:
        """ Undo all user settings and return to original state.
        """
        self.settings = self.get_default_settings()
        self.write_settings()

    def initialize_settings(self) -> None:
        """ Attempt to find and read the settings_file, creates a default
        if not found
        """
        if os.path.isfile(self.settings_file):
            self.load_settings()
        else:
            self.settings = self.get_default_settings()
            self.write_settings()

    def load_settings(self) -> None:
        with open(self.settings_file, "r") as infile:
            self.settings = json.load(infile)

    def write_settings(self) -> None:
        with open(self.settings_file, "w") as outfile:
            json.dump(self.settings, outfile, indent=4, sort_keys=True)


class FuturaSettings(BaseSettings):
    """
    Interface to the json settings file. Will create a userdata directory via appdirs if not
    already present.
    """
    def __init__(self, filename: str):
        futura_dir = appdirs.AppDirs("Futura", "Futura")
        if not os.path.isdir(futura_dir.user_data_dir):
            os.makedirs(futura_dir.user_data_dir, exist_ok=True)

        super().__init__(futura_dir.user_data_dir, filename)

    @classmethod
    def get_default_settings(cls) -> dict:
        """ Using methods from the commontasks file to set default settings
        EDIT THIS TO REFLECT FUTURA SETTINGS
        """
        return {
            "custom_bw_dir": cls.get_default_directory(),
            "startup_project": cls.get_default_project_name(),
        }

    # @property
    # def custom_bw_dir(self) -> str:
    #     """ Returns the custom brightway directory, or the default
    #     """
    #     return self.settings.get("custom_bw_dir", self.get_default_directory())
    #
    # @custom_bw_dir.setter
    # def custom_bw_dir(self, directory: str) -> None:
    #     """ Sets the custom brightway directory to `directory`
    #     """
    #     self.settings.update({"custom_bw_dir": directory})

    # @property
    # def startup_project(self) -> str:
    #     """ Get the startup project from the settings, or the default
    #     """
    #     project = self.settings.get(
    #         "startup_project", self.get_default_project_name()
    #     )
    #     if project not in bw.projects:
    #         project = self.get_default_project_name()
    #     return project

    # @startup_project.setter
    # def startup_project(self, project: str) -> None:
    #     """ Sets the startup project to `project`
    #     """
    #     self.settings.update({"startup_project": project})

    @staticmethod
    def get_default_directory() -> str:
        """ Returns the default brightway application directory
        """
        return None # bw.projects._get_base_directories()[0]

    @staticmethod
    def get_default_project_name() -> Optional[str]:
        """ Returns the default project name.
        """
        return None
        # if "default" in bw.projects:
        #     return "default"
        # elif len(bw.projects):
        #     return next(iter(bw.projects)).name
        # else:
        #     return None


# class ProjectSettings(BaseSettings):
#     """
#     Handles user settings which are specific to projects. Created initially to handle read-only/writable database status
#     Code based on ABSettings class, if more different types of settings are needed, could inherit from a base class
#
#     structure: singleton, loaded dependent on which project is selected.
#         Persisted on disc, Stored in the BW2 projects data folder for each project
#         a dictionary1 of dictionaries2
#         Dictionary1 keys are settings names (currently just 'read-only-databases'), values are dictionary2s
#         Dictionary2 keys are database names, values are bools
#
#     For now, decided to not include saving writable-activities to settings.
#     As activities are identified by tuples, and saving them to json requires extra code
#     https://stackoverflow.com/questions/15721363/preserve-python-tuples-with-json
#     This is currently not worth the effort but could be returned to later
#
#     """
#     def __init__(self, filename: str):
#         # on selection of a project (signal?), find the settings file for that project if it exists
#         # it can be a custom location, based on ABsettings. So check that, and if not, use default?
#         # once found, load the settings or just an empty dict.
#         self.connect_signals()
#         super().__init__(bw.projects.dir, filename)
#
#         # https://github.com/LCA-ActivityBrowser/activity-browser/issues/235
#         # Fix empty settings file and populate with currently active databases
#         if "read-only-databases" not in self.settings:
#             self.settings.update(self.process_brightway_databases())
#             self.write_settings()
#
#     def connect_signals(self):
#         """ Reload the project settings whenever a project switch occurs.
#         """
#         signals.project_selected.connect(self.reset_for_project_selection)
#         signals.delete_project.connect(self.reset_for_project_selection)
#
#     @classmethod
#     def get_default_settings(cls) -> dict:
#         """ Return default empty settings dictionary.
#         """
#         return cls.process_brightway_databases()
#
#     @staticmethod
#     def process_brightway_databases() -> dict:
#         """ Process brightway database list and return new settings dictionary.
#
#         NOTE: This ignores the existing database read-only settings.
#         """
#         return {
#             "read-only-databases": {name: True for name in bw.databases.list}
#         }
#
#     def reset_for_project_selection(self) -> None:
#         """ On switching project, attempt to read the settings for the new
#         project.
#         """
#         print("Reset project settings directory to:", bw.projects.dir)
#         self.settings_file = os.path.join(bw.projects.dir, self.filename)
#         self.initialize_settings()
#
#     def add_db(self, db_name: str, read_only: bool = True) -> None:
#         """ Store new databases and relevant settings here when created/imported
#         """
#         self.settings["read-only-databases"].setdefault(db_name, read_only)
#         self.write_settings()
#
#     def modify_db(self, db_name: str, read_only: bool) -> None:
#         """ Update write-rules for the given database
#         """
#         self.settings["read-only-databases"].update({db_name: read_only})
#         self.write_settings()
#
#     def remove_db(self, db_name: str) -> None:
#         """ When a database is deleted from a project, the settings are also deleted.
#         """
#         self.settings["read-only-databases"].pop(db_name, None)
#         self.write_settings()
#
#     def db_is_readonly(self, db_name: str) -> bool:
#         """ Check if given database is read-only, defaults to yes.
#         """
#         return self.settings["read-only-databases"].get(db_name, True)
#
#     def get_editable_databases(self):
#         """ Return list of database names where read-only is false
#
#         NOTE: discards the biosphere3 database based on name.
#         """
#         iterator = self.settings.get("read-only-databases", {}).items()
#         return (name for name, ro in iterator if not ro and name != "biosphere3")


futura_settings = FuturaSettings("FuturaSettings.json")
# project_settings = ProjectSettings("AB_project_settings.json")