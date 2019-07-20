import re

from Util.CustomError import CustomError


class DataValidate:


    def validate(self, org_data):



        self.chkArgCount(org_data.value);

        listNumber = org_data.value;

        reVal = [];
        reVal.append( self.chkNumberic(listNumber[0]));
        reVal.append( self.chkNumberic(listNumber[1]));
        return reVal;


    def chkArgCount(self, paramData):
        if len(paramData) != 2 :
            raise CustomError("Please enter two values");

        pass;


    def chkNumberic(self, paramData):
        p = re.compile('[^0-9]');
        if p.search(paramData) != None :
            raise CustomError("Please enter Integer");


        return int(paramData);
