class CsvReader():
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        #... Your code here ...
        self.filename =filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
    def __enter__(self):
        # ... Your code here ...
        # file = CsvReader(self.filename, self.sep, self.header, self.skip_top, self.skip_bottom)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # ... Your code here ...
        # print(exc_type)
        # print(exc_value)
        # print(exc_traceback)
        print("something bad has occurred")
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
        nested list (list(list, list, ...)) representing the data.
        """
        # ... Your code here ...
        self.f = open(self.filename, "r")
        if self.header:
            out = self.f.read()
        else :
            out = self.f.readline()
            out = self.f.read()
        return(out.split(self.sep))
    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
        list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        # ... Your code here ...
        self.f = open(self.filename, "r")
        if self.header:
            out = self.f.readline()
            return(out.split(self.sep))
        else :
            return None
        
if __name__ == "__main__":
    with CsvReader('good.csv', ) as file:
        data = file.getdata()
        new_data = data[0].split("\n")
        print(new_data)
        header = file.getheader()