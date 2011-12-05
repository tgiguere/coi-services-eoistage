__author__ = 'cmueller'

from pyon.public import IonObject, RT
from pyon.container.shell_api import container
from pyon.service.service import BaseClients
from pyon.util.context import LocalContextMixin
from pyon.public import IonObject
from pyon.public import log
from interface.services.coi.iresource_registry_service import ResourceRegistryServiceProcessClient
from interface.services.coi.idatastore_service import DatastoreServiceProcessClient
import pprint
from ion.eoi.agent.handler.dap_external_data_handler import DapExternalDataHandler

EXTERNAL_DATA_PROVIDER = "ext_data_prov"
EXTERNAL_DATA_SOURCE = "ext_data_src"
EXTERNAL_DATA_SET = "ext_data_set"

HFR = "hfr"
KOKAGG = "kokagg"
AST2 = "ast2"
SSTA = "ssta"
GHPM = "ghpm"
COMP1 = "comp1"
COMP2 = "comp2"

class EoiObjectSetupClients(BaseClients):
    def __init__(self, process=None):
        BaseClients.__init__(self)
        self.resource_registry = ResourceRegistryServiceProcessClient(process=process, node=container.node)
        self.datastore = DatastoreServiceProcessClient(process=process, node=container.node)

class EoiObjectSetup(LocalContextMixin):
    name = "eoi_obj_setup"
    def __init__(self, *args, **kwargs):
        LocalContextMixin.__init__(self)
        self.clients = EoiObjectSetupClients(process=self)

def get_dataset(x):
    if x == HFR:
        dprov = {}
        dprov["institution_name"]="HFRNET UCSD"
        dprov["institution_id"]="342"
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = "http://hfrnet.ucsd.edu:8080/thredds/dodsC/"
        dset = {}
        dset["dataset_path"] = "HFRNet/USEGC/6km/hourly/RTV"
        dset["temporal_id"] = "time"
#        dsdesc = {}
#        dsdesc["dataset_path"] = "HFRNet/USEGC/6km/hourly/RTV"
#        dsdesc["temporal_dimension"] = "time"
#        dsd_obj = IonObject("DapDatasetDescription", dsdesc)
#
#        dset["dataset_description"] = dsd_obj
    elif x == KOKAGG:
        dprov = {}
        dprov["institution_name"]="University of Hawaii"
        dprov["institution_id"]="128"
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = "http://oos.soest.hawaii.edu/thredds/dodsC/"
        dset = {}
        dset["dataset_path"] = "hioos/hfr/kokagg"
        dset["temporal_id"] = "time"
        dset["contact_name"]="Pierre Flament"
        dset["contact_email"]="pflament@hawaii.edu"
    elif x == AST2:
        dprov = {}
        dprov["institution_name"]="OOI CGSN"
        dprov["institution_id"]="5"
        dprov["contact_name"]="Robert Weller"
        dprov["contact_email"]="rweller@whoi.edu"
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = "http://ooi.whoi.edu/thredds/dodsC/"
        dsrc["contact_name"] = "Rich Signell"
        dsrc["contact_email"] = "rsignell@usgs.gov"
        dset = {}
        dset["dataset_path"] = "ooi/AS02CPSM_R_M.nc"
        dset["temporal_id"] = "time"
        dsrc["contact_name"] = "Nan Galbraith"
        dsrc["contact_email"] = "ngalbraith@whoi.edu"
    elif x == SSTA:
        dprov = {}
        dprov["institution_name"]="Remote Sensing Systems"
        dprov["institution_id"]="848"
        dprov["contact_email"]="support@gmss.com"
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = "http://thredds1.pfeg.noaa.gov/thredds/dodsC/"
        dset = {}
        dset["dataset_path"] = "satellite/GR/ssta/1day"
        dset["temporal_id"] = "time"
    elif x == GHPM:
        dprov = {}
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = ""
        dset = {}
        dset["dataset_path"] = "/Users/cmueller/Development/OOI/ast2_sample_data/ast2_ghpm_split/ast2_ghpm_spp_ctd.nc_1"
        dset["temporal_id"] = "time"
    elif x == COMP1:
        dprov = {}
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = ""
        dset = {}
        dset["dataset_path"] = "/Users/cmueller/Development/OOI/ast2_sample_data/ast2_ghpm_split/ast2_ghpm_spp_ctd.nc_1"
        dset["temporal_id"] = "time"
    elif x == COMP2:
        dprov = {}
        dsrc = {}
        dsrc["protocol_type"] = "DAP"
        dsrc["base_data_url"] = ""
        dset = {}
        dset["dataset_path"] = "/Users/cmueller/Development/OOI/ast2_sample_data/ast2_ghpm_split/ast2_ghpm_spp_ctd.nc_2"
        dset["temporal_id"] = "time"
    else:
        raise Exception("invalid dataset specified: %s" % x)

    ret = {}
    ret[EXTERNAL_DATA_PROVIDER] = dprov
    ret[EXTERNAL_DATA_SOURCE] = dsrc
    ret[EXTERNAL_DATA_SET] = dset
    return ret

def _setup():
    eos = EoiObjectSetup()
    ret = {}

    dprov_obj = IonObject(RT.ExternalDataProvider, name="UCSD HFR Network")
    dprov_obj.institution_name = "HFRNET UCSD"
    dprov_obj.institution_id = "342"
    dprov_id, _ = eos.clients.resource_registry.create(dprov_obj)

    dsrc_obj = IonObject(RT.ExternalDataSource, name="HFR TDS")
    dsrc_obj.protocol_type = "DAP"
    dsrc_obj.base_data_url = "http://hfrnet.ucsd.edu:8080/thredds/dodsC/"
    dsrc_id, _ = eos.clients.resource_registry.create(dsrc_obj)

#    dsdesc = {}
#    dsdesc["dataset_path"] = "HFRNet/USEGC/6km/hourly/RTV"
#    dsdesc["temporal_dimension"] = "time"
#    dsd_obj = IonObject("DapDatasetDescription", dsdesc)
#    pprint.pprint(dsd_obj)
#    dsd_id = eos.clients.datastore.create(dsd_obj, object_id="my_object")
#    pprint.pprint(dsd_id)
#    dsd_id = eos.clients.resource_registry.create(dsdesc)

#    dset["dataset_description"] = dsd_id
    dset_obj = IonObject(RT.ExternalDataset, name="6km RTV")
    dset_obj.dataset_path = "HFRNet/USEGC/6km/hourly/RTV"
    dset_obj.temporal_id = "time"
    dset_id, _ = eos.clients.resource_registry.create(dset_obj)

    dsr_obj = IonObject(RT.ExternalDataResource, name="UCSD 6km HFR")
    dsr_obj.data_provider_id = dprov_id
    dsr_obj.data_source_id = dsrc_id
    dsr_obj.dataset_id = dset_id
    dsr_id, _ = eos.clients.resource_registry.create(dsr_obj)

    ret[HFR] = dsr_id, {"provider": dprov_id, "data_source": dsrc_id, "dataset": dset_id}

    return ret


if __name__ == '__main__':
    dataset_map = _setup()
    pprint.pprint(dataset_map)

    eos = EoiObjectSetup()
    ret = eos.clients.resource_registry.read(object_id=dataset_map[HFR][0])
    pprint.pprint(ret)

#    ret = get_dataset(AST2)
#    dsh = DapExternalObservatoryHandler(ret[EXTERNAL_DATA_PROVIDER], ret[EXTERNAL_DATA_SOURCE], ret[EXTERNAL_DATA_SET])
#    import pprint
#    pprint.pprint(dsh)

#    h = EoiObjectSetup()
#
#    ret = h.clients.resource_registry.find_resources(restype="BankCustomer", id_only=True)
#    import pprint
#    pprint.pprint(ret)
#
#    customer_obj = IonObject("BankCustomer", name="test")
#    customer_id, _ = h.clients.resource_registry.create(customer_obj)
#    print customer_id