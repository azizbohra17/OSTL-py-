class Sony: 
    def __init__(self): 
        self.models = ['bravia', '6T', '7', '7T'] 
   

    def outModels(self): 
        print('These are the available models for Sony') 
        for model in self.models: 
            print('\t%s ' % model) 

class Samsung: 
    def __init__(self): 
        self.models = ['oled', 'J5', 'M4', 'A8'] 
   

    def outModels(self): 
        print('These are the available models for Samsung') 
        for model in self.models: 
            print('\t%s ' % model) 