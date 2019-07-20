import argparse

from Util.ArgumentParser import ArgumentParser
from Util.CustomError import CustomError
from Util.DataValidate import DataValidate



if __name__=="__main__":

    # 인자 값 확인
    dataValidate = DataValidate();

    # 인자 받기
    arg = ArgumentParser();



    # 최종 리턴 데이터
    out_msg = "";

    try :

        arg.add_argument('value', type=str, nargs='+');
        args = arg.parse_args();

        dataInfo = dataValidate.validate(args);

        out_msg = "SUM : " + str(dataInfo[0] + dataInfo[1]);

    except CustomError as ex :
        out_msg = "ERROR : " + str(ex);
    except Exception as ex :
        ex.with_traceback()
        out_msg = "ERROR : " + str(ex);



    print(out_msg);








