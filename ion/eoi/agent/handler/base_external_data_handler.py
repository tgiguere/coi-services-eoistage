#!/usr/bin/env python

__author__ = 'cmueller'

from pyon.service.service import BaseClients
from pyon.public import IonObject
from pyon.public import log
from zope.interface import implements
from ion.eoi.agent.interface.iexternal_data_handler_controller import IExternalDataHandlerController
from interface.services.coi.iresource_registry_service import ResourceRegistryServiceProcessClient

# Observatory Status Types
OBSERVATORY_ONLINE = 'ONLINE'
OBSERVATORY_OFFLINE = 'OFFLINE'

# Protocol Types
PROTOCOL_TYPE_DAP = "DAP"

class BaseExternalDataHandler():
    """ Base implementation of the External Observatory Handler"""
    implements(IExternalDataHandlerController)
    dependencies = ['resource_registry']

    ext_observatory_object = None
    ext_data_producer_object = None
    ext_data_set_object = None

    def __init__(self, *args, **kwargs):
        pass
    
    # IExternalObservatoryController functions
    def base_initialize(self, data_provider=None, data_source=None, ext_dset=None, **kwargs):
        if data_provider is None:
            edp = {}
            edp["institution_name"] = "ASA"
            edp["institution_id"] = "1"
            edp["institution_webpage"] = "www.asascience.com"
            edp["contact_name"] = "Christopher Mueller"
            edp["contact_phone"] = "401-789-6224"
            edp["contact_email"] = "cmueller@asascience.com"
            edp["contact_address"] = "55 Village Square Drive, South Kingstown, RI, 02886"
            data_provider = edp

        if data_source is None:
            dp = {}
            dp["base_data_url"] = "http://oos.soest.hawaii.edu/thredds/"
            dp["protocol_type"] = PROTOCOL_TYPE_DAP
            data_source = dp

        if ext_dset is None:
            ds = {}
            ds["dataset_path"] = "dodsC/hioos/hfr/kokagg"
            ds["temporal_id"] = "time"
            ext_dset = ds

        self.ext_observatory_object = IonObject("ExternalDataProvider", data_provider)
        self.ext_data_producer_object = IonObject("ExternalDataSource", data_source)
        self.ext_data_set_object = IonObject("ExternalDataset", ext_dset)
        
        if len(kwargs) > 0:
            log.info("initialize():: Keyword args:")
            for key in kwargs:
                log.info("  %s: %s" % (key, kwargs[key]))

        return

    def get_status(self, **kwargs):
        return NotImplemented

    def get_catalog(self, **kwargs):
        return NotImplemented

    def has_new_data(self, **kwargs):
        return False

    def acquire_new_data(self, request=None, **kwargs):
        return NotImplemented

    def acquire_historical_data(self, **kwargs):
        return NotImplemented

    def get_signature(self, recalculate=False, **kwargs):
        return NotImplemented

    def compare(self, BaseExternalObservatoryHandler=None):
        return NotImplemented

    # Generic, utility and helper methods

    def calculate_decomposition(self, **kwargs):
        return NotImplemented

    def __repr__(self):
#        return "on=%s off=%s" % (self.OBSERVATORY_ONLINE, self.OBSERVATORY_OFFLINE)
        return "\n>> ExternalObservatory:\n%s\n>> ExternalDataProducer:\n%s\n>>ExternalDataSet\n%s" % (self.ext_observatory_object, self.ext_data_producer_object, self.ext_data_set_object)



class ExternalObservatoryHandlerClients(BaseClients):
    def __init__(self, process=None):
        BaseClients.__init__(self)
        self.resource_registry = ResourceRegistryServiceProcessClient(process=process)