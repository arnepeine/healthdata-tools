# Split Dataset by header and data, check if column label is present, then put out a list of values.
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    def column(self, label):
        for idx, value in enumerate(self.header):
            if label in value:
                list_of_data = []
                for row in self.data:
                    list_of_data.append(row[idx])
                return list_of_data
            else:
                return None
