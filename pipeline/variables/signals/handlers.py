# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa

from django.dispatch import receiver
from django.db.utils import ProgrammingError
from pipeline.core.data.var import LazyVariable
from pipeline.models import VariableModel
from pipeline.core.signals import pre_variable_register


@receiver(pre_variable_register, sender=LazyVariable)
def pre_variable_register_handler(sender, variable_code, variable_cls, **kwargs):
    try:
        obj, created = VariableModel.objects.get_or_create(code=variable_code,
                                                           defaults={
                                                               'status': __debug__,
                                                           })
        if not created and not obj.status:
            obj.status = True
            obj.save()
    except ProgrammingError:
        # first migrate
        pass
