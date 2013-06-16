# -*- coding: GBK -*-
"""
    @author     : yuanyi
    @date       : Wed 09 Jan 2013 10:17:37 PM CST
    @last update: Wed 09 Jan 2013 10:17:37 PM CST
    @summary    : Logger lib 
    @version    : 1.0.0.0
"""

import sys,os,getopt,logging

LOGFILE="./log/XXXXX.log"
LOGLEVEL="NOTICE"
FORMAT="[%(levelname)s] %(asctime)s : %(pathname)s %(module)s:%(funcName)s[%(lineno)d] %(message)s"
LEVEL = {}
LEVEL['NOTICE'] = logging.NOTSET
LEVEL['DEBUG'] = logging.DEBUG
LEVEL['INFO'] = logging.INFO
LEVEL['WARNING'] = logging.WARNING
LEVEL['ERROR'] = logging.ERROR
LEVEL['CRITICAL'] = logging.CRITICAL
    

def InitLog():
    logger = logging.getLogger()
    hdlr = logging.FileHandler(LOGFILE)
    formatter = logging.Formatter(FORMAT)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(LEVEL[str(LOGLEVEL)])
    return logger
"""
def InitStreamLog():
    logger = logging.getLogger()
    streamhdl = logging.StreamHandler()
    hdlr = logging.FileHandler(LOGFILE)
    formatter = logging.Formatter(FORMAT)
    logger.addHandler(hdlr)
    logger.addHandler(streamhdl)
    logger.setLevel(LEVEL[str(LOGLEVEL)])
    return logger
"""    

LOG=InitLog()
#ERR=InitStreamLog()

def usage():
    print "Usage: Logger.py [options] ..."

def main():
    try:
        opts,args = getopt.getopt(sys.argv[1:],"vh",["version","help"])
    except GetoptError:
        sys.exit(2)
    LOG.info("test")
if __name__ == "__main__":
    main()
    pass
