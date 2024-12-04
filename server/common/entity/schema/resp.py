# !/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import TypeVar, Generic, Optional

from pydantic import BaseModel

from server.common import constants

T = TypeVar('T')


class RCode(BaseModel):
    code: int = constants.STATUS_0_OK


class RBase(RCode):
    msg: Optional[str] = None


class R(RBase, Generic[T]):
    data: Optional[T] = None

class R1(dict):

    @staticmethod
    def ins():
        return R1()

    def code(self, code):
        self['code'] = code
        return self

    def msg(self, msg):
        self['msg'] = msg
        return self

    def data(self, data):
        self['data'] = data
        return self

