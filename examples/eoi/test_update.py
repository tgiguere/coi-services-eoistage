__author__ = 'cmueller'

from examples.eoi.test_base import *
from ion.eoi.agent.handler.dap_external_data_handler import DapExternalDataHandler
from datetime import datetime, timedelta

if __name__ == '__main__':

    ret = get_dataset(GHPM)

    dsh = DapExternalDataHandler(ret[EXTERNAL_DATA_PROVIDER], ret[EXTERNAL_DATA_SOURCE], ret[EXTERNAL_DATA_SET])

    td=timedelta(days=-1)
    edt=datetime.utcnow()
    sdt=edt+td

    
    req={}
    req["start_time"] = sdt
    req["end_time"] = edt

    resp = dsh.acquire_new_data(req)
#    print resp