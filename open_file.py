import csv
class Reader:
    class_list = None
    headers = None
    #constructor
    def open_file (self, file_name):
        ''' receive file_name as args
            read file data
            initialize state variables'''
        my_list = []
        with open(file_name, 'r') as csvfile:
            rows = csv.reader(csvfile)
            self.headers = next(rows) #skips header row
            for list in rows: #iterate through data
                my_list.append(list)#add data to list
        self.class_list = my_list

    def remove_special_characters(self):
        ''' remove specified special charcters
            returns a new nested list'''
        my_list = []
        for list in self.class_list:
            local = []
            for i in list:
                item = i.replace('$', "").replace(',', '')
                local.append(item)
            my_list.append(local)
        return my_list
    def return_headers(self):
        '''returns a list of headers'''
        return self.headers
