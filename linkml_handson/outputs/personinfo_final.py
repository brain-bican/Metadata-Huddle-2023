from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, ConfigDict, Field
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class GenderType(str, Enum):
    """
    Allowed gender types.
    """
    
    man = "man"
    
    woman = "woman"
    
    other = "other"
    
    

class NamedThing(ConfiguredBaseModel):
    """
    A generic grouping for any identifiable entity.
    """
    id: str = Field(..., description="""A unique identifier.""")
    name: str = Field(..., description="""A full legal name.""")
    

class HasAliases(ConfiguredBaseModel):
    """
    A mixin applied to any class that can have aliases/alternateNames
    """
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alternate names.""")
    

class Person(HasAliases, NamedThing):
    """
    A person (alive, dead, undead, or fictional).
    """
    primary_email: Optional[str] = Field(None, description="""The primary email used by the entity.""")
    birth_date: Optional[str] = Field(None, description="""Day of birth""")
    age_in_years: int = Field(..., description="""Age in years.""", ge=0, le=200)
    gender: Optional[GenderType] = Field(None, description="""Gender provided by the person.""")
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alternate names.""")
    id: str = Field(..., description="""A unique identifier.""")
    name: str = Field(..., description="""A full legal name.""")
    

class Organization(HasAliases, NamedThing):
    """
    An organization such as a company or university
    """
    aliases: Optional[List[str]] = Field(default_factory=list, description="""Alternate names.""")
    id: str = Field(..., description="""A unique identifier.""")
    name: str = Field(..., description="""A full legal name.""")
    


# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
NamedThing.update_forward_refs()
HasAliases.update_forward_refs()
Person.update_forward_refs()
Organization.update_forward_refs()

