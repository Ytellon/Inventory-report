from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        data = cls.open_data(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)

    def open_data(path):
        with open(path, "r") as file:
            if path.endswith(".csv"):
                return list(csv.DictReader(file))
            elif path.endswith(".json"):
                return json.load(file)
            elif path.endswith(".xml"):
                return xmltodict.parse(file.read())["dataset"]["record"]
