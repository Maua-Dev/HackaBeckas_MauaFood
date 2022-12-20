import json
from src.modules.app.get_all_orders.get_all_order_presenter import lambda_handler


class Test_GetAllOrderPresenter:
    def test_get_all_orders(self):

        event = {
          "version": "2.0",
          "routeKey": "$default",
          "rawPath": "/my/path", 
          "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
          "cookies": [
            "cookie1",
            "cookie2"
          ],
          "headers": {
            "header1": "value1",
            "header2": "value1,value2"
          },
          "queryStringParameters": {
            "parameter2": "value"
          },
          "requestContext": {
            "accountId": "123456789012",
            "apiId": "<urlid>",
            "authentication": None,
            "authorizer": {
                "iam": {
                        "accessKey": "AKIA...",
                        "accountId": "111122223333",
                        "callerId": "AIDA...",
                        "cognitoIdentity": None,
                        "principalOrgId": None,
                        "userArn": "arn:aws:iam::111122223333:user/example-user",
                        "userId": "AIDA..."
                }
            },
            "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
            "domainPrefix": "<url-id>",
            "http": {
              "method": "POST",
              "path": "/my/path",
              "protocol": "HTTP/1.1",
              "sourceIp": "123.123.123.123",
              "userAgent": "agent"
            },
            "requestId": "id",
            "routeKey": "$default",
            "stage": "$default",
            "time": "12/Mar/2020:19:03:58 +0000",
            "timeEpoch": 1583348638390
          },
          "body": "Visualize all the orders",
          "pathParameters": None,
          "isBase64Encoded": None,
          "stageVariables": None
        }
     
        expected = {'all_orders': 
        [
        {'id': 1, 'table': 1, 'pizza': {'flavor': 'BACON', 'stuffed_edge': 'CHEDDAR'}, 'state': 'DONE', 'price': 35},
        {'id': 2, 'table': 2, 'pizza': {'flavor': 'MUSSARELA', 'stuffed_edge': 'CATUPIRY'}, 'state': 'DONE', 'price': 35},
        {'id': 3, 'table': 3, 'pizza': {'flavor': 'BEEF', 'stuffed_edge': 'RICOTTA'}, 'state': 'WAITING_PAYMENT', 'price': 38}, 
        {'id': 4, 'table': 4, 'pizza': {'flavor': 'VEGGIE', 'stuffed_edge': 'CLASSIC'}, 'state': 'DECLINED', 'price': 28}, 
        {'id': 5, 'table': 5, 'pizza': {'flavor': 'OLIVES', 'stuffed_edge': 'CHEDDAR'}, 'state': 'DELIVERING', 'price': 36}
        ], 
        'message': 'all orders have been shown'}
        
        response = lambda_handler(event, None)
        
        assert response["statusCode"] == 200
        assert json.loads(response['body']) == expected