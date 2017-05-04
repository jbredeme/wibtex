class SimpleLogger:

    def __init__(self):
        '''
        Constructs a logger for documenting code processes

        '''

        self.filepath = '../config/log.properties'
        self.logpath = '../logs/log_default.log'
        self.version = 1

        try:
            file = open(self.filepath, 'r')
            self.data = file.read()
            file.close()

            # If the file does not contain content
            if self.data is None or self.data is "":

                # Default to version one
                file = open(self.filepath, 'w')
                file.write('NEXT ' + str(self.version))
                file.close()

            # If the file contains content
            else:

                # Search for the version number
                for char in range(0, len(self.data)):
                    
                    # If we find the version
                    if self.data[char].isdigit():
                        self.version = int(self.data[char])

                # Rewrite the file and add the new version number
                file = open(self.filepath, 'w')
                file.write('NEXT ' + str(self.version + 1))
                file.close()
            
            # Construct the logpath now
            self.logpath = '../logs/log_' + str(self.version) + '.log'

        except(IOError):
            print("ERROR - Could not read log properties file.")

    def log_data( self, data_string ):
        '''
        Logs data to the predefined logging folder

        @param data_string the data to log
        '''

        file = open(self.logpath, 'a')

        file.write(str(data_string))

        file.close()