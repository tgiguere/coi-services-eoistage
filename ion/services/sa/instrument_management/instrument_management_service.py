#!/usr/bin/env python

__author__ = 'Maurice Manning'
__license__ = 'Apache 2.0'


#from pyon.public import Container
from pyon.core.bootstrap import IonObject
from pyon.core.exception import BadRequest, NotFound
from pyon.datastore.datastore import DataStore
#from pyon.net.endpoint import RPCClient
from pyon.util.log import log



from interface.services.sa.iinstrument_management_service import BaseInstrumentManagementService

class InstrumentManagementService(BaseInstrumentManagementService):
    
    # find whether a resource with the same type and name already exists
    def _check_name(self, resource_type, name):
        try:
            found_res, _ = self.clients.resource_registry.find_resources(resource_type, None, name, True)
        except NotFound:
            # New after all.  PROCEED.
            pass
        else:
            if 0 < len(found_res):
                raise BadRequest("%s resource named '%s' already exists" % (resource_type, name))
        
    # try to get a resource
    def _get_resource(self, resource_type, resource_id):
        resource = self.clients.resource_registry.read(resource_id)
        if not resource:
            raise NotFound("%s %s does not exist" % (resource_type, resource_id))
        return resource

    # return a valid message from a create
    def _return_create(self, resource_label, resource_id):
        retval = {}
        retval[resource_label] = resource_id
        return retval

    # return a valid message from an update
    def _return_update(self, success_bool):
        retval = {}
        retval["success"] = success_bool
        return retval

    # return a valid message from a read
    def _return_read(self, resource_type, resource_label, resource_id):
        retval = {}
        resource = self._get_resource(resource_type, resource_id)
        retval[resource_label] = resource
        return retval

    # return a valid message from a delete
    def _return_update(self, success_bool):
        retval = {}
        retval["success"] = success_bool
        return retval

    
    ##########################################################################
    #
    # INSTRUMENT AGENT
    #
    ##########################################################################

    def create_instrument_agent(self, instrument_agent_info={}):
        """
        method docstring
        """
        # Validate the input filter and augment context as required
        self._check_name("InstrumentAgent", name)

        #FIXME: more validation?

        #persist
        instrument_agent_obj = IonObject("InstrumentAgent", instrument_agent_info)
        instrument_agent_id, _ = self.clients.resource_registry.create(instrument_agent_obj)
~
        return self._return_create("instrument_agent_id", instrument_agent_id)


    def update_instrument_agent(self, instrument_agent_id='', instrument_agent_info={}):
        """
        method docstring
        """
        instrument_agent_obj = self._get_resource("InstrumentAgent", instrument_agent_id)        

        # Validate the input 
        
        #if the name is being changed, make sure it's not being changed to a duplicate
        self._check_name("InstrumentAgent", instrument_agent_info.name)

        # update some list of fields
        
        #persist
        self.clients.resource_registry.update(instrument_agent_obj)


        return self._return_update(True)

        

    def read_instrument_agent(self, instrument_agent_id=''):
        """
        method docstring
        """
        return self._return_read("InstrumentAgent", "instrument_agent_info", instrument_agent_id)



    def delete_instrument_agent(self, instrument_agent_id=''):
        """
        method docstring
        """

        instrument_agent_obj = self._get_resource("InstrumentAgent", instrument_agent_id)        
        
        self.clients.resource_registry.delete(instrument_agent_obj)
        
        return self._return_delete(True)

        # Return Value
        # ------------
        # {success: true}
        #
        pass



    def find_instrument_agents(self, filters={}):
        """
        method docstring
        """
        # Return Value
        # ------------
        # instrument_agent_info_list: []
        #
        raise NotImplementedError()
        pass



    def assign_instrument_agent(self, instrument_agent_id='', instrument_id='', instrument_agent_instance={}):
        """
        method docstring
        """
        # Return Value
        # ------------
        # {success: true}
        #
        raise NotImplementedError()
        pass

    def unassign_instrument_agent(self, instrument_agent_id='', instrument_id=''):
        """
        method docstring
        """
        # Return Value
        # ------------
        # {success: true}
        #
        raise NotImplementedError()
        pass


    
    ##########################################################################
    #
    # INSTRUMENT MODEL
    #
    ##########################################################################

    def create_instrument_model(self, instrument_model_info={}):
        """
        method docstring
        """
        # Define YAML/params from
        # Instrument metadata draft: https://confluence.oceanobservatories.org/display/CIDev/R2+Resource+Page+for+Instrument+Instance

        # Validate the input filter and augment context as required
        self._check_name("InstrumentModel", name)

        #FIXME: more validation?

        # Create instrument resource, set initial state, persist
        instrument_model_obj = IonObject("InstrumentModel", instrument_model_info)
        instrument_model_id, _ = self.clients.resource_registry.create(instrument_model_obj)

        # Create associations
        # ??????? WHAT ASSOCIATIONS?

        return self._return_create("instrument_model_id", instrument_model_id)


    def update_instrument_model(self, instrument_id='', instrument_model_info={}):
        """
        method docstring
        """

        instrument_model_obj = self._get_resource("Instrumentmodel", instrument_model_id)        

        # Validate the input 
        
        #if the name is being changed, make sure it's not being changed to a duplicate
        self._check_name("Instrumentmodel", instrument_model_info.name)

        # update some list of fields
        
        #persist
        self.clients.resource_registry.update(instrument_model_obj)

        return self._return_update(True)

    

    def read_instrument_model(self, instrument_model_id=''):
        """
        method docstring
        """
        return self._return_read("InstrumentModel", "instrument_model_info", instrument_model_id)


    def delete_instrument_model(self, instrument_model_id=''):
        """
        method docstring
        """
        instrument_model_obj = self._get_resource("InstrumentModel", instrument_model_id)        
        
        self.clients.resource_registry.delete(instrument_model_obj)
        
        return self._return_delete(True)


    def find_instrument_models(self, filters={}):
        """
        method docstring
        """
        # Return Value
        # ------------
        # instrument_model_info_list: []
        #
        raise NotImplementedError()
        pass







    ##########################################################################
    #
    # PHYSICAL INSTRUMENT
    #
    ##########################################################################



    def create_instrument_device(self, instrument_device_info={}):
        """
        method docstring
        """
        # Define YAML/params from
        # Instrument metadata draft: https://confluence.oceanobservatories.org/display/CIDev/R2+Resource+Page+for+Instrument+Instance

        # Validate the input filter and augment context as required
        self._check_name("InstrumentDevice", name)

        #FIXME: more validation?

        # Create instrument resource, set initial state, persist
        instrument_device_obj = IonObject("InstrumentDevice", instrument_device_info)
        instrument_device_id, _ = self.clients.resource_registry.create(instrument_device_obj)

        # Create data product (products?)

        # associate data product with instrument
        #_ = self.clients.resource_registry.create_association(org_id, AT.hasExchangeSpace, xs_id)

        return self._return_create("instrument_device_id", instrument_device_id)



    def update_instrument_device(self, instrument_id='', instrument_device_info={}):
        """
        method docstring
        """

        instrument_device_obj = self._get_resource("Instrumentdevice", instrument_device_id)        

        # Validate the input 
        
        #if the name is being changed, make sure it's not being changed to a duplicate
        self._check_name("Instrumentdevice", instrument_device_info.name)

        # update some list of fields
        
        #persist
        self.clients.resource_registry.update(instrument_device_obj)

        return self._return_update(True)

    

    def read_instrument_device(self, instrument_device_id=''):
        """
        method docstring
        """
        return self._return_read("InstrumentDevice", "instrument_device_info", instrument_device_id)


    def delete_instrument_device(self, instrument_device_id=''):
        """
        method docstring
        """
        instrument_device_obj = self._get_resource("InstrumentDevice", instrument_device_id)        
        
        self.clients.resource_registry.delete(instrument_device_obj)
        
        return self._return_delete(True)



    def find_instrument_devices(self, filters={}):
        """
        method docstring
        """
        # Return Value
        # ------------
        # instrument_device_info_list: []
        #
        raise NotImplementedError()
        pass

    def assign_instrument_device(self, instrument_id='', instrument_device_id=''):
        """
        method docstring
        """
        # Return Value
        # ------------
        # {success: true}
        #
        raise NotImplementedError()
        pass

    def unassign_instrument_device(self, instrument_id='', instrument_device_id=''):
        """
        method docstring
        """
        # Return Value
        # ------------
        # {success: true}
        #
        raise NotImplementedError()
        pass

    def activate_instrument_device(self, instrument_device_id=''):
        """
        method docstring
        """
        # Return Value
        # ------------
        # {success: true}
        #
        raise NotImplementedError()
        pass




    
    ##########################################################################
    #
    # LOGICAL INSTRUMENT
    #
    ##########################################################################


    def create_instrument_logical(self, instrument_logical_info={}):
        """
        method docstring
        """
        # Define YAML/params from
        # Instrument metadata draft: https://confluence.oceanobservatories.org/display/CIDev/R2+Resource+Page+for+Instrument+Instance

        # Validate the input filter and augment context as required
        self._check_name("InstrumentLogical", name)

        #FIXME: more validation?

        # Create instrument resource, set initial state, persist
        instrument_logical_obj = IonObject("InstrumentLogical", instrument_logical_info)
        instrument_logical_id, _ = self.clients.resource_registry.create(instrument_logical_obj)

        # Create data product (products?)

        # associate data product with instrument
        #_ = self.clients.resource_registry.create_association(org_id, AT.hasExchangeSpace, xs_id)

        return self._return_create("instrument_logical_id", instrument_logical_id)



    def update_instrument_logical(self, instrument_id='', instrument_logical_info={}):
        """
        method docstring
        """

        instrument_logical_obj = self._get_resource("Instrumentlogical", instrument_logical_id)        

        # Validate the input 
        
        #if the name is being changed, make sure it's not being changed to a duplicate
        self._check_name("Instrumentlogical", instrument_logical_info.name)

        # update some list of fields
        
        #persist
        self.clients.resource_registry.update(instrument_logical_obj)

        return self._return_update(True)

    

    def read_instrument_logical(self, instrument_logical_id=''):
        """
        method docstring
        """
        return self._return_read("InstrumentLogical", "instrument_logical_info", instrument_logical_id)


    def delete_instrument_logical(self, instrument_logical_id=''):
        """
        method docstring
        """
        instrument_logical_obj = self._get_resource("InstrumentLogical", instrument_logical_id)        
        
        self.clients.resource_registry.delete(instrument_logical_obj)
        
        return self._return_delete(True)


    def find_instrument_logical(self, filters={}):
        """
        method docstring
        """
        # Return Value
        # ------------
        # instrument_logical_info_list: []
        #
        raise NotImplementedError()
        pass


    ##
    ##
    ##  DIRECT ACCESS
    ##
    ##

    def request_direct_access(self, instrument_id=''):
        """
        method docstring
        """
        
        # determine whether id is for physical or logical instrument
        # look up instrument if not
        
        # Validate request; current instrument state, policy, and other

        # Retrieve and save current instrument settings

        # Request DA channel, save reference

        # Return direct access channel
        raise NotImplementedError()
        pass

    def stop_direct_access(self, instrument_id=''):
        """
        method docstring
        """
        # Return Value
        # ------------
        # {success: true}
        #
        raise NotImplementedError()
        pass


