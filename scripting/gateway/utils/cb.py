from graphql_client import GraphQLClient
from gists import GistFile, GObject
from logger import LogClient
import utils
import re


def callback(gistObject, result, logger):
    logger.writeLog("Checking pagination for organization list")

    query_name = re.search(r"^\{\s*?.*?\{\s*?(.*?)\(",gistObject.query)[1].strip()
    query_name = get_query_name(gistObject.query)

    filters = get_filters(gistObject.query)

    check = call_recursive(query_name, filters)
    return check


def call_recursive(query_name, filters):
    query = """
        query{
            admin{
                $$QUERY$$($$FILTERS$$){
			        pageInfo{
                    hasNextPage
                    startCursor
                }
                edges{
                    cursor
                    node{
                    code
                    adviseMessage{
                        code
                    }
                    }
                }
                }
            }
        }
    """
    
    query = query.replace("$$QUERY$$", query_name)
    query = query.replace("$$FILTERS$$", filters)
    
    gclient = GraphQLClient(utils.GRAPH_URL)
    gclient.inject_token(utils.GRAPH_TOKEN)

    result = gclient.execute(query)

    if result and "errors" not in result:
        for node in result['data']['admin'][query_name]['edges']:
            if node['node']['adviseMessage']:
                return False

       	import pdb; pdb.set_trace()
        if not result['data']['admin'][query_name]['pageInfo']['hasNextPage']:
            return True          
        else:
            next_cursor = orgs['cursor']
            if "after" in filters:
                filters = re.sub(r"(after:\s*?\").*?(\")", "\g<1>"+re.escape(next_cursor)+"\g<2>", filters)
            else:
                filters = re.sub(r"(before:\s*?\").*?(\")", "\g<1>"+re.escape(next_cursor)+"\g<2>", filters)
            return call_recursive(query_name, filters)
    else:
        return False


def get_query_name(query):
    if "organizations" in query:
        return "organizations"
    elif "products" in query:
        return "products"
    elif "members" in query:
        return "members"
    elif "groups" in query:
        return "groups"
    elif "apis" in query:
        return "apis"
    elif "resources" in query:
        return "resources"
    elif "roles" in query:
        return "roles"
    elif "operations" in query:
        return "operations"
    else:
        return None
