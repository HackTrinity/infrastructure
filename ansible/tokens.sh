#!/bin/sh
export SCW_TOKEN=$(ansible-vault view group_vars/scaleway/vault | yq r - cloud_token)
export VULTR_API_KEY=$(ansible-vault view group_vars/vultr/vault | yq r - cloud_token)
export HCLOUD_TOKEN=$(ansible-vault view group_vars/hcloud/vault | yq r - cloud_token)
