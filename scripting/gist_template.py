import utils


def callback(gistObject, result, logger):
    if not result or "errors" in result:
        logger.WriteLog("Error for gist: " + gistObject.gist_info.gid, utils.LOG_LEVEL.ERROR)
        if utils.Verbose():
            logger.WriteLog("With query : ", utils.LOG_LEVEL.ERROR)
            logger.WriteLog(gistObject.query, utils.LOG_LEVEL.ERROR)
        return False
    viewer = editor = executor = admin = creator = flow = False
    for role in result['data']['admin']['edges']:
        if "viewer" == role['node']['code']:
            viewer = True
        elif "editor" == role['node']['code']:
            editor = True
        elif "admin" == role['node']['code']:
            admin = True
        elif "creator" == role['node']['code']:
            creator = True
        elif "flow" == role['node']['code']:
            flow = True
    return viewer and editor and executor and admin and creator and flow
 