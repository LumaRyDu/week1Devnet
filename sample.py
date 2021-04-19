import logging


def foo():
    logging.info("Within Foo!")

def bar():
    logging.info("Within Bar!")


if __name__ == "__main__":
    logging.basicConfig(
    	level=logging.INFO, 
    	format='%(asctime)s - %(levelname)s - %(message)s',
    	handlers = [
    		logging.FileHandler("sample.log"),
    		logging.StreamHandler()
    		]
    	)
    logging.info("Starting up")
    foo()
    bar()
    logging.warning("EXITING!")

    print("marialde")