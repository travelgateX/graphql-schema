from graphql_client import GraphQLClient
from gists import GistFile, GObject
from logger import LogClient
import utils
import re


def callback(gistObject, result, logger):
    
    filters = get_filters(gistObject.query)

    check = call_recursive(0)
    return check


def call_recursive(filters):
    query = """
        query{
        admin{
            groups(type:$$FILTERS$$){
            edges{
                node{
                code
                adviseMessage{
                    code
                    description
                    level
                }
                }
            }
            }
        }
        }
    """
    types =["ROOT", "ORG", "ORG", "GROUP", "PROFILE", "TEAM", "FOLDER", "PRODUCT", "RESOURCE", "SPECIFIC_RESOURCE"]
    query = query.replace("$$FILTERS$$", type[filters])
    
    gclient = GraphQLClient(utils.GRAPH_URL)
    gclient.inject_token(utils.GRAPH_TOKEN)

    result = gclient.execute(query)

    if result and "errors" not in result:
        for node in result['data']['admin']['groups']['edges']:
            if node['node']['adviseMessage']:
                return False
            elif not node['node']['groupData']['type'] == type[filters]:
                if type[filters] == "SPECIFIC_RESOURCE":
                    return True
                return False

         return call_recursive(filters+1)

    else:
        return False
