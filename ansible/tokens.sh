#!/bin/sh
export SCW_TOKEN=$(ansible-vault view group_vars/all/vault | yq r - scaleway_token)
export HCLOUD_TOKEN=$(ansible-vault view group_vars/all/vault | yq r - hcloud_token)
export VULTR_API_KEY=$(ansible-vault view group_vars/all/vault | yq r - vultr_token)
