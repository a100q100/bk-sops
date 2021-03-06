# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
""" # noqa

from gcloud.conf import settings


def get_user_info(request):
    client = settings.ESB_GET_CLIENT_BY_REQUEST(request)
    auth = getattr(client, settings.ESB_AUTH_COMPONENT_SYSTEM)
    get_user_info = getattr(auth, settings.ESB_AUTH_GET_USER_INFO)
    user_info = get_user_info({})
    if 'data' in user_info:
        user_info['data']['bk_supplier_account'] = 0
    return user_info
