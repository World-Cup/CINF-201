from open_file import Reader

class StateData:
    '''
    instatiate reader class
    create: nested list of states tuition
    create: dict of states data
    '''
    state_list = None
    headers = None
    def __init__(self):
        # constructor
        reader = Reader()
        reader.open_file("us_avg_tuition.csv")
        self.state_list = reader.remove_special_characters()
        self.headers = reader.return_headers()

    def title (self):
        return(self.headers)

    def all_us_states_data (self):
        my_list = []
        for i in self.state_list:
            my_list.append(i[1:])
        return my_list

    def create_state_dict(self):
        states = dict()
        for data in self.state_list:
            key = ''.join(data[0])
            if key not in states:
                states[key] = data[1:]
        return (states)

class calculate():
    state_dict = None
    state_data = None
    tuition_inc = None
    us_states_data = None
    def __init__ (self, state):
        # paramitorized constructor
        #param: state name - state
        call = StateData()
        self.state_dict = call.create_state_dict()
        self.us_states_data = call.all_us_states_data()
        self.state_data = self.state_dict[state]
        self.tuition_inc = self.tuition_raise()

    def state_tuition (self):
        return(self.state_data)
        #return: avg of sum of data

    def tuition_raise (self):
        raised = []
        data = self.state_data
        for i in range(len(data)-1):
            the_sum = float(data[i+1]) - float(data[i])
            raised.append(the_sum)
        return raised

    def average_tuition (self, data):
        elements = 0
        average = 0
        for i in data:
            average += float(i)
            elements += 1
        return(average/elements)

    def prediction_recent (self):
        return (float(self.state_data[-1])
                +float(self.tuition_inc[-1]))

    def prediction_overall (self):
        t_sum = 0
        avg = 0
        for i in self.tuition_inc:
            t_sum += float(i)
            avg += 1
        average = t_sum/avg
        # last index of tuition + plus average
        data = float(self.state_data[-1]) + average
        return (data)

    def statesData (self):
        data = self.us_states_data
        row = len(data)-1
        new_list = []
        # if (row > 0):
        index = len(data[0])-1
        if (row > 0):
            new_list.append(data[row][index])
            index -=1
        # for i in self.state_dict.values():
        #     data.append(i)
        #     index = len(i)
        #     # for num in range (len(i)):
        #     #     index += 1
        return (new_list)
    def statesKeys (self):
        return(self.statesData())



def format_string (data):
    return (", ".join(str(i) for i in data))

def get_data (state):
    call = calculate(state)
    data = call.state_tuition()
    rise = call.tuition_raise()
    print ("State Tuition Data: %s"
            %format_string(data))
    print ("State Tuition Rise: %s"
            %format_string(rise))
    print ("State Average Tuition: %d"
            %call.average_tuition(data))
    print ("State Average Rise: %d"
            %call.average_tuition(rise))
    print ("Prediction (recent): %d"
            %call.prediction_recent())
    print("Prediction (overall):%d"
            %call.prediction_overall())
    print (call.statesKeys())
    # print (['5683', '4328', '5138', '5772', '5286', '4704', '7984', '8353', '3848', '4298'])

def get_user_input():
    option = input ("Please select which type of data you want. \n"+
    'Whole U.S. ("US"), selected State ("State"), or Exit ("Exit"): ')
    if option == "Exit":
        print ("Goodby!")
    elif (option == "State"):
        select = input("Please enter your selection: ")
        print("Your selection is %s" % select)
        get_data(select)
        data = input ("Would you like to enter a new selection")
        if data.lower() == "yes":
            get_user_input()
        else:
            print ("Goodby!")
    elif (option == "US"):
        print("we are working on it")
        data = input ("Would you like to enter a new selection")
        if data.lower() == "yes":
            get_user_input()
        else:
            print ("Goodby!")
    else:
        get_user_input()

def raise_exception ():
    try:
        get_user_input()
    except:
        print ("You entered an invalid input. Please try again. ")
        get_user_input()
        
raise_exception ()

