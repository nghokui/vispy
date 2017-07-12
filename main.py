import os, sys, json, unittest
from package.code.exceptions import *
from package.code.logger import Logger 


def loadSettings():
    with open('package/settings.json', 'r') as jfile:
        loaded_data = json.load(jfile)

    curr_path = '/'.join(os.path.realpath(__file__).split('\\')[:-1])
    loaded_data['logpath'] = '{}/{}'.format(curr_path, loaded_data['logpath'])
    
    return loaded_data

def testModules():
    import package.test.LoggerTester as TestLogger
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromModule(TestLogger))

    runner = unittest.TextTestRunner(verbosity = 3)
    result = runner.run(suite)

if __name__ == '__main__':
    settings = loadSettings()
    syslog = Logger(settings)
    syslog.logAction("Main initiated.")
    
    try:
        for sysarg in sys.argv[1:]:
            if sysarg == '-t' or sysarg == '-test':
                syslog.logAction("Testing procedures initiated.")
                testModules()
                syslog.logAction("Test fixtures executed successfully.")
            elif sysarg == '-c' or sysarg == '-clear':
                with open(syslog.log_path, 'w') as lfile:
                    lfile.write("")
                syslog.logAction("Log file purged.")
            else:
                raise MPArgvException
    except Exception as e:
        syslog.logAction(e)
        syslog.logAction("Ended with failure.")
    finally:
        syslog.logAction('Main End.\n')
        syslog.writeOut()    
    