import cfWebSocketApiV1 as cfWsApi
import util.cfLogging as cfLog
logger = cfLog.CfLogger.get_logger(" Fukuyu ")

api_path = "wss://www.cryptofacilities.com/ws/v1"
api_key = "NSq0xoXjpOYoboDe6PvzCpNcMDWX1y6CY0DxW/EVjBjCjRpfcnIB0BXc"  # accessible on your Account page under Settings -> API Keys
api_secret = "/yEHcrPNXoiril+0sPaP+CCl/RhiensFNFut1NJwCj+ZDqjteWHXtPTll5WmzLJ6I/DcfloVKaP5QKS2+XcXsGcO"  # accessible on your Account page under Settings -> API Keys
timeout = 10



cfWs = cfWsApi.CfWebSocketMethods(base_url=api_path, api_key=api_key, api_secret=api_secret, timeout=10)

def subscribe_api_focker():
    global product_ids
    product_ids=   ["fi_xbtusd_180928"]
    #["IN_XBTUSD"]

    # subscribe to trade
    feed = "book"
    cfWs.subscribe_public(feed, product_ids)

def unsubscribe_api_focker():
    """Test the unsubscribe methods"""

    ##### public feeds #####

    global product_ids

    # unsubscribe to trade
    feed = "book" \
           ""
    cfWs.unsubscribe_public(feed, product_ids)

logger.info("-----------------------------------------------------------")
logger.info("****PRESS ANY KEY TO SUBSCRIBE AND START RECEIVING INFO****")
logger.info("-----------------------------------------------------------")
input()

# Subscribe
subscribe_api_focker()
logger.info("-----------------------------------------------------------")
logger.info("****PRESS ANY KEY TO UNSUBSCRIBE AND EXIT APPLICATION****")
logger.info("-----------------------------------------------------------")
input()

# Unsubscribe
unsubscribe_api_focker()


# Exit
exit()