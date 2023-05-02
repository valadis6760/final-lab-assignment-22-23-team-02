from app_manager import *

if __name__ == '__main__':

    ## check arguments and init app
    app     = app_manager()
    if not app.check_init():
        sys.exit()
    
    app.start()