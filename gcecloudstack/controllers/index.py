#!/usr/bin/env python
# encoding: utf-8
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.


from gcecloudstack import app
from gcecloudstack import authentication
from gcecloudstack.services import requester
from flask import jsonify

@app.route('/example')
@authentication.required
def example(authorization):
    resp = jsonify({
            "jsessionid": authorization.jsessionid,
            "sessionkey": authorization.sessionkey,
        })
    resp.status_code = 200
    return resp

@app.route('/compute/v1beta15/projects/<projectid>/zones')
@authentication.required
def listzones(projectid,authorization):
    command = 'listZones'
    args = None
    logger = None
    response = requester.make_request(command, args, logger, authorization.jsessionid, authorization.sessionkey)
    print response

    return response

@app.route('/compute/v1beta15/projects/<projectid>')
@authentication.required
def getProject(projectid,authorization):
    resp = jsonify({
          "commonInstanceMetadata": {
            "kind": "compute#metadata"
          },
          "creationTimestamp": "2013-09-04T17:41:05.702-07:00",
          "description": "",
          "id": "14140363120428320211",
          "kind": "compute#project",
          "name": projectid,
          "quotas": [
            {
              "limit": 16.0,
              "metric": "INSTANCES",
              "usage": 0.0
            },
            {
              "limit": 24.0,
              "metric": "CPUS",
              "usage": 0.0
            },
            {
              "limit": 16.0,
              "metric": "EPHEMERAL_ADDRESSES",
              "usage": 0.0
            },
            {
              "limit": 16.0,
              "metric": "DISKS",
              "usage": 0.0
            },
            {
              "limit": 2048.0,
              "metric": "DISKS_TOTAL_GB",
              "usage": 0.0
            },
            {
              "limit": 1000.0,
              "metric": "SNAPSHOTS",
              "usage": 0.0
            },
            {
              "limit": 5.0,
              "metric": "NETWORKS",
              "usage": 1.0
            },
            {
              "limit": 100.0,
              "metric": "FIREWALLS",
              "usage": 2.0
            },
            {
              "limit": 100.0,
              "metric": "IMAGES",
              "usage": 0.0
            },
            {
              "limit": 7.0,
              "metric": "STATIC_ADDRESSES",
              "usage": 0.0
            },
            {
              "limit": 100.0,
              "metric": "ROUTES",
              "usage": 2.0
            },
            {
              "limit": 50.0,
              "metric": "FORWARDING_RULES",
              "usage": 0.0
            },
            {
              "limit": 50.0,
              "metric": "TARGET_POOLS",
              "usage": 0.0
            },
            {
              "limit": 50.0,
              "metric": "HEALTH_CHECKS",
              "usage": 0.0
            }
          ],
          "selfLink": "https://localhost:5000/compute/v1beta15/projects/silent-thunder-0001"
        })
    resp.status_code = 200

    return resp

@app.route('/discovery/v1/apis/compute/v1beta15/rest')
def discovery():
    resp = jsonify(
        {
         "kind": "discovery#restDescription",
         "etag": "\"wtgj9ZncHCe-ShJM8RewHb1DgWI/x3AWKn-_parTsyXrlyxIoGyiwxc\"",
         "discoveryVersion": "v1",
         "id": "compute:v1beta15",
         "name": "compute",
         "version": "v1beta15",
         "revision": "20130817",
         "title": "Compute Engine API",
         "description": "API for the Google Compute Engine service.",
         "ownerDomain": "google.com",
         "ownerName": "Google",
         "icons": {
          "x16": "http://www.google.com/images/icons/product/compute_engine-16.png",
          "x32": "http://www.google.com/images/icons/product/compute_engine-32.png"
         },
         "documentationLink": "https://developers.google.com/compute/docs/reference/v1beta15",
         "protocol": "rest",
         "baseUrl": "https://localhost:5000/compute/v1beta15/projects/",
         "basePath": "/compute/v1beta15/projects/",
         "rootUrl": "https://localhost:5000/",
         "servicePath": "compute/v1beta15/projects/",
         "batchPath": "batch",
         "parameters": {
          "alt": {
           "type": "string",
           "description": "Data format for the response.",
           "default": "json",
           "enum": [
            "json"
           ],
           "enumDescriptions": [
            "Responses with Content-Type of application/json"
           ],
           "location": "query"
          },
          "fields": {
           "type": "string",
           "description": "Selector specifying which fields to include in a partial response.",
           "location": "query"
          },
          "key": {
           "type": "string",
           "description": "API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.",
           "location": "query"
          },
          "oauth_token": {
           "type": "string",
           "description": "OAuth 2.0 token for the current user.",
           "location": "query"
          },
          "prettyPrint": {
           "type": "boolean",
           "description": "Returns response with indentations and line breaks.",
           "default": "true",
           "location": "query"
          },
          "quotaUser": {
           "type": "string",
           "description": "Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. Overrides userIp if both are provided.",
           "location": "query"
          },
          "userIp": {
           "type": "string",
           "description": "IP address of the site where the request originates. Use this if you want to enforce per-user limits.",
           "location": "query"
          }
         },
         "auth": {
          "oauth2": {
           "scopes": {
            "https://localhost:5000/auth/compute": {
             "description": "View and manage your Google Compute Engine resources"
            },
            "https://localhost:5000/auth/compute.readonly": {
             "description": "View your Google Compute Engine resources"
            },
            "https://localhost:5000/auth/devstorage.full_control": {
             "description": "Manage your data and permissions in Google Cloud Storage"
            },
            "https://localhost:5000/auth/devstorage.read_only": {
             "description": "View your data in Google Cloud Storage"
            },
            "https://localhost:5000/auth/devstorage.read_write": {
             "description": "Manage your data in Google Cloud Storage"
            }
           }
          }
         },
         "schemas": {
          "AccessConfig": {
           "id": "AccessConfig",
           "type": "object",
           "description": "An access configuration attached to an instance's network interface.",
           "properties": {
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#accessConfig"
            },
            "name": {
             "type": "string",
             "description": "Name of this access configuration."
            },
            "natIP": {
             "type": "string",
             "description": "An external IP address associated with this instance. Specify an unused static IP address available to the project. If not specified, the external IP will be drawn from a shared ephemeral pool."
            },
            "type": {
             "type": "string",
             "description": "Type of configuration. Must be set to \"ONE_TO_ONE_NAT\". This configures port-for-port NAT to the internet.",
             "default": "ONE_TO_ONE_NAT"
            }
           }
          },
          "Address": {
           "id": "Address",
           "type": "object",
           "description": "A reserved address resource.",
           "properties": {
            "address": {
             "type": "string",
             "description": "The IP address represented by this resource."
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#address"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.addresses.insert"
              ]
             }
            },
            "region": {
             "type": "string",
             "description": "URL of the region where the address resides (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "status": {
             "type": "string",
             "description": "The status of the address (output only)."
            },
            "user": {
             "type": "string",
             "description": "URL of the resource currently using this address (output only)."
            }
           }
          },
          "AddressAggregatedList": {
           "id": "AddressAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped address lists.",
             "additionalProperties": {
              "$ref": "AddressesScopedList",
              "description": "Name of the scope containing this set of addresses."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#addressAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "AddressList": {
           "id": "AddressList",
           "type": "object",
           "description": "Contains a list of address resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The address resources.",
             "items": {
              "$ref": "Address"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#addressList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "AddressesScopedList": {
           "id": "AddressesScopedList",
           "type": "object",
           "properties": {
            "addresses": {
             "type": "array",
             "description": "List of addresses contained in this scope.",
             "items": {
              "$ref": "Address"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of addresses when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "AttachedDisk": {
           "id": "AttachedDisk",
           "type": "object",
           "description": "An instance-attached disk resource.",
           "properties": {
            "boot": {
             "type": "boolean",
             "description": "Indicates that this is a boot disk. VM will use the first partition of the disk for its root filesystem."
            },
            "deviceName": {
             "type": "string",
             "description": "Persistent disk only; must be unique within the instance when specified. This represents a unique device name that is reflected into the /dev/ tree of a Linux operating system running within the instance. If not specified, a default will be chosen by the system."
            },
            "index": {
             "type": "integer",
             "description": "A zero-based index to assign to this disk, where 0 is reserved for the boot disk. If not specified, the server will choose an appropriate value (output only).",
             "format": "int32"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#attachedDisk"
            },
            "mode": {
             "type": "string",
             "description": "The mode in which to attach this disk, either \"READ_WRITE\" or \"READ_ONLY\"."
            },
            "source": {
             "type": "string",
             "description": "Persistent disk only; the URL of the persistent disk resource."
            },
            "type": {
             "type": "string",
             "description": "Type of the disk, either \"SCRATCH\" or \"PERSISTENT\". Note that persistent disks must be created before you can specify them here.",
             "annotations": {
              "required": [
               "compute.instances.insert"
              ]
             }
            }
           }
          },
          "DeprecationStatus": {
           "id": "DeprecationStatus",
           "type": "object",
           "description": "Deprecation status for a public resource.",
           "properties": {
            "deleted": {
             "type": "string",
             "description": "An optional RFC3339 timestamp on or after which the deprecation state of this resource will be changed to DELETED."
            },
            "deprecated": {
             "type": "string",
             "description": "An optional RFC3339 timestamp on or after which the deprecation state of this resource will be changed to DEPRECATED."
            },
            "obsolete": {
             "type": "string",
             "description": "An optional RFC3339 timestamp on or after which the deprecation state of this resource will be changed to OBSOLETE."
            },
            "replacement": {
             "type": "string",
             "description": "A URL of the suggested replacement for the deprecated resource. The deprecated resource and its replacement must be resources of the same kind."
            },
            "state": {
             "type": "string",
             "description": "The deprecation state. Can be \"DEPRECATED\", \"OBSOLETE\", or \"DELETED\". Operations which create a new resource using a \"DEPRECATED\" resource will return successfully, but with a warning indicating the deprecated resource and recommending its replacement. New uses of \"OBSOLETE\" or \"DELETED\" resources will result in an error."
            }
           }
          },
          "Disk": {
           "id": "Disk",
           "type": "object",
           "description": "A persistent disk resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#disk"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.disks.insert"
              ]
             }
            },
            "options": {
             "type": "string",
             "description": "Internal use only."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "sizeGb": {
             "type": "string",
             "description": "Size of the persistent disk, specified in GB. This parameter is optional when creating a disk from a disk image or a snapshot, otherwise it is required.",
             "format": "int64"
            },
            "sourceSnapshot": {
             "type": "string",
             "description": "The source snapshot used to create this disk. Once the source snapshot has been deleted from the system, this field will be cleared, and will not be set even if a snapshot with the same name has been re-created."
            },
            "sourceSnapshotId": {
             "type": "string",
             "description": "The 'id' value of the snapshot used to create this disk. This value may be used to determine whether the disk was created from the current or a previous instance of a given disk snapshot."
            },
            "status": {
             "type": "string",
             "description": "The status of disk creation (output only)."
            },
            "zone": {
             "type": "string",
             "description": "URL of the zone where the disk resides (output only)."
            }
           }
          },
          "DiskAggregatedList": {
           "id": "DiskAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped disk lists.",
             "additionalProperties": {
              "$ref": "DisksScopedList",
              "description": "Name of the scope containing this set of disks."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#diskAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "DiskList": {
           "id": "DiskList",
           "type": "object",
           "description": "Contains a list of persistent disk resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The persistent disk resources.",
             "items": {
              "$ref": "Disk"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#diskList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "DisksScopedList": {
           "id": "DisksScopedList",
           "type": "object",
           "properties": {
            "disks": {
             "type": "array",
             "description": "List of disks contained in this scope.",
             "items": {
              "$ref": "Disk"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of disks when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "Firewall": {
           "id": "Firewall",
           "type": "object",
           "description": "A firewall resource.",
           "properties": {
            "allowed": {
             "type": "array",
             "description": "The list of rules specified by this firewall. Each rule specifies a protocol and port-range tuple that describes a permitted connection.",
             "items": {
              "type": "object",
              "properties": {
               "IPProtocol": {
                "type": "string",
                "description": "Required; this is the IP protocol that is allowed for this rule. This can either be a well known protocol string (tcp, udp or icmp) or the IP protocol number."
               },
               "ports": {
                "type": "array",
                "description": "An optional list of ports which are allowed. It is an error to specify this for any protocol that isn't UDP or TCP. Each entry must be either an integer or a range. If not specified, connections through any port are allowed.\n\nExample inputs include: [\"22\"], [\"80\",\"443\"] and [\"12345-12349\"].",
                "items": {
                 "type": "string"
                }
               }
              }
             }
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#firewall"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.firewalls.insert",
               "compute.firewalls.patch"
              ]
             }
            },
            "network": {
             "type": "string",
             "description": "URL of the network to which this firewall is applied; provided by the client when the firewall is created.",
             "annotations": {
              "required": [
               "compute.firewalls.insert",
               "compute.firewalls.patch"
              ]
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "sourceRanges": {
             "type": "array",
             "description": "A list of IP address blocks expressed in CIDR format which this rule applies to. One or both of sourceRanges and sourceTags may be set; an inbound connection is allowed if either the range or the tag of the source matches.",
             "items": {
              "type": "string"
             }
            },
            "sourceTags": {
             "type": "array",
             "description": "A list of instance tags which this rule applies to. One or both of sourceRanges and sourceTags may be set; an inbound connection is allowed if either the range or the tag of the source matches.",
             "items": {
              "type": "string"
             }
            },
            "targetTags": {
             "type": "array",
             "description": "A list of instance tags indicating sets of instances located on network which may make network connections as specified in allowed. If no targetTags are specified, the firewall rule applies to all instances on the specified network.",
             "items": {
              "type": "string"
             }
            }
           }
          },
          "FirewallList": {
           "id": "FirewallList",
           "type": "object",
           "description": "Contains a list of firewall resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The firewall resources.",
             "items": {
              "$ref": "Firewall"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#firewallList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "ForwardingRule": {
           "id": "ForwardingRule",
           "type": "object",
           "description": "A ForwardingRule resource. A ForwardingRule resource specifies which pool of target VMs to forward a packet to if it matches the given [IPAddress, IPProtocol, portRange] tuple.",
           "properties": {
            "IPAddress": {
             "type": "string",
             "description": "Value of the reserved IP address that this forwarding rule is serving on behalf of. The address resource must live in the same region as the forwarding rule. If left empty (default value), an ephemeral IP will be assigned."
            },
            "IPProtocol": {
             "type": "string",
             "description": "The IP protocol to which this rule applies, can be either 'TCP' or 'UDP' (If left empty, will use TCP by default)."
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#forwardingRule"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?"
            },
            "portRange": {
             "type": "string",
             "description": "If 'IPProtocol' is 'TCP' or 'UDP', only packets addressed to ports in the specified range will be forwarded to 'target'. If left empty (default value), all ports are forwarded. Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint port ranges."
            },
            "region": {
             "type": "string",
             "description": "URL of the region where the forwarding rule resides (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "target": {
             "type": "string",
             "description": "The URL of the target resource to receive the matched traffic. It must live in the same region as this forwarding rule."
            }
           }
          },
          "ForwardingRuleAggregatedList": {
           "id": "ForwardingRuleAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped forwarding rule lists.",
             "additionalProperties": {
              "$ref": "ForwardingRulesScopedList",
              "description": "Name of the scope containing this set of addresses."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#forwardingRuleAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "ForwardingRuleList": {
           "id": "ForwardingRuleList",
           "type": "object",
           "description": "Contains a list of ForwardingRule resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The ForwardingRule resources.",
             "items": {
              "$ref": "ForwardingRule"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#forwardingRuleList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "ForwardingRulesScopedList": {
           "id": "ForwardingRulesScopedList",
           "type": "object",
           "properties": {
            "forwardingRules": {
             "type": "array",
             "description": "List of forwarding rules contained in this scope.",
             "items": {
              "$ref": "ForwardingRule"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of forwarding rules when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "HealthCheckReference": {
           "id": "HealthCheckReference",
           "type": "object",
           "properties": {
            "healthCheck": {
             "type": "string"
            }
           }
          },
          "HealthStatus": {
           "id": "HealthStatus",
           "type": "object",
           "properties": {
            "healthState": {
             "type": "string",
             "description": "Health state of the instance."
            },
            "instance": {
             "type": "string",
             "description": "URL of the instance resource."
            },
            "ipAddress": {
             "type": "string",
             "description": "The IP address represented by this resource."
            }
           }
          },
          "HttpHealthCheck": {
           "id": "HttpHealthCheck",
           "type": "object",
           "description": "An HttpHealthCheck resource. This resource defines a template for how individual VMs should be checked for health, via HTTP.",
           "properties": {
            "checkIntervalSec": {
             "type": "integer",
             "description": "How often (in seconds) to send a health check. The default value is 5 seconds.",
             "format": "int32"
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "healthyThreshold": {
             "type": "integer",
             "description": "A so-far unhealthy VM will be marked healthy after this many consecutive successes. The default value is 2.",
             "format": "int32"
            },
            "host": {
             "type": "string",
             "description": "The value of the host header in the HTTP health check request. If left empty (default value), the public IP on behalf of which this health check is performed will be used."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#httpHealthCheck"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?"
            },
            "port": {
             "type": "integer",
             "description": "The TCP port number for the HTTP health check request. The default value is 80.",
             "format": "int32"
            },
            "requestPath": {
             "type": "string",
             "description": "The request path of the HTTP health check request. The default value is \"/\"."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "timeoutSec": {
             "type": "integer",
             "description": "How long (in seconds) to wait before claiming failure. The default value is 5 seconds.",
             "format": "int32"
            },
            "unhealthyThreshold": {
             "type": "integer",
             "description": "A so-far healthy VM will be marked unhealthy after this many consecutive failures. The default value is 2.",
             "format": "int32"
            }
           }
          },
          "HttpHealthCheckList": {
           "id": "HttpHealthCheckList",
           "type": "object",
           "description": "Contains a list of HttpHealthCheck resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The HttpHealthCheck resources.",
             "items": {
              "$ref": "HttpHealthCheck"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#httpHealthCheckList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "Image": {
           "id": "Image",
           "type": "object",
           "description": "A disk image resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "deprecated": {
             "$ref": "DeprecationStatus",
             "description": "The deprecation status associated with this image."
            },
            "description": {
             "type": "string",
             "description": "Textual description of the resource; provided by the client when the resource is created."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#image"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.images.insert"
              ]
             }
            },
            "preferredKernel": {
             "type": "string",
             "description": "An optional URL of the preferred kernel for use with this disk image. If not specified, a server defined default kernel will be used.",
             "annotations": {
              "required": [
               "compute.images.insert"
              ]
             }
            },
            "rawDisk": {
             "type": "object",
             "description": "The raw disk image parameters.",
             "properties": {
              "containerType": {
               "type": "string",
               "description": "The format used to encode and transmit the block device. Should be TAR. This is just a container and transmission format and not a runtime format. Provided by the client when the disk image is created.",
               "default": "TAR"
              },
              "sha1Checksum": {
               "type": "string",
               "description": "An optional SHA1 checksum of the disk image before unpackaging; provided by the client when the disk image is created.",
               "pattern": "[a-f0-9]{40}"
              },
              "source": {
               "type": "string",
               "description": "The full Google Cloud Storage URL where the disk image is stored; provided by the client when the disk image is created.",
               "annotations": {
                "required": [
                 "compute.images.insert"
                ]
               }
              }
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "sourceType": {
             "type": "string",
             "description": "Must be \"RAW\"; provided by the client when the disk image is created.",
             "default": "RAW",
             "annotations": {
              "required": [
               "compute.images.insert"
              ]
             }
            },
            "status": {
             "type": "string",
             "description": "Status of the image (output only). It will be one of the following READY - after image has been successfully created and is ready for use FAILED - if creating the image fails for some reason PENDING - the image creation is in progress An image can be used to create other resources suck as instances only after the image has been successfully created and the status is set to READY."
            }
           }
          },
          "ImageList": {
           "id": "ImageList",
           "type": "object",
           "description": "Contains a list of disk image resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The disk image resources.",
             "items": {
              "$ref": "Image"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#imageList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "Instance": {
           "id": "Instance",
           "type": "object",
           "description": "An instance resource.",
           "properties": {
            "canIpForward": {
             "type": "boolean",
             "description": "Allows this instance to send packets with source IP addresses other than its own and receive packets with destination IP addresses other than its own. If this instance will be used as an IP gateway or it will be set as the next-hop in a Route resource, say true. If unsure, leave this set to false."
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "disks": {
             "type": "array",
             "description": "Array of disks associated with this instance. Persistent disks must be created before you can assign them.",
             "items": {
              "$ref": "AttachedDisk"
             }
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "image": {
             "type": "string",
             "description": "An optional URL of the disk image resource to be installed on this instance; provided by the client when the instance is created. Alternatively to passing the image, the client may choose to boot from a persistent disk, by setting boot=true flag on one of the entries in disks[] collection."
            },
            "kernel": {
             "type": "string",
             "description": "URL of the kernel resource to use when booting. In case of booting from persistent disk, this parameter is required. When booting from a disk image, it is optional, but may be provided to use a different kernel than the one associated with the image."
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#instance"
            },
            "machineType": {
             "type": "string",
             "description": "URL of the machine type resource describing which machine type to use to host the instance; provided by the client when the instance is created.",
             "annotations": {
              "required": [
               "compute.instances.insert"
              ]
             }
            },
            "metadata": {
             "$ref": "Metadata",
             "description": "Metadata key/value pairs assigned to this instance. Consists of custom metadata or predefined keys; see Instance documentation for more information."
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.instances.insert"
              ]
             }
            },
            "networkInterfaces": {
             "type": "array",
             "description": "Array of configurations for this interface. This specifies how this interface is configured to interact with other network services, such as connecting to the internet. Currently, ONE_TO_ONE_NAT is the only access config supported. If there are no accessConfigs specified, then this instance will have no external internet access.",
             "items": {
              "$ref": "NetworkInterface"
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            },
            "serviceAccounts": {
             "type": "array",
             "description": "A list of service accounts each with specified scopes, for which access tokens are to be made available to the instance through metadata queries.",
             "items": {
              "$ref": "ServiceAccount"
             }
            },
            "status": {
             "type": "string",
             "description": "Instance status. One of the following values: \"PROVISIONING\", \"STAGING\", \"RUNNING\", \"STOPPING\", \"STOPPED\", \"TERMINATED\" (output only)."
            },
            "statusMessage": {
             "type": "string",
             "description": "An optional, human-readable explanation of the status (output only)."
            },
            "tags": {
             "$ref": "Tags",
             "description": "A list of tags to be applied to this instance. Used to identify valid sources or targets for network firewalls. Provided by the client on instance creation. The tags can be later modified by the setTags method. Each tag within the list must comply with RFC1035."
            },
            "zone": {
             "type": "string",
             "description": "URL of the zone where the instance resides (output only)."
            }
           }
          },
          "InstanceAggregatedList": {
           "id": "InstanceAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped instance lists.",
             "additionalProperties": {
              "$ref": "InstancesScopedList",
              "description": "Name of the scope containing this set of instances."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#instanceAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "InstanceList": {
           "id": "InstanceList",
           "type": "object",
           "description": "Contains a list of instance resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "A list of instance resources.",
             "items": {
              "$ref": "Instance"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#instanceList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "InstanceReference": {
           "id": "InstanceReference",
           "type": "object",
           "properties": {
            "instance": {
             "type": "string"
            }
           }
          },
          "InstancesScopedList": {
           "id": "InstancesScopedList",
           "type": "object",
           "properties": {
            "instances": {
             "type": "array",
             "description": "List of instances contained in this scope.",
             "items": {
              "$ref": "Instance"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of instances when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "Kernel": {
           "id": "Kernel",
           "type": "object",
           "description": "A kernel resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "deprecated": {
             "$ref": "DeprecationStatus",
             "description": "The deprecation status associated with this kernel."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#kernel"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?"
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            }
           }
          },
          "KernelList": {
           "id": "KernelList",
           "type": "object",
           "description": "Contains a list of kernel resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The kernel resources.",
             "items": {
              "$ref": "Kernel"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#kernelList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "MachineType": {
           "id": "MachineType",
           "type": "object",
           "description": "A machine type resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "deprecated": {
             "$ref": "DeprecationStatus",
             "description": "The deprecation status associated with this machine type."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource."
            },
            "guestCpus": {
             "type": "integer",
             "description": "Count of CPUs exposed to the instance.",
             "format": "int32"
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "imageSpaceGb": {
             "type": "integer",
             "description": "Space allotted for the image, defined in GB.",
             "format": "int32"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#machineType"
            },
            "maximumPersistentDisks": {
             "type": "integer",
             "description": "Maximum persistent disks allowed.",
             "format": "int32"
            },
            "maximumPersistentDisksSizeGb": {
             "type": "string",
             "description": "Maximum total persistent disks size (GB) allowed.",
             "format": "int64"
            },
            "memoryMb": {
             "type": "integer",
             "description": "Physical memory assigned to the instance, defined in MB.",
             "format": "int32"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?"
            },
            "scratchDisks": {
             "type": "array",
             "description": "List of extended scratch disks assigned to the instance.",
             "items": {
              "type": "object",
              "properties": {
               "diskGb": {
                "type": "integer",
                "description": "Size of the scratch disk, defined in GB.",
                "format": "int32"
               }
              }
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "zone": {
             "type": "string",
             "description": "Url of the zone where the machine type resides (output only)."
            }
           }
          },
          "MachineTypeAggregatedList": {
           "id": "MachineTypeAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped machine type lists.",
             "additionalProperties": {
              "$ref": "MachineTypesScopedList",
              "description": "Name of the scope containing this set of machine types."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#machineTypeAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "MachineTypeList": {
           "id": "MachineTypeList",
           "type": "object",
           "description": "Contains a list of machine type resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The machine type resources.",
             "items": {
              "$ref": "MachineType"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#machineTypeList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "MachineTypesScopedList": {
           "id": "MachineTypesScopedList",
           "type": "object",
           "properties": {
            "machineTypes": {
             "type": "array",
             "description": "List of machine types contained in this scope.",
             "items": {
              "$ref": "MachineType"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of machine types when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "Metadata": {
           "id": "Metadata",
           "type": "object",
           "description": "A metadata key/value entry.",
           "properties": {
            "fingerprint": {
             "type": "string",
             "description": "Fingerprint of this resource. A hash of the metadata's contents. This field is used for optimistic locking. An up-to-date metadata fingerprint must be provided in order to modify metadata.",
             "format": "byte"
            },
            "items": {
             "type": "array",
             "description": "Array of key/value pairs. The total size of all keys and values must be less than 512 KB.",
             "items": {
              "type": "object",
              "properties": {
               "key": {
                "type": "string",
                "description": "Key for the metadata entry. Keys must conform to the following regexp: [a-zA-Z0-9-_]+, and be less than 128 bytes in length. This is reflected as part of a URL in the metadata server. Additionally, to avoid ambiguity, keys must not conflict with any other metadata keys for the project.",
                "pattern": "[a-zA-Z0-9-_]{1,128}",
                "annotations": {
                 "required": [
                  "compute.instances.insert",
                  "compute.projects.setCommonInstanceMetadata"
                 ]
                }
               },
               "value": {
                "type": "string",
                "description": "Value for the metadata entry. These are free-form strings, and only have meaning as interpreted by the image running in the instance. The only restriction placed on values is that their size must be less than or equal to 32768 bytes.",
                "annotations": {
                 "required": [
                  "compute.instances.insert",
                  "compute.projects.setCommonInstanceMetadata"
                 ]
                }
               }
              }
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#metadata"
            }
           }
          },
          "Network": {
           "id": "Network",
           "type": "object",
           "description": "A network resource.",
           "properties": {
            "IPv4Range": {
             "type": "string",
             "description": "Required; The range of internal addresses that are legal on this network. This range is a CIDR specification, for example: 192.168.0.0/16. Provided by the client when the network is created.",
             "pattern": "[0-9]{1,3}(?:\\.[0-9]{1,3}){3}/[0-9]{1,2}",
             "annotations": {
              "required": [
               "compute.networks.insert"
              ]
             }
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "gatewayIPv4": {
             "type": "string",
             "description": "An optional address that is used for default routing to other networks. This must be within the range specified by IPv4Range, and is typically the first usable address in that range. If not specified, the default value is the first usable address in IPv4Range.",
             "pattern": "[0-9]{1,3}(?:\\.[0-9]{1,3}){3}"
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#network"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.networks.insert"
              ]
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            }
           }
          },
          "NetworkInterface": {
           "id": "NetworkInterface",
           "type": "object",
           "description": "A network interface resource attached to an instance.",
           "properties": {
            "accessConfigs": {
             "type": "array",
             "description": "Array of configurations for this interface. This specifies how this interface is configured to interact with other network services, such as connecting to the internet. Currently, ONE_TO_ONE_NAT is the only access config supported. If there are no accessConfigs specified, then this instance will have no external internet access.",
             "items": {
              "$ref": "AccessConfig"
             }
            },
            "name": {
             "type": "string",
             "description": "Name of the network interface, determined by the server; for network devices, these are e.g. eth0, eth1, etc. (output only)."
            },
            "network": {
             "type": "string",
             "description": "URL of the network resource attached to this interface.",
             "annotations": {
              "required": [
               "compute.instances.insert"
              ]
             }
            },
            "networkIP": {
             "type": "string",
             "description": "An optional IPV4 internal network address assigned to the instance for this network interface (output only)."
            }
           }
          },
          "NetworkList": {
           "id": "NetworkList",
           "type": "object",
           "description": "Contains a list of network resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The network resources.",
             "items": {
              "$ref": "Network"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#networkList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "Operation": {
           "id": "Operation",
           "type": "object",
           "description": "An operation resource, used to manage asynchronous API requests.",
           "properties": {
            "clientOperationId": {
             "type": "string",
             "description": "An optional identifier specified by the client when the mutation was initiated. Must be unique for all operation resources in the project (output only)."
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "endTime": {
             "type": "string",
             "description": "The time that this operation was completed. This is in RFC 3339 format (output only)."
            },
            "error": {
             "type": "object",
             "description": "If errors occurred during processing of this operation, this field will be populated (output only).",
             "properties": {
              "errors": {
               "type": "array",
               "description": "The array of errors encountered while processing this operation.",
               "items": {
                "type": "object",
                "properties": {
                 "code": {
                  "type": "string",
                  "description": "The error type identifier for this error."
                 },
                 "location": {
                  "type": "string",
                  "description": "Indicates the field in the request which caused the error. This property is optional."
                 },
                 "message": {
                  "type": "string",
                  "description": "An optional, human-readable error message."
                 }
                }
               }
              }
             }
            },
            "httpErrorMessage": {
             "type": "string",
             "description": "If operation fails, the HTTP error message returned, e.g. NOT FOUND. (output only)."
            },
            "httpErrorStatusCode": {
             "type": "integer",
             "description": "If operation fails, the HTTP error status code returned, e.g. 404. (output only).",
             "format": "int32"
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "insertTime": {
             "type": "string",
             "description": "The time that this operation was requested. This is in RFC 3339 format (output only)."
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#operation"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource (output only)."
            },
            "operationType": {
             "type": "string",
             "description": "Type of the operation. Examples include \"insert\", \"update\", and \"delete\" (output only)."
            },
            "progress": {
             "type": "integer",
             "description": "An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess at when the operation will be complete. This number should be monotonically increasing as the operation progresses (output only).",
             "format": "int32"
            },
            "region": {
             "type": "string",
             "description": "URL of the region where the operation resides (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "startTime": {
             "type": "string",
             "description": "The time that this operation was started by the server. This is in RFC 3339 format (output only)."
            },
            "status": {
             "type": "string",
             "description": "Status of the operation. Can be one of the following: \"PENDING\", \"RUNNING\", or \"DONE\" (output only)."
            },
            "statusMessage": {
             "type": "string",
             "description": "An optional textual description of the current status of the operation (output only)."
            },
            "targetId": {
             "type": "string",
             "description": "Unique target id which identifies a particular incarnation of the target (output only).",
             "format": "uint64"
            },
            "targetLink": {
             "type": "string",
             "description": "URL of the resource the operation is mutating (output only)."
            },
            "user": {
             "type": "string",
             "description": "User who requested the operation, for example \"user@example.com\" (output only)."
            },
            "warnings": {
             "type": "array",
             "description": "If warning messages generated during processing of this operation, this field will be populated (output only).",
             "items": {
              "type": "object",
              "properties": {
               "code": {
                "type": "string",
                "description": "The warning type identifier for this warning."
               },
               "data": {
                "type": "array",
                "description": "Metadata for this warning in 'key: value' format.",
                "items": {
                 "type": "object",
                 "properties": {
                  "key": {
                   "type": "string",
                   "description": "A key for the warning data."
                  },
                  "value": {
                   "type": "string",
                   "description": "A warning data value corresponding to the key."
                  }
                 }
                }
               },
               "message": {
                "type": "string",
                "description": "Optional human-readable details for this warning."
               }
              }
             }
            },
            "zone": {
             "type": "string",
             "description": "URL of the zone where the operation resides (output only)."
            }
           }
          },
          "OperationAggregatedList": {
           "id": "OperationAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped operation lists.",
             "additionalProperties": {
              "$ref": "OperationsScopedList",
              "description": "Name of the scope containing this set of operations."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#operationAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "OperationList": {
           "id": "OperationList",
           "type": "object",
           "description": "Contains a list of operation resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The operation resources.",
             "items": {
              "$ref": "Operation"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#operationList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "OperationsScopedList": {
           "id": "OperationsScopedList",
           "type": "object",
           "properties": {
            "operations": {
             "type": "array",
             "description": "List of operations contained in this scope.",
             "items": {
              "$ref": "Operation"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of operations when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "Project": {
           "id": "Project",
           "type": "object",
           "description": "A project resource. Projects can be created only in the APIs Console. Unless marked otherwise, values can only be modified in the console.",
           "properties": {
            "commonInstanceMetadata": {
             "$ref": "Metadata",
             "description": "Metadata key/value pairs available to all instances contained in this project."
            },
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#project"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource."
            },
            "quotas": {
             "type": "array",
             "description": "Quotas assigned to this project.",
             "items": {
              "$ref": "Quota"
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            }
           }
          },
          "Quota": {
           "id": "Quota",
           "type": "object",
           "description": "A quotas entry.",
           "properties": {
            "limit": {
             "type": "number",
             "description": "Quota limit for this metric.",
             "format": "double"
            },
            "metric": {
             "type": "string",
             "description": "Name of the quota metric."
            },
            "usage": {
             "type": "number",
             "description": "Current usage of this metric.",
             "format": "double"
            }
           }
          },
          "Region": {
           "id": "Region",
           "type": "object",
           "description": "Region resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "deprecated": {
             "$ref": "DeprecationStatus",
             "description": "The deprecation status associated with this region."
            },
            "description": {
             "type": "string",
             "description": "Textual description of the resource."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#region"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource."
            },
            "quotas": {
             "type": "array",
             "description": "Quotas assigned to this region.",
             "items": {
              "$ref": "Quota"
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "status": {
             "type": "string",
             "description": "Status of the region, \"UP\" or \"DOWN\"."
            },
            "zones": {
             "type": "array",
             "description": "A list of zones homed in this region, in the form of resource URLs.",
             "items": {
              "type": "string"
             }
            }
           }
          },
          "RegionList": {
           "id": "RegionList",
           "type": "object",
           "description": "Contains a list of region resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The region resources.",
             "items": {
              "$ref": "Region"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#regionList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "Route": {
           "id": "Route",
           "type": "object",
           "description": "The route resource. A Route is a rule that specifies how certain packets should be handled by the virtual network. Routes are associated with VMs by tag and the set of Routes for a particular VM is called its routing table. For each packet leaving a VM, the system searches that VM's routing table for a single best matching Route. Routes match packets by destination IP address, preferring smaller or more specific ranges over larger ones. If there is a tie, the system selects the Route with the smallest priority value. If there is still a tie, it uses the layer three and four packet headers to select just one of the remaining matching Routes. The packet is then forwarded as specified by the next_hop field of the winning Route -- either to another VM destination, a VM gateway or a GCE operated gateway. Packets that do not match any Route in the sending VM's routing table will be dropped.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "destRange": {
             "type": "string",
             "description": "Which packets does this route apply to?",
             "annotations": {
              "required": [
               "compute.routes.insert"
              ]
             }
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#route"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
             "annotations": {
              "required": [
               "compute.routes.insert"
              ]
             }
            },
            "network": {
             "type": "string",
             "description": "URL of the network to which this route is applied; provided by the client when the route is created.",
             "annotations": {
              "required": [
               "compute.routes.insert"
              ]
             }
            },
            "nextHopGateway": {
             "type": "string",
             "description": "The URL to a gateway that should handle matching packets."
            },
            "nextHopInstance": {
             "type": "string",
             "description": "The URL to an instance that should handle matching packets."
            },
            "nextHopIp": {
             "type": "string",
             "description": "The network IP address of an instance that should handle matching packets."
            },
            "nextHopNetwork": {
             "type": "string",
             "description": "The URL of the local network if it should handle matching packets."
            },
            "priority": {
             "type": "integer",
             "description": "Breaks ties between Routes of equal specificity. Routes with smaller values win when tied with routes with larger values.",
             "format": "uint32",
             "annotations": {
              "required": [
               "compute.routes.insert"
              ]
             }
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "tags": {
             "type": "array",
             "description": "A list of instance tags to which this route applies.",
             "items": {
              "type": "string"
             },
             "annotations": {
              "required": [
               "compute.routes.insert"
              ]
             }
            },
            "warnings": {
             "type": "array",
             "description": "If potential misconfigurations are detected for this route, this field will be populated with warning messages.",
             "items": {
              "type": "object",
              "properties": {
               "code": {
                "type": "string",
                "description": "The warning type identifier for this warning."
               },
               "data": {
                "type": "array",
                "description": "Metadata for this warning in 'key: value' format.",
                "items": {
                 "type": "object",
                 "properties": {
                  "key": {
                   "type": "string",
                   "description": "A key for the warning data."
                  },
                  "value": {
                   "type": "string",
                   "description": "A warning data value corresponding to the key."
                  }
                 }
                }
               },
               "message": {
                "type": "string",
                "description": "Optional human-readable details for this warning."
               }
              }
             }
            }
           }
          },
          "RouteList": {
           "id": "RouteList",
           "type": "object",
           "description": "Contains a list of route resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The route resources.",
             "items": {
              "$ref": "Route"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#routeList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "SerialPortOutput": {
           "id": "SerialPortOutput",
           "type": "object",
           "description": "An instance serial console output.",
           "properties": {
            "contents": {
             "type": "string",
             "description": "The contents of the console output."
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#serialPortOutput"
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            }
           }
          },
          "ServiceAccount": {
           "id": "ServiceAccount",
           "type": "object",
           "description": "A service account.",
           "properties": {
            "email": {
             "type": "string",
             "description": "Email address of the service account."
            },
            "scopes": {
             "type": "array",
             "description": "The list of scopes to be made available for this service account.",
             "items": {
              "type": "string"
             }
            }
           }
          },
          "Snapshot": {
           "id": "Snapshot",
           "type": "object",
           "description": "A persistent disk snapshot resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "diskSizeGb": {
             "type": "string",
             "description": "Size of the persistent disk snapshot, specified in GB (output only).",
             "format": "int64"
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#snapshot"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?"
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "sourceDisk": {
             "type": "string",
             "description": "The source disk used to create this snapshot. Once the source disk has been deleted from the system, this field will be cleared, and will not be set even if a disk with the same name has been re-created (output only)."
            },
            "sourceDiskId": {
             "type": "string",
             "description": "The 'id' value of the disk used to create this snapshot. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given disk name."
            },
            "status": {
             "type": "string",
             "description": "The status of the persistent disk snapshot (output only)."
            }
           }
          },
          "SnapshotList": {
           "id": "SnapshotList",
           "type": "object",
           "description": "Contains a list of persistent disk snapshot resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The persistent snapshot resources.",
             "items": {
              "$ref": "Snapshot"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#snapshotList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "Tags": {
           "id": "Tags",
           "type": "object",
           "description": "A set of instance tags.",
           "properties": {
            "fingerprint": {
             "type": "string",
             "description": "Fingerprint of this resource. A hash of the tags stored in this object. This field is used optimistic locking. An up-to-date tags fingerprint must be provided in order to modify tags.",
             "format": "byte"
            },
            "items": {
             "type": "array",
             "description": "An array of tags. Each tag must be 1-63 characters long, and comply with RFC1035.",
             "items": {
              "type": "string"
             }
            }
           }
          },
          "TargetPool": {
           "id": "TargetPool",
           "type": "object",
           "description": "A TargetPool resource. This resource defines a pool of VMs, associated HttpHealthCheck resources, and the fallback TargetPool.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "description": {
             "type": "string",
             "description": "An optional textual description of the resource; provided by the client when the resource is created."
            },
            "healthChecks": {
             "type": "array",
             "description": "A list of URLs to the HttpHealthCheck resource. A member VM in this pool is considered healthy if and only if all specified health checks pass. An empty list means all member VMs will be considered healthy at all times.",
             "items": {
              "type": "string"
             }
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "instances": {
             "type": "array",
             "description": "A list of resource URLs to the member VMs serving this pool. They must live in zones contained in the same region as this pool.",
             "items": {
              "type": "string"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#targetPool"
            },
            "name": {
             "type": "string",
             "description": "Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035.",
             "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?"
            },
            "region": {
             "type": "string",
             "description": "URL of the region where the target pool resides (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            }
           }
          },
          "TargetPoolAggregatedList": {
           "id": "TargetPoolAggregatedList",
           "type": "object",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "object",
             "description": "A map of scoped target pool lists.",
             "additionalProperties": {
              "$ref": "TargetPoolsScopedList",
              "description": "Name of the scope containing this set of target pools."
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#targetPoolAggregatedList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "TargetPoolInstanceHealth": {
           "id": "TargetPoolInstanceHealth",
           "type": "object",
           "properties": {
            "healthStatus": {
             "type": "array",
             "items": {
              "$ref": "HealthStatus"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#targetPoolInstanceHealth"
            }
           }
          },
          "TargetPoolList": {
           "id": "TargetPoolList",
           "type": "object",
           "description": "Contains a list of TargetPool resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The TargetPool resources.",
             "items": {
              "$ref": "TargetPool"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#targetPoolList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          },
          "TargetPoolsScopedList": {
           "id": "TargetPoolsScopedList",
           "type": "object",
           "properties": {
            "targetPools": {
             "type": "array",
             "description": "List of target pools contained in this scope.",
             "items": {
              "$ref": "TargetPool"
             }
            },
            "warning": {
             "type": "object",
             "description": "Informational warning which replaces the list of addresses when the list is empty.",
             "properties": {
              "code": {
               "type": "string",
               "description": "The warning type identifier for this warning."
              },
              "data": {
               "type": "array",
               "description": "Metadata for this warning in 'key: value' format.",
               "items": {
                "type": "object",
                "properties": {
                 "key": {
                  "type": "string",
                  "description": "A key for the warning data."
                 },
                 "value": {
                  "type": "string",
                  "description": "A warning data value corresponding to the key."
                 }
                }
               }
              },
              "message": {
               "type": "string",
               "description": "Optional human-readable details for this warning."
              }
             }
            }
           }
          },
          "TargetReference": {
           "id": "TargetReference",
           "type": "object",
           "properties": {
            "target": {
             "type": "string"
            }
           }
          },
          "Zone": {
           "id": "Zone",
           "type": "object",
           "description": "A zone resource.",
           "properties": {
            "creationTimestamp": {
             "type": "string",
             "description": "Creation timestamp in RFC3339 text format (output only)."
            },
            "deprecated": {
             "$ref": "DeprecationStatus",
             "description": "The deprecation status associated with this zone."
            },
            "description": {
             "type": "string",
             "description": "Textual description of the resource."
            },
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only).",
             "format": "uint64"
            },
            "kind": {
             "type": "string",
             "description": "Type of the resource.",
             "default": "compute#zone"
            },
            "maintenanceWindows": {
             "type": "array",
             "description": "Scheduled maintenance windows for the zone. When the zone is in a maintenance window, all resources which reside in the zone will be unavailable.",
             "items": {
              "type": "object",
              "properties": {
               "beginTime": {
                "type": "string",
                "description": "Begin time of the maintenance window, in RFC 3339 format."
               },
               "description": {
                "type": "string",
                "description": "Textual description of the maintenance window."
               },
               "endTime": {
                "type": "string",
                "description": "End time of the maintenance window, in RFC 3339 format."
               },
               "name": {
                "type": "string",
                "description": "Name of the maintenance window."
               }
              }
             }
            },
            "name": {
             "type": "string",
             "description": "Name of the resource."
            },
            "quotas": {
             "type": "array",
             "description": "Quotas assigned to this zone.",
             "items": {
              "$ref": "Quota"
             }
            },
            "region": {
             "type": "string",
             "description": "Full URL reference to the region which hosts the zone (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for the resource (output only)."
            },
            "status": {
             "type": "string",
             "description": "Status of the zone. \"UP\" or \"DOWN\"."
            }
           }
          },
          "ZoneList": {
           "id": "ZoneList",
           "type": "object",
           "description": "Contains a list of zone resources.",
           "properties": {
            "id": {
             "type": "string",
             "description": "Unique identifier for the resource; defined by the server (output only)."
            },
            "items": {
             "type": "array",
             "description": "The zone resources.",
             "items": {
              "$ref": "Zone"
             }
            },
            "kind": {
             "type": "string",
             "description": "Type of resource.",
             "default": "compute#zoneList"
            },
            "nextPageToken": {
             "type": "string",
             "description": "A token used to continue a truncated list request (output only)."
            },
            "selfLink": {
             "type": "string",
             "description": "Server defined URL for this resource (output only)."
            }
           }
          }
         },
         "resources": {
          "addresses": {
           "methods": {
            "aggregatedList": {
             "id": "compute.addresses.aggregatedList",
             "path": "{project}/aggregated/addresses",
             "httpMethod": "GET",
             "description": "Retrieves the list of addresses grouped by scope.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "AddressAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "delete": {
             "id": "compute.addresses.delete",
             "path": "{project}/regions/{region}/addresses/{address}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified address resource.",
             "parameters": {
              "address": {
               "type": "string",
               "description": "Name of the address resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "address"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.addresses.get",
             "path": "{project}/regions/{region}/addresses/{address}",
             "httpMethod": "GET",
             "description": "Returns the specified address resource.",
             "parameters": {
              "address": {
               "type": "string",
               "description": "Name of the address resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "address"
             ],
             "response": {
              "$ref": "Address"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.addresses.insert",
             "path": "{project}/regions/{region}/addresses",
             "httpMethod": "POST",
             "description": "Creates an address resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "request": {
              "$ref": "Address"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.addresses.list",
             "path": "{project}/regions/{region}/addresses",
             "httpMethod": "GET",
             "description": "Retrieves the list of address resources contained within the specified region.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "response": {
              "$ref": "AddressList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "disks": {
           "methods": {
            "aggregatedList": {
             "id": "compute.disks.aggregatedList",
             "path": "{project}/aggregated/disks",
             "httpMethod": "GET",
             "description": "Retrieves the list of disks grouped by scope.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "DiskAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "createSnapshot": {
             "id": "compute.disks.createSnapshot",
             "path": "{project}/zones/{zone}/disks/{disk}/createSnapshot",
             "httpMethod": "POST",
             "parameters": {
              "disk": {
               "type": "string",
               "description": "Name of the persistent disk resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "disk"
             ],
             "request": {
              "$ref": "Snapshot"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "delete": {
             "id": "compute.disks.delete",
             "path": "{project}/zones/{zone}/disks/{disk}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified persistent disk resource.",
             "parameters": {
              "disk": {
               "type": "string",
               "description": "Name of the persistent disk resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "disk"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.disks.get",
             "path": "{project}/zones/{zone}/disks/{disk}",
             "httpMethod": "GET",
             "description": "Returns the specified persistent disk resource.",
             "parameters": {
              "disk": {
               "type": "string",
               "description": "Name of the persistent disk resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "disk"
             ],
             "response": {
              "$ref": "Disk"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.disks.insert",
             "path": "{project}/zones/{zone}/disks",
             "httpMethod": "POST",
             "description": "Creates a persistent disk resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "sourceImage": {
               "type": "string",
               "description": "Optional. Source image to restore onto a disk.",
               "location": "query"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "request": {
              "$ref": "Disk"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.disks.list",
             "path": "{project}/zones/{zone}/disks",
             "httpMethod": "GET",
             "description": "Retrieves the list of persistent disk resources contained within the specified zone.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "response": {
              "$ref": "DiskList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "firewalls": {
           "methods": {
            "delete": {
             "id": "compute.firewalls.delete",
             "path": "{project}/global/firewalls/{firewall}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified firewall resource.",
             "parameters": {
              "firewall": {
               "type": "string",
               "description": "Name of the firewall resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "firewall"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.firewalls.get",
             "path": "{project}/global/firewalls/{firewall}",
             "httpMethod": "GET",
             "description": "Returns the specified firewall resource.",
             "parameters": {
              "firewall": {
               "type": "string",
               "description": "Name of the firewall resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "firewall"
             ],
             "response": {
              "$ref": "Firewall"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.firewalls.insert",
             "path": "{project}/global/firewalls",
             "httpMethod": "POST",
             "description": "Creates a firewall resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "request": {
              "$ref": "Firewall"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.firewalls.list",
             "path": "{project}/global/firewalls",
             "httpMethod": "GET",
             "description": "Retrieves the list of firewall resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "FirewallList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "patch": {
             "id": "compute.firewalls.patch",
             "path": "{project}/global/firewalls/{firewall}",
             "httpMethod": "PATCH",
             "description": "Updates the specified firewall resource with the data included in the request. This method supports patch semantics.",
             "parameters": {
              "firewall": {
               "type": "string",
               "description": "Name of the firewall resource to update.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "firewall"
             ],
             "request": {
              "$ref": "Firewall"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "update": {
             "id": "compute.firewalls.update",
             "path": "{project}/global/firewalls/{firewall}",
             "httpMethod": "PUT",
             "description": "Updates the specified firewall resource with the data included in the request.",
             "parameters": {
              "firewall": {
               "type": "string",
               "description": "Name of the firewall resource to update.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "firewall"
             ],
             "request": {
              "$ref": "Firewall"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            }
           }
          },
          "forwardingRules": {
           "methods": {
            "aggregatedList": {
             "id": "compute.forwardingRules.aggregatedList",
             "path": "{project}/aggregated/forwardingRules",
             "httpMethod": "GET",
             "description": "Retrieves the list of forwarding rules grouped by scope.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "ForwardingRuleAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "delete": {
             "id": "compute.forwardingRules.delete",
             "path": "{project}/regions/{region}/forwardingRules/{forwardingRule}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified ForwardingRule resource.",
             "parameters": {
              "forwardingRule": {
               "type": "string",
               "description": "Name of the ForwardingRule resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "forwardingRule"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.forwardingRules.get",
             "path": "{project}/regions/{region}/forwardingRules/{forwardingRule}",
             "httpMethod": "GET",
             "description": "Returns the specified ForwardingRule resource.",
             "parameters": {
              "forwardingRule": {
               "type": "string",
               "description": "Name of the ForwardingRule resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "forwardingRule"
             ],
             "response": {
              "$ref": "ForwardingRule"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.forwardingRules.insert",
             "path": "{project}/regions/{region}/forwardingRules",
             "httpMethod": "POST",
             "description": "Creates a ForwardingRule resource in the specified project and region using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "request": {
              "$ref": "ForwardingRule"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.forwardingRules.list",
             "path": "{project}/regions/{region}/forwardingRules",
             "httpMethod": "GET",
             "description": "Retrieves the list of ForwardingRule resources available to the specified project and region.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "response": {
              "$ref": "ForwardingRuleList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "setTarget": {
             "id": "compute.forwardingRules.setTarget",
             "path": "{project}/regions/{region}/forwardingRules/{forwardingRule}/setTarget",
             "httpMethod": "POST",
             "description": "Changes target url for forwarding rule.",
             "parameters": {
              "forwardingRule": {
               "type": "string",
               "description": "Name of the ForwardingRule resource in which target is to be set.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "forwardingRule"
             ],
             "request": {
              "$ref": "TargetReference"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            }
           }
          },
          "globalOperations": {
           "methods": {
            "aggregatedList": {
             "id": "compute.globalOperations.aggregatedList",
             "path": "{project}/aggregated/operations",
             "httpMethod": "GET",
             "description": "Retrieves the list of all operations grouped by scope.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "OperationAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "delete": {
             "id": "compute.globalOperations.delete",
             "path": "{project}/global/operations/{operation}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified operation resource.",
             "parameters": {
              "operation": {
               "type": "string",
               "description": "Name of the operation resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "operation"
             ],
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.globalOperations.get",
             "path": "{project}/global/operations/{operation}",
             "httpMethod": "GET",
             "description": "Retrieves the specified operation resource.",
             "parameters": {
              "operation": {
               "type": "string",
               "description": "Name of the operation resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "operation"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.globalOperations.list",
             "path": "{project}/global/operations",
             "httpMethod": "GET",
             "description": "Retrieves the list of operation resources contained within the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "OperationList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "httpHealthChecks": {
           "methods": {
            "delete": {
             "id": "compute.httpHealthChecks.delete",
             "path": "{project}/global/httpHealthChecks/{httpHealthCheck}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified HttpHealthCheck resource.",
             "parameters": {
              "httpHealthCheck": {
               "type": "string",
               "description": "Name of the HttpHealthCheck resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "httpHealthCheck"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.httpHealthChecks.get",
             "path": "{project}/global/httpHealthChecks/{httpHealthCheck}",
             "httpMethod": "GET",
             "description": "Returns the specified HttpHealthCheck resource.",
             "parameters": {
              "httpHealthCheck": {
               "type": "string",
               "description": "Name of the HttpHealthCheck resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "httpHealthCheck"
             ],
             "response": {
              "$ref": "HttpHealthCheck"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.httpHealthChecks.insert",
             "path": "{project}/global/httpHealthChecks",
             "httpMethod": "POST",
             "description": "Creates a HttpHealthCheck resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "request": {
              "$ref": "HttpHealthCheck"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.httpHealthChecks.list",
             "path": "{project}/global/httpHealthChecks",
             "httpMethod": "GET",
             "description": "Retrieves the list of HttpHealthCheck resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "HttpHealthCheckList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "patch": {
             "id": "compute.httpHealthChecks.patch",
             "path": "{project}/global/httpHealthChecks/{httpHealthCheck}",
             "httpMethod": "PATCH",
             "description": "Updates a HttpHealthCheck resource in the specified project using the data included in the request. This method supports patch semantics.",
             "parameters": {
              "httpHealthCheck": {
               "type": "string",
               "description": "Name of the HttpHealthCheck resource to update.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "httpHealthCheck"
             ],
             "request": {
              "$ref": "HttpHealthCheck"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "update": {
             "id": "compute.httpHealthChecks.update",
             "path": "{project}/global/httpHealthChecks/{httpHealthCheck}",
             "httpMethod": "PUT",
             "description": "Updates a HttpHealthCheck resource in the specified project using the data included in the request.",
             "parameters": {
              "httpHealthCheck": {
               "type": "string",
               "description": "Name of the HttpHealthCheck resource to update.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "httpHealthCheck"
             ],
             "request": {
              "$ref": "HttpHealthCheck"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            }
           }
          },
          "images": {
           "methods": {
            "delete": {
             "id": "compute.images.delete",
             "path": "{project}/global/images/{image}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified image resource.",
             "parameters": {
              "image": {
               "type": "string",
               "description": "Name of the image resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "image"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "deprecate": {
             "id": "compute.images.deprecate",
             "path": "{project}/global/images/{image}/deprecate",
             "httpMethod": "POST",
             "description": "Sets the deprecation status of an image. If no message body is given, clears the deprecation status instead.",
             "parameters": {
              "image": {
               "type": "string",
               "description": "Image name.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "image"
             ],
             "request": {
              "$ref": "DeprecationStatus"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.images.get",
             "path": "{project}/global/images/{image}",
             "httpMethod": "GET",
             "description": "Returns the specified image resource.",
             "parameters": {
              "image": {
               "type": "string",
               "description": "Name of the image resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "image"
             ],
             "response": {
              "$ref": "Image"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.images.insert",
             "path": "{project}/global/images",
             "httpMethod": "POST",
             "description": "Creates an image resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "request": {
              "$ref": "Image"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/devstorage.full_control",
              "https://localhost:5000/auth/devstorage.read_only",
              "https://localhost:5000/auth/devstorage.read_write"
             ]
            },
            "list": {
             "id": "compute.images.list",
             "path": "{project}/global/images",
             "httpMethod": "GET",
             "description": "Retrieves the list of image resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "ImageList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "instances": {
           "methods": {
            "addAccessConfig": {
             "id": "compute.instances.addAccessConfig",
             "path": "{project}/zones/{zone}/instances/{instance}/addAccessConfig",
             "httpMethod": "POST",
             "description": "Adds an access config to an instance's network interface.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Instance name.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "networkInterface": {
               "type": "string",
               "description": "Network interface name.",
               "required": "true",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Project name.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance",
              "networkInterface"
             ],
             "request": {
              "$ref": "AccessConfig"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "aggregatedList": {
             "id": "compute.instances.aggregatedList",
             "path": "{project}/aggregated/instances",
             "httpMethod": "GET",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "InstanceAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "attachDisk": {
             "id": "compute.instances.attachDisk",
             "path": "{project}/zones/{zone}/instances/{instance}/attachDisk",
             "httpMethod": "POST",
             "description": "Attaches a disk resource to an instance.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Instance name.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Project name.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "request": {
              "$ref": "AttachedDisk"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "delete": {
             "id": "compute.instances.delete",
             "path": "{project}/zones/{zone}/instances/{instance}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified instance resource.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Name of the instance resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "deleteAccessConfig": {
             "id": "compute.instances.deleteAccessConfig",
             "path": "{project}/zones/{zone}/instances/{instance}/deleteAccessConfig",
             "httpMethod": "POST",
             "description": "Deletes an access config from an instance's network interface.",
             "parameters": {
              "accessConfig": {
               "type": "string",
               "description": "Access config name.",
               "required": "true",
               "location": "query"
              },
              "instance": {
               "type": "string",
               "description": "Instance name.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "networkInterface": {
               "type": "string",
               "description": "Network interface name.",
               "required": "true",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Project name.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance",
              "accessConfig",
              "networkInterface"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "detachDisk": {
             "id": "compute.instances.detachDisk",
             "path": "{project}/zones/{zone}/instances/{instance}/detachDisk",
             "httpMethod": "POST",
             "description": "Detaches a disk from an instance.",
             "parameters": {
              "deviceName": {
               "type": "string",
               "description": "Disk device name to detach.",
               "required": "true",
               "pattern": "\\w[\\w.-]{0,254}",
               "location": "query"
              },
              "instance": {
               "type": "string",
               "description": "Instance name.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Project name.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance",
              "deviceName"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.instances.get",
             "path": "{project}/zones/{zone}/instances/{instance}",
             "httpMethod": "GET",
             "description": "Returns the specified instance resource.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Name of the instance resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "response": {
              "$ref": "Instance"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "getSerialPortOutput": {
             "id": "compute.instances.getSerialPortOutput",
             "path": "{project}/zones/{zone}/instances/{instance}/serialPort",
             "httpMethod": "GET",
             "description": "Returns the specified instance's serial port output.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Name of the instance scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "response": {
              "$ref": "SerialPortOutput"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.instances.insert",
             "path": "{project}/zones/{zone}/instances",
             "httpMethod": "POST",
             "description": "Creates an instance resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "request": {
              "$ref": "Instance"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.instances.list",
             "path": "{project}/zones/{zone}/instances",
             "httpMethod": "GET",
             "description": "Retrieves the list of instance resources contained within the specified zone.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "response": {
              "$ref": "InstanceList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "reset": {
             "id": "compute.instances.reset",
             "path": "{project}/zones/{zone}/instances/{instance}/reset",
             "httpMethod": "POST",
             "description": "Performs a hard reset on the instance.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Name of the instance scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "setMetadata": {
             "id": "compute.instances.setMetadata",
             "path": "{project}/zones/{zone}/instances/{instance}/setMetadata",
             "httpMethod": "POST",
             "description": "Sets metadata for the specified instance to the data included in the request.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Name of the instance scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "request": {
              "$ref": "Metadata"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "setTags": {
             "id": "compute.instances.setTags",
             "path": "{project}/zones/{zone}/instances/{instance}/setTags",
             "httpMethod": "POST",
             "description": "Sets tags for the specified instance to the data included in the request.",
             "parameters": {
              "instance": {
               "type": "string",
               "description": "Name of the instance scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "instance"
             ],
             "request": {
              "$ref": "Tags"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            }
           }
          },
          "kernels": {
           "methods": {
            "get": {
             "id": "compute.kernels.get",
             "path": "{project}/global/kernels/{kernel}",
             "httpMethod": "GET",
             "description": "Returns the specified kernel resource.",
             "parameters": {
              "kernel": {
               "type": "string",
               "description": "Name of the kernel resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "kernel"
             ],
             "response": {
              "$ref": "Kernel"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.kernels.list",
             "path": "{project}/global/kernels",
             "httpMethod": "GET",
             "description": "Retrieves the list of kernel resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "KernelList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "machineTypes": {
           "methods": {
            "aggregatedList": {
             "id": "compute.machineTypes.aggregatedList",
             "path": "{project}/aggregated/machineTypes",
             "httpMethod": "GET",
             "description": "Retrieves the list of machine type resources grouped by scope.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "MachineTypeAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "get": {
             "id": "compute.machineTypes.get",
             "path": "{project}/zones/{zone}/machineTypes/{machineType}",
             "httpMethod": "GET",
             "description": "Returns the specified machine type resource.",
             "parameters": {
              "machineType": {
               "type": "string",
               "description": "Name of the machine type resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "machineType"
             ],
             "response": {
              "$ref": "MachineType"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.machineTypes.list",
             "path": "{project}/zones/{zone}/machineTypes",
             "httpMethod": "GET",
             "description": "Retrieves the list of machine type resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "response": {
              "$ref": "MachineTypeList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "networks": {
           "methods": {
            "delete": {
             "id": "compute.networks.delete",
             "path": "{project}/global/networks/{network}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified network resource.",
             "parameters": {
              "network": {
               "type": "string",
               "description": "Name of the network resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "network"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.networks.get",
             "path": "{project}/global/networks/{network}",
             "httpMethod": "GET",
             "description": "Returns the specified network resource.",
             "parameters": {
              "network": {
               "type": "string",
               "description": "Name of the network resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "network"
             ],
             "response": {
              "$ref": "Network"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.networks.insert",
             "path": "{project}/global/networks",
             "httpMethod": "POST",
             "description": "Creates a network resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "request": {
              "$ref": "Network"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.networks.list",
             "path": "{project}/global/networks",
             "httpMethod": "GET",
             "description": "Retrieves the list of network resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "NetworkList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "projects": {
           "methods": {
            "get": {
             "id": "compute.projects.get",
             "path": "{project}",
             "httpMethod": "GET",
             "description": "Returns the specified project resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project resource to retrieve.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "Project"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "setCommonInstanceMetadata": {
             "id": "compute.projects.setCommonInstanceMetadata",
             "path": "{project}/setCommonInstanceMetadata",
             "httpMethod": "POST",
             "description": "Sets metadata common to all instances within the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "request": {
              "$ref": "Metadata"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            }
           }
          },
          "regionOperations": {
           "methods": {
            "delete": {
             "id": "compute.regionOperations.delete",
             "path": "{project}/regions/{region}/operations/{operation}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified region-specific operation resource.",
             "parameters": {
              "operation": {
               "type": "string",
               "description": "Name of the operation resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "operation"
             ],
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.regionOperations.get",
             "path": "{project}/regions/{region}/operations/{operation}",
             "httpMethod": "GET",
             "description": "Retrieves the specified region-specific operation resource.",
             "parameters": {
              "operation": {
               "type": "string",
               "description": "Name of the operation resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "operation"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.regionOperations.list",
             "path": "{project}/regions/{region}/operations",
             "httpMethod": "GET",
             "description": "Retrieves the list of operation resources contained within the specified region.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "response": {
              "$ref": "OperationList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "regions": {
           "methods": {
            "get": {
             "id": "compute.regions.get",
             "path": "{project}/regions/{region}",
             "httpMethod": "GET",
             "description": "Returns the specified region resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "response": {
              "$ref": "Region"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.regions.list",
             "path": "{project}/regions",
             "httpMethod": "GET",
             "description": "Retrieves the list of region resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "RegionList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "routes": {
           "methods": {
            "delete": {
             "id": "compute.routes.delete",
             "path": "{project}/global/routes/{route}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified route resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "route": {
               "type": "string",
               "description": "Name of the route resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "route"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.routes.get",
             "path": "{project}/global/routes/{route}",
             "httpMethod": "GET",
             "description": "Returns the specified route resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "route": {
               "type": "string",
               "description": "Name of the route resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "route"
             ],
             "response": {
              "$ref": "Route"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.routes.insert",
             "path": "{project}/global/routes",
             "httpMethod": "POST",
             "description": "Creates a route resource in the specified project using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "request": {
              "$ref": "Route"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.routes.list",
             "path": "{project}/global/routes",
             "httpMethod": "GET",
             "description": "Retrieves the list of route resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "RouteList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "snapshots": {
           "methods": {
            "delete": {
             "id": "compute.snapshots.delete",
             "path": "{project}/global/snapshots/{snapshot}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified persistent disk snapshot resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "snapshot": {
               "type": "string",
               "description": "Name of the persistent disk snapshot resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "snapshot"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.snapshots.get",
             "path": "{project}/global/snapshots/{snapshot}",
             "httpMethod": "GET",
             "description": "Returns the specified persistent disk snapshot resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "snapshot": {
               "type": "string",
               "description": "Name of the persistent disk snapshot resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "snapshot"
             ],
             "response": {
              "$ref": "Snapshot"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.snapshots.list",
             "path": "{project}/global/snapshots",
             "httpMethod": "GET",
             "description": "Retrieves the list of persistent disk snapshot resources contained within the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "SnapshotList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "targetPools": {
           "methods": {
            "addHealthCheck": {
             "id": "compute.targetPools.addHealthCheck",
             "path": "{project}/regions/{region}/targetPools/{targetPool}/addHealthCheck",
             "httpMethod": "POST",
             "description": "Adds health check URL to targetPool.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to which health_check_url is to be added.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "request": {
              "$ref": "HealthCheckReference"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "addInstance": {
             "id": "compute.targetPools.addInstance",
             "path": "{project}/regions/{region}/targetPools/{targetPool}/addInstance",
             "httpMethod": "POST",
             "description": "Adds instance url to targetPool.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to which instance_url is to be added.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "request": {
              "$ref": "InstanceReference"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "aggregatedList": {
             "id": "compute.targetPools.aggregatedList",
             "path": "{project}/aggregated/targetPools",
             "httpMethod": "GET",
             "description": "Retrieves the list of target pools grouped by scope.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "TargetPoolAggregatedList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "delete": {
             "id": "compute.targetPools.delete",
             "path": "{project}/regions/{region}/targetPools/{targetPool}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified TargetPool resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.targetPools.get",
             "path": "{project}/regions/{region}/targetPools/{targetPool}",
             "httpMethod": "GET",
             "description": "Returns the specified TargetPool resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "response": {
              "$ref": "TargetPool"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "getHealth": {
             "id": "compute.targetPools.getHealth",
             "path": "{project}/regions/{region}/targetPools/{targetPool}/getHealth",
             "httpMethod": "POST",
             "description": "Gets the most recent health check results for each IP for the given instance that is referenced by given TargetPool.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to which the queried instance belongs.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "request": {
              "$ref": "InstanceReference"
             },
             "response": {
              "$ref": "TargetPoolInstanceHealth"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "insert": {
             "id": "compute.targetPools.insert",
             "path": "{project}/regions/{region}/targetPools",
             "httpMethod": "POST",
             "description": "Creates a TargetPool resource in the specified project and region using the data included in the request.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "request": {
              "$ref": "TargetPool"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "list": {
             "id": "compute.targetPools.list",
             "path": "{project}/regions/{region}/targetPools",
             "httpMethod": "GET",
             "description": "Retrieves the list of TargetPool resources available to the specified project and region.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region"
             ],
             "response": {
              "$ref": "TargetPoolList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "removeHealthCheck": {
             "id": "compute.targetPools.removeHealthCheck",
             "path": "{project}/regions/{region}/targetPools/{targetPool}/removeHealthCheck",
             "httpMethod": "POST",
             "description": "Removes health check URL from targetPool.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to which health_check_url is to be removed.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "request": {
              "$ref": "HealthCheckReference"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "removeInstance": {
             "id": "compute.targetPools.removeInstance",
             "path": "{project}/regions/{region}/targetPools/{targetPool}/removeInstance",
             "httpMethod": "POST",
             "description": "Removes instance URL from targetPool.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "region": {
               "type": "string",
               "description": "Name of the region scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "targetPool": {
               "type": "string",
               "description": "Name of the TargetPool resource to which instance_url is to be removed.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "region",
              "targetPool"
             ],
             "request": {
              "$ref": "InstanceReference"
             },
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            }
           }
          },
          "zoneOperations": {
           "methods": {
            "delete": {
             "id": "compute.zoneOperations.delete",
             "path": "{project}/zones/{zone}/operations/{operation}",
             "httpMethod": "DELETE",
             "description": "Deletes the specified zone-specific operation resource.",
             "parameters": {
              "operation": {
               "type": "string",
               "description": "Name of the operation resource to delete.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "operation"
             ],
             "scopes": [
              "https://localhost:5000/auth/compute"
             ]
            },
            "get": {
             "id": "compute.zoneOperations.get",
             "path": "{project}/zones/{zone}/operations/{operation}",
             "httpMethod": "GET",
             "description": "Retrieves the specified zone-specific operation resource.",
             "parameters": {
              "operation": {
               "type": "string",
               "description": "Name of the operation resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone",
              "operation"
             ],
             "response": {
              "$ref": "Operation"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.zoneOperations.list",
             "path": "{project}/zones/{zone}/operations",
             "httpMethod": "GET",
             "description": "Retrieves the list of operation resources contained within the specified zone.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone scoping this request.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "response": {
              "$ref": "OperationList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          },
          "zones": {
           "methods": {
            "get": {
             "id": "compute.zones.get",
             "path": "{project}/zones/{zone}",
             "httpMethod": "GET",
             "description": "Returns the specified zone resource.",
             "parameters": {
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              },
              "zone": {
               "type": "string",
               "description": "Name of the zone resource to return.",
               "required": "true",
               "pattern": "[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project",
              "zone"
             ],
             "response": {
              "$ref": "Zone"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            },
            "list": {
             "id": "compute.zones.list",
             "path": "{project}/zones",
             "httpMethod": "GET",
             "description": "Retrieves the list of zone resources available to the specified project.",
             "parameters": {
              "filter": {
               "type": "string",
               "description": "Optional. Filter expression for filtering listed resources.",
               "location": "query"
              },
              "maxResults": {
               "type": "integer",
               "description": "Optional. Maximum count of results to be returned. Maximum and default value is 100.",
               "default": "100",
               "format": "uint32",
               "minimum": "0",
               "maximum": "100",
               "location": "query"
              },
              "pageToken": {
               "type": "string",
               "description": "Optional. Tag returned by a previous list request truncated by maxResults. Used to continue a previous list request.",
               "location": "query"
              },
              "project": {
               "type": "string",
               "description": "Name of the project scoping this request.",
               "required": "true",
               "pattern": "(?:(?:[-a-z0-9]{1,63}\\.)*(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?):)?(?:[0-9]{1,19}|(?:[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?))",
               "location": "path"
              }
             },
             "parameterOrder": [
              "project"
             ],
             "response": {
              "$ref": "ZoneList"
             },
             "scopes": [
              "https://localhost:5000/auth/compute",
              "https://localhost:5000/auth/compute.readonly"
             ]
            }
           }
          }
         }
        })
    resp.status_code = 200
    return resp
