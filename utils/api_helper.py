from playwright.sync_api import Playwright


payload_for_order={"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}

class ApiHelper:

    def getToken(self, playwright:Playwright,credential_of_user):
        username=credential_of_user["username"]
        password=credential_of_user["password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post( url="/api/ecom/auth/login",
            data={"userEmail":username,"userPassword":password}
        )
        assert response.ok
        json_response=response.json()
        return json_response["token"]


    def createOrder(self,playwright:Playwright,credential_of_user):

        token=self.getToken(playwright,credential_of_user)

        api_request_context=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_context.post(
            url="/api/ecom/order/create-order",
            data=payload_for_order,
            headers={
                "Content-Type": "application/json; charset=utf-8",
                "authorization": token
            }
        )
        assert response.ok
        json_response=response.json()
        return json_response["orders"][0]



