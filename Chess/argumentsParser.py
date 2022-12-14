from optparse import OptionParser
from agents.NegamaxAgent import NegamaxAgent
from agents.NegaScoutAgent import NegaScoutAgent
from agents.PVSAgent import PVSAgent


def parseArguments(argv):
    usageStr = """
        COMMAND: python main.py <options>
    """
    parser = OptionParser(usageStr)

    parser.add_option('-a', '--agent', dest='agent', default='NegamaxAgent')
    parser.add_option('-d', '--depth', dest='depth', type='int', default=3)

    options, otherjunk = parser.parse_args(argv)
    if len(otherjunk) != 0:
        raise Exception('Command line input not understood: ' + str(otherjunk))
    args = dict()

    if options.agent == 'NegamaxAgent':
        args['agent'] = NegamaxAgent
    elif options.agent == 'NegaScoutAgent':
        args['agent'] = NegaScoutAgent
    elif options.agent == 'PVSAgent':
        args['agent'] = PVSAgent
    else:
        raise Exception('Can\'t find agent: ' + options.agent)

    args['depth'] = options.depth

    return args
