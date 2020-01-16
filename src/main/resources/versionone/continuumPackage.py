#
# Copyright 2020 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#


from com.xebialabs.xlrelease.api.v1.forms import StartRelease
from java.util import HashMap
import json
import sys


def handle_request(event, template_filter=None):

    try:
        # Assumption: Continuum might send stuff from other github branches, version is the branch???
        if event["package_revision"]["version"].lower() == "master":
            logger.info("Found packaging request from VersionOne with template filter %s " % template_filter)
            handle_push_event(event, template_filter)
    except:
        e = sys.exc_info()[1]
        msg = (
            "Could not parse payload, check your VersionOne Webhook "
            "configuration. Error: %s. Payload:\n%s" % (e, event)
        )
        logger.warn(msg)
        return


def handle_push_event(event, template_filter):
    full_version = str(event["package_revision"]["full_version"])
    revision_id = str(event["package_revision"]["revision_id"])
    revision = str(event["package_revision"]["revision"])

    raw_workitems = event["workitems"]
    workitemsMap = HashMap()
    for item in raw_workitems:
      workitemsMap.put(item["external_key"],item["title"])
    

    logger.info("Starting release for Package %s" % full_version)
    start_v1_release(
        full_version,
        revision_id,
        revision,
        workitemsMap,
        template_filter
    )


def start_v1_release(
    full_version,
    revision_id,
    revision,
    workitemsMap,
    template_filter=None,
):
    templates = templateApi.getTemplates(template_filter)
    if not templates:
        response.statusCode = 500
        raise Exception(
            "Could not find any templates by filter : %s " % template_filter
        )
    else:
        if len(templates) > 1:
            response.statusCode = 500
            raise Exception(
                "Found more than one template with tag '%s', please use more specific value. List Found : %s"
                % (template_filter, [item.title for item in templates])
            )

    template_id = templates[0].id




    params = StartRelease()
    params.setReleaseTitle("Package Request [%s]" % (full_version))
    variables = HashMap()
    variables.put("${full_version}", "%s" % full_version)
    variables.put("${revision_id}", "%s" % revision_id)
    variables.put("revision", revision)
    variables.put("workitems", workitemsMap)
    params.setReleaseVariables(variables)
    started_release = templateApi.start(template_id, params)
    response.entity = started_release
    logger.info(
        "Started release %s for Package %s" % (started_release.getId(), full_version)
    )


handle_request(request.entity, "SNOW Change Process for Packages")
