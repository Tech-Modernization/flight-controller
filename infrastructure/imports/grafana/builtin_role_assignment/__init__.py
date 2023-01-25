'''
# `grafana_builtin_role_assignment`

Refer to the Terraform Registory for docs: [`grafana_builtin_role_assignment`](https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class BuiltinRoleAssignment(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.builtinRoleAssignment.BuiltinRoleAssignment",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment grafana_builtin_role_assignment}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        builtin_role: builtins.str,
        roles: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BuiltinRoleAssignmentRoles", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment grafana_builtin_role_assignment} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param builtin_role: Organization roles (``Viewer``, ``Editor``, ``Admin``) or ``Grafana Admin`` to assign the roles to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#builtin_role BuiltinRoleAssignment#builtin_role}
        :param roles: roles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#roles BuiltinRoleAssignment#roles}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#id BuiltinRoleAssignment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90d32b658865a43635854e6805a47de116742af063479f69022ca0f90242c064)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BuiltinRoleAssignmentConfig(
            builtin_role=builtin_role,
            roles=roles,
            id=id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putRoles")
    def put_roles(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BuiltinRoleAssignmentRoles", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bee63d913e5fa74b5b34e4bb2d7490bdaa9f9edaf9c82cf6ad87446b38f77bb4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoles", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="roles")
    def roles(self) -> "BuiltinRoleAssignmentRolesList":
        return typing.cast("BuiltinRoleAssignmentRolesList", jsii.get(self, "roles"))

    @builtins.property
    @jsii.member(jsii_name="builtinRoleInput")
    def builtin_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "builtinRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="rolesInput")
    def roles_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BuiltinRoleAssignmentRoles"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BuiltinRoleAssignmentRoles"]]], jsii.get(self, "rolesInput"))

    @builtins.property
    @jsii.member(jsii_name="builtinRole")
    def builtin_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "builtinRole"))

    @builtin_role.setter
    def builtin_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ef2e56ca0da0a5f749e24da1673e2b667df107860e86cc579845ff1255083e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "builtinRole", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6a26d6c558f9e058ff61b0dee1c4666be61db3c616489194ca49c4b7ba8053a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="grafana.builtinRoleAssignment.BuiltinRoleAssignmentConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "builtin_role": "builtinRole",
        "roles": "roles",
        "id": "id",
    },
)
class BuiltinRoleAssignmentConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        builtin_role: builtins.str,
        roles: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["BuiltinRoleAssignmentRoles", typing.Dict[builtins.str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param builtin_role: Organization roles (``Viewer``, ``Editor``, ``Admin``) or ``Grafana Admin`` to assign the roles to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#builtin_role BuiltinRoleAssignment#builtin_role}
        :param roles: roles block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#roles BuiltinRoleAssignment#roles}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#id BuiltinRoleAssignment#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94160e7e458743a60957b26d559573ebc5dd0694639033922b3977d74401b994)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument builtin_role", value=builtin_role, expected_type=type_hints["builtin_role"])
            check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "builtin_role": builtin_role,
            "roles": roles,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if id is not None:
            self._values["id"] = id

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def builtin_role(self) -> builtins.str:
        '''Organization roles (``Viewer``, ``Editor``, ``Admin``) or ``Grafana Admin`` to assign the roles to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#builtin_role BuiltinRoleAssignment#builtin_role}
        '''
        result = self._values.get("builtin_role")
        assert result is not None, "Required property 'builtin_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def roles(
        self,
    ) -> typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BuiltinRoleAssignmentRoles"]]:
        '''roles block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#roles BuiltinRoleAssignment#roles}
        '''
        result = self._values.get("roles")
        assert result is not None, "Required property 'roles' is missing"
        return typing.cast(typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["BuiltinRoleAssignmentRoles"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#id BuiltinRoleAssignment#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuiltinRoleAssignmentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="grafana.builtinRoleAssignment.BuiltinRoleAssignmentRoles",
    jsii_struct_bases=[],
    name_mapping={"uid": "uid", "global_": "global"},
)
class BuiltinRoleAssignmentRoles:
    def __init__(
        self,
        *,
        uid: builtins.str,
        global_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    ) -> None:
        '''
        :param uid: Unique identifier of the role to assign to ``builtin_role``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#uid BuiltinRoleAssignment#uid}
        :param global_: States whether the assignment is available across all organizations or not. Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#global BuiltinRoleAssignment#global}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e40a5bd7526c5f18f29b73da930801888cdc541b87129af60b9043267dff4b2b)
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
            check_type(argname="argument global_", value=global_, expected_type=type_hints["global_"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "uid": uid,
        }
        if global_ is not None:
            self._values["global_"] = global_

    @builtins.property
    def uid(self) -> builtins.str:
        '''Unique identifier of the role to assign to ``builtin_role``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#uid BuiltinRoleAssignment#uid}
        '''
        result = self._values.get("uid")
        assert result is not None, "Required property 'uid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''States whether the assignment is available across all organizations or not. Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/grafana/r/builtin_role_assignment#global BuiltinRoleAssignment#global}
        '''
        result = self._values.get("global_")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuiltinRoleAssignmentRoles(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BuiltinRoleAssignmentRolesList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.builtinRoleAssignment.BuiltinRoleAssignmentRolesList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd783e1769c9b2a0969b91fe151c57232ef7081cf2e64dfccf5d93b70dcfbf3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BuiltinRoleAssignmentRolesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9e7519f25a8405a8b47ae89bd259691d5a4e322e262ad5adeb61316b04b87c2)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BuiltinRoleAssignmentRolesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5c912d90ff6c2360a0727c261bec0e4bbf3092b4141dca951ea3c93c6e572ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab015b0748e14aca97a6edda24ee538aee054fbb38d758c30de276a7670b302)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f962ade8d94f95c72f61192a7c9930219019d61b2f404e3142262bcfeeea938d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BuiltinRoleAssignmentRoles]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BuiltinRoleAssignmentRoles]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BuiltinRoleAssignmentRoles]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f1143864f16b5202d756d45cd2ea9131633156200ff9319c2da6b6c53d24c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BuiltinRoleAssignmentRolesOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="grafana.builtinRoleAssignment.BuiltinRoleAssignmentRolesOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5661055baa9e637cb0988041ff72e72967c9cdb5b9ab74f41af184606737588e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGlobal")
    def reset_global(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlobal", []))

    @builtins.property
    @jsii.member(jsii_name="globalInput")
    def global_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "globalInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="global")
    def global_(self) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "global"))

    @global_.setter
    def global_(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a94e79c84dabcd4939218c524cda88dd25f0599845dd2a6a9177dbed8a699ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "global", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf1a38a6f5cd37a969da4eb5382101bad47e5f9b6d1085e898feba036ddb3c5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BuiltinRoleAssignmentRoles, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BuiltinRoleAssignmentRoles, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BuiltinRoleAssignmentRoles, _cdktf_9a9027ec.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__522632480dba27a715e9e1abdc2c233e766181b6aeb7e887b2ddea6f4771eb62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BuiltinRoleAssignment",
    "BuiltinRoleAssignmentConfig",
    "BuiltinRoleAssignmentRoles",
    "BuiltinRoleAssignmentRolesList",
    "BuiltinRoleAssignmentRolesOutputReference",
]

publication.publish()

def _typecheckingstub__90d32b658865a43635854e6805a47de116742af063479f69022ca0f90242c064(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    builtin_role: builtins.str,
    roles: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BuiltinRoleAssignmentRoles, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bee63d913e5fa74b5b34e4bb2d7490bdaa9f9edaf9c82cf6ad87446b38f77bb4(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BuiltinRoleAssignmentRoles, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ef2e56ca0da0a5f749e24da1673e2b667df107860e86cc579845ff1255083e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6a26d6c558f9e058ff61b0dee1c4666be61db3c616489194ca49c4b7ba8053a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94160e7e458743a60957b26d559573ebc5dd0694639033922b3977d74401b994(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    builtin_role: builtins.str,
    roles: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[BuiltinRoleAssignmentRoles, typing.Dict[builtins.str, typing.Any]]]],
    id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e40a5bd7526c5f18f29b73da930801888cdc541b87129af60b9043267dff4b2b(
    *,
    uid: builtins.str,
    global_: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd783e1769c9b2a0969b91fe151c57232ef7081cf2e64dfccf5d93b70dcfbf3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9e7519f25a8405a8b47ae89bd259691d5a4e322e262ad5adeb61316b04b87c2(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5c912d90ff6c2360a0727c261bec0e4bbf3092b4141dca951ea3c93c6e572ca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab015b0748e14aca97a6edda24ee538aee054fbb38d758c30de276a7670b302(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f962ade8d94f95c72f61192a7c9930219019d61b2f404e3142262bcfeeea938d(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f1143864f16b5202d756d45cd2ea9131633156200ff9319c2da6b6c53d24c8(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[BuiltinRoleAssignmentRoles]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5661055baa9e637cb0988041ff72e72967c9cdb5b9ab74f41af184606737588e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a94e79c84dabcd4939218c524cda88dd25f0599845dd2a6a9177dbed8a699ce(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf1a38a6f5cd37a969da4eb5382101bad47e5f9b6d1085e898feba036ddb3c5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522632480dba27a715e9e1abdc2c233e766181b6aeb7e887b2ddea6f4771eb62(
    value: typing.Optional[typing.Union[BuiltinRoleAssignmentRoles, _cdktf_9a9027ec.IResolvable]],
) -> None:
    """Type checking stubs"""
    pass
