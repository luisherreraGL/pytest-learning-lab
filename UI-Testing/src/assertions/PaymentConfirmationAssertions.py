from datetime import datetime
from src.utils.DatetimeFunctions import add_months
from src.assertions.CommonAssertions import CommonAssertions
from allure import step


class PaymentConfirmationAssertions():
    commonAssertions = CommonAssertions()

    @step("Validate payment confirmation details")
    def validateConfirmationDetails(self, paymentInfo, paymentTotal, confirmationMessageDetails):

        dictionary = confirmationMessageDetails.split("\n")

        self.commonAssertions.assertEqualToRegex(r"^Id: \d+$", dictionary[0], "Payment ID")

        self.commonAssertions.assertEqualString(dictionary[1], "Amount: {0} USD".format(int(paymentTotal)), "Payment Amount")
        self.commonAssertions.assertEqualString(dictionary[2], "Card Number: {0}".format(paymentInfo.card), "Payment Card")
        self.commonAssertions.assertEqualString(dictionary[3], "Name: {0}".format(paymentInfo.name), "Payment Name")

        paymentDate = 'Date: {dt.day}/{dt.month}/{dt.year}'.format(dt = add_months(datetime.now(), -1)) 
        self.commonAssertions.assertEqualString(dictionary[4], paymentDate, "Payment Date")

        