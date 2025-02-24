# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, TYPE_CHECKING

import msrest.serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    import __init__ as _models


class AssociatedResourcesListResult(msrest.serialization.Model):
    """Azure resources returned by the resource action to get a list of assigned resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar total_count: Total number of Azure resources assigned to the identity.
    :vartype total_count: float
    :ivar value: The collection of Azure resources returned by the resource action to get a list of
     assigned resources.
    :vartype value: list[~azure.mgmt.msi.v2021_09_30_preview.models.AzureResource]
    :ivar next_link: The url to get the next page of results, if any.
    :vartype next_link: str
    """

    _validation = {
        'total_count': {'readonly': True},
        'value': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'total_count': {'key': 'totalCount', 'type': 'float'},
        'value': {'key': 'value', 'type': '[AzureResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(AssociatedResourcesListResult, self).__init__(**kwargs)
        self.total_count = None
        self.value = None
        self.next_link = None


class AzureResource(msrest.serialization.Model):
    """Describes an Azure resource that is attached to an identity.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The ID of this resource.
    :vartype id: str
    :ivar name: The name of this resource.
    :vartype name: str
    :ivar type: The type of this resource.
    :vartype type: str
    :ivar resource_group: The name of the resource group this resource belongs to.
    :vartype resource_group: str
    :ivar subscription_id: The ID of the subscription this resource belongs to.
    :vartype subscription_id: str
    :ivar subscription_display_name: The name of the subscription this resource belongs to.
    :vartype subscription_display_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_group': {'readonly': True},
        'subscription_id': {'readonly': True},
        'subscription_display_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'resource_group': {'key': 'resourceGroup', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'subscription_display_name': {'key': 'subscriptionDisplayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(AzureResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.resource_group = None
        self.subscription_id = None
        self.subscription_display_name = None


class CloudErrorBody(msrest.serialization.Model):
    """An error response from the ManagedServiceIdentity service.

    :ivar code: An identifier for the error.
    :vartype code: str
    :ivar message: A message describing the error, intended to be suitable for display in a user
     interface.
    :vartype message: str
    :ivar target: The target of the particular error. For example, the name of the property in
     error.
    :vartype target: str
    :ivar details: A list of additional details about the error.
    :vartype details: list[~azure.mgmt.msi.v2021_09_30_preview.models.CloudErrorBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[CloudErrorBody]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["_models.CloudErrorBody"]] = None,
        **kwargs
    ):
        """
        :keyword code: An identifier for the error.
        :paramtype code: str
        :keyword message: A message describing the error, intended to be suitable for display in a user
         interface.
        :paramtype message: str
        :keyword target: The target of the particular error. For example, the name of the property in
         error.
        :paramtype target: str
        :keyword details: A list of additional details about the error.
        :paramtype details: list[~azure.mgmt.msi.v2021_09_30_preview.models.CloudErrorBody]
        """
        super(CloudErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class Resource(msrest.serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: Required. The geo-location where the resource lives.
    :vartype location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: Required. The geo-location where the resource lives.
        :paramtype location: str
        """
        super(TrackedResource, self).__init__(**kwargs)
        self.tags = tags
        self.location = location


class Identity(TrackedResource):
    """Describes an identity resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: Required. The geo-location where the resource lives.
    :vartype location: str
    :ivar tenant_id: The id of the tenant which the identity belongs to.
    :vartype tenant_id: str
    :ivar principal_id: The id of the service principal object associated with the created
     identity.
    :vartype principal_id: str
    :ivar client_id: The id of the app associated with the identity. This is a random generated
     UUID by MSI.
    :vartype client_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'tenant_id': {'readonly': True},
        'principal_id': {'readonly': True},
        'client_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
        'client_id': {'key': 'properties.clientId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: Required. The geo-location where the resource lives.
        :paramtype location: str
        """
        super(Identity, self).__init__(tags=tags, location=location, **kwargs)
        self.tenant_id = None
        self.principal_id = None
        self.client_id = None


class IdentityUpdate(Resource):
    """Describes an identity resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar location: The geo-location where the resource lives.
    :vartype location: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar tenant_id: The id of the tenant which the identity belongs to.
    :vartype tenant_id: str
    :ivar principal_id: The id of the service principal object associated with the created
     identity.
    :vartype principal_id: str
    :ivar client_id: The id of the app associated with the identity. This is a random generated
     UUID by MSI.
    :vartype client_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'tenant_id': {'readonly': True},
        'principal_id': {'readonly': True},
        'client_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
        'client_id': {'key': 'properties.clientId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: Optional[str] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword location: The geo-location where the resource lives.
        :paramtype location: str
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        """
        super(IdentityUpdate, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.tenant_id = None
        self.principal_id = None
        self.client_id = None


class Operation(msrest.serialization.Model):
    """Operation supported by the Microsoft.ManagedIdentity REST API.

    :ivar name: The name of the REST Operation. This is of the format
     {provider}/{resource}/{operation}.
    :vartype name: str
    :ivar display: The object that describes the operation.
    :vartype display: ~azure.mgmt.msi.v2021_09_30_preview.models.OperationDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["_models.OperationDisplay"] = None,
        **kwargs
    ):
        """
        :keyword name: The name of the REST Operation. This is of the format
         {provider}/{resource}/{operation}.
        :paramtype name: str
        :keyword display: The object that describes the operation.
        :paramtype display: ~azure.mgmt.msi.v2021_09_30_preview.models.OperationDisplay
        """
        super(Operation, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDisplay(msrest.serialization.Model):
    """The object that describes the operation.

    :ivar provider: Friendly name of the resource provider.
    :vartype provider: str
    :ivar operation: The type of operation. For example: read, write, delete.
    :vartype operation: str
    :ivar resource: The resource type on which the operation is performed.
    :vartype resource: str
    :ivar description: A description of the operation.
    :vartype description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        operation: Optional[str] = None,
        resource: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword provider: Friendly name of the resource provider.
        :paramtype provider: str
        :keyword operation: The type of operation. For example: read, write, delete.
        :paramtype operation: str
        :keyword resource: The resource type on which the operation is performed.
        :paramtype resource: str
        :keyword description: A description of the operation.
        :paramtype description: str
        """
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.operation = operation
        self.resource = resource
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """A list of operations supported by Microsoft.ManagedIdentity Resource Provider.

    :ivar value: A list of operations supported by Microsoft.ManagedIdentity Resource Provider.
    :vartype value: list[~azure.mgmt.msi.v2021_09_30_preview.models.Operation]
    :ivar next_link: The url to get the next page of results, if any.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.Operation"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: A list of operations supported by Microsoft.ManagedIdentity Resource Provider.
        :paramtype value: list[~azure.mgmt.msi.v2021_09_30_preview.models.Operation]
        :keyword next_link: The url to get the next page of results, if any.
        :paramtype next_link: str
        """
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ProxyResource(Resource):
    """The resource model definition for a Azure Resource Manager proxy resource. It will not have tags and a location.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        """
        """
        super(ProxyResource, self).__init__(**kwargs)


class SystemAssignedIdentity(ProxyResource):
    """Describes a system assigned identity resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar location: Required. The geo-location where the resource lives.
    :vartype location: str
    :ivar tags: A set of tags. Resource tags.
    :vartype tags: dict[str, str]
    :ivar tenant_id: The id of the tenant which the identity belongs to.
    :vartype tenant_id: str
    :ivar principal_id: The id of the service principal object associated with the created
     identity.
    :vartype principal_id: str
    :ivar client_id: The id of the app associated with the identity. This is a random generated
     UUID by MSI.
    :vartype client_id: str
    :ivar client_secret_url: The ManagedServiceIdentity DataPlane URL that can be queried to obtain
     the identity credentials.
    :vartype client_secret_url: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'tenant_id': {'readonly': True},
        'principal_id': {'readonly': True},
        'client_id': {'readonly': True},
        'client_secret_url': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'tenant_id': {'key': 'properties.tenantId', 'type': 'str'},
        'principal_id': {'key': 'properties.principalId', 'type': 'str'},
        'client_id': {'key': 'properties.clientId', 'type': 'str'},
        'client_secret_url': {'key': 'properties.clientSecretUrl', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        """
        :keyword location: Required. The geo-location where the resource lives.
        :paramtype location: str
        :keyword tags: A set of tags. Resource tags.
        :paramtype tags: dict[str, str]
        """
        super(SystemAssignedIdentity, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.tenant_id = None
        self.principal_id = None
        self.client_id = None
        self.client_secret_url = None


class UserAssignedIdentitiesListResult(msrest.serialization.Model):
    """Values returned by the List operation.

    :ivar value: The collection of userAssignedIdentities returned by the listing operation.
    :vartype value: list[~azure.mgmt.msi.v2021_09_30_preview.models.Identity]
    :ivar next_link: The url to get the next page of results, if any.
    :vartype next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Identity]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["_models.Identity"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword value: The collection of userAssignedIdentities returned by the listing operation.
        :paramtype value: list[~azure.mgmt.msi.v2021_09_30_preview.models.Identity]
        :keyword next_link: The url to get the next page of results, if any.
        :paramtype next_link: str
        """
        super(UserAssignedIdentitiesListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link
