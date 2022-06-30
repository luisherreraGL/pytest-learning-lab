from datetime import datetime
import re

class PaymentConfirmationAssertions():
    def validateConfirmationDetails(self, paymentInfo, paymentTotal, confirmationMessageDetails):

        dictionary = confirmationMessageDetails.split("\n")

        pat = re.compile(r"^Id: \d+$")
        assert re.fullmatch(pat, dictionary[0]), "Error: no payment ID included"

        assert dictionary[1] == "Amount: {0} USD".format(int(paymentTotal)), "Error: Payment Amount not match Buy Amount"
        assert dictionary[2] == "Card Number: {0}".format(paymentInfo.card), "Error: Payment Card number not match"
        assert dictionary[3] == "Name: {0}".format(paymentInfo.name), "Error: Payment Name not match"
        assert dictionary[4] == "Date: 30/5/2022", "Error: Payment Date not match"
    #    assert dictionary[4] == "Date: {0}".format(datetime.today().strftime('%d/%m/%Y'))