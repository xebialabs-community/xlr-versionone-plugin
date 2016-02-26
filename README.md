# Preface #

This document describes the functionality provided by the xlr-versionone-plugin.

See the **XL Release Reference Manual** for background information on XL Release and release concepts.

# CI status #

[![Build Status](https://travis-ci.org/xebialabs-community/xlr-versionone-plugin.svg?branch=master)](https://travis-ci.org/xebialabs-community/xlr-versionone-plugin)

# Overview #

## Requirements ##

* From version 1.0.1+: XLR 4.8.0+

## Installation ##

* Define an Access Token using the VersionOne UI: Go to `Configuration - Applications` and add a new Application with name `XLRelease`. Use `Access Token` as an authentication mechanism.
* Place the versionone plugin into plugins
* Place the versionone java sdk into plugins (download from [Fixes V1Connector](https://github.com/jdewinne/VersionOne.SDK.Java.APIClient)). A [pull request](https://github.com/versionone/VersionOne.SDK.Java.APIClient/pull/21) has been send, as the official sdk can't handle properly failing requests.

## Types ##

+ CreateIssue
    * `assetType`: For a list of possible values, see [Asset Types](https://community.versionone.com/Developers/Developer-Library/Concepts/Asset_Type)
    * `projectId`: The oid of the project you want to create the issue for, f.e. Scope:1535
    * `attributes`: Map of key / value pairs
    * `token`: output property - Output token which is the oid reference


## Testing / Building ##


`./gradlew clean assemble`

And copy the `jar` from `build/libs` into your plugins folder.

