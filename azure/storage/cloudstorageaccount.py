﻿#-------------------------------------------------------------------------
# Copyright (c) Microsoft.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#--------------------------------------------------------------------------

# Note that we import BlobService/QueueService/TableService on demand
# because this module is imported by azure/storage/__init__
# ie. we don't want 'import azure.storage' to trigger an automatic import
# of blob/queue/table packages.

class CloudStorageAccount(object):

    """
    Provides a factory for creating the blob, queue, table, and file services
    with a common account name and account key.  Users can either use the
    factory or can construct the appropriate service directly.
    """

    def __init__(self, account_name=None, account_key=None):
        self.account_name = account_name
        self.account_key = account_key

    def create_block_blob_service(self):
        from .blob.blockblobservice import BlockBlobService
        return BlockBlobService(self.account_name, self.account_key)

    def create_page_blob_service(self):
        from .blob.pageblobservice import PageBlobService
        return PageBlobService(self.account_name, self.account_key)

    def create_append_blob_service(self):
        from .blob.appendblobservice import AppendBlobService
        return AppendBlobService(self.account_name, self.account_key)

    def create_table_service(self):
        from .table.tableservice import TableService
        return TableService(self.account_name, self.account_key)

    def create_queue_service(self):
        from .queue.queueservice import QueueService
        return QueueService(self.account_name, self.account_key)

    def create_file_service(self):
        from .file.fileservice import FileService
        return FileService(self.account_name, self.account_key)