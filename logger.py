import logging
from kafkahandler import KafkaHandler


class Main:

    def __init__(self):
        logging.basicConfig(
            filename="myapp.log", 
            format='%(asctime)s %(levelname)s %(message)s', 
            level=logging.INFO, 
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )
        self.logger = logging.getLogger('simple_example')
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        fl = logging.FileHandler("myapp.log")
        self.logger.addHandler(fl)
        kh = KafkaHandler("192.168.1.240:9092", "pylog")
        kh.setLevel(logging.INFO)
        self.logger.addHandler(kh)

        

    def run(self):
        while True:
            log = input("> ")
            self.logger.info(log)

if __name__ == "__main__":
    main = Main()
    main.run()
