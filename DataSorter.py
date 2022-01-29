from __future__ import unicode_literals
from xlwt import Workbook
import pandas as pd
import io, xlrd, os, glob, pathlib, json, time

current_path = os.path.dirname(os.path.realpath(__file__))

class XLSHandler:
    def __init__(self, current_tag_id):
        self.current_tag_id = current_tag_id
        self.find_xls()
        self.xls_clean()
        self.get_pfd()

    def find_xls(self):
        time.sleep(3)
        target_pattern = f"{current_path}\*.xls"
        self.xls_urls = glob.glob(target_pattern)

    def xls_clean(self):
        pfd_json = {
            "intensities": {
                "63": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                    "white": 0,
                    "farred": 0,
                },
                "126": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                    "white": 0,
                    "farred": 0,
                },  

                "189": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                    "white": 0,
                    "farred": 0,
                },  

                "252": {
                    "red": 0,
                    "green": 0,
                    "blue": 0,
                    "white": 0,
                    "farred": 0,
                },       
            },
        }

        for i, url in enumerate(self.xls_urls):
            file1 = io.open(url, "r", encoding="utf-8")
            data = file1.readlines()

            self.xldoc = Workbook()
            sheet = self.xldoc.add_sheet("Sheet1", cell_overwrite_ok=True)

            for y, row in enumerate(data):
                for j, col in enumerate(row.replace("\n", "").split("\t")):
                    sheet.write(y, j, col)

            intensities = ["63", "126", "189", "252"]
            colours = ["white", "red", "green", "blue", "farred"]

            duplicate_counter = 0

            for k, intensity in enumerate(range(4)):
                current_intensity = intensities[k]

                for j, colour in enumerate(range(5)):
                    current_colour = colours[j]

                    if duplicate_counter == i:
                        xls_save_path = f"{current_path}/captures/id/{self.current_tag_id}/intensity/{current_intensity}/"

                        pathlib.Path(xls_save_path).mkdir(parents=True, exist_ok=True)
                        self.xldoc.save(xls_save_path + current_colour + ".xls") 
                        self.url_link = xls_save_path + current_colour + ".xls"
                        
                        self.get_pfd()       
                        pfd_json["intensities"][str(current_intensity)][current_colour] = self.pfd

                        break

                    duplicate_counter += 1

        with open(f"{current_path}/captures/id/{self.current_tag_id}/pfds.json", "w", encoding="utf-8") as f:
            json.dump(pfd_json, f, ensure_ascii=False, indent=4)

        file1.close()

        for item in os.listdir(current_path):
            if item.endswith(".xls"):
                os.remove(os.path.join(current_path, item))

    def get_pfd(self):
        workbook = xlrd.open_workbook(self.url_link)
        worksheet = workbook.sheet_by_name("Sheet1")

        self.pfd = worksheet.cell(63, 1).value    
