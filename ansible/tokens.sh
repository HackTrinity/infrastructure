#!/bin/sh
export SCW_TOKEN=$(ansible-vault view group_vars/scaleway/vault | yq r - cloud_token)
