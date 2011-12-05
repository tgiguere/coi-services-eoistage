#!/usr/bin/env python

__author__ = 'cmueller'

from pyon.public import log
from ion.eoi.agent.handler.dap_external_data_handler import DapExternalDataHandler
import sys
from examples.eoi.test_base import *

if __name__ == '__main__':

#    if len(sys.argv) == 1:
#        arg = "ast2"
#    else:
#        arg = sys.argv[1]
#
##    url, eo, request = get_dataset(arg)
#    url, eo = get_dataset(arg)
#
#    dataset_handler = DapExternalObservatoryHandler()
#
#    dataset_handler.initialize(eo, DATASET_URL=url, kw_arg="another kw arg")

#    print str(dataset_handler)

    ret1 = get_dataset(COMP1)
    dsh1=DapExternalDataHandler(ret1[EXTERNAL_DATA_PROVIDER], ret1[EXTERNAL_DATA_SOURCE], ret1[EXTERNAL_DATA_SET])

    ret1b = get_dataset(COMP1)
    dsh1b=DapExternalDataHandler(ret1b[EXTERNAL_DATA_PROVIDER], ret1b[EXTERNAL_DATA_SOURCE], ret1b[EXTERNAL_DATA_SET])

    ret2 = get_dataset(COMP2)
    dsh2=DapExternalDataHandler(ret2[EXTERNAL_DATA_PROVIDER], ret2[EXTERNAL_DATA_SOURCE], ret2[EXTERNAL_DATA_SET])

    print "\nCompare COMP1 & COMP1"
    dsh1.compare(dsh1b)
    print "\nCompare COMP1 & COMP2"
    dsh1.compare(dsh2)